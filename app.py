from flask import Flask, render_template
from ProductionCode.birth_control import *


app = Flask(__name__)

@app.route('/')
def homepage():
    """
    Sets up a home page for the server with information on how
    to navigate and operate the server using parameters. This also
    shows the user how to access more details on how to use the site.
    Returns the text to be viewed on the home page in the browser.

    Thank you to Anna Fitzgerald from blog.hubspot.com for the information
    on how to change the fonts in HTML, and to stackoverflow.com for the
    information as to how to include new lines (breaks) and indentation in the browser.
    """

    return "This is the homepage for Team D's Project Component #2.\
    To see how often people of a certain demographic use birth control\
    when they are not trying to get pregnant, add /[DEMOGRAPHIC] to the current url.\
            Here are some demographic ideas to input:<br><pre><font face=\"Times New Roman\">\
            * state abbreviation (ex. MN, MA, HI)<br>\
            * religion (ex. Hindu, Protestant, Jewish/Judaism, etc)<br>\
            * education level<br>\
                - Two year associate degree from a college or university<br>\
                - High school graduate (Grade 12 with diploma or GED certificate)<br></pre></font>"

@app.route('/options', strict_slashes = False)
def get_parameter_options():
    """
    Returns a string of more parameter options by category
    to be displayed in the browser.
    """

    return "<h1>More Parameter Options</h1><br>\
        To see the responses, add /[yourParameterHere] to the current URL.\
            <h3>Religions</h3>"

@app.route('/<demographic>', strict_slashes = False)
def get_birth_control_use_by_demographic(demographic):
    """
    Returns a list of the responses to the question "How often do you
    use birth control when not trying to get pregnant?" from the csv
    based upon the demographic that is passed in. 

        Parameters:
            reponses = the list of responses to the question above
            
    Returns the string version of that list of responses.
    """

    responses = look_up_use_of_birth_control_by_demographic(demographic)
    #return render_template('index.html', resp = responses) 
    return responses

@app.errorhandler(404)
def page_not_found(e):
    """ Returns a statement with the correct formatting when an external error is encountered. """
    return "Oops! You've encountered and error. Double check your spelling and \
        make sure to follow the format from the homepage\
        by adding /[DEMOGRAPHIC] to the url! If you follow these directions and\
            encounter an empty list, your demographic is not included in the dataset."

@app.errorhandler(500)
def python_bug(e):
    """ Returns a message when there is an internal error. """
    return "Eek, a bug!"

if __name__ == '__main__':
    load_data()
    app.run()