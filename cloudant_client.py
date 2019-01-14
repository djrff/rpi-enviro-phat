from cloudant.client import CouchDB
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
client = CouchDB(config['Couch DB']['username'], config['Couch DB']['password'], url='http://127.0.0.1:5984', connect=True, auto_renew=True)

session = client.session()

print('Username: {0}'.format(session['userCtx']['name']))
print('Databases: {0}'.format(client.all_dbs()))

def __exit__(self, exc_type, exc_value, traceback):
  client.disconnect()