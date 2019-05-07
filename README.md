# Microservices container - boilerplate #



## Connecting microservice container to main-app

Please find below code snippets, for cheatsheet use.



#### Example;

copy boilerplate code for new microservice into folder which contains main-service (with docker-compose.yml and nginx/nginx.conf).

```
cd <dir main-service>
mkdir name_microservice
```

## Follow steps below (port number 7000 is arbitrare):


### 1. Add feature/service to docker-compose

file: ./main_app/docker-compose.yml

```
  name-service:
    container_name: name-service
    build:
      context: ../name_microservice
      dockerfile: Dockerfile
    volumes:
      - '../name_microservice:/project_path' # /local_folder:/container_folder
    ports:
      - '7001:7000'                          # HOST(port exposed to browser):CONTAINER(port nginx listens to)
```

### 2. Run wysgi microservice container on port

file: ../name_microservice/Dockerfile

`CMD gunicorn -w 2 -b 0.0.0.0:7000 --reload --access-logfile - "project.app:create_app()"`


### 3. Connect nginx to wysgi

Bind nginx incoming route to gunicorn route

file: ./main_app/nginx/nginx.conf

```
        location /api {
            proxy_pass              http://api-service:7000;
            proxy_http_version      1.1;
            proxy_set_header        Upgrade $http_upgrade;
            proxy_set_header        Connection "upgrade";
            # proxy_redirect          off;
            proxy_set_header        Host $host;
            proxy_set_header        X-Real-IP $remote_addr;
            proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
            # proxy_set_header        X-Forwarded-Host $server_name;  #
            client_max_body_size    5M;  #
        }
```

### 4. Instantiate blueprint in microservice

file: ../name_microservice/project/home/__init__.py

```
blueprint = Blueprint('hello_blueprint', __name__,
                        url_prefix='/some_prefix',
                        template_folder='templates',
                        # static_folder='static'
)
```

### 5. Import blueprint in views.py

file: ../name_microservice/project/home/views.py

`from . import blueprint`

### 6. Import -blueprint with views- in app.py and register

file: ../name_microservice/project/app.py

`from .home.views import blueprint`

`...`

`app.register_blueprint(blueprint)`

### 7. Run containers

Stop running containers (if any) with
`ctrl-c`

Stop, clean and start (with build) containers

`docker-compose stop && docker-compose rm -f && docker-compose up --build`


### 8. Reset database - with CLI setup
Open new terminal:
```
cd <main-service dir>
docker-compose exec main-service app_name db reset
```

### 9. Start browsing

localhost/route_name

shift-command-r to hard refresh


### 10. Git

Create GitHub repo

```
git init
git add ./*
git status
git commit -am "first commit"
git remote add origin https://github.com/<account/repo_name.git>
git push -u origin master
```

## When collaborating or using GitHub for containers or using CI-CD

### 11. Adjust docker-compose

Set context to Dockerfile location on GitHub (repo address)


```
  name-service:
    `container_name: name-service
    build:
      context: https://github.com/aixpact/microservice-api.git
      dockerfile: Dockerfile
    volumes:
      - '../name_microservice:/project_path' # /local_folder:/container_folder
    ports:
      - '7001:7000'                          # HOST(port exposed to browser):CONTAINER(port nginx listens to)
```

Build container from Git repo - change docker-compose build-context

### 12. Docker-compose up

Stop running containers (if any) with
`ctrl-c`

Stop, clean and start (with build) containers

`docker-compose stop && docker-compose rm -f && docker-compose up --build`

