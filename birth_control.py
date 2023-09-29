import csv
import argparse

data = []

def display_list(list):
    print(list)

#done
def load_data():
    csvfile = open('birthcontroldata.csv')
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        data.append(row)

def look_up_use_of_birth_control_by_education_level(educationLevel):
    user_ids=get_user_ids_by_column_for_educ(educationLevel)
    get_use_of_birth_control(user_ids)

def look_up_use_of_birth_control_by_religion(religion):
    user_ids = get_user_ids_by_column_for_religion(religion)
    get_use_of_birth_control(user_ids)

def get_user_ids_by_column_for_educ(topic):
    user_ids = []
    for row in data:
        if (row[21]) == topic:
          user_ids.append(row[0])
    #print(user_ids)
    return user_ids

def get_user_ids_by_column_for_religion(topic):
    user_ids = []
    for row in data:
        if (row[32]) == topic:
          user_ids.append(row[0])
    return user_ids

def get_use_of_birth_control(user_ids):
    #This is doing more than one thing. When/how/where do we call display_list?
    birt3_answers = []
    for user in user_ids:
        for row in data:
        #access birt3 column and append item to list
            if (row[0]==user):
                birt3_answers.append(row[45])
    #display_list(birt3_answers)
    display_list(birt3_answers)

def main():
    load_data()
    parser = argparse.ArgumentParser(description="Search for participants and filter by state, religion, or political view")
    parser.add_argument("--educ", help="Educational level of participants to search for")
    parser.add_argument("--religion", help="Religion of participants to search for")

    args = parser.parse_args()
    if args.religion:
        look_up_use_of_birth_control_by_religion(args.religion)
    elif args.educ:
        look_up_use_of_birth_control_by_education_level(args.educ)
    else:
        print("You must provide one of the valid command line arguments.")



if __name__ == "__main__":
    main()