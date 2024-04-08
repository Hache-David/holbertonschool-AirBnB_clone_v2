# AirBnB clone - Web framework

## Learning Objectives
- What is a Web Framework
- How to build a web framework with Flask
- How to define routes in Flask
- What is a route
- How to handle variables in a route
- What is a template
- How to create a HTML response in Flask by using a template
- How to create a dynamic template (loops, conditions…)
- How to display in HTML data from a MySQL database

### What is a Web Framework?
- A web framework is a software framework designed to support the development of web applications, web services, and web resources. It provides a standard way to build and deploy web applications on the World Wide Web. A web framework aims to automate the overhead associated with common activities performed in web development.

### How to build a web framework with Flask:
- Flask is a micro web framework in Python. To build a web application using Flask, you first need to set up a Flask environment, create a Flask application instance, define routes and views, and run the application server.

### How to define routes in Flask:
- Routes in Flask are defined using the @app.route decorator above a function. Each route is associated with a function which will be executed when the route is accessed through a web request.
```bash
@app.route('/')
def home():
    return 'Hello, World!'
```

### What is a route?
- A route is a URL pattern that is used to direct a request to a specific handler. It defines the way in which a client request (like a URL) is mapped to a function that will handle that request.

### How to handle variables in a route:
- You can handle variables in a route by specifying variable sections in the route definition. These variable sections are enclosed in angle brackets `<variable_name>`. The function then receives the variable as an argument.
```bash
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'
```

### What is a template?
- A template is a file that allows you to create a dynamic HTML page. It defines a structure of the HTML page, with placeholders for data that will be filled in when the page is rendered. Flask uses the Jinja2 template engine.

### How to create an HTML response in Flask by using a template:
- You can create an HTML response using a template in Flask by defining a template file (usually `.html`) and then rendering that template using `render_template()` function.
```bash
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html')
```

### How to create a dynamic template (loops, conditions…):
- Jinja2 templates allow you to use structures like loops and conditions:
```bash
<ul>
{% for user in users %}
  <li>{{ user.name }}</li>
{% endfor %}
</ul>
```

### How to display in HTML data from a MySQL database:
- First, you'll need to fetch data from your MySQL database in your route. Then, you can pass this data to your template and display it.
```bash
@app.route('/users')
def list_users():
    users = User.query.all()
    return render_template('users.html', users=users)
```
And in your `users.html` template:
```bash
<ul>
{% for user in users %}
  <li>{{ user.name }}</li>
{% endfor %}
</ul>
```

#### INFO
- These steps give you a high-level overview of building a web application with Flask, handling routes and variables, creating dynamic templates, and displaying data from a database.
