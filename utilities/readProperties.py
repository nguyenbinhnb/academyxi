import configparser

config=configparser.RawConfigParser()
config.read("./Configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL(link):
        if link == "baseURL":
           url=config.get('common info','baseURL')
        elif link == "Online Courses Page":
           url = config.get('common info', 'onlineCoursesURL')
        elif link == "All Courses Listing Page":
            url = config.get('common info', 'allCoursesListingURL')
        elif link == "Customer Experience Discipline Page":
            url = config.get('common info', 'customerExperienceDisciplineURL')
        elif link == "Buy Now Page":
            url = config.get('common info', 'buyNowURL')
        elif link == "LP Software Engineer Online Page":
            url = config.get('common info', 'lpSoftwareEngineerOnlineURL')
        elif link == "LP UX UI Online Page":
            url = config.get('common info', 'lpUXUIOnlineURL')
        elif link == "CX Self Paced Elevate Page":
            url = config.get('common info', 'cxSelfPacedElevateURL')
        elif link == "UXD Thank You Page":
            url = config.get('common info', 'uxdThankYouURL')
        elif link == "Checkout Page":
            url = config.get('common info', 'checkoutURL')
        elif link == "Blogs Page":
            url = config.get('common info', 'blogsURL')
        return url


