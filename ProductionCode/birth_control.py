import csv
import argparse
import sys


data = []

def display_results(totaled_answers):
    """
    Iterates through a dictionary to output the dataset answers
    and their percentage values to the user. Returns totaled_answers,
    which is the dictionary of possible answers and their percentages.
    The parameter being passed in is the same as totaled_answers above.
    """
    for key in totaled_answers:
        print(key, ":",totaled_answers[key], "%")
    return totaled_answers

def load_data():
    """
    Opens birthcontroldata.csv and reads it into a list of lists.
    """
    data.clear()
    csvfile = open('Data/birthcontroldata.csv')
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        data.append(row)
    csvfile.close()

def look_up_use_of_birth_control_by_demographic(demographic):
    """
    Retrieves the user ids of the specified demographic in order to
    total up the use of birth control for those user ids. Then, the results
    are counted and displayed as percentages. 
            Parameters:
                demographic = the string demographic the user selected and put
                in either the command line or the url. 
    Returns the dictionary of answers and their percentage results after being displayed. 
    """
    user_ids = get_user_ids_by_column(demographic)
    responses = get_use_of_birth_control(user_ids)
    results = count_birth_control_use_answers(responses)
    percent_results = calc_percentage(results)
    return display_results(percent_results)

def look_up_birth_control_access_concerns_by_demographic(demographic):
    """
    Retrieves the user ids of the specified demographic in order to
    total up the answers for the concern level of access to birth control
    for those user ids. Then, the results are counted and displayed as percentages. 
            Parameters:
                demographic = the string demographic the user selected and put
                in either the command line or the url. 
    Returns the dictionary of answers and their percentage results after being displayed. 
    """
    user_ids = get_user_ids_by_column(demographic)
    responses = get_birth_control_access_concerns(user_ids)
    results = count_birth_control_access_answers(responses)
    percent_results = calc_percentage(results)
    return display_results(percent_results)

def get_user_ids_by_column(topic):
    """
    Iterates through and searches the list of lists named data in order
    to create a list of the user ids who are part of the appropriate demographic.
        Parameters:
            topic = the string demographic of people in the dataset whose user ids will be
            appended to the user_ids list.
    Returns the list of user_ids with the requested demographic.
    """
    user_ids = []
    for row in data:
        for item in row:
            #if item == topic:
            item=item.lower()
            if topic.lower() in item:
                user_ids.append(row[0])
    if user_ids==[]:
        print("Sorry, this demographic is not in the dataset.")
    return user_ids

def get_use_of_birth_control(user_ids):
    """
    Iterates through the list of user ids and creates a list of their
    answers to the appropriate question in the dataset.
        Parameters:
            user_ids = the list of user_ids of the appropriate demographic.
    Returns the list of answers to the question about how often birth control is used.
    """
    birt3_answers = []
    for user in user_ids:
        for row in data:
        #access birt3 column and append item to list
            if (row[0]==user):
                birt3_answers.append(row[45])
    if user_ids == []:
        print("List is empty")
    return birt3_answers

def get_birth_control_access_concerns(user_ids):
    """
    Iterates through the list of user ids and creates a list of their
    answers to the appropriate question in the dataset.
        Parameters:
            user_ids = the list of user_ids of the appropriate demographic.
    Returns the list of answers to the question about how concerned the person is
    regarding future access to birth control considering the recent political climate.
    """
    birt7_answers = []
    for user in user_ids:
        for row in data:
            if (row[0]==user):
                birt7_answers.append(row[58])
    if user_ids == []:
        print("List is empty")
    return birt7_answers

def count_birth_control_use_answers(birt3_answers):
    """
    Counts the amount of each possible response to the birt3 question in the dataset
    regarding birth control use for the appropriate list of users based on inputted demographic.
    Then, compiles a dictionary of each possible response and the amount of times that
    response was chosen. 
        Parameters:
            birt3_answers = the list of answers to the question about birth control use
            from the people in the specified demographic.
    Returns the dictionary totaled_answers which includes the amount of each possible response
    for the question of birth control use.
    """
    never=0
    na=0
    always=0
    half=0
    some=0
    almost=0
    refused=0

    totaled_answers={}
    for item in birt3_answers:
        if item == "Never":
            never=never+1
        elif item== "Not applicable/Does not have vaginal intercourse/sex":
            na= na+1
        elif item == "Every time":
            always= always+1
        elif item == "About half the time":
            half=half+1
        elif item== "Once in a while":
            some= some+1
        elif item == "Almost every time":
            almost= almost+1
        else:
            refused=refused+1
    totaled_answers["Never"]=never
    totaled_answers["Not applicable/Does not have vaginal intercourse/sex"]=na
    totaled_answers["Every time"]=always
    totaled_answers["About half the time"]=half
    totaled_answers["Once in a while"]=some
    totaled_answers["Almost every time"]=almost
    return totaled_answers

