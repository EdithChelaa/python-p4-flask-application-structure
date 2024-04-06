#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
# print (__name__) # Outputs __main__

@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

# Without validation:
# @app.route('/<username>')
# def user(username):
#     return f'<h1>Profile for {username}</h1>'


# With validation:
@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

# We can also run a development server through 
# treating our application module as a script with the app.run() method:
if __name__ == '__main__':
    app.run(port=5555, debug=True)


