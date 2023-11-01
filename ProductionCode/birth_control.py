import csv

class BirthControl:

    def __init__(self):

        self.data = []
        self.load_data()

    def display_results(self, totaled_answers):
        """
        Iterates through a dictionary to output the dataset answers
        and their percentage values to the user. Returns totaled_answers,
        which is the dictionary of possible answers and their percentages.
        The parameter being passed in is the same as totaled_answers above.
        """
        for response in totaled_answers:
            print(response, ":",totaled_answers[response], "%")
        return totaled_answers
    

    #TODO: rename xvals and yvals to be more meaningful, same with key, vals could be values
    def xvals(self, totaled_answers):
        keys=[]
        for key in totaled_answers:
            keys.append(key)
        return keys
    def yvals(self,totaled_answers):
        vals=[]
        for key in totaled_answers:
            vals.append(totaled_answers[key])
        return vals

    def load_data(self):
        """
        Opens birthcontroldata.csv and reads it into a list of lists.
        """
        self.data.clear()
        csvfile = open('Data/birthcontroldata.csv')
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            self.data.append(row)
        csvfile.close()

    def get_use_of_birth_control_by_demographic(self, demographic):
        """
        Retrieves the user ids of the specified demographic in order to
        total up the use of birth control for those user ids. Then, the results
        are counted and displayed as percentages. 
                Parameters:
                    demographic = the string demographic the user selected and put
                    in either the command line or the url. 
        Returns the dictionary of answers and their percentage results after being displayed. 
        """
        user_ids = self.get_user_ids_by_demographic(demographic)
        responses = self.get_birth_control_info(user_ids, "use")
        results = self.count_birth_control_use_answers(responses)
        percent_results = self.calc_percentage(results)
        return self.display_results(percent_results)

    def get_use_of_birth_control_access_concerns_by_demographic(self, demographic):
        """
        Retrieves the user ids of the specified demographic in order to
        total up the answers for the concern level of access to birth control
        for those user ids. Then, the results are counted and displayed as percentages. 
                Parameters:
                    demographic = the string demographic the user selected and put
                    in either the command line or the url. 
        Returns the dictionary of answers and their percentage results after being displayed. 
        """
        user_ids = self.get_user_ids_by_demographic(demographic)
        responses = self.get_birth_control_info(user_ids, "access")
        results = self.count_birth_control_access_answers(responses)
        percent_results = self.calc_percentage(results)
        return self.display_results(percent_results)

    def get_user_ids_by_demographic(self, topic):
        """
        Iterates through and searches the list of lists named data in order
        to create a list of the user ids who are part of the appropriate demographic.
            Parameters:
                topic = the string demographic of people in the dataset whose user ids will be
                appended to the user_ids list.
        Returns the list of user_ids with the requested demographic.
        """
        user_ids = []
        for row in self.data:
            for demographic in row:
                demographic=demographic.lower()
                if topic.lower() in demographic:
                    user_ids.append(row[0])
        if user_ids==[]:
            print("Sorry, this demographic is not in the dataset.")
            return []
        return user_ids

    def get_birth_control_info(self, user_ids, useOrAccess):
        """
        Iterates through the list of user ids and creates a list of their
        answers to the appropriate question in the dataset.
            Parameters:
                user_ids = the list of user_ids of the appropriate demographic.
        Returns the list of answers to the question about how often birth control is used.
        """
        use_answers = []
        access_answers = []
        for user in user_ids:
            for row in self.data:
                if (row[0]==user):
                    if useOrAccess == "use":
                        use_answers.append(row[45])
                    else:
                        access_answers.append(row[58])
        if user_ids == []:
            print("List is empty")
            return []
        if useOrAccess == "use":
            return use_answers
        else:
            return access_answers

    def count_birth_control_use_answers(self, use_answers):
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
        for item in use_answers:
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

    def count_birth_control_access_answers(self, access_answers):
        """
        Counts the amount of each possible response to the birt7 question in the dataset
        regarding concerns about future access to birth control for the appropriate list 
        of users based on inputted demographic. Then, compiles a dictionary of each possible 
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
        for item in access_answers:
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

    def calc_percentage(self, totaled_answers):
        """
        Calculates the percentage of each possible response to the question in the dataset.
            Parameters:
                totaled_answers = the dictionary including each possible response and the
                amount of times that response was chosen by people in the dataset.
        Returns the same dictionary, but formatted based upon percentages instead of total responses.
        """
        total=0
        if totaled_answers == {}:
            print("Dictionary is empty, try again.")
            return {}
        #TODO: rename key to be more specific
        for response in totaled_answers:
            total=total+totaled_answers[response]
        for response in totaled_answers:
            if total!=0:   
                totaled_answers[response]= round((totaled_answers[response]/total)*100)
        return totaled_answers