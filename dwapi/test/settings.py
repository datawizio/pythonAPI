#coding:utf-8
"""
Settings for testing scripts\

"""
from dwapi import datawiz
import pandas as pd
import random

shops = [595, 601, 641]

products = [2878566,2866043,2878839, 2845754,2850917,2845745,2878624,2844069,2871351,2867438,2849660,2870150,2882463,
			2918164,2913382,2873280,2881468,2873680,2911063,2899776,2882766,2895664,2858931,2903645,2851149,2841367,
			2888743,2897929,2845992,2872696,2860948,2907155,2904705,2846582,2906189,2856060,2923132,2846763,2917255,
			2847805,2879915,2890229,2894724,2918461,2904405,2901026,2915329,2908002,2897594,2840779]

categories = [69051, 68821, 70512, 70553, 68300, 73153, 72651, 73373, 70883, 73093]


class SettingsManager:

    def __init__(self):

        self.USER = datawiz.DW()
        self.SETTINGS = {'shops': shops,
                         'products': products,
                         'categories': categories
                         }
        client_info = self.USER.get_client_info()
        self.SETTINGS['date_from'] = client_info['date_from']
        self.SETTINGS['date_to'] = client_info['date_to']

    def restore_default(self):

        settings = self.USER.get_client_info()
        return settings

    def split_date_range(self, date_range, parts=3, chunk_size=None):

        date_range_list=[x.date() for x in pd.date_range(start=date_range[0], end=date_range[1])]
        if chunk_size is None:
            chunk_size = int(len(date_range_list)/float(parts))
        result_list = []
        for i in range(0, len(date_range_list), chunk_size):
            if len(date_range_list)<(i+2*(chunk_size)):
                date_list = date_range_list[i:]
                result_list.append([date_list[0], date_list[-1]])
                break
            else:
                date_list = date_range_list[i:i+chunk_size]
            if len(date_list)>1:
                result_list.append([date_list[0], date_list[-1]])
            else:
                break
        return result_list


    def get_sample(self, key):
        return random.choice(self.SETTINGS.get(key))

    def get_samples(self, key):

        data = self.SETTINGS.get(key)
        return data[:random.randint(2,len(data))]

    def get_sample_interval(self):

        max_interval = self.SETTINGS.get('max_interval', 30)
        min_interval = self.SETTINGS.get('min_interval', 10)
        intervals = self.split_date_range((self.SETTINGS['date_from'], self.SETTINGS['date_to']), chunk_size=(max_interval-min_interval))
        return random.choice(intervals)