# google_api
A repository for python classes to read and write the google sheets with the help of Google API 

For the class gsheets to be initiated, credentials.json file that contains the keys of your service account must be in the path, where google_sheets.py file is placed.

To obatain credentials.json file create a google developer account. For references on how to create a developer account please visit https://developers.google.com

After creating a developer account can proceed with creating a service account and its keys in the credentials section. For references on how to create service account please visit  https://developers.google.com/identity/protocols/oauth2/service-account#:~:text=A%20service%20account%27s%20credentials%20include,of%20the%20service%20account%27s%20credentials.

If you have successfully created a service account and its keys, then you can download the keys and store it in the the path of google_sheets.

Now you can simply initiate the class and use the methods to read and write the google sheets.

- Note : Name the .json file containing keys as credentials.json. if you wish to rename it please make the subsequent changes in service_account_file = 'credentials.json' line 
