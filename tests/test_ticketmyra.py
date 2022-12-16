from ticketmyra import ticketmyra

import requests
import pandas as pd
import os
#from dotenv import load_dotenv
import json
from json import dumps, loads
from pandas import json_normalize
import pytest
import re
from pandas.testing import assert_frame_equal
from pandas.testing import assert_series_equal
from datetime import datetime, timedelta



def test_attraction_id():
    example = "taylor_swift"
    expected = "K8vZ9175Tr0"
    actual = ticketmyra.attraction_id(name = example)
    assert expected == actual

    
def test_get_data():
    path = 'ts_full_list.csv'
    expected_df = ticketmyra.get_data("taylor_swift")
    actual_df = pd.read_csv(path)
#     print(len(expected_df))
#     print(len(actual_df))
#     print(expected_df)
#     print(actual_df)
    expected_df.reset_index(drop=True).compare(actual_df.reset_index(drop=True))
    assert (expected_df.sort_index().sort_index(axis=1).columns == actual_df.sort_index().sort_index(axis=1).columns).all()
       


def test_date_search():
    df = ticketmyra.get_data(name='taylor_swift')
    expected_df = ticketmyra.date_search(df, startdate = '2023-04-01', enddate = '2023-04-30')
    expected_df.to_csv('ts_april_list.csv', index=False, header=True)
    path ='ts_april_list.csv'  
    actual_df = pd.read_csv(path)
#     print(len(expected_df))
#     print(len(actual_df))
#     print(expected_df)
#     print(actual_df)
    expected_df.reset_index(drop=True).compare(actual_df.reset_index(drop=True))
    assert (expected_df.sort_index().sort_index(axis=1).columns == actual_df.sort_index().sort_index(axis=1).columns).all()



def test_price_min():
    df = ticketmyra.get_data(name='taylor_swift')
    df2 = ticketmyra.date_search(df, startdate = '2023-04-01', enddate = '2023-04-30')
    expected_df = ticketmyra.price_min(df2)
    expected_df.to_csv('ts_final_list.csv', index=False, header=True)
    path ='ts_final_list.csv'  
    actual_df = pd.read_csv(path)
#     print(len(expected_df))
#     print(len(actual_df))
#     print(expected_df)
#     print(actual_df)
    expected_df.reset_index(drop=True).compare(actual_df.reset_index(drop=True))
    assert (expected_df.sort_index().sort_index(axis=1).columns == actual_df.sort_index().sort_index(axis=1).columns).all()
