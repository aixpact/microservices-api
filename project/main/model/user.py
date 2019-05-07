from flask import current_app
from project.extensions import db, flask_bcrypt
import datetime
from .blacklist import BlacklistToken
# from ..config import key
import jwt


class User(UserMixin, ResourceMixin, db.Model):
    ROLE = OrderedDict([
        ('unregistered', 'Unregistered'),
        ('super', 'Super'),
        ('member', 'Member'),
        ('admin', 'Admin')
    ])

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    # Relationships.
    # credit_card = db.relationship(CreditCard, uselist=False, backref='users',
    #                               passive_deletes=True)
    # subscription = db.relationship(Subscription, uselist=False,
    #                                backref='users', passive_deletes=True)
    # invoices = db.relationship(Invoice, backref='users', passive_deletes=True)
    # bets = db.relationship(Bet, backref='bets', passive_deletes=True)

    # Authentication.
    role = db.Column(db.Enum(*ROLE, name='role_types', native_enum=False),
                     index=True, nullable=False, server_default='member')
    active = db.Column('is_active', db.Boolean(), nullable=False,
                       server_default='1')
    registered = db.Column(db.Boolean(), nullable=False,
                       server_default='0')
    online = db.Column(db.Boolean(), nullable=False,
                       server_default='0')
    username = db.Column(db.String(24), unique=True, index=True)
    email = db.Column(db.String(255), unique=True, index=True, nullable=False,
                      server_default='')
    password_hash = db.Column(db.String(128), nullable=False, server_default='')

    # Billing.
    name = db.Column(db.String(128), index=True)
    payment_id = db.Column(db.String(128), index=True)
    cancelled_subscription_on = db.Column(AwareDateTime())
    previous_plan = db.Column(db.String(128))

    # Bet.
    coins = db.Column(db.BigInteger())
    last_bet_on = db.Column(AwareDateTime())

    # Activity tracking.
    sign_in_count = db.Column(db.Integer, nullable=False, default=0)
    current_sign_in_on = db.Column(AwareDateTime())
    current_sign_in_ip = db.Column(db.String(45))
    last_sign_in_on = db.Column(AwareDateTime())
    last_sign_in_ip = db.Column(db.String(45))

    # Additional settings.
    locale = db.Column(db.String(5), nullable=False, server_default='en')



# class User(db.Model):
#     """ User Model for storing user related details """
#     __tablename__ = "user"

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     email = db.Column(db.String(255), unique=True, nullable=False)
#     registered_on = db.Column(db.DateTime, nullable=False)
#     admin = db.Column(db.Boolean, nullable=False, default=False)
#     public_id = db.Column(db.String(100), unique=True)
#     username = db.Column(db.String(50), unique=True)
#     password_hash = db.Column(db.String(100))

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    @staticmethod
    def encode_auth_token(user_id):
        """
        Generates the Auth Token

        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                current_app.config['SECRET_KEY'],  # key,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token

        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, key)
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def __repr__(self):
        return "<User '{}'>".format(self.username)
