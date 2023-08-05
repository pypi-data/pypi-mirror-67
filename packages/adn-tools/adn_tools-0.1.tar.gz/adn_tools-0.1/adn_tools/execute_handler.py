import csv
import pandas as pd
import pprint as pp
import math

def sanetize(data):
    returnValues = []
    for item in data:
        item_copy = item.copy()
        for key,value in item.items():
            if value == True: item_copy[key] = 'true'
            if value == False: item_copy[key] = 'false'
            if type(value) is float: 
                if math.isnan(value):del item_copy[key]
        returnValues.append(item_copy)
    
    return returnValues
        

def construct(self, type, data):
	print(type)
	function = getattr(self, type, lambda x: False)
	return function(data)


def upload(self, XLSX_FILE):
	df = pd.read_excel(XLSX_FILE, sheet_name=None)
	for sheet in df:
		request_object = self.construct( 
			sheet, 
			sanetize(df[sheet].to_dict(orient='records'))
		)


		if request_object : 
			endpoint = f'/{sheet.lower()}'
			print(self.post(endpoint, request_object))



