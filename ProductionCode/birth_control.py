import csv
import argparse


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
            if item == topic:
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
            dontknow=dontknow+1
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
        totaled_answers[key]= round((totaled_answers[key]/total)*100)
    return totaled_answers

def main():
    
# print usage/help statement function 
# need to make our command line interface work with all demographics
# fix tests
# needs to print without command line args
    """
    Creates the command line interface for the user to ask for specific religion or education and get the birth control use.
    """
    load_data()
    parser = argparse.ArgumentParser(description="Search for participants and filter by state, religion, or political view")
    parser.add_argument("--educ", help="Educational level of participants to search for")
    parser.add_argument("--religion", help="Religion of participants to search for")

    args = parser.parse_args()
    if args.religion:
        look_up_use_of_birth_control_by_demographic(args.religion)
    elif args.educ:
        look_up_use_of_birth_control_by_demographic(args.educ)
    else:
        print("You must provide one of the valid command line arguments.")


if __name__ == "__main__":
    main()