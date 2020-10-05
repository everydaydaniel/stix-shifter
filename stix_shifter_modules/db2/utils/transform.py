# Transform from datetime.datetime(1,2,3) => miliseconds
def time_transform(result):
    result['STIME'] = result['STIME'].strftime("%s")
    result['ETIME'] = result['ETIME'].strftime("%s")
