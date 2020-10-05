# Documentation for stix db2 connector for CP4S 1.4 for DHS

## Note

as of September 30th 2020
Spoke with Danny Elliot and in order to have a custom connector working with 1.4 you have to base your branch off of `3.1.8` tag.

## Important links

Link to documentation: https://github.com/opencybersecurityalliance/stix-shifter/tree/3.1.8

Link to documentation on integrating connector to CP4S: https://github.com/opencybersecurityalliance/stix-shifter/tree/3.1.8/deployment/ibm_cloud_pak_for_security

Link to IBM DB2 python api documentation: https://github.com/ibmdb/python-ibmdb/wiki/APIs

# Documentation

## Initial installation and set up

- Stix shifter uses python3 so you will need to set up a virtualenv with python3.
- make sure you have python3 installed
- in your terminal run `python3 -m venv venv` (you can create the venv within the repo since it is gitignored).
- Now that you have your virtual env activate it with `source venv/bin/activate`. To deactivate simply run `deactivate`
- create a copy of `stix_shifter_modules/synchronous_dummy` and name it `db2`
- within `stix_shifter_modules/db2` create a `requirements.txt` file and populate it with `ibm-db==3.0.1`, This will add the ibm db2 library to the `requirements-dev.txt` since it performs a tree walk.
- generate the requirements with `python generate_requirements.py`
- install the requirements `pip install -r requirements-dev.txt` (if you notice this file contains the requirements.txt inside of it).
- now we need to run the setup script for stix so run `python setup.py install`
- test to see that it is working locally `python main.py translate db2 query {} "[ipv4-addr:value = '127.0.0.1']" {}` If this returns a result then you're good to go. If not scream and tell someone and figure it out and document it!

## Writing the db2 connector

Note: This document was created after we had developed a POC connector in April. So might not be as detailed.

### translation module

The Translation module is what is used to translate stix object notation to native query language notation and vice versa.

- create the file `from_stix_map.json` in the `stix_shifter_modules/db2/stix_translation/json/` directory. You will see `dialect<1/2>_from_stix_map.json` in the file structure. These are good to use for reference when building connectors. Multiple dialects are for different schemas. Delete them, they will be in the `synchronous_dummy` module folder if you need to see them again.
- the `from_stix_map.json` is what is used to map columns from the database over to stix objects
  Example:

```
{
  "ipv4-addr": {
    "fields": {
      "value": ["SIP", "DIP"]
    }
  }
}
```

this tells the connector that values from the columns `SIP` and `DIP` from the datasource map over to an `ipv4-addr` stix object.

### transmission module

This module is where you define how to connect to your datasource and perform queries.
We will be modifying the `api_client.py` file. This is where we define connection as well as queriying.
