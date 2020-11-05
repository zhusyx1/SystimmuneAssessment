# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 21:55:34 2020

How to use:
python carDealer.py --input_csv_name car.csv

@author: Coco Zhu
"""

import pandas as pd
import argparse
import flask

csv_path= 'car.csv'

def main(csv_path):

    auto_df=pd.read_csv(csv_path,index_col=None)

    gy_df=auto_df.groupby(['CarModleId','CarModleName','SoldMonth']).agg(
     sum_sold=('NumberSold', sum))
    gy_df =gy_df.reset_index()
    gy_df=gy_df.sort_values(['sum_sold','SoldMonth'],ascending=False)
    ## ignore that cases that needing breaking tie!!
    gy_df=gy_df.groupby(['SoldMonth']).first()
    top1_df =gy_df.reset_index()
    ## the part of sales man
    sales_df=auto_df.groupby('SalesName').agg(
        sell_point=('NumberSold', sum)
       )
    sales_df =sales_df.reset_index()
    ## the part of output results
    top1_df.to_html('top.html')
    sales_df.to_html('sales.html')
    return 
# print(sales_df)
if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('--input_csv_name', default=None,help='the path of csv source')
    opt=parser.parse_args()
    main(opt.input_csv_name)


