# Portfolio

Hello!

Welcome to the beginning of my programming journey! This portfolio showcases my first project, where I combined various technologies and tools to learn by doing. Each part of this project reflects how I gradually developed my skills, exploring different aspects of programming.

I’m a beginner programmer, but I’m full of passion and eager to keep growing. What you’ll find here is just the start – a project born from my enthusiasm for learning and my desire to understand more advanced concepts.

Feel free to explore my work and follow my progress.

## Project info:

| Tool category         | Tool name            |
|-----------------------|----------------------|
| IDE                   | Visual Studio Code   |
| SCM                   | GIT                  |
| Project management    | Jira                 |
| Project documentation | Confluence           |
| Environment           | Docker               |
| Language / Framework  | Python 3.x / Flask 3 |
| Database              | MySQL 8.0.x          |

## Learning goals

- SOLID Principles: Ensuring that the code is modular, maintainable, and scalable
- DRY (Don't Repeat Yourself): Writing reusable code to avoid redundancy
- Containerizing the application for consistent development and deployment environments
- Using a relational database to store and manage data in conjunction with Flask-SQLAlchemy ORM
- Using database migrations
- Building basic web basic applications using the Flask framework
- Utilizing various Flask extensions for added functionality (e.g., Flask-SQLAlchemy, Flask-Migrate)
- API resources and logic creation

## Folder structure:

    portfolio/
    ├── .docker
    │    └── app
    ├── app
    │   ├── api
    │   │   └── v1
    │   ├── config
    │   ├── controllers
    │   │   └── projects
    │   ├── error_handlers
    │   ├── extensions
    │   │   └── logging
    │   │       └── filters
    │   ├── forms
    │   ├── models
    │   ├── routes
    │   ├── services
    │   ├── static
    │   │   ├── css
    │   │   ├── images
    │   │   └── js
    │   ├── templates
    │   └── tests
    ├── logs
    ├── migrations
    │   └── versions    
    ├── app.py
    ├── docker-compose.yaml
    ├── README.md
    ├── requirements.txt
    └── sample.env

- `.docker/`
  - `app`: Contains Docker configurations specific to `app` service, like Dockerfile, entry-point scripts etc.,
- `app`: Holds the source code of the application,
  - `api`: Defining resources and logic for application API,
  - `config`: Place for config classes to be used in `app.config.from_object` based on provided `.env` values,
  - `controllers`: Business logic, connects models and routes,
  - `error_handlers`: Custom application error handlers,
  - `extensions`: Scripts for initializations of Flask extensions,
  - `forms`: Flask-WTF HTML form classes are located here,
  - `models`: Data models with business logic and corresponding DB table (handled by Flask-SQLAlchemy),
  - `routes`: URL routing using Flask Blueprints,
  - `services`: Services classes to encapsulate internal application bussiness logic,
  - `static`: css, images and js static files for websites,
  - `templates`: HTML templates, Jinja2 template engine,
  - `tests`: Place to test individual application functionalities,
- `logs`: Docker mounted path with application logs,
- `migrations`: Flask-Migrate work folder for storing migrations versions and configurations,
  - `versions`: Individual migration files,
- `app.py`: Main entry point, initializes and runs Flask application,
- `docker-compose.yaml`: Docker Compose config, describes services, networks, and volumes,
- `README.md`: Documentation, explains how to set up and use the project,
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
You should be seeing the application home page.

**The first time the website is launched, the user will be asked to create a new account.<br>
On subsequent visits, please use the credentials provided on initial user creation.**

Only after logging in can you read the content of the website.

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
