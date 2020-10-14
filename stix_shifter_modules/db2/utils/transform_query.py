import json
import ipaddress

# Utilities for data transformations go in this class
class Transformer():
    def __init__(self):
        pass

    def transformIpv4(self, value):
        # Users can use both IP dot format and integer format
        # Check if ip is in integer format, if it iss keep it since that
        # is how they are currently stored in the DB
        try:
            transformed_value = int(value)
            return value
            
        except Exception as e:
            # this library will take in the dot format IP and when int() is
            # called it will return the integer rep
            return_adress = str(int(ipaddress.IPv4Address(value)))
            return return_adress
