import csv

def display_list(list):
    print(list)

def load_data():
    csvfile = open('31118270.csv')
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        print(', '.join(row))

def look_up_use_of_birth_control_by_education_level(educationLevel):
    #This and look_up_use_of_birth_control_by_religion should be combined because
    #they are repetitive...how can we do this and know which column to access?
    user_ids = get_user_ids_by_column("educ", educationLevel)
    get_use_of_birth_control(user_ids)

def look_up_use_of_birth_control_by_religion(religion):
    user_ids = get_user_ids_by_column("religion", religion)
    get_use_of_birth_control(user_ids)

def get_user_ids_by_column(col, topic):
    #How to access data by column and add it to a list?

def get_use_of_birth_control(user_ids):
    #This is doing more than one thing. When/how/where do we call display_list?
    birt3_answers = []
    for user in user_ids:
        #access birt3 column and append item to list
        birt3_answers.append()
    display_list(birt3_answers)

def main():
    load_data()

if __name__ == "__main__":
    main()
