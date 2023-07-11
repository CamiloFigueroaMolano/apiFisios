from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

KEY = 'key2.json'
SPREADSHEET_ID = '1qPCC9ZkAzca-YiTt52rQBWYRrRWARC-cuRPmWBEOekc'

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes = SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

result = sheet.values().get(spreadsheetId = SPREADSHEET_ID, range = 'LIRA!A:AA').execute()

values = result.get('values', [])
print(values)
#
#
#html = "<table>"
#
#for fila in values:
#    html += "<tr>"
#    for elemento in fila:
#        html += f"<td>{elemento}</td>"
#    html += "</tr>"
#html += "</table>"
#
#with open("datos_matriz.html", "w") as file:
#    file.write(html)
#

