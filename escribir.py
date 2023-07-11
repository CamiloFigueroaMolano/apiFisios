from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'key.json'
SPREADSHEET_ID= '1dvpWYUKYYmdkTBPEvfczZZzSAVgrOtL10A130zrjMUM'

creds = None
creds = service_account.Credentials.from_service_account_file(KEY,scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds )

#manipulaciond e la hoja segun los datos
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range='A:I').execute()
values = result.get('values', [])

# Encontrar el último ID
last_id = 0
if values:
    last_id = max(int(row[0]) for row in values[1:])  # Ignorar la primera fila de encabezados
# Generar el nuevo ID autoincrementable
new_id = last_id + 1


var1 = input('Nombre: ')
var2 = input('Apellido: ')
var3 = input('Direccion: ')



#Debe ser una matriz por eso el doble [[]]
values = [[new_id,var1,var2,var3]]
#Llamamos a la api
result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
                            range='A1:I1', 
                            valueInputOption='USER_ENTERED',
                            body = {'values':values}).execute()

print(f"Datos instertados correctamente.\n{(result.get('updates').get('updateCells'))}")
