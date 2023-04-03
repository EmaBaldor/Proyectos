import mysql.connector

cnn = mysql.connector.connect(host="localhost", user="root", passwd="", database="transporte")


cur = cnn.cursor()

#cur.execute("insert into codigos (CODIGO) values ('123456786')")

#cnn.commit()

#cur.execute("delete from codigos where CODIGO = '123456789'")

#cnn.commit()

cur.execute("select count(*) from viajes")


print (cur.fetchall()) 

#datos = cur.fetchall()
#for fila in datos:
#    print(fila)



print(cur)