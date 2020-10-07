import datetime

# Transform from datetime.datetime(1,2,3) => miliseconds
def time_transform(result):
    for key in result:
        if isinstance(result[key], datetime.datetime):
            result['STIME'] = result['STIME'].strftime("%s")
            result['ETIME'] = result['ETIME'].strftime("%s")
