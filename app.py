from flask import *
from data.link import datalink
from data.content import empresas
import os

app = Flask(__name__)

#Fisios #Fisios #Fisios #Fisios #Fisios #Fisios #Fisios #Fisios #Fisios #Fisios #Fisios #Fisios #Fisios #Fisios #Fisios #Fisios #Fisios
@app.route("/fisios-2946")
def fisios():
    for i in datalink:
        return render_template("inicio.html",val=datalink.values())

#7-24 LTDA  #7-24 LTDA  #7-24 LTDA  #7-24 LTDA  #7-24 LTDA  #7-24 LTDA  #7-24 LTDA  #7-24 LTDA  #7-24 LTDA  #7-24 LTDA  #7-24 LTDA  #7-24 LTDA
rout1 = empresas['empresa1']['rout']
compani1 = empresas['empresa1']['compani']


@app.route(rout1)
def ltda_info():
    return compani1.info()

@app.route(rout1+"list")
def ltda_listarl():
    return compani1.listl()

@app.route(rout1+"list/<string:id>")
def ltda_listar_id(id):
    print(id)
    return compani1.listlid(id)

@app.route(rout1+"cr")
def ltda_listar_cre1():
    return compani1.createl()

@app.route(rout1+"create2", methods=["POST"])
def ltda_listar_cre2():
    return compani1.create2l()

@app.route(rout1+"edit1/<string:id>")
def ltda_edit1(id):
    print(id)
    return compani1.edit1(id)

@app.route(rout1+"editl/<string:id>", methods=["POST"])
def ltda_editl(id):
    return compani1.editl(id)

#ADMEJORES SEGURIDAD LTDA   #ADMEJORES SEGURIDAD LTDA   #ADMEJORES SEGURIDAD LTDA   #ADMEJORES SEGURIDAD LTDA   #ADMEJORES SEGURIDAD LTDA

rout2 = empresas['empresa2']['rout']
compani2 = empresas['empresa2']['compani']

@app.route(rout2)
def ads_info():
    return compani2.info()

@app.route(rout2+"list")
def ads_listarl():
    return compani2.listl()

@app.route(rout2+"list/<string:id>")
def ads_listar_id(id):
    return compani2.listlid(id)

@app.route(rout2+"cr")
def ads_listar_cre1():
    return compani2.createl()

@app.route(rout2+"create2", methods=["POST"])
def ads_listar_cre2():
    return compani2.create2l()

@app.route(rout2+"edit1/<string:id>")
def ads_edit1(id):
    return compani2.edit1(id)

@app.route(rout2+"editl/<string:id>", methods=["POST"])
def ads_editl(id):
    return compani2.editl(id)


#ALPHA SEGURIDAD PRIVADA LTDA #ALPHA SEGURIDAD PRIVADA LTDA #ALPHA SEGURIDAD PRIVADA LTDA  #ALPHA SEGURIDAD PRIVADA LTDA #ALPHA SEGURIDAD PRIVADA LTDA

rout3 = empresas['empresa3']['rout']
compani3 = empresas['empresa3']['compani']

@app.route(rout3)
def asp_info():
    return compani3.info()

@app.route(rout3+"list")
def asp_listarl():
    return compani3.listl()

@app.route(rout3+"list/<string:id>")
def asp_listar_id(id):
    return compani3.listlid(id)

@app.route(rout3 +"cr")
def asp_listar_cre1():
    return compani3.createl()

@app.route(rout3+"create2", methods=["POST"])
def asp_listar_cre2():
    return compani3.create2l()

@app.route(rout3+"edit1/<string:id>")
def asp_edit1(id):
    return compani3.edit1(id)

@app.route(rout3+"editl/<string:id>", methods=["POST"])
def asp_editl(id):
    return compani3.editl(id)


#AMCOVIT LTDA #AMCOVIT LTDA #AMCOVIT LTDA #AMCOVIT LTDA #AMCOVIT LTDA  #AMCOVIT LTDA#AMCOVIT LTDA #AMCOVIT LTDA #AMCOVIT LTDA #AMCOVIT LTDA #AMCOVIT LTDA #AMCOVIT LTDA #AMCOVIT LTDA #AMCOVIT LTDA

rout4 = empresas['empresa4']['rout']
compani4 = empresas['empresa4']['compani']

@app.route(rout4)
def amcovit_info():
    return compani4.info()

@app.route(rout4+"list")
def amcovit_listarl():
    return compani4.listl()

@app.route(rout4+"list/<string:id>")
def amcovit_listar_id(id):
    return compani4.listlid(id)

@app.route(rout4+"cr")
def amcovit_listar_cre1():
    return compani4.createl()

@app.route(rout4+"create2", methods=["POST"])
def amcovit_listar_cre2():
    return compani4.create2l()

@app.route(rout4+"edit1/<string:id>")
def amcovit_edit1(id):
    return compani4.edit1(id)

@app.route(rout4+"editl/<string:id>", methods=["POST"])
def amcovit_editl(id):
    return compani4.editl(id)


#ANILLOS DE SEGURIDAD LTDA #ANILLOS DE SEGURIDAD LTDA #ANILLOS DE SEGURIDAD LTDA #ANILLOS DE SEGURIDAD LTDA #ANILLOS DE SEGURIDAD LTDA #ANILLOS DE SEGURIDAD LTDA

rout5 = empresas['empresa5']['rout']
compani5 = empresas['empresa5']['compani']

@app.route(rout5)
def anis_info():
    return compani5.info()

@app.route(rout5+"list")
def anis_listarl():
    return compani5.listl()

@app.route(rout5+"list/<string:id>")
def anis_listar_id(id):
    return compani5.listlid(id)

@app.route(rout5+"cr")
def anis_listar_cre1():
    return compani5.createl()

@app.route(rout5+"create2", methods=["POST"])
def anis_listar_cre2():
    return compani5.create2l()

@app.route(rout5+"edit1/<string:id>")
def anis_edit1(id):
    return compani5.edit1(id)

@app.route(rout5+"editl/<string:id>", methods=["POST"])
def anis_editl(id):
    return compani5.editl(id)


#ASEISA LTDA #ASEISA LTDA #ASEISA LTDA #ASEISA LTDA #ASEISA LTDA #ASEISA LTDA#ASEISA LTDA #ASEISA LTDA #ASEISA LTDA #ASEISA LTDA #ASEISA LTDA #ASEISA LTDA #ASEISA LTDA #ASEISA LTDA

rout6 = empresas['empresa6']['rout']
compani6 = empresas['empresa6']['compani']

@app.route(rout6)
def aseisa_info():
    return compani6.info()

@app.route(rout6+"list")
def aseisa_listarl():
    return compani6.listl()

@app.route(rout6+"list/<string:id>")
def aseisa_listar_id(id):
    return compani6.listlid(id)

@app.route(rout6+"cr")
def aseisa_listar_cre1():
    return compani6.createl()

@app.route(rout6+"create2", methods=["POST"])
def aseisa_listar_cre2():
    return compani6.create2l()

@app.route(rout6+"edit1/<string:id>")
def aseisa_edit1(id):
    return compani6.edit1(id)

@app.route(rout6+"editl/<string:id>", methods=["POST"])
def aseisa_editl(id):
    return compani6.editl(id)


#ASEP LTDA #ASEP LTDA #ASEP LTDA #ASEP LTDA #ASEP LTDA #ASEP LTDA#ASEP LTDA #ASEP LTDA #ASEP LTDA #ASEP LTDA #ASEP LTDA #ASEP LTDA #ASEP LTDA #ASEP LTDA

rout7 = empresas['empresa7']['rout']
compani7 = empresas['empresa7']['compani']

@app.route(rout7)
def asep_info():
    return compani7.info()

@app.route(rout7+"list")
def asep_listarl():
    return compani7.listl()

@app.route(rout7+"list/<string:id>")
def asep_listar_id(id):
    return compani7.listlid(id)

@app.route(rout7+"cr")
def asep_listar_cre1():
    return compani7.createl()

@app.route(rout7+"create2", methods=["POST"])
def asep_listar_cre2():
    return compani7.create2l()

@app.route(rout7+"edit1/<string:id>")
def asep_edit1(id):
    return compani7.edit1(id)

@app.route(rout7+"editl/<string:id>", methods=["POST"])
def asep_editl(id):
    return compani7.editl(id)


#ATLANTA CIA DE VIGILANCIA PRIVADA LTDA #ATLANTA CIA DE VIGILANCIA PRIVADA LTDA #ATLANTA CIA DE VIGILANCIA PRIVADA LTDA #ATLANTA CIA DE VIGILANCIA PRIVADA LTDA #ATLANTA CIA DE VIGILANCIA PRIVADA LTDA

rout8 = empresas['empresa8']['rout']
compani8 = empresas['empresa8']['compani']

@app.route(rout8)
def atlacia_info():
    return compani8.info()

@app.route(rout8+"list")
def atlacia_listarl():
    return compani8.listl()

@app.route(rout8+"list/<string:id>")
def atlacia_listar_id(id):
    return compani8.listlid(id)

@app.route(rout8+"cr")
def atlacia_listar_cre1():
    return compani8.createl()

@app.route(rout8+"create2", methods=["POST"])
def atlacia_listar_cre2():
    return compani8.create2l()

@app.route(rout8+"edit1/<string:id>")
def atlacia_edit1(id):
    return compani8.edit1(id)

@app.route(rout8+"editl/<string:id>", methods=["POST"])
def atlacia_editl(id):
    return compani8.editl(id)


#ATMOSFERA DE SEGURIDAD LTDA #ATMOSFERA DE SEGURIDAD LTDA #ATMOSFERA DE SEGURIDAD LTDA #ATMOSFERA DE SEGURIDAD LTDA #ATMOSFERA DE SEGURIDAD LTDA

rout9 = empresas['empresa9']['rout']
compani9 = empresas['empresa9']['compani']

@app.route(rout9)
def atmoseg_info():
    return compani9.info()

@app.route(rout9+"list")
def atmoseg_listarl():
    return compani9.listl()

@app.route(rout9+"list/<string:id>")
def atmoseg_listar_id(id):
    return compani9.listlid(id)

@app.route(rout9+"cr")
def atmoseg_listar_cre1():
    return compani9.createl()

@app.route(rout9+"create2", methods=["POST"])
def atmoseg_listar_cre2():
    return compani9.create2l()

@app.route(rout9+"edit1/<string:id>")
def atmoseg_edit1(id):
    return compani9.edit1(id)

@app.route(rout9+"editl/<string:id>", methods=["POST"])
def atmoseg_editl(id):
    return compani9.editl(id)


#BOGOTANA DE SEGURIDAD LTDA #BOGOTANA DE SEGURIDAD LTDA #BOGOTANA DE SEGURIDAD LTDA #BOGOTANA DE SEGURIDAD LTDA #BOGOTANA DE SEGURIDAD LTDA

rout10 = empresas['empresa10']['rout']
compani10 = empresas['empresa10']['compani']

@app.route(rout10)
def bogseg_info():
    return compani10.info()

@app.route(rout10+"list")
def bogseg_listarl():
    return compani10.listl()

@app.route(rout10+"list/<string:id>")
def bogseg_listar_id(id):
    return compani10.listlid(id)

@app.route(rout10+"cr")
def bogseg_listar_cre1():
    return compani10.createl()

@app.route(rout10+"create2", methods=["POST"])
def bogseg_listar_cre2():
    return compani10.create2l()

@app.route(rout10+"edit1/<string:id>")
def bogseg_edit1(id):
    return compani10.edit1(id)

@app.route(rout10+"editl/<string:id>", methods=["POST"])
def bogseg_editl(id):
    return compani10.editl(id)



#BRINKS DE COLOMBIA S.A. #BRINKS DE COLOMBIA S.A. #BRINKS DE COLOMBIA S.A. #BRINKS DE COLOMBIA S.A. #BRINKS DE COLOMBIA S.A.

rout11 = empresas['empresa11']['rout']
compani11 = empresas['empresa11']['compani']

@app.route(rout11)
def brinks_info():
    return compani11.info()

@app.route(rout11+"list")
def brinks_listarl():
    return compani11.listl()

@app.route(rout11+"list/<string:id>")
def brinks_listar_id(id):
    return compani11.listlid(id)

@app.route(rout11+"cr")
def brinks_listar_cre1():
    return compani11.createl()

@app.route(rout11+"create2", methods=["POST"])
def brinks_listar_cre2():
    return compani11.create2l()

@app.route(rout11+"edit1/<string:id>")
def brinks_edit1(id):
    return compani11.edit1(id)

