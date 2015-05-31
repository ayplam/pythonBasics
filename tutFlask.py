__author__ = 'goldenxradian'

from flask import Flask, url_for

from flask import render_template

# Name of application's module/package. This helps Flask figure out where to find templates/static files
app = Flask(__name__)

#
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

# route() tells Flask what URL should trigger the function
@app.route('/')
def index():
    return 'You have been added to...the index'

@app.route("/hello")
def hello_world():
    return 'Hello World!'

@app.route('/login')
def login(): pass

@app.route('/user/<username>')
def profile(username): pass

# Behave as if it's handling a request
with app.test_request_context():
    print url_for('index')
    print url_for('login')
    print url_for('login', next="/")
    print url_for('profile', username = 'John Doe')


@app.route('/usertest/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/projects/')
def projects():
    return 'The project has a trailing slash, and is therefore a FOLDER on the file system'


@app.route('/about')
def about():
    return 'The about page has NO slash. Adding the end slash in the URL will cause an ERROR'



# This ensures that the server only runs the script if THIS script is executed, not called from anywhere else.
# Thus, you can't import this.
if __name__ == '__main__':
    app.run('0.0.0.0')

