import pymysql.cursors
class MYSQL:
    def __init__(self,host,port,user,password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        
    def create_database(self,database_name):
        try:
            connection = pymysql.connect(host=self.host,user=self.user,password=self.password,
                                     cursorclass=pymysql.cursors.DictCursor)
            cursor = connection.cursor()
            query  = f"""CREATE DATABASE IF NOT EXISTS `{database_name}`"""
            cursor.execute(query)
            connection.commit()
            return f"{database_name} is created successfully" 
        except Exception as err:
            return {
                "error": err
            }

    def create_table(self,database_name,table_name):
        try:
            connection = pymysql.connect(host=self.host,user=self.user,password=self.password,database=database_name,
                                     cursorclass=pymysql.cursors.DictCursor)
            cursor = connection.cursor()
            
            query_table = f"""CREATE TABLE IF NOT EXISTS `{table_name}` (`id` int(11) NOT NULL AUTO_INCREMENT,
                                           `firstname` varchar(255) COLLATE utf8_bin NOT NULL,
                                           `lastname` varchar(255) COLLATE utf8_bin NOT NULL,
                                           `email` varchar(255) COLLATE utf8_bin NOT NULL,
                                            PRIMARY KEY (`id`)) 
                                            ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
                                            AUTO_INCREMENT=1 ;"""

            
            cursor.execute(query_table)
            connection.commit()
            return f"{table_name} is created successfully" 

        except Exception as err:
            return {
                "error": err
            }

    def execute_command(self,database_name,query,args:tuple):
        try: 
            connection = pymysql.connect(host=self.host,user=self.user,password=self.password,
                                     database=database_name,cursorclass=pymysql.cursors.DictCursor)
            cursor = connection.cursor()
            cursor.execute(query,args)
            connection.commit()
            return "Successfully executed the command"
        except Exception as err:
            return {
                "error": err
            }

    def fetch(self,database_name,query,args: tuple):
        try: 
            connection = pymysql.connect(host=self.host,user=self.user,password=self.password,
                                     database=database_name,cursorclass=pymysql.cursors.DictCursor)
            cursor = connection.cursor()
            cursor.execute(query,args)
            connection.commit()
          
            rows = cursor.fetchall()
            print("Successfully executed the command")
            return rows
        except Exception as err:
            return {
                "error": err
            }
#mysql =MYSQL('localhost',3306,'root','password')

#print(mysql.create_database('stars'))
#print(mysql.create_table('stars','heros'))

#query = """INSERT INTO `heros` (`firstname`,`lastname`,`email`) VALUES (%s,%s,%s)"""
#print(mysql.execute_command('stars',query,('Sai',"prakash","ksaiprakash@gmail.com")))
#query = """SELECT * FROM  `heros`"""
#print(mysql.fetch('stars',query,()))