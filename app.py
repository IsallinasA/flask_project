from flask import request
from flask import url_for


from flask import Flask
from markupsafe import escape


from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
	 return render_template('index.html')


@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)



@app.route("/<name>")
def hi(name):
    return f"Hello, {escape(name)}!"


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
	return render_template('uder.html')


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


@app.route('/projects/')
def projects():
        return render_template('projects.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/user/<username>')
def profile(username):
	return render_template('user.html')

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='isallinas'))


with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'





if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)

