from flask import Flask, redirect, render_template, request, url_for
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
    return render_template('homepage.html')

"""This is the page that allows the users to look up for the results of birth control use by their input of a demographic value"""
@app.route('/birth-control-use', strict_slashes=False, methods=['GET', 'POST'])
def get_birth_control_use():
    if request.method == 'POST':
        demographic = request.form.get('demographic')
        if demographic:
            return redirect(url_for('get_birth_control_use_by_demographic', demographic=demographic))
        else:
            return "Invalid input. Please provide a valid demographic value."

    return render_template('search.html',header="Birth Control Use By Demographic",description="Search a demographic to analyze how often that subset using birth control during sex when not trying to reproduce")

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
        use=data_accessor.look_up_use_of_birth_control_by_demographic(demographic)
        displaylist={}
        return render_template('datapage.html',title2="Birth Control Use by Demographic",header2=demographic, question= "Birth Control Use", displaylist=use)
    else:
        return "Invalid Input. The demographic you chose is not in our dataset. Plase try another one."

"""This is the page that allows the users to look up for the results of birth control accesses by their input of a demographic value"""    
@app.route('/birth-control-access', strict_slashes=False, methods=['GET', 'POST'])
def get_birth_control_access():
    if request.method == 'POST':
        demographic = request.form.get('demographic')
        if demographic:
            return redirect(url_for('get_birth_control_access_concerns_by_demographic', demographic=demographic))
        else:
            return "Invalid input. Please provide a valid demographic value."

    return render_template('search.html',header="Birth Control Access by Demographic",description="Search a demographic to analyze how concerned that subset is over birth control acess policy today" )


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
        concerns=data_accessor.look_up_birth_control_access_concerns_by_demographic(demographic)
        x=data_accessor.xvals(concerns)
        y=data_accessor.yvals(concerns)
        return render_template('datapage.html',title2="Birth Control Policy Concerns by Demographic",header2=demographic,question="Birth Control Access", displaylist=concerns,xValues=x,yValues=y)
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