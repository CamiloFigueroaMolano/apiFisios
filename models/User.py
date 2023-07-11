from werkzeug.security import check_password_hash

class User():
    def __init__(self, email, password, fullname):
        self.email = email
        self.password = password
        self.fullname = fullname
        
        
    def check_password_hash(self,hashed_password,password):
        return check_password_hash(hashed_password,password)
    
    
    