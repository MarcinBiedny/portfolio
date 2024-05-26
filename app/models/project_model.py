from flask import url_for


class Project:
    def get_all(self):
        return [
            {
                "title": "Simple Calculator",
                "description": "This is simple calculator project where I learn basics of HTML and Java Script.",
                "url": url_for("projects.calculator_index"),
                "image_url": url_for(
                    "static",
                    filename="images/projects/calculator/thumbnail.jpg",
                ),
                "button_style": "btn btn-dark",
            },
            {
                "title": "Password Generator",
                "description": (
                    "This is a simple password generator project where I learn"
                    " basics of HTTP request/response, REST, APIs, CSRF and"
                    " HTML forms using Flask extensions. Extensions used:"
                    " Flask-JSON, FLASK-RESTX, Flask-WTF."
                ),
                "url": url_for("projects.password_generator_index"),
                "image_url": url_for(
                    "static",
                    filename="images/projects/password-generator/thumbnail.png",
                ),
                "button_style": "btn btn-primary",
            },
        ]
