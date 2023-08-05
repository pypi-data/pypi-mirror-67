#! /usr/local/bin/python
# -*- coding: utf-8 -*-


import json
import requests


class adn():

    """
    Helper Class that will initialize a connection with ADN API
    """

    def __init__(self, config):
        self.data_frame = {}
        self.host = config['url']
        self.version = '/v1'
        self.context = config['network']
        self.params = {"context": config['network']}
        self.token_request = requests.post(
            self.host+'/authenticate',
            params=self.params,
            json={
                "grant_type": "password",
                "scope": "ng_api",
                "username": config['username'],
                "password": config['password']
            },
            headers={'Content-Type': 'application/json'}
        ).json()
        self.token = self.token_request['access_token']
        self.params['auth_token'] = self.token
        self.headers = {
            'Content-Type': 'application/json',
            "Authorization": "Bearer " + self.token
        }

    from .request_handler import get, post, post_file
    from .item_handler import earningsAccounts, siteGroups, sites, teams, adUnits
    from .execute_handler import upload, construct

