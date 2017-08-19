# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 17:38:29 2017

@author: romulo
"""
import pandas as pd
from . import etl_settings
import dateutil

def flatten_response_list(data, restrict_columns = False,cols = etl_settings.RESPONSE_COL_REQUIRED):
    frame = pd.DataFrame(data)
    if (restrict_columns):
        cols = list(set.intersection(set(frame.columns),set(cols)))
        return frame[cols]
    return frame


def calculate_days_to_closure_dict(record):
    if ('closed_date' in record.keys()):
        record['time_to_closure'] = dateutil.parser.parse(record['closed_date']) - dateutil.parser.parse(record['created_date'])
    