@app.route(rout11+"editl/<string:id>", methods=["POST"])
def brinks_editl(id):
    return compani11.editl(id)


#CLASICA DE SEGURIDAD LIMITADA #CLASICA DE SEGURIDAD LIMITADA #CLASICA DE SEGURIDAD LIMITADA #CLASICA DE SEGURIDAD LIMITADA #CLASICA DE SEGURIDAD LIMITADA

rout12 = empresas['empresa12']['rout']
compani12 = empresas['empresa12']['compani']

@app.route(rout12)
def claseg_info():
    return compani12.info()

@app.route(rout12+"list")
def claseg_listarl():
    return compani12.listl()

@app.route(rout12+"list/<string:id>")
def claseg_listar_id(id):
    return compani12.listlid(id)

@app.route(rout12+"cr")
def claseg_listar_cre1():
    return compani12.createl()

@app.route(rout12+"create2", methods=["POST"])
def claseg_listar_cre2():
    return compani12.create2l()

@app.route(rout12+"edit1/<string:id>")
def claseg_edit1(id):
    return compani12.edit1(id)

@app.route(rout12+"editl/<string:id>", methods=["POST"])
def claseg_editl(id):
    return compani12.editl(id)


#COMPANIA DE VIGILANCIA PPH LTDA #COMPANIA DE VIGILANCIA PPH LTDA #COMPANIA DE VIGILANCIA PPH LTDA #COMPANIA DE VIGILANCIA PPH LTDA #COMPANIA DE VIGILANCIA PPH LTDA

rout13 = empresas['empresa13']['rout']
compani13 = empresas['empresa13']['compani']

@app.route(rout13)
def pph_info():
    return compani13.info()

@app.route(rout13+"list")
def pph_listarl():
    return compani13.listl()

@app.route(rout13+"list/<string:id>")
def pph_listar_id(id):
    return compani13.listlid(id)

@app.route(rout13+"cr")
def pph_listar_cre1():
    return compani13.createl()

@app.route(rout13+"create2", methods=["POST"])
def pph_listar_cre2():
    return compani13.create2l()

@app.route(rout13+"edit1/<string:id>")
def pph_edit1(id):
    return compani13.edit1(id)

@app.route(rout13+"editl/<string:id>", methods=["POST"])
def pph_editl(id):
    return compani13.editl(id)


#COMPAÑIA COLOMBIANA DE SEGURIDAD TRANSBA #COMPAÑIA COLOMBIANA DE SEGURIDAD TRANSBA #COMPAÑIA COLOMBIANA DE SEGURIDAD TRANSBA #COMPAÑIA COLOMBIANA DE SEGURIDAD TRANSBA #COMPAÑIA COLOMBIANA DE SEGURIDAD TRANSBA

rout14 = empresas['empresa14']['rout']
compani14 = empresas['empresa14']['compani']

@app.route(rout14)
def ccst_info():
    return compani14.info()

@app.route(rout14+"list")
def ccst_listarl():
    return compani14.listl()

@app.route(rout14+"list/<string:id>")
def ccst_listar_id(id):
    return compani14.listlid(id)

@app.route(rout14+"cr")
def ccst_listar_cre1():
    return compani14.createl()

@app.route(rout14+"create2", methods=["POST"])
def ccst_listar_cre2():
    return compani14.create2l()

@app.route(rout14+"edit1/<string:id>")
def ccst_edit1(id):
    return compani14.edit1(id)

@app.route(rout14+"editl/<string:id>", methods=["POST"])
def ccst_editl(id):
    return compani14.editl(id)


#COMPAÑIA DE SEGURIDAD Y VIGILANCIA PRIVA #COMPAÑIA DE SEGURIDAD Y VIGILANCIA PRIVA #COMPAÑIA DE SEGURIDAD Y VIGILANCIA PRIVA #COMPAÑIA DE SEGURIDAD Y VIGILANCIA PRIVA #COMPAÑIA DE SEGURIDAD Y VIGILANCIA PRIVA

rout15 = empresas['empresa15']['rout']
compani15 = empresas['empresa15']['compani']

@app.route(rout15)
def csvp_info():
    return compani15.info()

@app.route(rout15+"list")
def csvp_listarl():
    return compani15.listl()

@app.route(rout15+"list/<string:id>")
def csvp_listar_id(id):
    return compani15.listlid(id)

@app.route(rout15+"cr")
def csvp_listar_cre1():
    return compani15.createl()

@app.route(rout15+"create2", methods=["POST"])
def csvp_listar_cre2():
    return compani15.create2l()

@app.route(rout15+"edit1/<string:id>")
def csvp_edit1(id):
    return compani15.edit1(id)

@app.route(rout15+"e    ditl/<id>", methods=["POST"])
def csvp_editl(id):
    return compani15.editl(id)


#CONFIAR SEGURIDAD LTDA #CONFIAR SEGURIDAD LTDA #CONFIAR SEGURIDAD LTDA #CONFIAR SEGURIDAD LTDA #CONFIAR SEGURIDAD LTDA #CONFIAR SEGURIDAD LTDA #CONFIAR SEGURIDAD LTDA #CONFIAR SEGURIDAD LTDA

rout16 = empresas['empresa16']['rout']
compani16 = empresas['empresa16']['compani']

@app.route(rout16)
def confiar_info():
    return compani16.info()

@app.route(rout16+"list")
def confiar_listarl():
    return compani16.listl()

@app.route(rout16+"list/<string:id>")
def confiar_listar_id(id):
    return compani16.listlid(id)

@app.route(rout16+"cr")
def confiar_listar_cre1():
    return compani16.createl()

@app.route(rout16+"create2", methods=["POST"])
def confiar_listar_cre2():
    return compani16.create2l()

@app.route(rout16+"edit1/<string:id>")
def confiar_edit1(id):
    return compani16.edit1(id)

@app.route(rout16+"editl/<string:id>", methods=["POST"])
def confiar_editl(id):
    return compani16.editl(id)

#CONTROLAR LTDA #CONTROLAR LTDA #CONTROLAR LTDA #CONTROLAR LTDA #CONTROLAR LTDA #CONTROLAR LTDA#CONTROLAR LTDA #CONTROLAR LTDA #CONTROLAR LTDA #CONTROLAR LTDA #CONTROLAR LTDA #CONTROLAR LTDA #CONTROLAR LTDA #CONTROLAR LTDA

rout17 = empresas['empresa17']['rout']
compani17 = empresas['empresa17']['compani']

@app.route(rout17)
def controlar_info():
    return compani17.info()

@app.route(rout17+"list")
def controlar_listarl():
    return compani17.listl()

@app.route(rout17+"list/<string:id>")
def controlar_listar_id(id):
    return compani17.listlid(id)

@app.route(rout17+"cr")
def controlar_listar_cre1():
    return compani17.createl()

@app.route(rout17+"create2", methods=["POST"])
def controlar_listar_cre2():
    return compani17.create2l()

@app.route(rout17+"edit1/<string:id>")
def controlar_edit1(id):
    return compani17.edit1(id)

@app.route(rout17+"editl/<string:id>", methods=["POST"])
def controlar_editl(id):
    return compani17.editl(id)

#COOPERATIVA DE TRABAJO ASOCIADO DE VIGILANCIA SOCIAL COOVISOCIAL #COOPERATIVA DE TRABAJO ASOCIADO DE VIGILANCIA SOCIAL COOVISOCIAL #COOPERATIVA DE TRABAJO ASOCIADO DE VIGILANCIA SOCIAL COOVISOCIAL #COOPERATIVA DE TRABAJO ASOCIADO DE VIGILANCIA SOCIAL COOVISOCIAL #COOPERATIVA DE TRABAJO ASOCIADO DE VIGILANCIA SOCIAL COOVISOCIAL

rout18 = empresas['empresa18']['rout']
compani18 = empresas['empresa18']['compani']

@app.route(rout18)
def cooptra_info():
    return compani18.info()

@app.route(rout18+"list")
def cooptra_listarl():
    return compani18.listl()

@app.route(rout18+"list/<string:id>")
def cooptra_listar_id(id):
    return compani18.listlid(id)

@app.route(rout18+"cr")
def cooptra_listar_cre1():
    return compani18.createl()

@app.route(rout18+"create2", methods=["POST"])
def cooptra_listar_cre2():
    return compani18.create2l()

@app.route(rout18+"edit1/<string:id>")
def cooptra_edit1(id):
    return compani18.edit1(id)

@app.route(rout18+"editl/<string:id>", methods=["POST"])
def cooptra_editl(id):
    return compani18.editl(id)

#COOPERATIVA DE TRABAJO ASOCIADO PARA L #COOPERATIVA DE TRABAJO ASOCIADO PARA L #COOPERATIVA DE TRABAJO ASOCIADO PARA L #COOPERATIVA DE TRABAJO ASOCIADO PARA L #COOPERATIVA DE TRABAJO ASOCIADO PARA L

rout19 = empresas['empresa19']['rout']
compani19 = empresas['empresa19']['compani']

@app.route(rout19)
def coopl_info():
    return compani19.info()

@app.route(rout19+"list")
def coopl_listarl():
    return compani19.listl()

@app.route(rout19+"list/<string:id>")
def coopl_listar_id(id):
    return compani19.listlid(id)

@app.route(rout19+"cr")
def coopl_listar_cre1():
    return compani19.createl()

@app.route(rout19+"create2", methods=["POST"])
def coopl_listar_cre2():
    return compani19.create2l()

@app.route(rout19+"edit1/<string:id>")
def coopl_edit1(id):
    return compani19.edit1(id)

@app.route(rout19+"editl/<string:id>", methods=["POST"])
def coopl_editl(id):
    return compani19.editl(id)

#COOVIPORFAC C.T.A#COOVIPORFAC C.T.A #COOVIPORFAC C.T.A #COOVIPORFAC C.T.A #COOVIPORFAC C.T.A #COOVIPORFAC C.T.A #COOVIPORFAC C.T.A #COOVIPORFAC C.T.A #COOVIPORFAC C.T.A

rout20 = empresas['empresa20']['rout']
compani20 = empresas['empresa20']['compani']

@app.route(rout20)
def coovi_info():
    return compani20.info()

@app.route(rout20+"list")
def coovi_listarl():
    return compani20.listl()

@app.route(rout20+"list/<string:id>")
def coovi_listar_id(id):
    return compani20.listlid(id)

@app.route(rout20+"cr")
def coovi_listar_cre1():
    return compani20.createl()

@app.route(rout20+"create2", methods=["POST"])
def coovi_listar_cre2():
    return compani20.create2l()

@app.route(rout20+"edit1/<string:id>")
def coovi_edit1(id):
    return compani20.edit1(id)

@app.route(rout20+"editl/<string:id>", methods=["POST"])
def coovi_editl(id):
    return compani20.editl(id)

#COSERVICREA LTDA-COMPANIA DE SERVICIOS D #COSERVICREA LTDA-COMPANIA DE SERVICIOS D #COSERVICREA LTDA-COMPANIA DE SERVICIOS D #COSERVICREA LTDA-COMPANIA DE SERVICIOS D #COSERVICREA LTDA-COMPANIA DE SERVICIOS D

rout21 = empresas['empresa21']['rout']
compani21 = empresas['empresa21']['compani']

@app.route(rout21)
def coservi_info():
    return compani21.info()

@app.route(rout21+"list")
def coservi_listarl():
    return compani21.listl()

@app.route(rout21+"list/<string:id>")
def coservi_listar_id(id):
    return compani21.listlid(id)

@app.route(rout21+"cr")
def coservi_listar_cre1():
    return compani21.createl()

@app.route(rout21+"create2", methods=["POST"])
def coservi_listar_cre2():
    return compani21.create2l()

@app.route(rout21+"edit1/<string:id>")
def coservi_edit1(id):
    return compani21.edit1(id)

@app.route(rout21+"editl/<string:id>", methods=["POST"])
def coservi_editl(id):
    return compani21.editl(id)

#COSERVIPP LTDA #COSERVIPP LTDA #COSERVIPP LTDA #COSERVIPP LTDA #COSERVIPP LTDA  #COSERVIPP LTDA #COSERVIPP LTDA #COSERVIPP LTDA #COSERVIPP LTDA #COSERVIPP LTDA

rout22 = empresas['empresa22']['rout']
compani22 = empresas['empresa22']['compani']

@app.route(rout22)
def cospp_info():
    return compani22.info()

@app.route(rout22+"list")
def cospp_listarl():
    return compani22.listl()

@app.route(rout22+"list/<string:id>")
def cospp_listar_id(id):
    return compani22.listlid(id)

