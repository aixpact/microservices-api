from flask import Blueprint


blueprint = Blueprint('hello_blueprint', __name__,
                        url_prefix='/api',
                        template_folder='templates',
                        # static_folder='static'
)
