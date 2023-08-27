class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class DataBaseConnection(metaclass=SingletonMeta):
    username = "Youness"
    Password = "000111"

    def __init__(self, Username, Password):
        self.Username = Username
        self.Password = Password

    @classmethod
    def Access(cls, Username, Password):
        Acess: bool = True
        try:
            if Username == cls.username and Password == cls.Password:
                return Acess
        except ValueError:
            raise ValueError("Invalid Username or Password")

    def Connected(self):
        if self.Access(self.Username, self.Password) == True:
            return "Connected to DataBase"
        return "Failed to connect to DataBase"

if __name__ == "__main__":
    username = "Youness"
    password_1 = "0000111"
    password_2= "0000111"  # Corrected password
    connection_1 = DataBaseConnection(username, password_1).Connected()
    connection_2 = DataBaseConnection(username, password_2).Connected()

    assert connection_1 == connection_2
     # Reusing the same credentials
    if connection_1 == connection_2:
        print("Database connection Created")
    else:
        print("Failed")
