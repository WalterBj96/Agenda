from flask import *
from pymongo import MongoClient

app = Flask(__name__)

#MongoDB connexion
client = MongoClient('localhost', 27017)
db = client['carnet_adresses']
contacts_collection = db['contacts']

#Route Flask
@app.route('/')
def index():
    contacts = contacts_collection.find()
    return render_template('index.html', contacts = contacts)

@app.route('/ajouter', methods=['POST'])
def ajouter():
    nom = request.form['nom']
    prenom = request.form['prenom']
    email = request.form['email']
    
    nouveau_contact = {'nom':nom, 'prenom':prenom, 'email':email}
    contacts_collection.insert_one(nouveau_contact)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
    