from flask import *
from data.link import datalink
from data.content import empresas
import os

app = Flask(__name__)

#inicio
@app.route("/")
def inicio():
    for i in datalink:
        return render_template("inicio.html",val=datalink.values())

#ADMEJORES SEGURIDAD LTDA   #ADMEJORES SEGURIDAD LTDA   #ADMEJORES SEGURIDAD LTDA   #ADMEJORES SEGURIDAD LTDA   #ADMEJORES SEGURIDAD LTDA

rout2 = empresas['empresa2']['rout']
compani2 = empresas['empresa2']['compani']

@app.route(rout2+"list")
def ads_listarl():
    return compani2.listl()

@app.route(rout2+"list/<int:id>")
def ads_listar_id(id):
    return compani2.listlid(id)

@app.route(rout2)
def ads_listar_cre1():
    return compani2.createl()

@app.route(rout2+"create2", methods=["POST"])
def ads_listar_cre2():
    return compani2.create2l()

@app.route(rout2+"stade/<int:id>")
def ads_stade(id):
    return compani2.inactive(id)


key_file = 'key2.json'
key_path = os.path.abspath(key_file)

print(key_path)

if __name__== "__main__":
    app.run(port=5017)

    