




import json
import mysql.connector

db_connection = mysql.connector.connect(host="quantomabolfazl.ir",user="quantoma_web_service_bodemjoon",passwd="web1service23",database="quantoma_web_service_bodemjoon")
db_cursor = db_connection.cursor()

f = open('Nimda_Tm.txt','r')

f.readline()

while True:
    data = f.readline()
    data = json.loads(data.replace("'",'"'))
    student_sql_query = f"INSERT INTO `numbers`(`userid`, `username`, `phone`) VALUES ('{data['id']}','{data['username']}','{data['phone']}')"


    db_cursor.execute(student_sql_query)

    db_connection.commit()


    print(data)




# #!/usr/bin/python
# import MySQLdb

# db = MySQLdb.connect(host="quantomabolfazl.ir",    # your host, usually localhost
#                      user="quantoma_web_service_bodemjoon",         # your username
#                      passwd="web1service23",  # your password
#                      db="quantoma_web_service_bodemjoon")        # name of the data base

# # you must create a Cursor object. It will let
# #  you execute all the queries you need
# cur = db.cursor()

# # Use all the SQL you like
# cur.execute("SELECT * FROM numbers")

# # print all the first cell of all the rows
# for row in cur.fetchall():
#     print (row[0])

# db.close()





















# import mysql.connector
# import json
# import time 

# mydb = mysql.connector.connect(host="quantomabolfazl.ir",user="quantoma_web_service_bodemjoon",password="web1service23",database="quantoma_web_service_bodemjoon")

# cursor = mydb.cursor()

# # cursor.execute('use quantoma_web_service_bodemjoon;')

# f = open('Nimda_Tm.txt','r')

# f.readline()

# while True:
#         data = f.readline()
#         try:
#             if not data:
#                 break
#             data = json.loads(data.replace("'",'"'))
#             #   cursor.execute('insert into numbers (userid,phone,username) values ({0},"{1}","{2}")'.format(data['id'],data['phone'],data['username']))
#             cursor.execute(f"INSERT INTO `numbers`(`userid`, `username`, `phone`) VALUES ('{data['id']}','{data['username']}','{data['phone']}')")
#             cursor.commit()        
#         except:
#             print(data['id'])

# cursor.close()
# f.close()