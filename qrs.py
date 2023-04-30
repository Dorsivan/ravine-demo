import asyncio
import csv
import ssl
import requests
import pathlib
import websocket
import json

headers = {"X-Qlik-XrfKey": "iiUNaaVTY3nQmTTZ", "X-Qlik-User": "UserDirectory=EC2AMAZ-OKLUS7R; UserId=qlikadmin"}

xref = 'iiUNaaVTY3nQmTTZ'
host = '54.216.153.136:4242'

certificate = ('client.pem','client_key.pem')
root = 'root.pem'

def test_connection():
	endpoint = 'qrs/about'
	response = requests.get("https://{0}/{1}?xrfkey={2}".format(host, endpoint, xref), headers=headers, verify=False, cert=certificate)
	respjson = json.loads(response.content.decode('utf-8'))
	return respjson
	
def get_apps():
	endpoint = 'qrs/app'
	response = requests.get("https://{0}/{1}?xrfkey={2}".format(host, endpoint, xref), headers=headers, verify=False, cert=certificate)
	print(response.content.decode('utf-8'))
	respjson = json.loads(response.content.decode('utf-8'))
	return respjson

get_apps()
