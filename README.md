# portfolio
My portfolio

## Folder structure:

    portfolio/
    ├── .docker
    │   └── app
    ├── migrations
    ├── src
    │    ├── controllers
    │    ├── error_handlers
    │    ├── extensions
    │    ├── models
    │    ├── routes
    │    ├── static
    │    └── templates
    ├── LICENSE
    ├── README.md
    ├── app.py
    ├── docker-compose.yaml
    ├── requirements.txt
    └── sample.env

- `.docker/`
  - `app`: Contains Docker configurations specific to your Flask app, like Dockerfile,
- `migrations`: Extension to support SQLAlchemy database migrations for Flask applications using Alembic,
  - `versions`: Individual migration files,
- `src`: Holds the source code of your application,
  - `controllers`: Business logic, connects models and routes,
  - `error_handlers`: Handler for custom error pages,
  - `extensions`: Scripts for installed flask_migrate and flask_sqlalchemy extensions,
  - `models`: Data models, usually represents database tables,
  - `routes`: URL routing using Flask Blueprints,
  - `static`: css, images and js static files for websites,
  - `templates`: HTML templates, Jinja2 templating engine,
- `app.py`: Main entry point, initializes and runs Flask application,
- `docker-compose.yaml`: Docker Compose config, describes services, networks, and volumes,
- `LICENSE`: License file, dictates terms under which code can be used,
- `README.md`: Documentation, explains how to set up and use your project,
- `requirements.txt`: All the dependencies and their specific versions required for the application,
- `sample.env`: Sample environment variables, template for .env file.

## Running application using Docker

### Build image
Build the Docker image with the following command:
```bash
docker-compose build
```
### Run containers in detached mode
To start the services in detached mode, run:
```bash
docker-compose up -d
```
### Check application is running
To assess if the ```app``` service (container) is running correctly. Run below:
```bash
docker-composer logs app
```
You should see similar output to below:

    portfolio-app-1  |  * Serving Flask app 'src'
    portfolio-app-1  |  * Debug mode: on
    portfolio-app-1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    portfolio-app-1  |  * Running on all addresses (0.0.0.0)
    portfolio-app-1  |  * Running on http://127.0.0.1:5000
    portfolio-app-1  |  * Running on http://172.23.0.3:5000

### Enter application
Open the [localhost:5000](http://localhost:5000) or [127.0.0.1:5000](http://127.0.0.1:5000) link.
You should be seeing your application home page.

### Stop Docker Services
To stop all containers, run:
```bash
docker-compose stop
```

### Other useful `docker/docer-compose` commands

#### Service logs with follow option
```bash
docker-composer logs -f <service-name>
```
Example for `app` service:
```bash
docker-composer logs -f app
```
