
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)

# import the flask library 
from flask import Flask 
# set up our app variable so that we can start writting routes 
app = Flask(__name__)

# indicates the URL we need to visit in order to see our results 
@app.route('/')
# defines the route function
def homepage():
    # describes the route in a human-readable way. It's completely optional 
    """Shows a greeting to the user."""
    # returns page content 
    return 'Are you there, world? It\'s me, Ducky!'

# route for the user can type their favorite animal 
@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

# route for users favorite dessert 
@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert): 
    """Display a message to the user that changes based on their favorite dessert"""
    return f'How did you know I liked {users_dessert}?'

# route for mad libs 
@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun): 
    '''display a message to the user based off their input for the madlib'''
    return f'Early on a Saturday morning the {adjective} {noun} appeared on the front step of the capital. It was the start of an interesting adventure'

# multipy 2 numbers 
@app.route('/multiply/<number1>/<number2>')
def multiply_number(number1, number2): 
    if number1.isdigit() and number2.isdigit():
        total = int(number1) * int(number2)
        return str(total)
    else: 
        return f'Invalid inputs. Please try again by entering 2 numbers!'





if __name__ == '__main__':
    app.run(debug=True)


