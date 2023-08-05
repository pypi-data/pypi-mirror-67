import hashlib
import datetime
import requests
import os
import json



def get(self, endpoint, params={}):
	request_params = self.params.copy()
	request_params.update(params)
	return requests.get(
		self.host + self.version + endpoint,
		params=request_params,
		headers=self.headers
	).json()


def post(self, endpoint, data):
	return requests.post(
		self.host + self.version + endpoint,
		params=self.params,
		json=data,
		headers=self.headers
	).json()


def post_file(self, creative_id, file):
	asset = {}
	try:
		params = {
			"auth_token": self.token,
			"context": self.context
		}
		file = os.path.dirname(os.path.abspath(
			__file__)).replace('workers', '')+file
		print(file)
		files = {'media': open(file, 'rb')}
		print(files)

		assetId = hashlib.sha512(
			bytes('asset_'+creative_id, 'utf8')).hexdigest()[:24]
		print(assetId)
		print(self.host + self.version + '/assets/' +
				creative_id + '/' + assetId)
		asset = requests.post(
			self.host + self.version + '/assets/' + creative_id + '/' + assetId,
			params=params,
			files=files
		).json()

	except:
		print('nofile')

	print(asset)
	return asset