@app.route(rout22+"cr")
def cospp_listar_cre1():
    return compani22.createl()

@app.route(rout22+"create2", methods=["POST"])
def cospp_listar_cre2():
    return compani22.create2l()

@app.route(rout22+"edit1/<string:id>")
def cospp_edit1(id):
    return compani22.edit1(id)

@app.route(rout22+"editl/<string:id>", methods=["POST"])
def cospp_editl(id):
    return compani22.editl(id)

#COSMOVIG LTDA #COSMOVIG LTDA #COSMOVIG LTDA #COSMOVIG LTDA #COSMOVIG LTDA #COSMOVIG LTDA#COSMOVIG LTDA #COSMOVIG LTDA #COSMOVIG LTDA #COSMOVIG LTDA #COSMOVIG LTDA #COSMOVIG LTDA #COSMOVIG LTDA #COSMOVIG LTDA

rout23 = empresas['empresa23']['rout']
compani23 = empresas['empresa23']['compani']

@app.route(rout23)
def cosmovig_info():
    return compani23.info()

@app.route(rout23+"list")
def cosmovig_listarl():
    return compani23.listl()

@app.route(rout23+"list/<string:id>")
def cosmovig_listar_id(id):
    return compani23.listlid(id)

@app.route(rout23+"cr")
def cosmovig_listar_cre1():
    return compani23.createl()

@app.route(rout23+"create2", methods=["POST"])
def cosmovig_listar_cre2():
    return compani23.create2l()

@app.route(rout23+"edit1/<string:id>")
def cosmovig_edit1(id):
    return compani23.edit1(id)

@app.route(rout23+"editl/<string:id>", methods=["POST"])
def cosmovig_editl(id):
    return compani23.editl(id)


#CUIDAR LIMITADA #CUIDAR LIMITADA #CUIDAR LIMITADA #CUIDAR LIMITADA #CUIDAR LIMITADA #CUIDAR LIMITADA#CUIDAR LIMITADA #CUIDAR LIMITADA #CUIDAR LIMITADA #CUIDAR LIMITADA #CUIDAR LIMITADA #CUIDAR LIMITADA #CUIDAR LIMITADA #CUIDAR LIMITADA

rout24 = empresas['empresa24']['rout']
compani24 = empresas['empresa24']['compani']

@app.route(rout24)
def cuidar_info():
    return compani24.info()

@app.route(rout24+"list")
def cuidar_listarl():
    return compani24.listl()

@app.route(rout24+"list/<string:id>")
def cuidar_listar_id(id):
    return compani24.listlid(id)

@app.route(rout24+"cr")
def cuidar_listar_cre1():
    return compani24.createl()

@app.route(rout24+"create2", methods=["POST"])
def cuidar_listar_cre2():
    return compani24.create2l()

@app.route(rout24+"edit1/<string:id>")
def cuidar_edit1(id):
    return compani24.edit1(id)

@app.route(rout24+"editl/<string:id>", methods=["POST"])
def cuidar_editl(id):
    return compani24.editl(id)

#DEAS LTDA #DEAS LTDA #DEAS LTDA #DEAS LTDA #DEAS LTDA #DEAS LTDA#DEAS LTDA #DEAS LTDA #DEAS LTDA #DEAS LTDA #DEAS LTDA #DEAS LTDA #DEAS LTDA #DEAS LTDA

rout25 = empresas['empresa25']['rout']
compani25 = empresas['empresa25']['compani']

@app.route(rout25)
def deas_info():
    return compani25.info()

@app.route(rout25+"list")
def deas_listarl():
    return compani25.listl()

@app.route(rout25+"list/<string:id>")
def deas_listar_id(id):
    return compani25.listlid(id)

@app.route(rout25+"cr")
def deas_listar_cre1():
    return compani25.createl()

@app.route(rout25+"create2", methods=["POST"])
def deas_listar_cre2():
    return compani25.create2l()

@app.route(rout25+"edit1/<string:id>")
def deas_edit1(id):
    return compani25.edit1(id)

@app.route(rout25+"editl/<string:id>", methods=["POST"])
def deas_editl(id):
    return compani25.editl(id)


#EFECTIVE SEGURITY JR LTDA #EFECTIVE SEGURITY JR LTDA #EFECTIVE SEGURITY JR LTDA #EFECTIVE SEGURITY JR LTDA #EFECTIVE SEGURITY JR LTDA

rout26 = empresas['empresa26']['rout']
compani26 = empresas['empresa26']['compani']


@app.route(rout26)
def efective_info():
    return compani26.info()

@app.route(rout26+"list")
def efective_listarl():
    return compani26.listl()

@app.route(rout26+"list/<string:id>")
def efective_listar_id(id):
    return compani26.listlid(id)

@app.route(rout26+"cr")
def efective_listar_cre1():
    return compani26.createl()

@app.route(rout26+"create2", methods=["POST"])
def efective_listar_cre2():
    return compani26.create2l()

@app.route(rout26+"edit1/<string:id>")
def efective_edit1(id):
    return compani26.edit1(id)

@app.route(rout26+"editl/<string:id>", methods=["POST"])
def efective_editl(id):
    return compani26.editl(id)

#ELECTROEQUIPOS COLOMBIA S.A.S. #ELECTROEQUIPOS COLOMBIA S.A.S. #ELECTROEQUIPOS COLOMBIA S.A.S. #ELECTROEQUIPOS COLOMBIA S.A.S. #ELECTROEQUIPOS COLOMBIA S.A.S.

rout27 = empresas['empresa27']['rout']
compani27 = empresas['empresa27']['compani']

@app.route(rout27)
def electro_info():
    return compani27.info()

@app.route(rout27+"list")
def electro_listarl():
    return compani27.listl()

@app.route(rout27+"list/<string:id>")
def electro_listar_id(id):
    return compani27.listlid(id)

@app.route(rout27+"cr")
def electro_listar_cre1():
    return compani27.createl()

@app.route(rout27+"create2", methods=["POST"])
def electro_listar_cre2():
    return compani27.create2l()

@app.route(rout27+"edit1/<string:id>")
def electro_edit1(id):
    return compani27.edit1(id)

@app.route(rout27+"editl/<string:id>", methods=["POST"])
def electro_editl(id):
    return compani27.editl(id)

#EXTRA SEGURIDAD LIMITADA #EXTRA SEGURIDAD LIMITADA #EXTRA SEGURIDAD LIMITADA #EXTRA SEGURIDAD LIMITADA #EXTRA SEGURIDAD LIMITADA

rout28 = empresas['empresa28']['rout']
compani28 = empresas['empresa28']['compani']

@app.route(rout28)
def extra_info():
    return compani28.info()

@app.route(rout28+"list")
def extra_listarl():
    return compani28.listl()

@app.route(rout28+"list/<string:id>")
def extra_listar_id(id):
    return compani28.listlid(id)

@app.route(rout28+"cr")
def extra_listar_cre1():
    return compani28.createl()

@app.route(rout28+"create2", methods=["POST"])
def extra_listar_cre2():
    return compani28.create2l()

@app.route(rout28+"edit1/<string:id>")
def extra_edit1(id):
    return compani28.edit1(id)

@app.route(rout28+"editl/<string:id>", methods=["POST"])
def extra_editl(id):
    return compani28.editl(id)

#FALCON FARMS DE COLOMBIA SA #FALCON FARMS DE COLOMBIA SA #FALCON FARMS DE COLOMBIA SA #FALCON FARMS DE COLOMBIA SA #FALCON FARMS DE COLOMBIA SA

rout29 = empresas['empresa29']['rout']
compani29 = empresas['empresa29']['compani']

@app.route(rout29)
def falcon_info():
    return compani29.info()

@app.route(rout29+"list")
def falcon_listarl():
    return compani29.listl()

@app.route(rout29+"list/<string:id>")
def falcon_listar_id(id):
    return compani29.listlid(id)

@app.route(rout29+"cr")
def falcon_listar_cre1():
    return compani29.createl()

@app.route(rout29+"create2", methods=["POST"])
def falcon_listar_cre2():
    return compani29.create2l()

@app.route(rout29+"edit1/<string:id>")
def falcon_edit1(id):
    return compani29.edit1(id)

@app.route(rout29+"editl/<string:id>", methods=["POST"])
def falcon_editl(id):
    return compani29.editl(id)

#FIDELITY SECURITY COMPANY LTDA #FIDELITY SECURITY COMPANY LTDA #FIDELITY SECURITY COMPANY LTDA #FIDELITY SECURITY COMPANY LTDA #FIDELITY SECURITY COMPANY LTDA

rout30 = empresas['empresa30']['rout']
compani30 = empresas['empresa30']['compani']

@app.route(rout30)
def fidelity_info():
    return compani30.info()

@app.route(rout30+"list")
def fidelity_listarl():
    return compani30.listl()

@app.route(rout30+"list/<string:id>")
def fidelity_listar_id(id):
    return compani30.listlid(id)

@app.route(rout30+"cr")
def fidelity_listar_cre1():
    return compani30.createl()

@app.route(rout30+"create2", methods=["POST"])
def fidelity_listar_cre2():
    return compani30.create2l()

@app.route(rout30+"edit1/<string:id>")
def fidelity_edit1(id):
    return compani30.edit1(id)

@app.route(rout30+"editl/<string:id>", methods=["POST"])
def fidelity_editl(id):
    return compani30.editl(id)

#FORTOX S A #FORTOX S A #FORTOX S A #FORTOX S A #FORTOX S A #FORTOX S A#FORTOX S A #FORTOX S A #FORTOX S A #FORTOX S A #FORTOX S A #FORTOX S A #FORTOX S A #FORTOX S A

rout31 = empresas['empresa31']['rout']
compani31 = empresas['empresa31']['compani']

@app.route(rout31)
def fortox_info():
    return compani31.info()

@app.route(rout31+"list")
def fortox_listarl():
    return compani31.listl()

@app.route(rout31+"list/<string:id>")
def fortox_listar_id(id):
    return compani31.listlid(id)

@app.route(rout31+"cr")
def fortox_listar_cre1():
    return compani31.createl()

@app.route(rout31+"create2", methods=["POST"])
def fortox_listar_cre2():
    return compani31.create2l()

@app.route(rout31+"edit1/<string:id>")
def fortox_edit1(id):
    return compani31.edit1(id)

@app.route(rout31+"editl/<string:id>", methods=["POST"])
def fortox_editl(id):
    return compani31.editl(id)


#G4S SECURE SOLUTIONS COLOMBIA S. A #G4S SECURE SOLUTIONS COLOMBIA S. A #G4S SECURE SOLUTIONS COLOMBIA S. A #G4S SECURE SOLUTIONS COLOMBIA S. A #G4S SECURE SOLUTIONS COLOMBIA S. A

rout32 = empresas['empresa32']['rout']
compani32 = empresas['empresa32']['compani']

@app.route(rout32)
def gsssol_info():
    return compani32.info()

@app.route(rout32+"list")
def gsssol_listarl():
    return compani32.listl()

@app.route(rout32+"list/<string:id>")
def gsssol_listar_id(id):
    return compani32.listlid(id)

@app.route(rout32+"cr")
def gsssol_listar_cre1():
    return compani32.createl()

@app.route(rout32+"create2", methods=["POST"])
def gsssol_listar_cre2():
    return compani32.create2l()

@app.route(rout32+"edit1/<string:id>")
def gsssol_edit1(id):
    return compani32.edit1(id)

@app.route(rout32+"editl/<string:id>", methods=["POST"])
def gsssol_editl(id):
    return compani32.editl(id)

#GENDARMES DE SEGURIDAD LTDA #GENDARMES DE SEGURIDAD LTDA #GENDARMES DE SEGURIDAD LTDA #GENDARMES DE SEGURIDAD LTDA #GENDARMES DE SEGURIDAD LTDA

rout33 = empresas['empresa33']['rout']
compani33 = empresas['empresa33']['compani']

@app.route(rout33)
def gendar_info():
    return compani33.info()

@app.route(rout33+"list")
def gendar_listarl():
    return compani33.listl()

@app.route(rout33+"list/<string:id>")
def gendar_listar_id(id):
    return compani33.listlid(id)

@app.route(rout33+"cr")
def gendar_listar_cre1():
    return compani33.createl()

@app.route(rout33+"create2", methods=["POST"])
def gendar_listar_cre2():
    return compani33.create2l()

@app.route(rout33+"edit1/<string:id>")
def gendar_edit1(id):
    return compani33.edit1(id)

