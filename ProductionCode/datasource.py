import psycopg2
import ProductionCode.psqlConfig as config


class DataSource:

    def __init__(self):
        '''Constructor that initiates the connection to the database'''
        self.connection = self.connect()

    def connect(self):
        '''Initiates connection to database using information in the psqlConfig.py file.
        Returns the connection object. Prints an error if any
        exceptions are encountered.'''

        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host="localhost")
        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection
    
    

    
    
    def get_access_column_by_demographic(self,demographic):
        """examine whether the specific demographic input belongs to religion category or political party category.
          search for the corresponding query."""


        religions = ["Non-denominational or Independent Church", "Lutheran", "Protestant", 
                 "Catholic, Roman Catholic", "Evangelical", 
                 "Church of Christ, or Disciples of Christ (Christian Church)", 
                 "Church of God", "Episcopalian or Anglican", "Methodist", 
                 "Baptist", "Buddhist", "Agnostic", "Jehovah's Witness", "Atheist", 
                 "Nothing in particular", "Hindu", "Presbyterian", 
                 "Pentecostal (Assemblies of God, Four-Square Gospel)"]

        political_parties = ["Republican", "Independent", "Democratic"]
        if demographic in religions:
            return self.get_access_column_by_religion(demographic)
        if demographic in political_parties:
            return self.get_access_column_by_poliParty(demographic)



    def get_access_column_by_religion(self,religion):
        """
        Searches all demographic columns and retrieves the birth control access concerns column 
        for subjects of the religion demographic.
        access_column_for_demographic is a list that contains 
        all of the answers to the access concerns question.
        Returns None if an error is encountered.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT birthcontrol_access FROM reproductiveResponsesByDemographics WHERE religion=%s", (religion,))
            access_column_for_demographic = cursor.fetchall()
            return access_column_for_demographic
        
        except Exception as e:
            print("Something went wrong when executing the query: ", e)
            return None
        

    def get_access_column_by_poliParty(self,poliParty):
        """
        Searches all demographic columns and retrieves the birth control access concerns column 
        for subjects of the political party demographic.
        access_column_for_demographic is a list that contains 
        all of the answers to the access concerns question.
        Returns None if an error is encountered.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT birthcontrol_access FROM reproductiveResponsesByDemographics WHERE poliParty=%s", (poliParty,))
            access_column_for_demographic = cursor.fetchall()
            return access_column_for_demographic
        
        except Exception as e:
            print("Something went wrong when executing the query: ", e)
            return None
        
    
    

    def get_use_column_by_demographic(self, demographic):
    
        """examine whether the specific demographic input belongs to religion category or political party category.
          search for the corresponding query."""

        religions = ["Non-denominational or Independent Church", "Lutheran", "Protestant", 
                 "Catholic, Roman Catholic", "Evangelical", 
                 "Church of Christ, or Disciples of Christ (Christian Church)", 
                 "Church of God", "Episcopalian or Anglican", "Methodist", 
                 "Baptist", "Buddhist", "Agnostic", "Jehovah's Witness", "Atheist", 
                 "Nothing in particular", "Hindu", "Presbyterian", 
                 "Pentecostal (Assemblies of God, Four-Square Gospel)"]

        political_parties = ["Republican", "Independent", "Democratic"]
        if demographic in religions:
            return self.get_use_column_by_religion(demographic)
        if demographic in political_parties:
            return self.get_use_column_by_poliParty(demographic)

        

    


    def get_use_column_by_religion(self,religion):

        """
        Retrieves the birth control use column for the subjects of the religion category.
        use_column_for_demographic is a list that contains 
        all of the answers to the use question in the dataset. 
        Returns None if an error is encountered."""

        try: 
            cursor = self.connection.cursor()
            cursor.execute("SELECT birthcontrol_use FROM reproductiveResponsesByDemographics WHERE religion=%s", (religion, ))
            use_column_for_demographic = cursor.fetchall()
            return use_column_for_demographic

        except Exception as e:
            print("Something went wrong when executing the query: ", e)
            return None
    
    def get_use_column_by_poliParty(self,poliParty):

        """
        Retrieves the birth control use column for the subjects of the political party category.
        use_column_for_demographic is a list that contains 
        all of the answers to the use question in the dataset. 
        Returns None if an error is encountered."""

        try: 
            cursor = self.connection.cursor()
            cursor.execute("SELECT birthcontrol_use FROM reproductiveResponsesByDemographics WHERE poliParty=%s", (poliParty, ))
            use_column_for_demographic = cursor.fetchall()
            return use_column_for_demographic

        except Exception as e:
            print("Something went wrong when executing the query: ", e)
            return None
            
    
    
    

