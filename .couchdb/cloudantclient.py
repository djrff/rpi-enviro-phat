from cloudant.client import CouchDB
import credentials
client = CouchDB(credentials.USERNAME, credentials.PASSWORD, url="http://127.0.0.1:5050", connect=True, auto_renew=True, admin_party=True)

session = client.session()

print('Databases: {0}'.format(client.all_dbs()))

def __exit__(self, exc_type, exc_value, traceback):
  client.disconnect()