import csv
import argparse

def load_participants_from_csv(csv_file):
    participants = []
    with open(csv_file, mode='r', newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            participants.append(row)
    return participants

def search_use_of_control_(participants, target_educ):
    matching_uses = []
    for participant in participants:
        if 'educ' in participant:
            educ_value = participant['educ'].strip()
            if educ_value == target_educ.strip():
                matching_uses.append(participant['birt3'])
    return matching_uses

def main():
    parser = argparse.ArgumentParser(description="Search for uses of control by education levels in birthcontrol.csv")
    parser.add_argument("--educ", required=True, help="educational level of participants to search for")
    args = parser.parse_args()

    csv_file = "birthcontrol.csv"
    participants = load_participants_from_csv(csv_file)
  
    matching_uses = search_use_of_control_(participants, args.educ)
    
    if matching_uses:
        print(f"Birth control use of people with the educational level '{args.educ}':")
        for use in matching_uses:
            print(use)
    else:
        print(f"No people found with the educational level '{args.educ}'")

if __name__ == "__main__":
    main()
