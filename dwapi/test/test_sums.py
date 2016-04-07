import pandas as pd
import unittest
import datetime
from dwapi import datawiz
import random
import pandas as pd
from dwapi.test.settings import SettingsManager

class TestMain(unittest.TestCase):
    
    TEST_SETTINGS = SettingsManager()
    dw = TEST_SETTINGS.USER

    def setUp(self):
        pass
 
    def tearDown(self):
        pass

    def assertEqual(self, x, y, rnd=2):
        # assert round(x,2)==round(y,2)
        return super(TestMain, self).assertEqual(round(x, rnd), round(y,rnd))

    def test_get_products_sale(self):

        interval  = self.TEST_SETTINGS.get_sample_interval()
        products = self.TEST_SETTINGS.get_samples('products')
        shops = self.TEST_SETTINGS.get_samples('shops')
        df = self.dw.get_products_sale(products = products,
                                by='turnover',
                                shops = shops,
                                date_from = interval[0],
                                date_to = interval[1],
                                interval = datawiz.DAYS)
        
        list_colums = df.columns
        if df.empty:
            return True
        result = 0
        for d_f,d_t in self.TEST_SETTINGS.split_date_range(interval):
            df_periods = self.dw.get_products_sale(products = products,by='turnover',
                                    shops = shops,
                                    date_from = d_f,
                                    date_to = d_t,
                                    interval = datawiz.DAYS)
            result += df_periods.sum().sum()
        self.assertEqual(df.sum().sum() , result)

        
    def test_get_categories_sale(self):
        categories = self.TEST_SETTINGS.get_samples('categories')
        interval = self.TEST_SETTINGS.get_sample_interval()
        df = self.dw.get_categories_sale(categories = categories,by='turnover', 
                                date_from = interval[0],
                                date_to = interval[1],
                                interval = datawiz.DAYS 
                                )
        list_colums = df.columns
        if df.empty:
            return True
        result = 0
        for d_f,d_t in self.TEST_SETTINGS.split_date_range(interval):
            df_periods = self.dw.get_categories_sale(categories = categories,by='turnover', 
                                date_from = d_f,
                                date_to = d_t,
                                interval = datawiz.DAYS )
            
            result += df_periods[list_colums].sum().sum()
        self.assertEqual(df.sum().sum() , result)
    
    def test_get_products_stock(self):

        products = self.TEST_SETTINGS.get_samples('products')
        shops = self.TEST_SETTINGS.get_samples('shops')
        interval = self.TEST_SETTINGS.get_sample_interval()

        df = self.dw.get_products_stock(products = products, by='stock_value',
                                                shops = shops,
                                                date_from = interval[0],
                                                date_to = interval[1],
                                                )
        
        list_colums = df.columns
        if df.empty:
            return True
        result = 0
        for d_f,d_t in self.TEST_SETTINGS.split_date_range(interval):
            df_periods = self.dw.get_products_stock(products = products, by='stock_value',
                                                shops = shops,
                                                date_from = d_f,
                                                date_to = d_t,
                                                )
            
            result += df_periods.sum().sum()
        self.assertEqual(df.sum().sum() , result)
        
    def test_get_categories_stock(self):


        categories = self.TEST_SETTINGS.get_samples('categories')
        shops = self.TEST_SETTINGS.get_samples('shops')
        interval = self.TEST_SETTINGS.get_sample_interval()

        df = self.dw.get_categories_stock(categories = categories, by='stock_value',
                                                shops = shops,
                                                date_from = interval[0],
                                                date_to = interval[1],
                                                )
        list_colums = df.columns
        if df.empty:
            return True
        result = 0
        for d_f,d_t in self.TEST_SETTINGS.split_date_range(interval):
            df_periods = self.dw.get_categories_stock(categories = categories, by='stock_value',
                                                shops =shops ,
                                                date_from = d_f,
                                                date_to = d_t,
                                                )
            result += df_periods.sum().sum()
        self.assertEqual(df.sum().sum() , result)
        
    def test_get_lost_sales(self):


        category = self.TEST_SETTINGS.get_sample('categories')
        shops = self.TEST_SETTINGS.get_samples('shops')
        interval = self.TEST_SETTINGS.get_sample_interval()

        df = self.dw.get_lost_sales(category = category,
                                    shops = shops,
                                    date_from = interval[0],
                                    date_to = interval[1],
                                    )
        if df.empty:
            return True

        df = df[[u'Average Sales Quantity per Day' , u'Losing Days' , u'Losing Turnover' , u'Lost Sales Quantity']]
        list_colums = df.columns
        result = 0
        for d_f,d_t in self.TEST_SETTINGS.split_date_range(interval):
            df_periods = self.dw.get_lost_sales(category = categories,
                                                shops = shops,
                                                date_from = d_f,
                                                date_to = d_t,
                                                )
            result += df_periods[list_colums].sum().sum()
        self.assertEqual(df.sum().sum() , result)

    def test_get_sales(self):


        interval = self.TEST_SETTINGS.get_sample_interval()
        df =  self.dw.get_sales(
                    date_from = interval[0],
                    date_to = interval[1],
        )
        if df.empty:
            return True
        print df
        df = df[[u'profit',u'qty',u'receipts_qty',u'sale_id',u'turnover']]
        list_colums = df.columns
        result = 0
        for d_f,d_t in self.TEST_SETTINGS.split_date_range(interval):
            df_periods = self.dw.get_sales(
                                date_from = d_f,
                                date_to = d_t,
                                )
            df_periods[list_colums].sum().sum()
        self.assertEqual(df.sum().sum() , result )
    
    
    def test_get_loyalty_sales(self):
        


        interval = self.TEST_SETTINGS.get_sample_interval()
        shops = self.TEST_SETTINGS.get_samples('shops')

        df = self.dw.get_loyalty_sales(
                shops = shops,
                date_from = interval[0],
                date_to = interval[1],
                )

        if df.empty:
            return True
        df = df[[u'conversion' ,u'male_percent' ,u'new_clients' 
              ,u'profit' ,u'receipts_qty',u'turnover']]
        list_colums = df.columns
        result = 0
        for d_f,d_t in self.TEST_SETTINGS.split_date_range(interval):
            df_periods = self.dw.get_loyalty_sales(
                                                    shops = shops,
                                                    date_from = d_f,
                                                    date_to = d_t,
                                                    )

            result += df_periods[list_colums].sum().sum()
        self.assertEqual(df.sum().sum() , result/2)
        