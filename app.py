from flask import Flask#, render_template
from ProductionCode.birth_control import *


data_accessor = BirthControl()

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
    when they are not trying to get pregnant, add /birth-control-use/[DEMOGRAPHIC] to the current url.\
    To see how concerned people of a certain demographic are about future access to birth control\
    due to the political climate, add /birth-control-access/[DEMOGRAPHIC] to the current url.\
            Here are some demographic ideas to input:<br><pre><font face=\"Times New Roman\">\
            * state abbreviation (ex. MN, MA, HI)<br>\
            * religion (ex. Hindu, Protestant, Jewish/Judaism, etc)<br>\
            * education level<br>\
                - Two year associate degree from a college or university<br>\
                - High school graduate (Grade 12 with diploma or GED certificate)<br></pre></font>"

@app.route('/birth-control-use/<demographic>', strict_slashes = False)
def get_birth_control_use_by_demographic(demographic):
    """
    Returns a list of the responses to the question "How often do you
    use birth control when not trying to get pregnant?" from the csv
    based upon the demographic that is passed in. 

        Parameters:
            demographic = the demographic that was passed in;\
            all output will be from people in that demographic.
        
        Variables:
            reponses = the list of responses to the question above
            
    Returns the string version of that list of responses.
    """
    user_ids = data_accessor.get_user_ids_by_column(demographic)
    if user_ids != []:
        return data_accessor.look_up_use_of_birth_control_by_demographic(demographic)
    else:
        return "Invalid Input. The demographic you chose is not in our dataset. Plase try another one."

@app.route('/birth-control-access/<demographic>', strict_slashes = False)
def get_birth_control_access_concerns_by_demographic(demographic):
    """
    Returns a list of the responses to the question "How concerned, if at all, are you that \
    women may not be able to access the full range of birth control methods, such as oral \
    contraceptives, implants, and IUDs in the future because of changes in the political landscape?"\
    from the csv based on the demographic that is passed in.
    
        Parameters:
            demographic = the user's chosen demographic that they passed in via the url;
            all output will be based off of responsers with  this demographic.
            
        Variables:
            responses = the list of responses to the question above.
            
    Return the string version of that list of responses.
    """
    user_ids = data_accessor.get_user_ids_by_column(demographic)
    if user_ids != []:
        return data_accessor.look_up_birth_control_access_concerns_by_demographic(demographic)
    else:
        return "Invalid Input. The demographic you chose is not in our dataset. Plase try another one."



@app.errorhandler(404)
def page_not_found(e):
    """ Returns a statement with the correct formatting when an external error is encountered. """
    return "Oops! You've encountered an error. Double check your spelling and \
        make sure to follow the format from the homepage\
        by adding either /birth-control-use/[DEMOGRAPHIC] or /birth-control-access/[DEMOGRAPHIC] \
            to the url! Head back to the homepage if you need demographic ideas. \
                If you follow these directions and\
            encounter an empty list, your demographic is not included in the dataset."

@app.errorhandler(500)
def python_bug(e):
    """ Returns a message when there is an internal error. """
    return "Eek, a bug! Make sure to double check your spelling\
        and follow the format from the homepage by adding either\
            /birth-control-use/[DEMOGRAPHIC] or /birth-control-access/[DEMOGRAPHIC]\
                to the url. Head back to the homepage if you need demographic ideas."

if __name__ == '__main__':
    data_accessor.load_data()
    app.run()