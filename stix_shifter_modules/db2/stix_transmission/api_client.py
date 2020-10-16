import json
import ibm_db

from stix_shifter_utils.stix_transmission.utils.RestApiClient import RestApiClient
from stix_shifter_modules.db2.utils.transform_results import Transformer

class APIClient():


    def __init__(self, connection, configuration):
        self.auth = configuration.get('auth')
        try:
            self.client = ibm_db.pconnect(
                "DATABASE=" + self.auth.get("database") +
                ";HOSTNAME=" + connection.get("host") +
                ";PORT=" + str(connection.get("port")) +
                ";UID=" + self.auth.get("username") +
                ";PWD=" + self.auth.get("password"),
                "", "")
        except Exception as e:
            print("Error connecting to DB2 CLIENT:", e)
            raise e

        self.state = ibm_db.active(self.client)


    def ping_data_source(self):
        # Pings the data source
        if self.state:
            return {"code": 200, "success": True}
        return {"code": 400, "success": False}


    def get_search_results(self, search_id, range_start=None, range_end=None):
        # Return the search results. Results must be in JSON format before being
        # translated into STIX
        # search_id == translated native query language
        transform = Transformer()
        sql = search_id
        stmt = ibm_db.exec_immediate(self.client, sql)
        results_list = []
        result = ibm_db.fetch_assoc(stmt)
        num_rows = 0
        while result is not False and num_rows < 10000:
                num_rows += 1
                # Format datetime objects into strings
                transform.time_transform(result)
                transform.protocol_transform(result)
                results_list.append(result)
                result = ibm_db.fetch_assoc(stmt)

        return_obj = dict()
        return_obj["code"] = 200
        return_obj["data"] = results_list
        return {"code": 200, "data": results_list}

    def delete_search(self, search_id):
        # Optional since this may not be supported by the data source API
        # Delete the search
        return {"code": 200, "success": True}
