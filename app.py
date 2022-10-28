
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
        return f'{number1} times {number2} is {str(total)}'
    else: 
        return f'Invalid inputs. Please try again by entering 2 numbers!'


# Write a route, sayntimes, that will repeat a string a given number of times. It should use the URL /sayntimes/<word>/<n>. For example:

# If I go to the URL /sayntimes/hello/6, I should see the result: hello hello hello hello hello hello
# If I go to the URL /sayntimes/world/3, I should see the result: world world world
# If I go to the URL /sayntimes/hello/world, I should see the result: Invalid input. Please try again by entering a word and a number!
# HINT: Use a for loop to add up lots of small strings into one large string!

# Try out your route in the browser! What happens when you use a very large number (e.g. 1000000)?

# Say n times 
# come back to this (look at type method )
@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n): 
    word_list = " "
    # n = int(n)

    # if n == (type(int)) and word_list == (type(str)): 
    #     for i in range(n):
    #         word_list += (" " + word)
    #         return word_list 
    # else: 
    #     return f'Please try entering a word and a number!'

    if n.isnumeric():
        n = int(n)
        for i in range(n):
            word_list += (" " + word)
        return word_list 
    else: 
        return f'Please try entering a word and a number!'




# dice game
@app.route('/dicegame')
def dice_game(): 
    import random
    n = random.randint(0,6)
    

    if n == 6: 
       return f'You win'
    else:
       return  f'You lose'
    # return str(n)
    

if __name__ == '__main__':
    app.run(debug=True)


