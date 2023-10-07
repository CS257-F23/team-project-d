import csv
import argparse

# Add another functionality
# print usage/help statenent function 
# add what the parameters and output is in each docstring to make them clearer
# need to make our command line interface work with all demographics
# test main is not working
#needs to print without command line args

data = []

def display_results(totaled_answers):
    """outputs results to user"""
    for key in totaled_answers:
        print(key, ":",totaled_answers[key], "%")
    return totaled_answers

def load_data():
    """loads data from csv file into list of strings"""
    data.clear()
    csvfile = open('Data/birthcontroldata.csv')
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        data.append(row)
    csvfile.close()

def look_up_use_of_birth_control_by_demographic(demographic):
    """calls the functions to get the birth control use for inputted religion"""
    user_ids = get_user_ids_by_column(demographic)
    responses = get_use_of_birth_control(user_ids)
    results = count_answers(responses)
    percent_results = calc_percentage(results)
    return display_results(percent_results)

def look_up_abortion_concerns_by_demographic(demographic):
    user_ids = get_user_ids_by_column(demographic)
    responses = get_political_abortion_concerns(user_ids)
    return display_results(responses)

def get_user_ids_by_column(topic):
    """searches csv file matching religion and returns list of ids that match with it"""
    user_ids = []
    for row in data:
        for item in row:
            if item == topic:
                user_ids.append(row[0])
    if user_ids==[]:
        print("Sorry, this demographic is not in the dataset.")
    return user_ids

def get_use_of_birth_control(user_ids):
    """takes returned user_id list and gets the birth control use for each id and adds it to list"""
    birt3_answers = []
    for user in user_ids:
        for row in data:
        #access birt3 column and append item to list
            if (row[0]==user):
                birt3_answers.append(row[45])
    if user_ids == []:
        print("List is empty")
    return birt3_answers

def get_political_abortion_concerns(user_ids):
    birt7_answers = []
    for user in user_ids:
        for row in data:
            if (row[0]==user):
                birt7_answers.append(row[58])
    if user_ids == []:
        print("List is empty")
    return birt7_answers

def count_answers(birt3_answers):
    """adds up number of users in specified demographic for each possible answer to birt3 question"""
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

def calc_percentage(totaled_answers):
    """takes in dictionary with totaled answers and calculates the percentage using total number of responses"""
    total=0
    for key in totaled_answers:
        total=total+totaled_answers[key]
    for key in totaled_answers:
        totaled_answers[key]= round((totaled_answers[key]/total)*100)
    return totaled_answers

def main():
    """creates command line interface for user to ask for specific religion or education and get the birth control use"""
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