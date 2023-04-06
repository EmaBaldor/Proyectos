from flask import Flask,jsonify,request
from flask_mysqldb import MySQL
from config_transporte import config
import datetime

app = Flask(__name__)

conexion = MySQL(app)

@app.route('/viajes',methods=['GET'])
def mostrar_viajes():
    try:
        cursor=conexion.connection.cursor()
        sql="""SELECT   nro_servicio, 
                        fecha_servicio, 
                        horario_servicio, 
                        vehiculo, 
                        cant_pasajeros 
                FROM viajes"""
        cursor.execute(sql)
        datos = cursor.fetchall()
        viajes = []
        for fila in datos:
            viaje={
                'Servicio:':fila[0],
                'Fecha':fila[1],
                'Hora':fila[2],
                'Vehiculo':fila[3],
                'Pasajeros':fila[4]
                }
            viajes.append(viaje)
        return jsonify({'Viajes:':viajes,'Mensaje:':"Listado viajes"})
    except Exception as ex:
        return jsonify({'Mensaje:':"Error."})

@app.route('/viajesAct',methods=['GET'])
def mostrar_viajes_activos():
    try:
        cursor=conexion.connection.cursor()
        sql="""SELECT   nro_servicio, 
                        fecha_servicio, 
                        horario_servicio, 
                        vehiculo, 
                        cant_pasajeros 
                FROM viajes 
                WHERE finalizado = 0"""
        cursor.execute(sql)
        datos = cursor.fetchall()
        viajes = []
        for fila in datos:
            viaje={
                'Servicio:':fila[0],
                'Fecha':fila[1],
                'Hora':fila[2],
                'Vehiculo':fila[3],
                'Pasajeros':fila[4]
                }
            viajes.append(viaje)
        return jsonify({'Viajes:':viajes,'Mensaje:':"Viajes activos"})
    except Exception as ex:
        return jsonify({'Mensaje:':"Error."})


@app.route('/viajes/<codigo>',methods=['GET'])
def mostrar_viaje(codigo):
    try:
        viaje = viaje_bd(codigo)
        if viaje != None:
            return jsonify({'Viajes:':viaje,'Mensaje:':"Viaje encontrado."})
        else:
            return jsonify({'Mensaje:':"Viaje no encontrado."})

    except Exception as ex:
        return jsonify({'Mensaje:':"Error."})

@app.route('/viajes',methods=['POST'])
def cargar_viaje():
    try:
        cursor=conexion.connection.cursor()
        sql="""INSERT INTO viajes 
                    (nro_servicio,
                    fecha_servicio,
                    horario_servicio,
                    vehiculo,
                    cant_pasajeros) 
                VALUES ('{0}','{1}','{2}','{3}')""".format(
                                                    request.json['Viaje'],
                                                    request.json['Fecha'],
                                                    request.json['Hora'],
                                                    request.json['Vehiculo'],
                                                    request.json['Pasajeros']
                                                    )
        cursor.execute(sql)
        conexion.connection.commit() #confirma la accion
        return jsonify({'Mensaje:':"Viaje cargado."})
    except Exception as ex:
        return jsonify({'Mensaje:':"Error."})

@app.route('/viajes/<codigo>', methods=['DELETE'])
def eliminar_viaje(codigo):
    try:
        viaje = viaje_bd(codigo)
        if viaje != None:
            cursor = conexion.connection.cursor()
            sql = "DELETE FROM viajes WHERE nro_servicio = '{0}'".format(codigo)
            cursor.execute(sql)
            conexion.connection.commit()  # Confirma la acción de eliminación.
            return jsonify({'mensaje': "Viaje eliminado.", 'exito': True})
        else:
            return jsonify({'mensaje': "Viaje no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})

@app.route('/viajes/<codigo>', methods=['PUT'])
def actualizar_viaje(codigo):
        try:
            curso = viaje_bd(codigo)
            if curso != None:
                cursor = conexion.connection.cursor()
                sql = """UPDATE viajes 
                SET 
                fecha_servicio = '{0}', 
                hora_servicio = '{1}', 
                vehiculo = {2} ,
                cant_pasajeros = {3} 
                WHERE nro_servicio = '{4}'""".format(
                                                    request.json['Fecha'],
                                                    request.json['Hora'],
                                                    request.json['Vehiculo'],
                                                    request.json['Pasajeros'],
                                                    codigo
                                                    )
                cursor.execute(sql)
                conexion.connection.commit()  # Confirma la acción de actualización.
                return jsonify({'mensaje': "viaje actualizado.", 'exito': True})
            else:
                return jsonify({'mensaje': "viaje no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})

def viaje_bd(codigo):
    try:
        cursor=conexion.connection.cursor()
        sql="""SELECT   nro_servicio, 
                        fecha_servicio, 
                        horario_servicio, 
                        vehiculo, 
                        cant_pasajeros 
                FROM viajes 
                WHERE nro_servicio = '{0}'""".format(codigo)
        cursor.execute(sql)
        datos=cursor.fetchone()

        if datos != None:
            viaje={
                'Servicio:':datos[0],
                'Fecha':datos[1],
                'Hora':datos[2],
                'Vehiculo':datos[3],
                'Pasajeros':datos[4]
                }
            return viaje
        else:
            return None
    except Exception as ex:
        raise ex

@app.route('/')
def index():
    return "Bienvenido"

def pagina_no_encontrada(error):
    return "<h1>Pagina no encontrada<h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404,pagina_no_encontrada)
    app.run()