import sys

from flask import (
    Flask,
    redirect,
    render_template,
    request,
)
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/vehiculos_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

sys.version_info()


listado_nombres ={'Pedro', 'juan', 'jose'}
diccionario_nombre=[
    dict(
        name=dict(
            first='agustin',
            last='invalid'
        ),
        location=dict(
            city='canals'

        ),
        email="agustin@nollenolacancha.com"
    ),
    dict(
        name=dict(
            first="Pedro",
            last='Lemo'
        ),
        location=dict(
            city='Alpa Corral'

        ),
        email="peter@lemo.com"
    ),
    dict(
        name=dict(
            first="fernan",
            last='casanova'
        ),
        location=dict(
            city='Villa Huidobro'

        ),
        email="Fernan@casanova.com"
    ),
]


@app.route('/') # app es la instancia, route el metodo, '/' es el disparador
def index():
    return render_template(
        'index.html',
    )
personas_list=["pablo","juan","maria","elina"]
@app.route('/info') # app es la instancia, route el metodo, '/' es el disparador
def informacion():
    return render_template(
        'informacion.html',
    )

@app.route('/bienvenido/<nombre>')
def bienvenida(nombre):
    return render_template(
        'bienvenida.html',
    )

@app.route('/personas')
def personas():
    listado=diccionario_nombre
    return render_template(
        'personas.html',
        listado=listado
  
    )

@app.route('/personas_add', methods=['GET','POST'])
def agregar_personas():
                #post=peticion-formulario-clave
    if request.method=='POST':
        nombre= request.form['nombre']
        apellido= request.form['apellido']
        email= request.form['email'] 
        ciudad= request.form['ciudad'] 

        persona= dict(
            name=dict(
                first=nombre,
                last=apellido
        ),
            location=dict(
                city=ciudad

        ),
            email=email
        )
        diccionario_nombre.append(persona)
        return redirect('personas')
    return render_template('add_personas.html')