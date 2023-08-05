
import sys
import pprint
import csv
import hashlib
import math


def earningsAccounts(self, data):
    for item in data:
        if 'labels' in item:
            item['labels'] = item['labels'].replace(', ', ',').split(',')
    return data



def siteGroups(self, data):
    for item in data:
        if 'labels' in item:
            item['labels'] = item['labels'].replace(', ', ',').split(',')
    return data



def adUnits(self, data):
    for item in data:
        
        if 'site' in item: 
            item['site'] = {'id': item['site']}
        if 'labels' in item:
            item['labels'] = item['labels'].replace(', ', ',').split(',')
    return data



def teams(self, data):
    for item in data:
        if 'sites' in item:
            item['sites'] = item['sites'].replace(', ', ',').split(',')
            site_holder = []
            for site in item['sites']:
                site_holder.append({
                    'id': site
                })

        if 'labels' in item:
            item['labels'] = item['labels'].replace(', ', ',').split(',')
    return data


def sites(self, data):
    for item in data:
        if 'earningsAccount' in item:
            item['earningsAccount'] = {'id': item['earningsAccount']}
        if 'siteGroup' in item:
            item['siteGroup'] = {'id': item['siteGroup']}
        if 'labels' in item: 
            item['labels'] = item['labels'].replace(', ', ',').split(',')

    print(data)
    return data

# def users(self, data):
#     print('heeey')
#     print(data)
#     return data
