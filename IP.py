from dotenv import load_dotenv
import ipinfo, os

class IP():
    load_dotenv()  # setup use for getting environment variables

    # connect to ipinfo api to get location info from ip address
    handler = ipinfo.getHandler(os.getenv("IP_ACCESS_TOKEN"))

    def __init__(self, ip_address):
        self.ip_address = ip_address
        details = self.handler.getDetails(ip_address)
        city = details.city
        latitude = details.latitude
        longitude = details.longitude
        hostname = details.hostname
        country = details.country_name

