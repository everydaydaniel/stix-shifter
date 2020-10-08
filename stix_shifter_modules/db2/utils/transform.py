import json

# key value switch
def key_switch(dic):
    to_return = {}
    for key in dic:
        value = dic[key]
        to_return[value] = key
    return to_return

# Utilities for data transformations go in this class
class Transformer():
    def __init__(self):
        # initialize json load
        try:
            with open("stix_shifter_modules/db2/stix_translation/json/network_protocol_map.json") as json_file:
                self.protocols = json.load(json_file)
                self.reverse_protocols = key_switch(self.protocols)
        except Exception as e:
            raise e

    def protocol_transform(self, result):
        # protocol is in result as PROTOCOL with IANA
        value = str(result["PROTOCOL"])
        if value in self.reverse_protocols:
            result["PROTOCOL"] = self.reverse_protocols[value]



    # Transform from datetime.datetime(1,2,3) => miliseconds
    def time_transform(self, result):
        result['STIME'] = result['STIME'].strftime("%s")
        result['ETIME'] = result['ETIME'].strftime("%s")
