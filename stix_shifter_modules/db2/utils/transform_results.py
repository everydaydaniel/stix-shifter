import json
from datetime import datetime, timezone
from os import path


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
        basepath = path.dirname(__file__)
        protocol_map = "network_protocol_map.json"
        filepath = path.abspath(path.join(basepath, ".." , "stix_translation" ,"json", protocol_map))
        # initialize json load
        try:
            with open(filepath) as json_file:
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
        start = datetime.timestamp(result['STIME'])
        end = datetime.timestamp(result['ETIME'])
        start = datetime.fromtimestamp(int(start), timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
        end = datetime.fromtimestamp(int(end), timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
        result['STIME'] = start
        result['ETIME'] = end