@app.route(rout33+"editl/<string:id>", methods=["POST"])
def gendar_editl(id):
    return compani33.editl(id)

#HOLDING DE SEGURIDAD LTDA #HOLDING DE SEGURIDAD LTDA #HOLDING DE SEGURIDAD LTDA #HOLDING DE SEGURIDAD LTDA #HOLDING DE SEGURIDAD LTDA

rout34 = empresas['empresa34']['rout']
compani34 = empresas['empresa34']['compani']

@app.route(rout34)
def holding_info():
    return compani34.info()

@app.route(rout34+"list")
def holding_listarl():
    return compani34.listl()

@app.route(rout34+"list/<string:id>")
def holding_listar_id(id):
    return compani34.listlid(id)

@app.route(rout34+"cr")
def holding_listar_cre1():
    return compani34.createl()

@app.route(rout34+"create2", methods=["POST"])
def holding_listar_cre2():
    return compani34.create2l()

@app.route(rout34+"edit1/<string:id>")
def holding_edit1(id):
    return compani34.edit1(id)

@app.route(rout34+"editl/<string:id>", methods=["POST"])
def holding_editl(id):
    return compani34.editl(id)

#IMPROCAN SEGURIDAD LTDA #IMPROCAN SEGURIDAD LTDA #IMPROCAN SEGURIDAD LTDA #IMPROCAN SEGURIDAD LTDA #IMPROCAN SEGURIDAD LTDA

rout35 = empresas['empresa35']['rout']
compani35 = empresas['empresa35']['compani']

@app.route(rout35)
def improcan_info():
    return compani35.info()

@app.route(rout35+"list")
def improcan_listarl():
    return compani35.listl()

@app.route(rout35+"list/<string:id>")
def improcan_listar_id(id):
    return compani35.listlid(id)

@app.route(rout35+"cr")
def improcan_listar_cre1():
    return compani35.createl()

@app.route(rout35+"create2", methods=["POST"])
def improcan_listar_cre2():
    return compani35.create2l()

@app.route(rout35+"edit1/<string:id>")
def improcan_edit1(id):
    return compani35.edit1(id)

@app.route(rout35+"editl/<string:id>", methods=["POST"])
def improcan_editl(id):
    return compani35.editl(id)

#KEY STELL SECURITY LTDA #KEY STELL SECURITY LTDA #KEY STELL SECURITY LTDA #KEY STELL SECURITY LTDA #KEY STELL SECURITY LTDA #KEY STELL SECURITY LTDA#KEY STELL SECURITY LTDA #KEY STELL SECURITY LTDA #KEY STELL SECURITY LTDA #KEY STELL SECURITY LTDA #KEY STELL SECURITY LTDA #KEY STELL SECURITY LTDA #KEY STELL SECURITY LTDA #KEY STELL SECURITY LTDA

rout36 = empresas['empresa36']['rout']
compani36 = empresas['empresa36']['compani']

@app.route(rout36)
def keystell_info():
    return compani36.info()

@app.route(rout36+"list")
def keystell_listarl():
    return compani36.listl()

@app.route(rout36+"list/<string:id>")
def keystell_listar_id(id):
    return compani36.listlid(id)

@app.route(rout36+"cr")
def keystell_listar_cre1():
    return compani36.createl()

@app.route(rout36+"create2", methods=["POST"])
def keystell_listar_cre2():
    return compani36.create2l()

@app.route(rout36+"edit1/<string:id>")
def keystell_edit1(id):
    return compani36.edit1(id)

@app.route(rout36+"editl/<string:id>", methods=["POST"])
def keystell_editl(id):
    return compani36.editl(id)

#LATAMSEC SECURITY LTDA#LATAMSEC SECURITY LTDA #LATAMSEC SECURITY LTDA #LATAMSEC SECURITY LTDA #LATAMSEC SECURITY LTDA #LATAMSEC SECURITY LTDA #LATAMSEC SECURITY LTDA #LATAMSEC SECURITY LTDA #LATAMSEC SECURITY LTDA

rout37 = empresas['empresa37']['rout']
compani37 = empresas['empresa37']['compani']

@app.route(rout37)
def latamsec_info():
    return compani37.info()

@app.route(rout37+"list")
def latamsec_listarl():
    return compani37.listl()

@app.route(rout37+"list/<string:id>")
def latamsec_listar_id(id):
    return compani37.listlid(id)

@app.route(rout37+"cr")
def latamsec_listar_cre1():
    return compani37.createl()

@app.route(rout37+"create2", methods=["POST"])
def latamsec_listar_cre2():
    return compani37.create2l()

@app.route(rout37+"edit1/<string:id>")
def latamsec_edit1(id):
    return compani37.edit1(id)

@app.route(rout37+"editl/<string:id>", methods=["POST"])
def latamsec_editl(id):
    return compani37.editl(id)


# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA # LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA# LIRA#

rout = empresas['empresa38']['rout']
compani = empresas['empresa38']['compani']

@app.route(rout)
def lir_info():
    return compani.info()

@app.route(rout+"list")
def lir_listarl():
    return compani.listl()

@app.route(rout+"list/<string:id>")
def lir_listar_id(id):
    return compani.listlid(id)

@app.route(rout+"cr")
def lir_listar_cre1():
    return compani.createl()

@app.route(rout+"create2", methods=["POST"])
def lir_listar_cre2():
    return compani.create2l()

@app.route(rout+"edit1/<string:id>")
def lir_edit1(id):
    return compani.edit1(id)

@app.route(rout+"editl/<string:id>", methods=["POST"])
def lir_editl(id):
    return compani.editl(id)


#MAGNUS SEGURIDAD LTDA #MAGNUS SEGURIDAD LTDA #MAGNUS SEGURIDAD LTDA #MAGNUS SEGURIDAD LTDA #MAGNUS SEGURIDAD LTDA #MAGNUS SEGURIDAD LTDA

rout39 = empresas['empresa39']['rout']
compani39 = empresas['empresa39']['compani']

@app.route(rout39)
def magnus_info():
    return compani39.info()

@app.route(rout39+"list")
def magnus_listarl():
    return compani39.listl()

@app.route(rout39+"list/<string:id>")
def magnus_listar_id(id):
    return compani39.listlid(id)

@app.route(rout39+"cr")
def magnus_listar_cre1():
    return compani39.createl()

@app.route(rout39+"create2", methods=["POST"])
def magnus_listar_cre2():
    return compani39.create2l()

@app.route(rout39+"edit1/<string:id>")
def megnus_edit1(id):
    return compani39.edit1(id)

@app.route(rout39+"editl/<string:id>", methods=["POST"])
def megnus_editl(id):
    return compani39.editl(id)

#MASTIN SEGURIDAD LTDA #MASTIN SEGURIDAD LTDA #MASTIN SEGURIDAD LTDA #MASTIN SEGURIDAD LTDA #MASTIN SEGURIDAD LTDA #MASTIN SEGURIDAD LTDA

rout40 = empresas['empresa40']['rout']
compani40 = empresas['empresa40']['compani']

@app.route(rout40)
def mastin_info():
    return compani40.info()

@app.route(rout40+"list")
def mastin_listarl():
    return compani40.listl()

@app.route(rout40+"list/<string:id>")
def mastin_listar_id(id):
    return compani40.listlid(id)

@app.route(rout40+"cr")
def mastin_listar_cre1():
    return compani40.createl()

@app.route(rout40+"create2", methods=["POST"])
def mastin_listar_cre2():
    return compani40.create2l()

@app.route(rout40+"edit1/<string:id>")
def mastin_edit1(id):
    return compani40.edit1(id)

@app.route(rout40+"editl/<string:id>", methods=["POST"])
def mastin_editl(id):
    return compani40.editl(id)

#MEGASEGURIDAD LTDA #MEGASEGURIDAD LTDA #MEGASEGURIDAD LTDA #MEGASEGURIDAD LTDA #MEGASEGURIDAD LTDA #MEGASEGURIDAD LTDA

rout41 = empresas['empresa41']['rout']
compani41 = empresas['empresa41']['compani']

@app.route(rout41)
def mseg_info():
    return compani41.info()

@app.route(rout41+"list")
def mseg_listarl():
    return compani41.listl()

@app.route(rout41+"list/<string:id>")
def mseg_listar_id(id):
    return compani41.listlid(id)

@app.route(rout41+"cr")
def mseg_listar_cre1():
    return compani41.createl()

@app.route(rout41+"create2", methods=["POST"])
def mseg_listar_cre2():
    return compani41.create2l()

@app.route(rout41+"edit1/<string:id>")
def mseg_edit1(id):
    return compani41.edit1(id)

@app.route(rout41+"editl/<string:id>", methods=["POST"])
def mseg_editl(id):
    return compani41.editl(id)

#NAPOLES LTDA #NAPOLES LTDA #NAPOLES LTDA #NAPOLES LTDA #NAPOLES LTDA #NAPOLES LTDA #NAPOLES LTDA #NAPOLES LTDA #NAPOLES LTDA #NAPOLES LTDA #NAPOLES LTDA #NAPOLES LTDA

rout42 = empresas['empresa42']['rout']
compani42 = empresas['empresa42']['compani']

@app.route(rout42)
def napoles_info():
    return compani42.info()

@app.route(rout42+"list")
def napoles_listarl():
    return compani42.listl()

@app.route(rout42+"list/<string:id>")
def napoles_listar_id(id):
    return compani42.listlid(id)

@app.route(rout42+"cr")
def napoles_listar_cre1():
    return compani42.createl()

@app.route(rout42+"create2", methods=["POST"])
def napoles_listar_cre2():
    return compani42.create2l()

@app.route(rout42+"edit1/<string:id>")
def napoles_edit1(id):
    return compani42.edit1(id)

@app.route(rout42+"editl/<string:id>", methods=["POST"])
def napoles_editl(id):
    return compani42.editl(id)


#NASER LTDA #NASER LTDA #NASER LTDA #NASER LTDA #NASER LTDA #NASER LTDA #NASER LTDA #NASER LTDA #NASER LTDA #NASER LTDA #NASER LTDA #NASER LTDA

rout43 = empresas['empresa43']['rout']
compani43 = empresas['empresa43']['compani']

@app.route(rout43)
def naser_info():
    return compani43.info()

@app.route(rout43+"list")
def naser_listarl():
    return compani43.listl()

@app.route(rout43+"list/<string:id>")
def naser_listar_id(id):
    return compani43.listlid(id)

@app.route(rout43+"cr")
def naser_listar_cre1():
    return compani43.createl()

@app.route(rout43+"create2", methods=["POST"])
def naser_listar_cre2():
    return compani43.create2l()

@app.route(rout43+"edit1/<string:id>")
def naser_edit1(id):
    return compani43.edit1(id)

@app.route(rout43+"editl/<string:id>", methods=["POST"])
def naser_editl(id):
    return compani43.editl(id)

#OPERADORES Y ADMINISTRADORES INTERNACIONALES DE VIAS S.A.S. #OPERADORES Y ADMINISTRADORES INTERNACIONALES DE VIAS S.A.S. #OPERADORES Y ADMINISTRADORES INTERNACIONALES DE VIAS S.A.S. #OPERADORES Y ADMINISTRADORES INTERNACIONALES DE VIAS S.A.S. #OPERADORES Y ADMINISTRADORES INTERNACIONALES DE VIAS S.A.S. #OPERADORES Y ADMINISTRADORES INTERNACIONALES DE VIAS S.A.S.

rout44 = empresas['empresa44']['rout']
compani44 = empresas['empresa44']['compani']

@app.route(rout44)
def opeadin_info():
    return compani44.info()

@app.route(rout44+"list")
def opeadin_listarl():
    return compani44.listl()

@app.route(rout44+"list/<string:id>")
def opeadin_listar_id(id):
    return compani44.listlid(id)

@app.route(rout44+"cr")
def opeadin_listar_cre1():
    return compani44.createl()

@app.route(rout44+"create2", methods=["POST"])
def opeadin_listar_cre2():
    return compani44.create2l()

@app.route(rout44+"edit1/<string:id>")
def opeadin_edit1(id):
    return compani44.edit1(id)

@app.route(rout44+"editl/<string:id>", methods=["POST"])
def opeadin_editl(id):
    return compani44.editl(id)

#PROSEGUR #PROSEGUR #PROSEGUR #PROSEGUR #PROSEGUR #PROSEGUR #PROSEGUR #PROSEGUR #PROSEGUR #PROSEGUR #PROSEGUR #PROSEGUR #PROSEGUR #PROSEGUR #PROSEGUR #PROSEGUR #PROSEGUR #PROSEGUR

