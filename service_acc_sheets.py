from googleapiclient.discovery import build
from google.oauth2 import service_account


class gsheets():

    def __init__(self,Id):
        service_account_file = 'credentials.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        credentials = None
        credentials = service_account.Credentials.from_service_account_file(service_account_file, scopes = SCOPES)
        service = build('sheets', 'v4', credentials=credentials)
        # Call the Sheets API
        self.sheet = service.spreadsheets()
        self.SAMPLE_SPREADSHEET_ID = Id
        
    def sheet_read(self,read_range):
        self.SAMPLE_RANGE_NAME = read_range
        result = self.sheet.values().get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
                    range=self.SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])
        return(values)
    
    def sheet_write(self,values,write_range):
        self.wr = write_range
        self.vals = values
        request = self.sheet.values().update(spreadsheetId=self.SAMPLE_SPREADSHEET_ID, 
            range= self.wr, valueInputOption='USER_ENTERED', body={'values':self.vals}).execute()
        return()

