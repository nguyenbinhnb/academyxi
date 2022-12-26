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
        elif link == "DA Transform Part Time Page":
            url = config.get('common info', 'daTransformPartTimeURL')
        elif link == "UUD Transform Full Time Page":
            url = config.get('common info', 'uudTransformFullTimeURL')
        elif link == "UUD Transform Part Time Page":
            url = config.get('common info', 'uudTransformPartTimeURL')
        elif link == "UUD Elevate Self Paced Page":
            url = config.get('common info', 'uudElevateSelfPacedURL')
        elif link == "DA Analytics Self Paced Elevate Page":
            url = config.get('common info', 'daDataAnalyticsSelfPacedElevateURL')
        elif link == "FEWD Transform Part Time Page":
            url = config.get('common info', 'fewdTransformPartTimeURL')
        elif link == "SE Transform Full Time Page":
            url = config.get('common info', 'seTransformFullTimeURL')
        elif link == "SE Transform Part Time Page":
            url = config.get('common info', 'seTransformPartTimeURL')
        elif link == "GD Transform Part Time Page":
            url = config.get('common info', 'gdTransformPartTimeURL')
        elif link == "GD Elevate Self Paced Page":
            url = config.get('common info', 'gdElevateSelfPacedURL')
        elif link == "CS Transform Part Time Page":
            url = config.get('common info', 'csTransformPartTimeURL')
        elif link == "PM Transform Part Time Page":
            url = config.get('common info', 'pmTransformPartTimeURL')
        elif link == "PM Elevate Self Paced Page":
            url = config.get('common info', 'pmElevateSelfPacedURL')
        elif link == "SD Elevate Self Paced Page":
            url = config.get('common info', 'sdElevateSelfPacedURL')
        elif link == "DT Elevate Self Paced Page":
            url = config.get('common info', 'dtElevateSelfPacedURL')
        elif link == "CE Elevate Self Paced Page":
            url = config.get('common info', 'ceElevateSelfPacedURL')
        elif link == "SMM Elevate Self Paced Page":
            url = config.get('common info', 'smmElevateSelfPacedURL')
        elif link == "DM Transform Part Time Page":
            url = config.get('common info', 'dmTransformPartTimeURL')
        elif link == "DM Elevate Self Paced Page":
            url = config.get('common info', 'dmElevateSelfPacedURL')
        elif link == "DPM Elevate Self Paced Page":
            url = config.get('common info', 'dpmElevateSelfPacedURL')
        return url


