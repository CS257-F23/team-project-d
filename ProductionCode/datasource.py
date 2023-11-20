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
    
    

    
    def get_access_column_by_demographic(self, demographic):
        """
        Searches all demographic columns and retrieves the birth control access concerns column 
        for subjects of the specified demographic.
        access_column_for_demographic is a list that contains 
        all of the answers to the access concerns question.
        Returns None if an error is encountered.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT birthcontrol_access FROM reproductiveResponsesOnDemographics WHERE states=%s OR poliParty=%s OR poliView=%s OR religion=%s", (demographic, demographic, demographic, demographic,))
            access_column_for_demographic = cursor.fetchall()
            return access_column_for_demographic
        
        except Exception as e:
            print("Something went wrong when executing the query: ", e)
            return None

    def get_use_column_by_demographic(self, demographic):
        """
        Retrieves the birth control use column for the subjects of the specified demographic.
        use_column_for_demographic is a list that contains 
        all of the answers to the use question in the dataset. 
        Returns None if an error is encountered.
        """

        try: 
            cursor = self.connection.cursor()
            cursor.execute("SELECT birthcontrol_use FROM reproductiveResponsesOnDemographics WHERE states=%s OR poliParty=%s OR poliView=%s OR religion=%s", (demographic, demographic, demographic, demographic,))
            use_column_for_demographic = cursor.fetchall()
            return use_column_for_demographic

        except Exception as e:
            print("Something went wrong when executing the query: ", e)
            return None