rout45 = empresas['empresa45']['rout']
compani45 = empresas['empresa45']['compani']

@app.route(rout45)
def proseguir_info():
    return compani45.info()

@app.route(rout45+"list")
def proseguir_listarl():
    return compani45.listl()

@app.route(rout45+"list/<string:id>")
def proseguir_listar_id(id):
    return compani45.listlid(id)

@app.route(rout45+"cr")
def proseguir_listar_cre1():
    return compani45.createl()

@app.route(rout45+"create2", methods=["POST"])
def proseguir_listar_cre2():
    return compani45.create2l()

@app.route(rout45+"edit1/<string:id>")
def proseguir_edit1(id):
    return compani45.edit1(id)

@app.route(rout45+"editl/<string:id>", methods=["POST"])
def proseguir_editl(id):
    return compani45.editl(id)

#PROSEGUR VIGILANCIA Y SEGURIDAD PRIVADA #PROSEGUR VIGILANCIA Y SEGURIDAD PRIVADA #PROSEGUR VIGILANCIA Y SEGURIDAD PRIVADA #PROSEGUR VIGILANCIA Y SEGURIDAD PRIVADA #PROSEGUR VIGILANCIA Y SEGURIDAD PRIVADA #PROSEGUR VIGILANCIA Y SEGURIDAD PRIVADA

rout46 = empresas['empresa46']['rout']
compani46 = empresas['empresa46']['compani']

@app.route(rout46)
def provigys_info():
    return compani46.info()

@app.route(rout46+"list")
def provigys_listarl():
    return compani46.listl()

@app.route(rout46+"list/<string:id>")
def provigys_listar_id(id):
    return compani46.listlid(id)

@app.route(rout46+"cr")
def provigys_listar_cre1():
    return compani46.createl()

@app.route(rout46+"create2", methods=["POST"])
def provigys_listar_cre2():
    return compani46.create2l()

@app.route(rout46+"edit1/<string:id>")
def provigys_edit1(id):
    return compani46.edit1(id)

@app.route(rout46+"editl/<string:id>", methods=["POST"])
def provigys_editl(id):
    return compani46.editl(id)

#PROTECCION Y VIGILANCIA TURIN PROVITURIN #PROTECCION Y VIGILANCIA TURIN PROVITURIN #PROTECCION Y VIGILANCIA TURIN PROVITURIN #PROTECCION Y VIGILANCIA TURIN PROVITURIN #PROTECCION Y VIGILANCIA TURIN PROVITURIN #PROTECCION Y VIGILANCIA TURIN PROVITURIN

rout47 = empresas['empresa47']['rout']
compani47 = empresas['empresa47']['compani']

@app.route(rout47)
def proyvigtu_info():
    return compani47.info()

@app.route(rout47+"list")
def proyvigtu_listarl():
    return compani47.listl()

@app.route(rout47+"list/<string:id>")
def proyvigtu_listar_id(id):
    return compani47.listlid(id)

@app.route(rout47+"cr")
def proyvigtu_listar_cre1():
    return compani47.createl()

@app.route(rout47+"create2", methods=["POST"])
def proyvigtu_listar_cre2():
    return compani47.create2l()

@app.route(rout47+"edit1/<string:id>")
def proyvigtu_edit1(id):
    return compani47.edit1(id)

@app.route(rout47+"editl/<string:id>", methods=["POST"])
def proyvigtu_editl(id):
    return compani47.editl(id)

#RISK Y SOLUTIONS GROUP LTDA #RISK Y SOLUTIONS GROUP LTDA #RISK Y SOLUTIONS GROUP LTDA #RISK Y SOLUTIONS GROUP LTDA #RISK Y SOLUTIONS GROUP LTDA #RISK Y SOLUTIONS GROUP LTDA

rout48 = empresas['empresa48']['rout']
compani48 = empresas['empresa48']['compani']

@app.route(rout48)
def risksol_info():
    return compani48.info()

@app.route(rout48+"list")
def risksol_listarl():
    return compani48.listl()

@app.route(rout48+"list/<string:id>")
def risksol_listar_id(id):
    return compani48.listlid(id)

@app.route(rout48+"cr")
def risksol_listar_cre1():
    return compani48.createl()

@app.route(rout48+"create2", methods=["POST"])
def risksol_listar_cre2():
    return compani48.create2l()

@app.route(rout48+"edit1/<string:id>")
def risksol_edit1(id):
    return compani48.edit1(id)

@app.route(rout48+"editl/<string:id>", methods=["POST"])
def risksol_editl(id):
    return compani48.editl(id)

#SEGURIDAD APOLO LIMITADA #SEGURIDAD APOLO LIMITADA #SEGURIDAD APOLO LIMITADA #SEGURIDAD APOLO LIMITADA #SEGURIDAD APOLO LIMITADA #SEGURIDAD APOLO LIMITADA

rout49 = empresas['empresa49']['rout']
compani49 = empresas['empresa49']['compani']

@app.route(rout49)
def segapolo_info():
    return compani49.info()

@app.route(rout49+"list")
def segapolo_listarl():
    return compani49.listl()

@app.route(rout49+"list/<string:id>")
def segapolo_listar_id(id):
    return compani49.listlid(id)

@app.route(rout49+"cr")
def segapolo_listar_cre1():
    return compani49.createl()

@app.route(rout49+"create2", methods=["POST"])
def segapolo_listar_cre2():
    return compani49.create2l()

@app.route(rout49+"edit1/<string:id>")
def segapolo_edit1(id):
    return compani49.edit1(id)

@app.route(rout49+"editl/<string:id>", methods=["POST"])
def segapolo_editl(id):
    return compani49.editl(id)

#SEGURIDAD ATLANTIS LTDA #SEGURIDAD ATLANTIS LTDA #SEGURIDAD ATLANTIS LTDA #SEGURIDAD ATLANTIS LTDA #SEGURIDAD ATLANTIS LTDA #SEGURIDAD ATLANTIS LTDA

rout50 = empresas['empresa50']['rout']
compani50 = empresas['empresa50']['compani']

@app.route(rout50)
def segatlas_info():
    return compani50.info()

@app.route(rout50+"list")
def segatlas_listarl():
    return compani50.listl()

@app.route(rout50+"list/<string:id>")
def segatlas_listar_id(id):
    return compani50.listlid(id)

@app.route(rout50+"cr")
def segatlas_listar_cre1():
    return compani50.createl()

@app.route(rout50+"create2", methods=["POST"])
def segatlas_listar_cre2():
    return compani50.create2l()

@app.route(rout50+"edit1/<string:id>")
def segatlas_edit1(id):
    return compani50.edit1(id)

@app.route(rout50+"editl/<string:id>", methods=["POST"])
def segatlas_editl(id):
    return compani50.editl(id)

#SEGURIDAD CANADA LTDA #SEGURIDAD CANADA LTDA #SEGURIDAD CANADA LTDA #SEGURIDAD CANADA LTDA #SEGURIDAD CANADA LTDA #SEGURIDAD CANADA LTDA

rout51 = empresas['empresa51']['rout']
compani51 = empresas['empresa51']['compani']

@app.route(rout51)
def segcan_info():
    return compani51.info()

@app.route(rout51+"list")
def segcan_listarl():
    return compani51.listl()

@app.route(rout51+"list/<string:id>")
def segcan_listar_id(id):
    return compani51.listlid(id)

@app.route(rout51+"cr")
def segcan_listar_cre1():
    return compani51.createl()

@app.route(rout51+"create2", methods=["POST"])
def segcan_listar_cre2():
    return compani51.create2l()

@app.route(rout51+"edit1/<string:id>")
def segcan_edit1(id):
    return compani51.edit1(id)

@app.route(rout51+"editl/<string:id>", methods=["POST"])
def segcan_editl(id):
    return compani51.editl(id)


#SEGURIDAD CANINA DE COLOMBIA LTDA SECAN #SEGURIDAD CANINA DE COLOMBIA LTDA SECAN #SEGURIDAD CANINA DE COLOMBIA LTDA SECAN #SEGURIDAD CANINA DE COLOMBIA LTDA SECAN #SEGURIDAD CANINA DE COLOMBIA LTDA SECAN #SEGURIDAD CANINA DE COLOMBIA LTDA SECAN

rout52 = empresas['empresa52']['rout']
compani52 = empresas['empresa52']['compani']

@app.route(rout52)
def segcanina_info():
    return compani52.info()

@app.route(rout52+"list")
def segcanina_listarl():
    return compani52.listl()

@app.route(rout52+"list/<string:id>")
def segcanina_listar_id(id):
    return compani52.listlid(id)

@app.route(rout52+"cr")
def segcanina_listar_cre1():
    return compani52.createl()

@app.route(rout52+"create2", methods=["POST"])
def segcanina_listar_cre2():
    return compani52.create2l()

@app.route(rout52+"edit1/<string:id>")
def segcanina_edit1(id):
    return compani52.edit1(id)

@app.route(rout52+"editl/<string:id>", methods=["POST"])
def segcanina_editl(id):
    return compani52.editl(id)

#SEGURIDAD CENTRAL LTDA #SEGURIDAD CENTRAL LTDA #SEGURIDAD CENTRAL LTDA #SEGURIDAD CENTRAL LTDA #SEGURIDAD CENTRAL LTDA #SEGURIDAD CENTRAL LTDA

rout53 = empresas['empresa53']['rout']
compani53 = empresas['empresa53']['compani']

@app.route(rout53)
def segcentral_info():
    return compani53.info()

@app.route(rout53+"list")
def segcentral_listarl():
    return compani53.listl()

@app.route(rout53+"list/<string:id>")
def segcentral_listar_id(id):
    return compani53.listlid(id)

@app.route(rout53+"cr")
def segcentral_listar_cre1():
    return compani53.createl()

@app.route(rout53+"create2", methods=["POST"])
def segcentral_listar_cre2():
    return compani53.create2l()

@app.route(rout53+"edit1/<string:id>")
def segcentral_edit1(id):
    return compani53.edit1(id)

@app.route(rout53+"editl/<string:id>", methods=["POST"])
def segcentral_editl(id):
    return compani53.editl(id)


#SEGURIDAD DECAPOLIS LTDA #SEGURIDAD DECAPOLIS LTDA #SEGURIDAD DECAPOLIS LTDA #SEGURIDAD DECAPOLIS LTDA #SEGURIDAD DECAPOLIS LTDA #SEGURIDAD DECAPOLIS LTDA

rout54 = empresas['empresa54']['rout']
compani54 = empresas['empresa54']['compani']

@app.route(rout54)
def segdeca_info():
    return compani54.info()

@app.route(rout54+"list")
def segdeca_listarl():
    return compani54.listl()

@app.route(rout54+"list/<string:id>")
def segdeca_listar_id(id):
    return compani54.listlid(id)

@app.route(rout54+"cr")
def segdeca_listar_cre1():
    return compani54.createl()

@app.route(rout54+"create2", methods=["POST"])
def segdeca_listar_cre2():
    return compani54.create2l()

@app.route(rout54+"edit1/<string:id>")
def segdeca_edit1(id):
    return compani54.edit1(id)

@app.route(rout54+"editl/<string:id>", methods=["POST"])
def segdeca_editl(id):
    return compani54.editl(id)


#SEGURIDAD DIGITAL LTDA #SEGURIDAD DIGITAL LTDA #SEGURIDAD DIGITAL LTDA #SEGURIDAD DIGITAL LTDA #SEGURIDAD DIGITAL LTDA #SEGURIDAD DIGITAL LTDA

rout55 = empresas['empresa55']['rout']
compani55 = empresas['empresa55']['compani']

@app.route(rout55)
def segdig_info():
    return compani55.info()

@app.route(rout55+"list")
def segdig_listarl():
    return compani55.listl()

@app.route(rout55+"list/<string:id>")
def segdig_listar_id(id):
    return compani55.listlid(id)

@app.route(rout55+"cr")
def segdig_listar_cre1():
    return compani55.createl()

@app.route(rout55+"create2", methods=["POST"])
def segdig_listar_cre2():
    return compani55.create2l()

@app.route(rout55+"edit1/<string:id>")
def segdig_edit1(id):
    return compani55.edit1(id)

@app.route(rout55+"editl/<string:id>", methods=["POST"])
def segdig_editl(id):
    return compani55.editl(id)

#SEGURIDAD ELIAR LTDA #SEGURIDAD ELIAR LTDA #SEGURIDAD ELIAR LTDA #SEGURIDAD ELIAR LTDA #SEGURIDAD ELIAR LTDA #SEGURIDAD ELIAR LTDA

