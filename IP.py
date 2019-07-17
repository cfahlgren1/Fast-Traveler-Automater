from dotenv import load_dotenv
import ipinfo, os

class IP:
    load_dotenv()  # setup use for getting environment variables

    # connect to ipinfo api to get location info from ip address
    handler = ipinfo.getHandler(os.getenv("IP_ACCESS_TOKEN"))

    def __init__(self, ip_address):
        self.ip_address = ip_address
        details = self.handler.getDetails(ip_address)
        self.city = details.city
        self.latitude = details.latitude
        self.longitude = details.longitude
        self.hostname = details.hostname
        self.country = details.country_name

    # string method for string representation of object
    def __str__(self):
        return "ip: " + self.ip_address + "\ncity: " + self.city + "\nhostname: " \
               + self.hostname + "\nlatitude: " + self.latitude + "\nlongitude: " \
               + self.longitude + "\ncountry: " + self.country

    # for use when printing from list
    def __repr__(self):
        return str(self)


