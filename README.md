### DesginPatterns 

***This Repo include some Design Patterns in Software Engineering***

first we implment SinglTon an Example DataBase Connection

1. Create MetaClass to Save instance of Obejct to make sure is Called once over all prorammer to reduce the complexity memory 

```python 
#MeraClass Obejct 

class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
```
2. Creat the Class Connection Database 

```python 

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


```


