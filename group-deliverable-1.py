import csv

data = []

def display_list(list):
    print(list)

def load_data():
    csvfile = open('birthcontroldata.csv')
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        #print(', '.join(row))
        data.append(row)
    #print(data)

def look_up_use_of_birth_control_by_education_level(educationLevel):
    user_ids = get_user_ids_by_column(educationLevel)
    #get_use_of_birth_control(user_ids)

def look_up_use_of_birth_control_by_religion(religion):
    user_ids = get_user_ids_by_column("religion", religion)
    #get_use_of_birth_control(user_ids)

def get_user_ids_by_column(topic):
    educationData = []
    for row in data:
        print(data[row, 21])
        #if (row, 21) == topic:
            #educationData.append((row, 0))
    #print(educationData)
            

#def get_use_of_birth_control(user_ids):
    #This is doing more than one thing. When/how/where do we call display_list?
    #birt3_answers = []
    #for user in user_ids:
        #access birt3 column and append item to list
        #birt3_answers.append()
    #display_list(birt3_answers)

def main():
    load_data()
    look_up_use_of_birth_control_by_education_level('Four year college or university degree/Bachelor.s degree (e.g., BS, BA, AB)')

if __name__ == "__main__":
    main()
