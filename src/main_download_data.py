#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
import pandas as pd
import yfinance as yf


def run():
    
    # Read JSON file with parameters
    path_inputs = "./downloader_inputs.json"
    with open(path_inputs, "r") as f:
        inputs = json.load(f)
    tickers = inputs['tickers']
    data = yf.download(tickers, **inputs['params'])
        
    # Get rid of the multi-index for columns
    series = []
    for c in data.columns:
        serie = data[c]
        serie.name = '_'.join(serie.name)
        series.append(serie)
    df_out = pd.concat(series, axis=1)
    
    # Save file
    out_path = './output/'
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    out_name = os.path.join(out_path, "prices.csv")
    df_out.to_csv(out_name)

if __name__ == '__main__':
    run()
    