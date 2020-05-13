"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

STINKINESS = ['smelly', 'gross', 'super stinky', 'funny looking', 
    'cootie-infested', 'Stinky McStinker']

@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>Hi! This is the home page.
    <br>
    <body>
    <a href="http://localhost:5000/hello">Let's say hello!</a>
    <br>
    <a href="http://localhost:5000/smelly">Wait -what's that smell??</a>
    </body>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>

        <form action="/greet">
           
          <label for="name">What's your name?</label>
          <input id="name" type="text" name="person">
        
          <label for="coolness">How cool are you?</label>
          <select id="coolness" name="cool_factor">
          <option value="awesome">Awesome</option>
          <option value="terrific">Terrific</option>
          <option value="fantastic">Fantastic</option>
          <option value="neato">Neato</option>
          <option value="fantabulous">Fantabulous</option>
          <option value="wowza">Wowza</option>
          <option value="oh-so-not-meh">Oh-so-not-meh</option>
          <option value="brilliant">Brilliant</option>
          <option value="ducky">Ducky</option>
          <option value="coolio">Coolio</option>
          <option value="incredible">Incredible</option>
          <option value="wonderful">Wonderful</option>
          <option value="smashing">Smashing</option>
          <option value="lovely">Lovely</option>
          </select>
         
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """

@app.route('/smelly')
def you_smell():
    """Say something rude about the user"""

    return """
    <!doctype html>
    <html lang="en">
        <head>
            <title>Why are you here?</title>
        </head>

        <body>
            <h1>Gross! It's you, stinky-pants! Why are <em>you</em> here?</h1>

            <form action="/diss">

                <label for="name">Because I'm:</label>
                <input id="name" type="text" name="person">

                <label for="coolness">and I think I'm</label>
                <select id="coolness" name="stink-factor">
                    <option value="awesome">Awesome</option>
                    <option value="terrific">Terrific</option>
                    <option value="fantastic">Fantastic</option>
                    <option value="neato">Neato</option>
                    <option value="fantabulous">Fantabulous</option>
                    <option value="all_that">All That</option>
                    <option value="incredible">Incredible</option>
                    <option value="wonderful">Wonderful</option>
                    <option value="smashing">Smashing</option>
                </select>

                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("cool_factor")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


@app.route('/diss')
def you_stinker():
    """Give a rude response to a user, by name"""

    player = request.args["person"]

    rudeness = choice(STINKINESS)

    return """
    <!doctype html>
    <html lang="en">
        <head>
            <title>A Wicked Diss</title>
        </head>
        <body>
            As if, {}! Everyone knows you're {}!!!!!!!!!
        </body>
    </html>
    """.format(player, rudeness)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
