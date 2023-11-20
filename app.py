from flask import Flask, redirect, render_template, request, url_for, json
from ProductionCode.birth_control import *
from ProductionCode.datasource import *

data_accessor = BirthControl()

app = Flask(__name__)

"""Displays two question options"""
@app.route('/')
def homepage():
    return render_template('homepage.html')

"""Allows the users to look up for the results of birth control use by their input of a demographic value"""
@app.route('/birth-control-use',methods=['GET','POST'])
def get_birth_control_use():
    if request.method == 'POST':
        category = request.form.get('category')
        if category == 'Religion':
            return redirect(url_for('search_birth_control_use_by_religion'))
        elif category == "PoliticalParty":
            return redirect(url_for('search_birth_control_use_by_poliParty'))
        else:
            return render_template('notFound.html')
    return render_template('search_use.html', header="Birth Control Use By Demographic", 
                           description="When not trying to get pregnant, how often, if at all, do you use some form of birth control such as birth control pills or condoms when you have vaginal intercourse?")

"""Intermediate page for religion"""
@app.route('/birth-control-use/religion', methods=['GET', 'POST'])
def search_birth_control_use_by_religion():
    if request.method == 'POST':
        religion = request.form.get('demographic')
        return redirect(url_for('get_birth_control_use_by_religion', demographic=religion))
    return render_template('religion_use.html', description="Search for the results of your question in Religion")
    
@app.route('/birth-control-use/religion/<demographic>', strict_slashes = False)
def get_birth_control_use_by_religion(demographic):
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
    use=data_accessor.get_use_of_birth_control_by_demographic(demographic)
    keys=[]
    vals=[]
    for key in use:
        keys.append(key)
    for key in use: 
        vals.append(use[key])
    x=json.dumps(keys)
    y=json.dumps(vals)
    displaylist={}
    if demographic:
        return render_template('datapage.html',title2="Birth Control Use by Demographic",subset=demographic, question= "How often do you use birth control when not trying to get pregnant?", displaylist=use, xValues=x, yValues=y)
    else:
        return render_template('notFound.html')


"""Intermediate page for politcalparty"""
@app.route('/birth-control-use/politicalparty', methods=['GET', 'POST'])
def search_birth_control_use_by_poliParty():
    if request.method == 'POST':
        poliParty = request.form.get('demographic')
        return redirect(url_for('get_birth_control_use_by_poliParty', demographic=poliParty))
    return render_template('poliParty_use.html', description="Search for the results of your question in Political Party")
    
@app.route('/birth-control-use/politicalparty/<demographic>', strict_slashes = False)
def get_birth_control_use_by_poliParty(demographic):
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
    use=data_accessor.get_use_of_birth_control_by_demographic(demographic)
    keys=[]
    vals=[]
    for key in use:
        keys.append(key)
    for key in use: 
        vals.append(use[key])
    x=json.dumps(keys)
    y=json.dumps(vals)
    displaylist={}
    if demographic:
        return render_template('datapage.html',title2="Birth Control Use by Demographic",subset=demographic, question= "How often do you use birth control when not trying to get pregnant?", displaylist=use, xValues=x, yValues=y)
    else:
        return render_template('notFound.html')


"""Allows the users to look up for the results of birth control accesses by their input of a demographic value"""    
@app.route('/birth-control-access', strict_slashes=False, methods=['GET', 'POST'])
def get_birth_control_access():
    if request.method == 'POST':
        demographic = request.form.get('demographic')
        if demographic:
            return redirect(url_for('get_birth_control_access_concerns_by_demographic', demographic=demographic))
        else:
            return render_template('notFound.html')

    return render_template('search_access.html',header="Birth Control Access by Demographic",description="With the passing of Supreme Court Justice Ruth Bader Ginsburg there is now a vacancy on the supreme court. How concerned, if at all, are you about the upcoming change to the Supreme Court impacting your ability to afford or access your preferred birth control method?",rows=['Political view','Relgion'])


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
    concerns=data_accessor.get_birth_control_access_concerns_by_demographic(demographic)
    keys=[]
    vals=[]
    for key in concerns:
        keys.append(key)
    for key in concerns: 
        vals.append(concerns[key])
    x=json.dumps(keys)
    y=json.dumps(vals)
    if demographic:
        return render_template('datapage.html',title2="Birth Control Policy Concerns by Demographic",subset=demographic,question="How concerned are you about the upcoming change to the Supreme Court impacting your ability to afford or access your preferred birth control method?", displaylist=concerns, xValues=x, yValues=y)
    else:
        return render_template('notFound.html')


@app.errorhandler(404)
def page_not_found(e):
    """ Returns a statement with the instructions when an external error is encountered. """
    
    return render_template('notFound.html')

@app.route('/about',strict_slashes=False)
def aboutPage():
    return render_template('about.html')
   

@app.errorhandler(500)
def python_bug(e):
    """ Returns a message when there is an internal error. """
    return "Eek, a bug! Make sure to double check your spelling\
        and follow the format from the homepage by adding either\
            /birth-control-use/[DEMOGRAPHIC] or /birth-control-access/[DEMOGRAPHIC]\
                to the url. Head back to the homepage if you need demographic ideas."

if __name__ == '__main__':
    data_accessor.load_data()
    app.run(port=5125,host='0.0.0.0',debug=False)