from config import get_mongo_collection

class ModelUser:
    def __init__(self):
        self.collection = get_mongo_collection()

    def find_user_by_email(self, email):
        query = {"email": email}
        result = self.collection.find(query)
        return list(result)
        
    def find_user_by_email_and_password(self, user,password):
        query = {"email": user,"password": password}
        result = self.collection.find(query)
        return list(result)
        