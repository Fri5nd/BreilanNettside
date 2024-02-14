import platform, sys

def database_URI():
    operatingSystem = platform.system()
    match operatingSystem:
        case 'Windows':
            print(f"running on {operatingSystem}", file=sys.stderr)
            return 'sqlite:///database.sqlite'
        case _ :
            print(f"running on {operatingSystem}", file=sys.stderr)
            return 'sqlite://instance/database.sqlite'
   

class CONFIG:
    SECRET_KEY = 'abc'
    SQLALCHEMY_DATABASE_URI = database_URI()
    SQLALCHEMY_TRACK_MODIFICATIONS = False