rout56 = empresas['empresa56']['rout']
compani56 = empresas['empresa56']['compani']

@app.route(rout56)
def segelir_info():
    return compani56.info()

@app.route(rout56+"list")
def segelir_listarl():
    return compani56.listl()

@app.route(rout56+"list/<string:id>")
def segelir_listar_id(id):
    return compani56.listlid(id)

@app.route(rout56+"cr")
def segelir_listar_cre1():
    return compani56.createl()

@app.route(rout56+"create2", methods=["POST"])
def segelir_listar_cre2():
    return compani56.create2l()

@app.route(rout56+"edit1/<string:id>")
def segelir_edit1(id):
    return compani56.edit1(id)

@app.route(rout56+"editl/<string:id>", methods=["POST"])
def segelir_editl(id):
    return compani56.editl(id)

#SEGURIDAD EXPLORER LTDA #SEGURIDAD EXPLORER LTDA #SEGURIDAD EXPLORER LTDA #SEGURIDAD EXPLORER LTDA #SEGURIDAD EXPLORER LTDA #SEGURIDAD EXPLORER LTDA

rout57 = empresas['empresa57']['rout']
compani57 = empresas['empresa57']['compani']

@app.route(rout57)
def segexplo_info():
    return compani57.info()

@app.route(rout57+"list")
def segexplo_listarl():
    return compani57.listl()

@app.route(rout57+"list/<string:id>")
def segexplo_listar_id(id):
    return compani57.listlid(id)

@app.route(rout57+"cr")
def segexplo_listar_cre1():
    return compani57.createl()

@app.route(rout57+"create2", methods=["POST"])
def segexplo_listar_cre2():
    return compani57.create2l()

@app.route(rout57+"edit1/<string:id>")
def segexplo_edit1(id):
    return compani57.edit1(id)

@app.route(rout57+"editl/<string:id>", methods=["POST"])
def segexplo_editl(id):
    return compani57.editl(id)

#SEGURIDAD GRAN METROPOLIS LTDA #SEGURIDAD GRAN METROPOLIS LTDA #SEGURIDAD GRAN METROPOLIS LTDA #SEGURIDAD GRAN METROPOLIS LTDA #SEGURIDAD GRAN METROPOLIS LTDA #SEGURIDAD GRAN METROPOLIS LTDA

rout58 = empresas['empresa58']['rout']
compani58 = empresas['empresa58']['compani']

@app.route(rout58)
def seggran_info():
    return compani58.info()

@app.route(rout58+"list")
def seggran_listarl():
    return compani58.listl()

@app.route(rout58+"list/<string:id>")
def seggran_listar_id(id):
    return compani58.listlid(id)

@app.route(rout58+"cr")
def seggran_listar_cre1():
    return compani58.createl()

@app.route(rout58+"create2", methods=["POST"])
def seggran_listar_cre2():
    return compani58.create2l()

@app.route(rout58+"edit1/<string:id>")
def seggran_edit1(id):
    return compani58.edit1(id)

@app.route(rout58+"editl/<string:id>", methods=["POST"])
def seggran_editl(id):
    return compani58.editl(id)

#SEGURIDAD HORUS LTDA #SEGURIDAD HORUS LTDA #SEGURIDAD HORUS LTDA #SEGURIDAD HORUS LTDA #SEGURIDAD HORUS LTDA #SEGURIDAD HORUS LTDA

rout59 = empresas['empresa59']['rout']
compani59 = empresas['empresa59']['compani']

@app.route(rout59)
def seghorus_info():
    return compani59.info()

@app.route(rout59+"list")
def seghorus_listarl():
    return compani59.listl()

@app.route(rout59+"list/<string:id>")
def seghorus_listar_id(id):
    return compani59.listlid(id)

@app.route(rout59+"cr")
def seghorus_listar_cre1():
    return compani59.createl()

@app.route(rout59+"create2", methods=["POST"])
def seghorus_listar_cre2():
    return compani59.create2l()

@app.route(rout59+"edit1/<string:id>")
def seghorus_edit1(id):
    return compani59.edit1(id)

@app.route(rout59+"editl/<string:id>", methods=["POST"])
def seghorus_editl(id):
    return compani59.editl(id)

#SEGURIDAD LOS VIRREYES LTDA #SEGURIDAD LOS VIRREYES LTDA #SEGURIDAD LOS VIRREYES LTDA #SEGURIDAD LOS VIRREYES LTDA #SEGURIDAD LOS VIRREYES LTDA #SEGURIDAD LOS VIRREYES LTDA

rout60 = empresas['empresa60']['rout']
compani60 = empresas['empresa60']['compani']

@app.route(rout60)
def segvirrey_info():
    return compani60.info()

@app.route(rout60+"list")
def segvirrey_listarl():
    return compani60.listl()

@app.route(rout60+"list/<string:id>")
def segvirrey_listar_id(id):
    return compani60.listlid(id)

@app.route(rout60+"cr")
def segvirrey_listar_cre1():
    return compani60.createl()

@app.route(rout60+"create2", methods=["POST"])
def segvirrey_listar_cre2():
    return compani60.create2l()

@app.route(rout60+"edit1/<string:id>")
def segvirrey_edit1(id):
    return compani60.edit1(id)

@app.route(rout60+"editl/<string:id>", methods=["POST"])
def segvirrey_editl(id):
    return compani60.editl(id)

#SEGURIDAD MODERNA COLOMBIANA LTDA #SEGURIDAD MODERNA COLOMBIANA LTDA #SEGURIDAD MODERNA COLOMBIANA LTDA #SEGURIDAD MODERNA COLOMBIANA LTDA #SEGURIDAD MODERNA COLOMBIANA LTDA #SEGURIDAD MODERNA COLOMBIANA LTDA

rout61 = empresas['empresa61']['rout']
compani61 = empresas['empresa61']['compani']

@app.route(rout61)
def segmod_info():
    return compani61.info()

@app.route(rout61+"list")
def segmod_listarl():
    return compani61.listl()

@app.route(rout61+"list/<string:id>")
def segmod_listar_id(id):
    return compani61.listlid(id)

@app.route(rout61+"cr")
def segmod_listar_cre1():
    return compani61.createl()

@app.route(rout61+"create2", methods=["POST"])
def segmod_listar_cre2():
    return compani61.create2l()

@app.route(rout61+"edit1/<string:id>")
def segmod_edit1(id):
    return compani61.edit1(id)

@app.route(rout61+"editl/<string:id>", methods=["POST"])
def segmod_editl(id):
    return compani61.editl(id)

#SEGURIDAD MONSERRATE LTDA #SEGURIDAD MONSERRATE LTDA #SEGURIDAD MONSERRATE LTDA #SEGURIDAD MONSERRATE LTDA #SEGURIDAD MONSERRATE LTDA #SEGURIDAD MONSERRATE LTDA

rout62 = empresas['empresa62']['rout']
compani62 = empresas['empresa62']['compani']

@app.route(rout62)
def segmon_info():
    return compani62.info()

@app.route(rout62+"list")
def segmon_listarl():
    return compani62.listl()

@app.route(rout62+"list/<string:id>")
def segmon_listar_id(id):
    return compani62.listlid(id)

@app.route(rout62+"cr")
def segmon_listar_cre1():
    return compani62.createl()

@app.route(rout62+"create2", methods=["POST"])
def segmon_listar_cre2():
    return compani62.create2l()

@app.route(rout62+"edit1/<string:id>")
def segmon_edit1(id):
    return compani62.edit1(id)

@app.route(rout62+"editl/<string:id>", methods=["POST"])
def segmon_editl(id):
    return compani62.editl(id)

#SEGURIDAD NAPOLES LTDA #SEGURIDAD NAPOLES LTDA #SEGURIDAD NAPOLES LTDA #SEGURIDAD NAPOLES LTDA #SEGURIDAD NAPOLES LTDA #SEGURIDAD NAPOLES LTDA

rout63 = empresas['empresa63']['rout']
compani63 = empresas['empresa63']['compani']

@app.route(rout63)
def segnap_info():
    return compani63.info()

@app.route(rout63+"list")
def segnap_listarl():
    return compani63.listl()

@app.route(rout63+"list/<string:id>")
def segnap_listar_id(id):
    return compani63.listlid(id)

@app.route(rout63+"cr")
def segnap_listar_cre1():
    return compani63.createl()

@app.route(rout63+"create2", methods=["POST"])
def segnap_listar_cre2():
    return compani63.create2l()

@app.route(rout63+"edit1/<string:id>")
def segnap_edit1(id):
    return compani63.edit1(id)

@app.route(rout63+"editl/<string:id>", methods=["POST"])
def segnap_editl(id):
    return compani63.editl(id)

#SEGURIDAD ORIENTAL LTDA #SEGURIDAD ORIENTAL LTDA #SEGURIDAD ORIENTAL LTDA #SEGURIDAD ORIENTAL LTDA #SEGURIDAD ORIENTAL LTDA #SEGURIDAD ORIENTAL LTDA

rout64 = empresas['empresa64']['rout']
compani64 = empresas['empresa64']['compani']

@app.route(rout64)
def segori_info():
    return compani64.info()

@app.route(rout64+"list")
def segori_listarl():
    return compani64.listl()

@app.route(rout64+"list/<string:id>")
def segori_listar_id(id):
    return compani64.listlid(id)

@app.route(rout64+"cr")
def segori_listar_cre1():
    return compani64.createl()

@app.route(rout64+"create2", methods=["POST"])
def segori_listar_cre2():
    return compani64.create2l()

@app.route(rout64+"edit1/<string:id>")
def segori_edit1(id):
    return compani64.edit1(id)

@app.route(rout64+"editl/<string:id>", methods=["POST"])
def segori_editl(id):
    return compani64.editl(id)


#SEGURIDAD PRIVADA ASESORIAS Y SERVICIO #SEGURIDAD PRIVADA ASESORIAS Y SERVICIO #SEGURIDAD PRIVADA ASESORIAS Y SERVICIO #SEGURIDAD PRIVADA ASESORIAS Y SERVICIO #SEGURIDAD PRIVADA ASESORIAS Y SERVICIO #SEGURIDAD PRIVADA ASESORIAS Y SERVICIO

rout65 = empresas['empresa65']['rout']
compani65 = empresas['empresa65']['compani']

@app.route(rout65)
def segpri_info():
    return compani65.info()

@app.route(rout65+"list")
def segpri_listarl():
    return compani65.listl()

@app.route(rout65+"list/<string:id>")
def segpri_listar_id(id):
    return compani65.listlid(id)

@app.route(rout65+"cr")
def segpri_listar_cre1():
    return compani65.createl()

@app.route(rout65+"create2", methods=["POST"])
def segpri_listar_cre2():
    return compani65.create2l()

@app.route(rout65+"edit1/<string:id>")
def segpri_edit1(id):
    return compani65.edit1(id)

@app.route(rout65+"editl/<string:id>", methods=["POST"])
def segpri_editl(id):
    return compani65.editl(id)

#SEGURIDAD PRIVADA CASTELL Y CIA LTDA #SEGURIDAD PRIVADA CASTELL Y CIA LTDA #SEGURIDAD PRIVADA CASTELL Y CIA LTDA #SEGURIDAD PRIVADA CASTELL Y CIA LTDA #SEGURIDAD PRIVADA CASTELL Y CIA LTDA #SEGURIDAD PRIVADA CASTELL Y CIA LTDA

rout66 = empresas['empresa66']['rout']
compani66 = empresas['empresa66']['compani']

@app.route(rout66)
def segpricast_info():
    return compani66.info()

@app.route(rout66+"list")
def segpricast_listarl():
    return compani66.listl()

@app.route(rout66+"list/<string:id>")
def segpricast_listar_id(id):
    return compani66.listlid(id)

@app.route(rout66+"cr")
def segpricast_listar_cre1():
    return compani66.createl()

@app.route(rout66+"create2", methods=["POST"])
def segpricast_listar_cre2():
    return compani66.create2l()

@app.route(rout66+"edit1/<string:id>")
def segpricast_edit1(id):
    return compani66.edit1(id)

@app.route(rout66+"editl/<string:id>", methods=["POST"])
def segpricast_editl(id):
    return compani66.editl(id)

#SEGURIDAD PRIVADA TEXAS LTDA #SEGURIDAD PRIVADA TEXAS LTDA #SEGURIDAD PRIVADA TEXAS LTDA #SEGURIDAD PRIVADA TEXAS LTDA #SEGURIDAD PRIVADA TEXAS LTDA #SEGURIDAD PRIVADA TEXAS LTDA

