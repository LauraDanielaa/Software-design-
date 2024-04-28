class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.rol = "User"

class Admin(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password) #Toma los atributos que tiene un usuario
        self.rol = "Admin"

class Authentication:
    def __init__(self):
        self.users = []

    def register_user(self, user):
        self.users.append(user)

    def authenticate_user(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                return user
        return None