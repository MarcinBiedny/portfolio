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
    ├── README.md
    ├── app.py
    ├── docker-compose.yaml
    ├── requirements.txt
    └── sample.env

- `.docker/`
  - `app`: Contains Docker configurations specific to `app` service, like Dockerfile, entry-point scripts etc.,
- `migrations`: Flask-Migrate work folder for storing migrations versions and configurations,
  - `versions`: Individual migration files,
- `src`: Holds the source code of your application,
  - `controllers`: Business logic, connects models and routes,
  - `error_handlers`: Handler for custom error pages,
  - `extensions`: Scripts for initializations of Flask extensions,
  - `models`: Data models with business logic and corresponding DB table (handled by Flask-SQLAlchemy),
  - `routes`: URL routing using Flask Blueprints,
  - `static`: css, images and js static files for websites,
  - `templates`: HTML templates, Jinja2 templating engine,
- `app.py`: Main entry point, initializes and runs Flask application,
- `docker-compose.yaml`: Docker Compose config, describes services, networks, and volumes,
- `README.md`: Documentation, explains how to set up and use your project,
- `requirements.txt`: All the dependencies and their specific versions required for the application,
- `sample.env`: Sample environment variables, template for .env file.

## Running application using Docker

### Run containers in detached mode
To start the services in detached mode, run below command in project root directory:
```bash
docker compose up -d
```

### Run application
To start the application, run below command:
```bash
docker compose exec app flask run
```
You should see similar output to below:
```
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.18.0.3:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 332-694-836
```

### Enter application
Open the [localhost:5000](http://localhost:5000) or [127.0.0.1:5000](http://127.0.0.1:5000) link.
You should be seeing your application home page.

### Stop Docker Services
To stop all containers, run:
```bash
docker compose stop
```

### Other useful `docker/docker compose` commands

#### Service logs with follow option
```bash
docker compose logs -f <service-name>
```
Example for `app` service:
```bash
docker compose logs -f app
```
