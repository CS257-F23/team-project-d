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
    
    def get_all_rows(self):
        """Returns all the rows of the table as a list"""

        #Establishing a cursor
        cursor = self.connection.cursor()

        #Pulling all the rows from the table
        cursor.execute("SELECT * FROM subjectIDs_and_religion")

        #displaying all selected rows
        records = cursor.fetchall()
        print(records)

    def get_religion_rows(self, religion):
        """Retrieves and displays all the rows in the table
        that have the specified religion. Prints an error
        message if an exception is encountered.
        """

        try:
            #Establishes a cursor and executes the prompt to
            #retrieve all the rows in the table with the matching
            #religion, then prints the results. 
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM subjectIDs_and_religion WHERE religion=%s", (religion,))
            print(cursor.fetchall())

        except Exception as e:
            #In the case of an exception, prints error message
            print("Something went wrong when executing the query: ", e)
            return None