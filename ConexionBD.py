import mysql.connector

cnn = mysql.connector.connect(host="localhost", user="root", passwd="", database="EP")


cur = cnn.cursor()
cur.execute("select * from CODIGOS")

datos = cur.fetchall()

for fila in datos:
    print(fila)



print(cur)