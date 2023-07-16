from flask import *
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime

app = Flask(__name__)


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'key2.json'
SPREADSHEET_ID = '1qPCC9ZkAzca-YiTt52rQBWYRrRWARC-cuRPmWBEOekc'

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes = SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

####UNIÓN TEMPORAL TAC CENTRAL TRANSMILENIO####

class untacctrans:

    def __init__(self, page,template):
        self.page = page
        self.template = template
        
    def listl(self):
    #llamda a la api
        result = sheet.values().get(spreadsheetId = SPREADSHEET_ID, range = self.page+'!A2:XFD').execute()
        values = result.get('values',[])
        return render_template(self.template +"/list.html",val=values)

    def listlid(self,id):
        criterio = str(id) 

        # Obtener los datos actuales de la hoja
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=self.page+'!A:XFD').execute()
        values = result.get('values', [])
        
        resultados = []
        # Buscar la fila que coincida con el criterio de búsqueda (ID)
        for row in values[1:]:
            if str(row[0]) == criterio:  # Comparar el ID en la primera columna con el criterio
                resultados.append(row)
                break  # Romper el bucle una vez que se encuentre la coincidencia
        return render_template(self.template+"/seemore.html", val=resultados)

    def createl(self): 
        return render_template(self.template+"/create.html")

    def create2l(self):  
        fecha = datetime.now()
        var0 = str(fecha)
        var15 = request.form['Persona_quien_registra']
        var1 = request.form['tipo_documento']
        var2 = request.form['numero_documento']
        var3 = request.form['nombre']
        var12 = request.form['Apellido']
        var13 = request.form.getlist('Tipo_examen[]')
        var16 = request.form['Cargo']
        var4 = request.form['direccion']
        var5 = request.form['correo']
        var6 = request.form['celular']
        var7 = request.form['telefono']
        var14 = request.form['Genero']
        var8 = request.form['RH']
        var9 = request.form['fecha_nacimiento']
        var10 = request.form['pais_nacimiento']
        var11 = request.form['ciudad_nacimiento']

        # Verificar campos vacíos
        if any(value.strip() == '' for value in
                [var15, var1, var2, var3, var12, var16, var4, var5, var6, var7, var14, var8, var9, var10, var11]):
            error_message = "Por favor, complete todos los campos."
            return render_template(self.template+"/create.html", error_message=error_message,
                                    var0=var0, var15=var15, var1=var1, var2=var2, var3=var3, var12=var12,
                                    var13=var13, var16=var16, var4=var4, var5=var5, var6=var6, var7=var7,
                                    var14=var14, var8=var8, var9=var9, var10=var10, var11=var11)

        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=self.page+'!A:XFD').execute()
        values = result.get('values', [])

        # Encontrar el último ID
        if len(values) > 1:
            last_id = max(int(row[0]) for row in values[1:])
        else:# Manejar el caso en el que la secuencia está vacía
            last_id = 0  
        new_id = last_id + 1

        # Convertir la lista de valores en una cadena separada por comas
        var13 = ",".join(var13)
        #solicitu se cra como activa
        var17 = 'ACTIVO'
        #Debe ser una matriz por eso el doble [[]]
        values = [[new_id,var0,var15,var1,var2,var3,var12,var13,var16,var4,var5,var6,var7,var14,var8,var9,var10,var11,var17]]

        #Llamamos a la api
        result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
                                    range=self.page+'!A1:XFD', 
                                    valueInputOption='USER_ENTERED',
                                    body = {'values':values}).execute()

        #print(f"Datos instertados correctamente.\n{(result.get('create').get('createcells'))}")
        return render_template(self.template+"/create.html",datos=values)

    def inactive(self,id):
        """Función para cambiar estado del usuario"""
        criterio = str(id) 

        # Obtener los datos actuales de la hoja
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=self.page+'!A:XDF').execute()
        values = result.get('values', [])

        # Buscar la fila que coincida con el criterio de búsqueda (ID)
        for row in values[1:]:
            if str(row[0]) == criterio:  
                row[18] = 'INACTIVO' 
                break  
        update_values = {'values': values}
        update_result = sheet.values().update(spreadsheetId=SPREADSHEET_ID, range=self.page+'!A:XDF',
                                                valueInputOption='USER_ENTERED', body=update_values).execute()
        return redirect(url_for('uniontemtrans_listarl'))