def count_birth_control_access_answers(birt7_answers):
    """
    Counts the amount of each possible response to the birt7 question in the dataset
    regarding concerns about future access to birth control for the appropriate list 
    of users based on inputted demographic.Then, compiles a dictionary of each possible 
    response and the amount of times that response was chosen. 
        Parameters:
            birt7_answers = the list of answers to the question about birth control access concerns
            from the people in the specified demographic.
    Returns the dictionary totaled_answers which includes the amount of each possible response
    for the question of birth control access concerns.
    """
    veryConcerned=0
    somewhatConcerned=0
    notVeryConcerned=0
    notAtAllConcerned=0
    notApplicable=0
    dontKnow=0
    refused=0

    totaled_answers={}
    for item in birt7_answers:
        if item == "Very concerned":
            veryConcerned=veryConcerned+1
        elif item== "Not applicable/don't believe in birth control":
            notApplicable= notApplicable+1
        elif item == "Somewhat concerned":
            somewhatConcerned= somewhatConcerned+1
        elif item == "Not very concerned":
            notVeryConcerned=notVeryConcerned+1
        elif item== "Not at all concerned":
            notAtAllConcerned=notAtAllConcerned+1
        elif item == "Don't know":
            dontKnow=dontKnow+1
        else:
            refused=refused+1
    totaled_answers["Very concerned"]=veryConcerned
    totaled_answers["Not applicable/don't believe in birth control"]=notApplicable
    totaled_answers["Somewhat concerned"]=somewhatConcerned
    totaled_answers["Not very concerned"]=notVeryConcerned
    totaled_answers["Not at all concerned"]=notAtAllConcerned
    totaled_answers["Don't know"]=dontKnow
    totaled_answers["Refused"]=refused
    return totaled_answers

def calc_percentage(totaled_answers):
    """
    Calculates the percentage of each possible response to the question in the dataset.
        Parameters:
            totaled_answers = the dictionary including each possible response and the
            amount of times that response was chosen by people in the dataset.
    Returns the same dictionary, but formatted based upon percentages instead of total responses.
    """
    total=0
    for key in totaled_answers:
        total=total+totaled_answers[key]
    for key in totaled_answers:
        if total!=0:   
            totaled_answers[key]= round((totaled_answers[key]/total)*100)
    return totaled_answers

def setUpParser():
    """Set up the search options that users could use. Take in the users' input and then return it."""
    parser = argparse.ArgumentParser(description="Search for participants and filter by demographic")
    parser.add_argument("--BirthControlUseByDemo",help="Specific subset within demographic to search for")
    parser.add_argument("--BirthControlAccessByDemo",help="Specific subset within demographic to search for")
    parser.add_argument("--option", action="store_true", help="list all options for the demographic")
    args= parser.parse_args()
    return args


def runMain():
    """calling different functions to give the correct information to users according to the different input from users """
    args= setUpParser()
    if args.BirthControlUseByDemo:
        print("How often do you use birth control? Demographic:", args.BirthControlUseByDemo)
        look_up_use_of_birth_control_by_demographic(args.BirthControlUseByDemo)
    elif args.BirthControlAccessByDemo:
        print("Given the current political climate(2020), are you concerned with birth control access in the future? Demographic:", args.BirthControlAccessByDemo)
        look_up_birth_control_access_concerns_by_demographic(args.BirthControlAccessByDemo)
    elif args.option:
        optionsDisplay()
    else:
        Usage()

def optionsDisplay():
    """shows users all demographic options they could search for when they type in --option"""
    option= """Demographic Options: State:MA,MN...\n 
        Region:North East, South... \n 
        Own home: Owned, Rented \n 
        Marital Status: never married, Widowed,Married, Divorced, Single \n 
        Employ: Retired, Homemaker, Full-time, Part-time, Other, Temporarily unemployed, Disabled \n
        Education: Four year college, High School graduate, Some college, Two year associate degree, Postgraduate or professional degree,Some postgraduate or professional schooling, Refused, Less than high school \n 
        Race: White Non-Hispanic, Native American, White Hispanic,Black Non-Hispanic, Mixed, Asian, Refused, Black Hispanic \n 
        Political party: An Independant, A Republican, A Democrat, Refused \n
        Political View: Somewhat conservative, Moderate, Somewhat liberal, Very liberal, Very conservative, Refused \n
        Religion:Protestant, Orthodox, Jewish, Catholic, Christian, Methodist, Baptist, Unitarian, Mormon, Agnostic, Jehovah's Witness, Episcopalian, Athiest, Nothing, Pentacostal \n 
        Insured: covered by health insurance, not covered by health insurance, Don't know"""

    print(option)

def Usage():
    """print an usage message if the users did not use the correct format for searching"""
    usage="Usage: python3 ProductionCode/birth_control.py --BirthControlUseByDemo or --BirthContolAccessByDemo 'the specific demographic you wanna search for' . Try python3 ProductionCode/birth_control.py --option for all demographic options you could search."
    print(usage)
        


def main():
    
    """
    load the data and return information according to the users' inputs.
    """
    load_data()
    runMain()

 
if __name__ == "__main__":
    main()