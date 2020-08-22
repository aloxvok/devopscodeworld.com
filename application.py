from flask import Flask

# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>Home Page</title> </head>\n<body>'''
instructions = '''
    <p>
    <h1 style="background-color: aqua ; color: white">Welcome to San Francisco!</h1>
     <br/>
    <hr/><iframe width="560" height="315" src="https://www.youtube.com/embed/hanE_bysWro" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/vOWdIacP3xs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
     <hr/>
    <h1 style="background-color: ; color: black">Watch the city from Twin Peaks</h1>
    <br/>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/bAjq4II85PU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
     <hr/>
    <h1 style="background-color: ; color: black">while feeling the ocean breeze</h1>
    <hr/>
    <h1 style="background-color: ; color: black">also the bay splashing salty water</h1>
    <hr/>
    <h1 style="background-color: ; color: black">You can see the Coit Tower!</h1>
    <hr/>
    <h1 style="background-color: ; color: black">and see the Golden Gate!</h1>
    <hr/>
    <h1 style="background-color: ; color: black">You can see almost every skyrise!</h1>
    <hr/>
    <h1 style="background-color: ; color: black">near the Bay Bridge!</h1>
    <hr/>
    <h1 style="background-color: ; color: black">dont forget see the tiny houses!</h1>
    <hr/>
    <h1 style="background-color: ; color: black">but most importantly you can see humanity!</h1>
    <hr/>
   '''
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
