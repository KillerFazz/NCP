import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\confing.ini")

class Readconfig:
    @staticmethod
    def getApplicationURl():
        url = config.get("common info", "BaseURL")
        return url

    @staticmethod
    def getUserName():
        uname = config.get("common info", "username")
        return uname

    @staticmethod
    def getPassword():
        password = config.get("common info", "password")
        return password
