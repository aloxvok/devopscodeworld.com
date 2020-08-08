from flask import Flask

# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>welcome</title> </head>\n<body>'''
instructions = '''
    <p>
    <hr/>
    <h1 style="background-color: blue; color: white">Welcome to San Francisco!</h1>
<<<<<<< HEAD
    <hr/>
    <h1 style="background-color: red; color: white">Watch the city from Twin Peaks</h1>
    <hr/>
    <h1 style="background-color: purple; color: white">Watch the city from Twin Peaks</h1>
=======
    <br/>
    <h1/> style="background-color: purple; color: white">Watch the city from Twin Peaks</h1>
>>>>>>> 354a55016d365ddb1d1b9fbb85d5e181af999c2f
    <hr/>
    <h1 style="background-color: green; color: white">You can see the Coit Tower!</h1>
    <hr/>
    <h1 style="background-color: red; color: white">You can see the Golden Gate!</h1>
    <hr/>
    <h1 style="background-color: yellow; color: black">You can see the Bay Bridge!</h1>
    <hr/>
    <h1 style="background-color: yellow; color: black">You can see the Bay Bridge!</h1>
    <hr/>
    <h1 style="background-color: aqua; color: red">You can see the tiny houses!</h1>
    <br/>
    <h1 style="background-color: aqua; color: red">You can see the tiny houses!</h1>
    <hr/>
    <h1> Watch the city from Twin Peaks</h1>
    <hr/>
    <em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