rout67 = empresas['empresa67']['rout']
compani67 = empresas['empresa67']['compani']

@app.route(rout67)
def segtexas_info():
    return compani67.info()

@app.route(rout67+"list")
def segtexas_listarl():
    return compani67.listl()

@app.route(rout67+"list/<string:id>")
def segtexas_listar_id(id):
    return compani67.listlid(id)

@app.route(rout67+"cr")
def segtexas_listar_cre1():
    return compani67.createl()

@app.route(rout67+"create2", methods=["POST"])
def segtexas_listar_cre2():
    return compani67.create2l()

@app.route(rout67+"edit1/<string:id>")
def segtexas_edit1(id):
    return compani67.edit1(id)

@app.route(rout67+"editl/<string:id>", methods=["POST"])
def segtexas_editl(id):
    return compani67.editl(id)

#SEGURIDAD Q A P LIMITADA #SEGURIDAD Q A P LIMITADA #SEGURIDAD Q A P LIMITADA #SEGURIDAD Q A P LIMITADA #SEGURIDAD Q A P LIMITADA #SEGURIDAD Q A P LIMITADA

rout68 = empresas['empresa68']['rout']
compani68 = empresas['empresa68']['compani']

@app.route(rout68)
def segqapl_info():
    return compani68.info()

@app.route(rout68+"list")
def segqapl_listarl():
    return compani68.listl()

@app.route(rout68+"list/<string:id>")
def segqapl_listar_id(id):
    return compani68.listlid(id)

@app.route(rout68+"cr")
def segqapl_listar_cre1():
    return compani68.createl()

@app.route(rout68+"create2", methods=["POST"])
def segqapl_listar_cre2():
    return compani68.create2l()

@app.route(rout68+"edit1/<string:id>")
def segqapl_edit1(id):
    return compani68.edit1(id)

@app.route(rout68+"editl/<string:id>", methods=["POST"])
def segqapl_editl(id):
    return compani68.editl(id)

#SEGURIDAD SIRIUS LTDA #SEGURIDAD SIRIUS LTDA #SEGURIDAD SIRIUS LTDA #SEGURIDAD SIRIUS LTDA #SEGURIDAD SIRIUS LTDA #SEGURIDAD SIRIUS LTDA

rout69 = empresas['empresa69']['rout']
compani69 = empresas['empresa69']['compani']

@app.route(rout69)
def segsirius_info():
    return compani69.info()

@app.route(rout69+"list")
def segsirius_listarl():
    return compani69.listl()

@app.route(rout69+"list/<string:id>")
def segsirius_listar_id(id):
    return compani69.listlid(id)

@app.route(rout69+"cr")
def segsirius_listar_cre1():
    return compani69.createl()

@app.route(rout69+"create2", methods=["POST"])
def segsirius_listar_cre2():
    return compani69.create2l()

@app.route(rout69+"edit1/<string:id>")
def segsirius_edit1(id):
    return compani69.edit1(id)

@app.route(rout69+"editl/<string:id>", methods=["POST"])
def segsirius_editl(id):
    return compani69.editl(id)

#SEGURIDAD SUPER LTDA #SEGURIDAD SUPER LTDA #SEGURIDAD SUPER LTDA #SEGURIDAD SUPER LTDA #SEGURIDAD SUPER LTDA #SEGURIDAD SUPER LTDA

rout70 = empresas['empresa70']['rout']
compani70 = empresas['empresa70']['compani']

@app.route(rout70)
def segsuperl_info():
    return compani70.info()

@app.route(rout70+"list")
def segsuperl_listarl():
    return compani70.listl()

@app.route(rout70+"list/<string:id>")
def segsuperl_listar_id(id):
    return compani70.listlid(id)

@app.route(rout70+"cr")
def segsuperl_listar_cre1():
    return compani70.createl()

@app.route(rout70+"create2", methods=["POST"])
def segsuperl_listar_cre2():
    return compani70.create2l()

@app.route(rout70+"edit1/<string:id>")
def segsuperl_edit1(id):
    return compani70.edit1(id)

@app.route(rout70+"editl/<string:id>", methods=["POST"])
def segsuperl_editl(id):
    return compani70.editl(id)

#SEGURIDAD TRANSBA #SEGURIDAD TRANSBA #SEGURIDAD TRANSBA #SEGURIDAD TRANSBA #SEGURIDAD TRANSBA #SEGURIDAD TRANSBA

rout71 = empresas['empresa71']['rout']
compani71 = empresas['empresa71']['compani']

@app.route(rout71)
def segtrans_info():
    return compani71.info()

@app.route(rout71+"list")
def segtrans_listarl():
    return compani71.listl()

@app.route(rout71+"list/<string:id>")
def segtrans_listar_id(id):
    return compani71.listlid(id)

@app.route(rout71+"cr")
def segtrans_listar_cre1():
    return compani71.createl()

@app.route(rout71+"create2", methods=["POST"])
def segtrans_listar_cre2():
    return compani71.create2l()

@app.route(rout71+"edit1/<string:id>")
def segtrans_edit1(id):
    return compani71.edit1(id)

@app.route(rout71+"editl/<string:id>", methods=["POST"])
def segtrans_editl(id):
    return compani71.editl(id)

#SEGURIDAD Y VIGILANCIA EXITO DE COLOMBIA #SEGURIDAD Y VIGILANCIA EXITO DE COLOMBIA #SEGURIDAD Y VIGILANCIA EXITO DE COLOMBIA #SEGURIDAD Y VIGILANCIA EXITO DE COLOMBIA #SEGURIDAD Y VIGILANCIA EXITO DE COLOMBIA #SEGURIDAD Y VIGILANCIA EXITO DE COLOMBIA

rout72 = empresas['empresa72']['rout']
compani72 = empresas['empresa72']['compani']

@app.route(rout72)
def segexitocol_info():
    return compani72.info()

@app.route(rout72+"list")
def segexitocol_listarl():
    return compani72.listl()

@app.route(rout72+"list/<string:id>")
def segexitocol_listar_id(id):
    return compani72.listlid(id)

@app.route(rout72+"cr")
def segexitocol_listar_cre1():
    return compani72.createl()

@app.route(rout72+"create2", methods=["POST"])
def segexitocol_listar_cre2():
    return compani72.create2l()

@app.route(rout72+"edit1/<string:id>")
def segexitocol_edit1(id):
    return compani72.edit1(id)

@app.route(rout72+"editl/<string:id>", methods=["POST"])
def segexitocol_editl(id):
    return compani72.editl(id)

#SEGURIDAD Y VIGILANCIA SERVICONCEL #SEGURIDAD Y VIGILANCIA SERVICONCEL #SEGURIDAD Y VIGILANCIA SERVICONCEL #SEGURIDAD Y VIGILANCIA SERVICONCEL #SEGURIDAD Y VIGILANCIA SERVICONCEL #SEGURIDAD Y VIGILANCIA SERVICONCEL

rout73 = empresas['empresa73']['rout']
compani73 = empresas['empresa73']['compani']

@app.route(rout73)
def segservicon_info():
    return compani73.info()

@app.route(rout73+"list")
def segservicon_listarl():
    return compani73.listl()

@app.route(rout73+"list/<string:id>")
def segservicon_listar_id(id):
    return compani73.listlid(id)

@app.route(rout73+"cr")
def segservicon_listar_cre1():
    return compani73.createl()

@app.route(rout73+"create2", methods=["POST"])
def segservicon_listar_cre2():
    return compani73.create2l()

@app.route(rout73+"edit1/<string:id>")
def segservicon_edit1(id):
    return compani73.edit1(id)

@app.route(rout73+"editl/<string:id>", methods=["POST"])
def segservicon_editl(id):
    return compani73.editl(id)

#SERVICIO DE VIGILANCIA HORIZONTAL LTDA S #SERVICIO DE VIGILANCIA HORIZONTAL LTDA S #SERVICIO DE VIGILANCIA HORIZONTAL LTDA S #SERVICIO DE VIGILANCIA HORIZONTAL LTDA S #SERVICIO DE VIGILANCIA HORIZONTAL LTDA S #SERVICIO DE VIGILANCIA HORIZONTAL LTDA S

rout74 = empresas['empresa74']['rout']
compani74 = empresas['empresa74']['compani']

@app.route(rout74)
def servihorizon_info():
    return compani74.info()

@app.route(rout74+"list")
def servihorizon_listarl():
    return compani74.listl()

@app.route(rout74+"list/<string:id>")
def servihorizon_listar_id(id):
    return compani74.listlid(id)

@app.route(rout74+"cr")
def servihorizon_listar_cre1():
    return compani74.createl()

@app.route(rout74+"create2", methods=["POST"])
def servihorizon_listar_cre2():
    return compani74.create2l()

@app.route(rout74+"edit1/<string:id>")
def servihorizon_edit1(id):
    return compani74.edit1(id)

@app.route(rout74+"editl/<string:id>", methods=["POST"])
def servihorizon_editl(id):
    return compani74.editl(id)

#SERVICIOS DE SEGURIDAD STAR DE COLOMBIA #SERVICIOS DE SEGURIDAD STAR DE COLOMBIA #SERVICIOS DE SEGURIDAD STAR DE COLOMBIA #SERVICIOS DE SEGURIDAD STAR DE COLOMBIA #SERVICIOS DE SEGURIDAD STAR DE COLOMBIA #SERVICIOS DE SEGURIDAD STAR DE COLOMBIA

rout75 = empresas['empresa75']['rout']
compani75 = empresas['empresa75']['compani']

@app.route(rout75)
def sstarcol_info():
    return compani75.info()

@app.route(rout75+"list")
def sstarcol_listarl():
    return compani75.listl()

@app.route(rout75+"list/<string:id>")
def sstarcol_listar_id(id):
    return compani75.listlid(id)

@app.route(rout75+"cr")
def sstarcol_listar_cre1():
    return compani75.createl()

@app.route(rout75+"create2", methods=["POST"])
def sstarcol_listar_cre2():
    return compani75.create2l()

@app.route(rout75+"edit1/<string:id>")
def sstarcol_edit1(id):
    return compani75.edit1(id)

@app.route(rout75+"editl/<string:id>", methods=["POST"])
def sstarcol_editl(id):
    return compani75.editl(id)

#SERVICIOS SEGURIDAD STAR DE COLOMBIA LTD #SERVICIOS SEGURIDAD STAR DE COLOMBIA LTD #SERVICIOS SEGURIDAD STAR DE COLOMBIA LTD #SERVICIOS SEGURIDAD STAR DE COLOMBIA LTD #SERVICIOS SEGURIDAD STAR DE COLOMBIA LTD #SERVICIOS SEGURIDAD STAR DE COLOMBIA LTD

rout76 = empresas['empresa76']['rout']
compani76 = empresas['empresa76']['compani']

@app.route(rout76)
def servstarq_info():
    return compani76.info()

@app.route(rout76+"list")
def servstarq_listarl():
    return compani76.listl()

@app.route(rout76+"list/<string:id>")
def servstarq_listar_id(id):
    return compani76.listlid(id)

@app.route(rout76+"cr")
def servstarq_listar_cre1():
    return compani76.createl()

@app.route(rout76+"create2", methods=["POST"])
def servstarq_listar_cre2():
    return compani76.create2l()

@app.route(rout76+"edit1/<string:id>")
def servstarq_edit1(id):
    return compani76.edit1(id)

@app.route(rout76+"editl/<string:id>", methods=["POST"])
def servstarq_editl(id):
    return compani76.editl(id)

#SERVISION DE COLOMBIA Y CIA LTDA #SERVISION DE COLOMBIA Y CIA LTDA #SERVISION DE COLOMBIA Y CIA LTDA #SERVISION DE COLOMBIA Y CIA LTDA #SERVISION DE COLOMBIA Y CIA LTDA #SERVISION DE COLOMBIA Y CIA LTDA

rout77 = empresas['empresa77']['rout']
compani77 = empresas['empresa77']['compani']

@app.route(rout77)
def servcol_info():
    return compani77.info()

@app.route(rout77+"list")
def servcol_listarl():
    return compani77.listl()

@app.route(rout77+"list/<string:id>")
def servcol_listar_id(id):
    return compani77.listlid(id)

@app.route(rout77+"cr")
def servcol_listar_cre1():
    return compani77.createl()

@app.route(rout77+"create2", methods=["POST"])
def servcol_listar_cre2():
    return compani77.create2l()

@app.route(rout77+"edit1/<string:id>")
def servcol_edit1(id):
    return compani77.edit1(id)

