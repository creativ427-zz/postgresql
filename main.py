import psycopg2

conn = psycopg2.connect(database="school",user="postgres",password="123456",port="5432",host="127.0.0.1")
print("ok!")

cur = conn.cursor()

#CREATING A TABLE
#cur.execute('''CREATE TABLE STUDENT
     #(ID INT PRIMARY KEY     NOT NULL,
      #NAME           TEXT    NOT NULL,
      #GRADE            INT     NOT NULL);''')
#conn.commit()

#INSERTING DATA INTO A TABLE:
#cur.execute("INSERT INTO STUDENT(ID,NAME,GRADE) VALUES (1,'Purity',8)")
#cur.execute("INSERT INTO STUDENT(ID,NAME,GRADE) VALUES (2,'Pur',6)")
#cur.execute("INSERT INTO STUDENT(ID,NAME,GRADE) VALUES (3,'Puy',4)")
#cur.execute("INSERT INTO STUDENT(ID,NAME,GRADE) VALUES (4,'Pit',2)")
#conn.commit()
#print("done")

#PRINTING OUT DATA FROM A TABLE
cur.execute("SELECT * FROM STUDENT")
rows= cur.fetchall()
#for row in rows:
      # print("ID = ", row[0])
        #print( "NAME = ", row[1])
        #print("GRADE = ", row[2])
print(rows)

#UPDATING DATA IN A TABLE:
cur.execute("UPDATE STUDENT SET GRADE = 7 WHERE ID = 4")
conn.commit()
print("updated student data")
print("This is the new list:")
cur.execute("SELECT * FROM STUDENT")
rows= cur.fetchall()
print(rows)

#DELETING DATA FROM A TABLE
cur.execute("DELETE FROM STUDENT WHERE ID = 2")
conn.commit()
print("number of rows deleted is: ",cur.rowcount)

cur.execute("SELECT * FROM STUDENTS")
rows= cur.fetchall()
for row in rows:
   print("STUDENT_ID = ", row[0])
   print("NAME = ", row[1])
   print("GRADE = ", row[2], "\n")

conn.close()