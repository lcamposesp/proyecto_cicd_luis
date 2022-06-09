from flask import Flask,jsonify


application = Flask(__name__)
SECRET_KEY = '1393459340023492'
application.config['SECRET_KEY'] = SECRET_KEY

dict_usuarios = {
        1:{'nombre':'Luis Campos','cedula':'503960918','edad':'28','correo':'lcamposesp@ucreativa.com','direccion':'Pavas'},
        2:{'nombre':'David Campos','cedula':'11111111','edad':'31','correo':'david@test.com','direccion':'Moravia'},
        3:{'nombre':'Michelle Hernandez','cedula':'11111111','edad':'31','correo':'mich@test.com','direccion':'Pavas'},
        4:{'nombre':'Andrea Segura','cedula':'11111119','edad':'18','correo':'andre@correo.com','direccion':'Pavas'},
        5:{'nombre':'Jose Sanchez','cedula':'2540699','edad':'42','correo':'jose@correo.com','direccion':'Moravia'},
        6:{'nombre':'Carlos Benavides','cedula':'11341119','edad':'28','correo':'joseb@correo.com','direccion':'Alajuela'},
        7:{'nombre':'Maria Sanchez','cedula':'123341119','edad':'45','correo':'msanchez@correo.com','direccion':'Alajuela'},
        8:{'nombre':'Vanessa Soto','cedula':'17741119','edad':'28','correo':'sotom@correo.com','direccion':'Guanacaste'}
    }
@application.route('/')
def hello_world():  
        return('<h1>API Sencilla de Flask </h1>')
@application.route('/usuarios',methods=['GET'])
def ver_usuarios():
        dict = dict_usuarios
        return jsonify(dict)
@application.route('/usuarios/<id>',methods=['GET'])
def buscar_usuario_id(id):
        usuario = dict_usuarios[int(id)]
        return jsonify(usuario)
@application.route('/usuarios/cedula/<cedula>',methods=['GET'])
def buscar_usuario_cedula(cedula):
        for keys in dict_usuarios:
            if dict_usuarios[int(keys)]['cedula']==cedula:
                usuario = dict_usuarios[int(keys)]
                return jsonify(usuario)
@application.route('/usuarios/edad/<edad>')
def buscar_usuario_edad(edad):
    usuario_edad = {}
    key = 1
    for keys in dict_usuarios:
        if dict_usuarios[int(keys)]['edad'] == edad:
            usuario = dict_usuarios[int(keys)]
            usuario_edad[int(key)] = dict_usuarios[int(keys)]
            key+=1
        else:
            print("No se encontro usuario")
            
    return jsonify(usuario_edad)
@application.route('/usuarios/direccion/<direccion>')
def buscar_usuario_direccion(direccion):
    usuario_dir = {}
    key = 1
    for keys in dict_usuarios:
        if dict_usuarios[int(keys)]['direccion'].lower() == direccion:
            usuario = dict_usuarios[int(keys)]
            usuario_dir[int(key)] = dict_usuarios[int(keys)]
            key+=1
        else:
            print("No se encontro usuario")
            
    return jsonify(usuario_dir)

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()