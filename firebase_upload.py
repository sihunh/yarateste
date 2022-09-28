import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def firebase_upload(json_data, collection_name, file_name):
    if not firebase_admin._apps:
        cred = credentials.Certificate('fire_base_key.json')
        firebase_admin.initialize_app(cred)

    db = firestore.client()
    db.collection(collection_name).document(file_name).set(json_data)