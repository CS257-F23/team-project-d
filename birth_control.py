
import csv
import argparse
def load_participants_from_csv(csv_file):
    participants = []
    with open(csv_file, mode='r', newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            participants.append(row)
    return participants
def search_participants(participants, field_name, target_value, result_field):
    matching_results = []
    for participant in participants:
        if participant[field_name] == target_value:
            matching_results.append(participant[result_field])
    return matching_results
def main():
    parser = argparse.ArgumentParser(description="Search for participants and filter by state, religion, or political view")
    parser.add_argument("--educ", help="Educational level of participants to search for")
    parser.add_argument("--religion", help="Religion of participants to search for")
    parser.add_argument("--state", help="State abbreviation to filter by")
    parser.add_argument("--political", help="Political view of participants to search for")
    args = parser.parse_args()
    csv_file = "birthcontrol.csv"
    participants = load_participants_from_csv(csv_file)
    search_field = None
    search_value = None
    result_field = None
    if args.educ:
        search_field = "educ"
        search_value = args.educ
        result_field = "birt3"
    elif args.religion:
        search_field = "religion"
        search_value = args.religion
        result_field = "birt3"
    elif args.state:
        search_field = "state"
        search_value = args.state
        result_field = "birt6a"
    elif args.political:
        search_field = "polview"
        search_value = args.political
        result_field = "birt7"
    if search_field and search_value:
        matching_results = search_participants(participants, search_field, search_value, result_field)
        if matching_results:
            print(f"Results for {search_field} '{search_value}':")
            for result in matching_results:
                print(result)
        else:
            print(f"No information found for {search_field} '{search_value}'")
    else:
        print("You must provide one of the valid command line arguments.")
if __name__ == "__main__":
    main()