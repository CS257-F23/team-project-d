import argparse
import sys
from ProductionCode.birth_control import *

data_accessor = BirthControl()

def setUpParser(command):
    """
    Sets up the parser component by adding and returning the args
    """
    parser = argparse.ArgumentParser(description="Search for participants and filter by demographic")
    parser.add_argument("--BirthControlUseByDemo",help="Specific subset within demographic to search for")
    parser.add_argument("--BirthControlAccessByDemo",help="Specific subset within demographic to search for")
    parser.add_argument("--option", action="store_true", help="list all options for the demographic")
    args= parser.parse_args()
    return args


def runMain():
    """
    Determines the args being input and calls the correct function based on the input
    If input does not match a listed option, the usage statement is printed
    """
    args= setUpParser(sys.argv)
    if args.BirthControlUseByDemo:
        print("How often do you use birth control when not trying to get pregnant? Demographic:", args.BirthControlUseByDemo)
        data_accessor.get_use_of_birth_control_by_demographic(args.BirthControlUseByDemo)
    elif args.BirthControlAccessByDemo:
        print("Given the current political climate (2020), how concerned are you with birth control access in the future? Demographic:", args.BirthControlAccessByDemo)
        data_accessor.get_birth_control_access_concerns_by_demographic(args.BirthControlAccessByDemo)
    elif args.option:
        optionsDisplay()
    else:
        Usage()

def optionsDisplay():
    """
    Displays and returns a string of possible input options.
    """
    option= """Demographic Options: State:MA,MN...\n 
        Region:North East, South... \n 
        Own home: Owned, Rented \n 
        Marital Status: never married, Widowed, Married, Divorced, Single \n 
        Employ: Retired, Homemaker, Full-time, Part-time, Other, Temporarily unemployed, Disabled \n
        Education: Four year college, High School graduate, Some college, Two year associate degree, Postgraduate or professional degree,Some postgraduate or professional schooling, Refused, Less than high school \n 
        Race: White Non-Hispanic, Native American, White Hispanic,Black Non-Hispanic, Mixed, Asian, Refused, Black Hispanic \n 
        Political party: An Independent, A Republican, A Democrat, Refused \n
        Political View: Somewhat conservative, Moderate, Somewhat liberal, Very liberal, Very conservative, Refused \n
        Religion:Protestant, Orthodox, Jewish, Catholic, Christian, Methodist, Baptist, Unitarian, Mormon, Agnostic, Jehovah's Witness, Episcopalian, Athiest, Nothing, Pentecostal \n 
        Insured: covered by health insurance, not covered by health insurance, Don't know"""

    print(option)
    return option

def Usage():
    """
    Displays and returns a string usage statement.
    """
    usage="Usage: python3 cl.py --BirthControlUseByDemo or --BirthControlAccessByDemo 'the specific demographic you are searching for' . Try python3 cl.py --option for all demographic options you could search."
    print(usage)
    return usage
        


def main():
    
    """
    Creates the command line interface for the user to ask for specific religion or education and get the birth control use.
    """
    runMain()

    

 
if __name__ == "__main__":
    main()