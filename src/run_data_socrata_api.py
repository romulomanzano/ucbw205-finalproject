# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 14:34:41 2017

@author: romulo
"""

from sodapy import Socrata
from socrata_311 import settings, etl,api
import datetime



#Setting up the initial connector
client = Socrata(settings.APP_NYC_API_DOMAIN ,settings.APP_TOKEN_311,timeout=90)

#Getting a sense of the metadata available for this dataset
meta = client.get_metadata(settings.APP_NYC_DATASET)

#some experiments about downloading data based on key
data_key = client.get(settings.APP_NYC_DATASET,limit = 100,where = "unique_key == '36805062'")
#some experiments about downloading data based on date
dataDate = client.get(settings.APP_NYC_DATASET,limit = 1000,where = "created_date >= '2017-07-28'")
#some experiments about downloading data based on timestamp
dataTimestamp = client.get(settings.APP_NYC_DATASET,limit = 10000,where = "created_date >= '2017-07-27T00:01:02.000'")

#if wanted to convert to dataframe
fr = etl.flatten_response_list(dataTimestamp,restrict_columns=True)


#experiment to get data since a given timestamp as string
#constructing the string
#can pass days,hours,minutes,hours,seconds
st = datetime.datetime.now() - datetime.timedelta(days=2)
since = st.isoformat()
#calling the function
#receives a date object or timestamp in isoformat
#beware of the restrictive optional parameters
dataSince = api.pull_data_modified_since(since)


list(map(lambda x: etl.calculate_days_to_closure_dict(x),dataSince))
frameDelta = etl.flatten_response_list(dataSince,restrict_columns=True)

