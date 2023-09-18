import json
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
import os

load_dotenv()

firebaseConfig = json.loads(os.getenv("firebase_key", "{}"))


class FirebaseModel:
    def __init__(self):
        self.cred = credentials.Certificate(firebaseConfig)
        firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()

    async def __get_request(self, table):
        doc_ref = self.db.collection(table)
        if table == 'experiences':
            query = doc_ref.order_by('date_start', direction=firestore.Query.ASCENDING)
            docs = query.stream()
        else:
            docs = doc_ref.stream()

        doc_array = []
        for x in docs:
            doc_array.append(x.to_dict())

        return doc_array

    async def get(self, table):
        data = await self.__get_request(table)
        return data
