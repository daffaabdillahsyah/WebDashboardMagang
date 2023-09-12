from application import app
from flask import render_template
import pandas as pd
from collections import defaultdict


@app.route('/')
def index():    
    data1 = pd.read_csv('cleansing_data.csv')
    # # data1_dict = data1.to_dict(orient='records')
    # # total_id = len(data1_dict)
    # # # total_sale = sum(row['SalePrice'] for row in data1_dict)
    # # # average_price = total_sale / total_id
    return render_template('index.html', list_data=[data1.to_html()])
    #data_dict=data1_dict, total_id=total_id, total_sale=total_sale, average_price=average_price)
