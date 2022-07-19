import psycopg2

class Database:
    host = "covid.cs56gtsx8sfq.us-east-1.rds.amazonaws.com"
    user = "COVID"
    password = "vincent2391118"
    sslmode = "require"
    
    def __init__(self, db):
        connect = psycopg2.connect(host=self.host, user=self.user, password=self.password, database=db)
        self.cursor = connect.cursor()
    
    def execute(self, command):
        try:
            self.cursor.execute(command)
        except Exception as e:
            return e
        else:
            #fetchall()回傳陳述句的執行結果，并以元組的形式保存
            return self.cursor.fetchall()