@app.route(rout77+"editl/<string:id>", methods=["POST"])
def servcol_editl(id):
    return compani77.editl(id)

#SEVIN LTDA #SEVIN LTDA #SEVIN LTDA #SEVIN LTDA #SEVIN LTDA #SEVIN LTDA #SEVIN LTDA #SEVIN LTDA #SEVIN LTDA #SEVIN LTDA #SEVIN LTDA #SEVIN LTDA

rout78 = empresas['empresa78']['rout']
compani78 = empresas['empresa78']['compani']

@app.route(rout78)
def servin_info():
    return compani78.info()

@app.route(rout78+"list")
def servin_listarl():
    return compani78.listl()

@app.route(rout78+"list/<string:id>")
def servin_listar_id(id):
    return compani78.listlid(id)

@app.route(rout78+"cr")
def servin_listar_cre1():
    return compani78.createl()

@app.route(rout78+"create2", methods=["POST"])
def servin_listar_cre2():
    return compani78.create2l()

@app.route(rout78+"edit1/<string:id>")
def servin_edit1(id):
    return compani78.edit1(id)

@app.route(rout78+"editl/<string:id>", methods=["POST"])
def servin_editl(id):
    return compani78.editl(id)

#TOP GUARD LTDA #TOP GUARD LTDA #TOP GUARD LTDA #TOP GUARD LTDA #TOP GUARD LTDA #TOP GUARD LTDA #TOP GUARD LTDA #TOP GUARD LTDA #TOP GUARD LTDA #TOP GUARD LTDA #TOP GUARD LTDA #TOP GUARD LTDA

rout79 = empresas['empresa79']['rout']
compani79 = empresas['empresa79']['compani']

@app.route(rout79)
def topguard_info():
    return compani79.info()

@app.route(rout79+"list")
def topguard_listarl():
    return compani79.listl()

@app.route(rout79+"list/<string:id>")
def topguard_listar_id(id):
    return compani79.listlid(id)

@app.route(rout79+"cr")
def topguard_listar_cre1():
    return compani79.createl()

@app.route(rout79+"create2", methods=["POST"])
def topguard_listar_cre2():
    return compani79.create2l()

@app.route(rout79+"edit1/<string:id>")
def topguard_edit1(id):
    return compani79.edit1(id)

@app.route(rout79+"editl/<string:id>", methods=["POST"])
def topguard_editl(id):
    return compani79.editl(id)

#TORONTO DE COLOMBIA LTDA #TORONTO DE COLOMBIA LTDA #TORONTO DE COLOMBIA LTDA #TORONTO DE COLOMBIA LTDA #TORONTO DE COLOMBIA LTDA #TORONTO DE COLOMBIA LTDA

rout80 = empresas['empresa80']['rout']
compani80 = empresas['empresa80']['compani']

@app.route(rout80)
def toronto_info():
    return compani80.info()

@app.route(rout80+"list")
def toronto_listarl():
    return compani80.listl()

@app.route(rout80+"list/<string:id>")
def toronto_listar_id(id):
    return compani80.listlid(id)

@app.route(rout80+"cr")
def toronto_listar_cre1():
    return compani80.createl()

@app.route(rout80+"create2", methods=["POST"])
def toronto_listar_cre2():
    return compani80.create2l()

@app.route(rout80+"edit1/<string:id>")
def toronto_edit1(id):
    return compani80.edit1(id)

@app.route(rout80+"editl/<string:id>", methods=["POST"])
def toronto_editl(id):
    return compani80.editl(id)

#UNION TEMPORAL MINTRANSPORTE C C 2018 #UNION TEMPORAL MINTRANSPORTE C C 2018 #UNION TEMPORAL MINTRANSPORTE C C 2018 #UNION TEMPORAL MINTRANSPORTE C C 2018 #UNION TEMPORAL MINTRANSPORTE C C 2018 #UNION TEMPORAL MINTRANSPORTE C C 2018

rout81 = empresas['empresa81']['rout']
compani81 = empresas['empresa81']['compani']

@app.route(rout81)
def uniontemmin_info():
    return compani81.info()

@app.route(rout81+"list")
def uniontemmin_listarl():
    return compani81.listl()

@app.route(rout81+"list/<string:id>")
def uniontemmin_listar_id(id):
    return compani81.listlid(id)

@app.route(rout81+"cr")
def uniontemmin_listar_cre1():
    return compani81.createl()

@app.route(rout81+"create2", methods=["POST"])
def uniontemmin_listar_cre2():
    return compani81.create2l()

@app.route(rout81+"edit1/<string:id>")
def uniontemmin_edit1(id):
    return compani81.edit1(id)

@app.route(rout81+"editl/<string:id>", methods=["POST"])
def uniontemmin_editl(id):
    return compani81.editl(id)

#UNIÓN TEMPORAL TAC CENTRAL TRANSMILENIO #UNIÓN TEMPORAL TAC CENTRAL TRANSMILENIO #UNIÓN TEMPORAL TAC CENTRAL TRANSMILENIO #UNIÓN TEMPORAL TAC CENTRAL TRANSMILENIO #UNIÓN TEMPORAL TAC CENTRAL TRANSMILENIO #UNIÓN TEMPORAL TAC CENTRAL TRANSMILENIO

rout82 = empresas['empresa82']['rout']
compani82 = empresas['empresa82']['compani']

@app.route(rout82)
def uniontemtrans_info():
    return compani82.info()

@app.route(rout82+"list")
def uniontemtrans_listarl():
    return compani82.listl()

@app.route(rout82+"list/<string:id>")
def uniontemtrans_listar_id(id):
    return compani82.listlid(id)

@app.route(rout82+"cr")
def uniontemtrans_listar_cre1():
    return compani82.createl()

@app.route(rout82+"create2", methods=["POST"])
def uniontemtrans_listar_cre2():
    return compani82.create2l()

@app.route(rout82+"edit1/<string:id>")
def uniontemtrans_edit1(id):
    return compani82.edit1(id)

@app.route(rout82+"editl/<string:id>", methods=["POST"])
def uniontemtrans_editl(id):
    return compani82.editl(id)

#VIGIAS DE COLOMBIA SRL LTDA #VIGIAS DE COLOMBIA SRL LTDA #VIGIAS DE COLOMBIA SRL LTDA #VIGIAS DE COLOMBIA SRL LTDA #VIGIAS DE COLOMBIA SRL LTDA #VIGIAS DE COLOMBIA SRL LTDA

rout83 = empresas['empresa83']['rout']
compani83 = empresas['empresa83']['compani']

@app.route(rout83)
def vigcol_info():
    return compani83.info()

@app.route(rout83+"list")
def vigcol_listarl():
    return compani83.listl()

@app.route(rout83+"list/<string:id>")
def vigcol_listar_id(id):
    return compani83.listlid(id)

@app.route(rout83+"cr")
def vigcol_listar_cre1():
    return compani83.createl()

@app.route(rout83+"create2", methods=["POST"])
def vigcol_listar_cre2():
    return compani83.create2l()

@app.route(rout83+"edit1/<string:id>")
def vigcol_edit1(id):
    return compani83.edit1(id)

@app.route(rout83+"editl/<string:id>", methods=["POST"])
def vigcol_editl(id):
    return compani83.editl(id)

#VIGILANCIA ACOSTA LIMITADA #VIGILANCIA ACOSTA LIMITADA #VIGILANCIA ACOSTA LIMITADA #VIGILANCIA ACOSTA LIMITADA #VIGILANCIA ACOSTA LIMITADA #VIGILANCIA ACOSTA LIMITADA

rout84 = empresas['empresa84']['rout']
compani84 = empresas['empresa84']['compani']

@app.route(rout84)
def vacosta_info():
    return compani84.info()

@app.route(rout84+"list")
def vacosta_listarl():
    return compani84.listl()

@app.route(rout84+"list/<string:id>")
def vacosta_listar_id(id):
    return compani84.listlid(id)

@app.route(rout84+"cr")
def vacosta_listar_cre1():
    return compani84.createl()

@app.route(rout84+"create2", methods=["POST"])
def vacosta_listar_cre2():
    return compani84.create2l()

@app.route(rout84+"edit1/<string:id>")
def vacosta_edit1(id):
    return compani84.edit1(id)

@app.route(rout84+"editl/<string:id>", methods=["POST"])
def vacosta_editl(id):
    return compani84.editl(id)

#VIGILANCIA Y SEGURIDAD PRIVADA 007 LTDA #VIGILANCIA Y SEGURIDAD PRIVADA 007 LTDA #VIGILANCIA Y SEGURIDAD PRIVADA 007 LTDA #VIGILANCIA Y SEGURIDAD PRIVADA 007 LTDA #VIGILANCIA Y SEGURIDAD PRIVADA 007 LTDA #VIGILANCIA Y SEGURIDAD PRIVADA 007 LTDA

rout85 = empresas['empresa85']['rout']
compani85 = empresas['empresa85']['compani']

@app.route(rout85)
def vigsegl_info():
    return compani85.info()

@app.route(rout85+"list")
def vigsegl_listarl():
    return compani85.listl()

@app.route(rout85+"list/<string:id>")
def vigsegl_listar_id(id):
    return compani85.listlid(id)

@app.route(rout85+"cr")
def vigsegl_listar_cre1():
    return compani85.createl()

@app.route(rout85+"create2", methods=["POST"])
def vigsegl_listar_cre2():
    return compani85.create2l()

@app.route(rout85+"edit1/<string:id>")
def vigsegl_edit1(id):
    return compani85.edit1(id)

@app.route(rout85+"editl/<string:id>", methods=["POST"])
def vigsegl_editl(id):
    return compani85.editl(id)

#VIGONSA LTDA #VIGONSA LTDA #VIGONSA LTDA #VIGONSA LTDA #VIGONSA LTDA #VIGONSA LTDA #VIGONSA LTDA #VIGONSA LTDA #VIGONSA LTDA #VIGONSA LTDA #VIGONSA LTDA #VIGONSA LTDA

rout86 = empresas['empresa86']['rout']
compani86 = empresas['empresa86']['compani']

@app.route(rout86)
def vigonsa_info():
    return compani86.info()

@app.route(rout86+"list")
def vigonsa_listarl():
    return compani86.listl()

@app.route(rout86+"list/<string:id>")
def vigonsa_listar_id(id):
    return compani86.listlid(id)

@app.route(rout86+"cr")
def vigonsa_listar_cre1():
    return compani86.createl()

@app.route(rout86+"create2", methods=["POST"])
def vigonsa_listar_cre2():
    return compani86.create2l()

@app.route(rout86+"edit1/<string:id>")
def vigonsa_edit1(id):
    return compani86.edit1(id)

@app.route(rout86+"editl/<string:id>", methods=["POST"])
def vigonsa_editl(id):
    return compani86.editl(id)

#VISE LTDA #VISE LTDA #VISE LTDA #VISE LTDA #VISE LTDA #VISE LTDA

rout87 = empresas['empresa87']['rout']
compani87 = empresas['empresa87']['compani']

@app.route(rout87)
def vise_info():
    return compani87.info()

@app.route(rout87+"list")
def vise_listarl():
    return compani87.listl()

@app.route(rout87+"list/<string:id>")
def vise_listar_id(id):
    return compani87.listlid(id)

@app.route(rout87+"cr")
def vise_listar_cre1():
    return compani87.createl()

@app.route(rout87+"create2", methods=["POST"])
def vise_listar_cre2():
    return compani87.create2l()

@app.route(rout87+"edit1/<string:id>")
def vise_edit1(id):
    return compani87.edit1(id)

@app.route(rout87+"editl/<string:id>", methods=["POST"])
def vise_editl(id):
    return compani87.editl(id)


#embajada #embajada #embajada

rout88 = empresas['empresa88']['rout']
compani88 = empresas['empresa88']['compani']

@app.route(rout88)
def embri_info():
    return compani88.info()

@app.route(rout88+"list")
def embri_listarl():
    return compani88.listl()

@app.route(rout88+"list/<string:id>")
def embri_listar_id(id):
    return compani88.listlid(id)

@app.route(rout88+"cr")
def embri_listar_cre1():
    return compani88.createl()

@app.route(rout88+"create2", methods=["POST"])
def embri_listar_cre2():
    return compani88.create2l()

@app.route(rout88+"edit1/<string:id>")
def embri_edit1(id):
    return compani88.edit1(id)

@app.route(rout88+"editl/<string:id>", methods=["POST"])
def embri_editl(id):
    return compani88.editl(id)


if __name__== "__main__":
    app.run(debug=True, port=5017)

    