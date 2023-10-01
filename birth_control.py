import csv
import argparse

data = []

def display_list(list):
    """outputs results to user"""
    print(list)

#done
def load_data():
    """loads data from csv file into list of strings"""
    csvfile = open('birthcontroldata.csv')
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        data.append(row)

def look_up_use_of_birth_control_by_education_level(educationLevel):
    """calls the functions to get the birth control use for inputted education level"""
    user_ids=get_user_ids_by_column_for_educ(educationLevel)
    get_use_of_birth_control(user_ids)

def look_up_use_of_birth_control_by_religion(religion):
    """calls the functions to get the birth control use for inputted religion"""
    user_ids = get_user_ids_by_column_for_religion(religion)
    get_use_of_birth_control(user_ids)

def get_user_ids_by_column_for_educ(topic):
    """searches csv file matching education level and returns list of ids that match with it"""
    user_ids = []
    for row in data:
        if (row[21]) == topic:
          user_ids.append(row[0])
    if user_ids==[]:
        raise IndexError("Education level not in dataset")
    return user_ids

def get_user_ids_by_column_for_religion(topic):
    """searches csv file matching religion and returns list of ids that match with it"""
    user_ids = []
    for row in data:
        if (row[32]) == topic:
          user_ids.append(row[0])
    if user_ids==[]:
        raise IndexError("Religion not in dataset")
    return user_ids

def get_use_of_birth_control(user_ids):
    """takes returned user_id list and gets the birth control use for each id and adds it to list"""
    birt3_answers = []
    for user in user_ids:
        for row in data:
        #access birt3 column and append item to list
            if (row[0]==user):
                birt3_answers.append(row[45])
    display_list(birt3_answers)

def main():
    """creates command line interface for user to ask for specific religion or education and get the birth control use"""
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