import configparser

config=configparser.RawConfigParser()
config.read("./Configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL(link):
        if link == "baseURL":
           url=config.get('common info','baseURL')
        elif link =="Online Courses Page":
            url = config.get('common info', 'onlineCoursesURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('common info','useremail')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password

