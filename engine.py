import asyncio
import csv
import ssl
import requests
import pathlib
import websocket
import json

engine_header = {'X-Qlik-User: UserDirectory=EC2AMAZ-OKLUS7R; UserId=qlikadmin'}
certs = ({"ca_certs": "root.pem", "certfile": "client.pem", "keyfile": "client_key.pem", "cert_reqs": ssl.CERT_NONE, "server_side": False})
engine_endpoint = "54.216.153.136"

getDocList = {
	"handle": -1,
	"method": "GetDocList",
	"params": {},
	"outKey": -1,
	"id": 3
}


getScript = {
	"handle": 1,
	"method": "GetScript",
	"params": {},
	"outKey": -1,
	"id": 3
}

def get_doc_list(ws):
	ws.send(json.dumps(getDocList))
	return json.loads(ws.recv())

def get_script(ws):
	ws.send(json.dumps(getScript))
	return json.loads(ws.recv())

def open_doc(ws, appid):
	ws.send(json.dumps({
		"method": "OpenDoc",
		"handle": -1,
		"params": [
			f"{appid}"
		],
		"outKey": -1,
		"id": 2
		}))
	return ws.recv()

def swap_script(app_id, addword):
	uri = f"wss://{engine_endpoint}:4747/app"
	ws = websocket.create_connection(uri, sslopt=certs, header=engine_header, verify=False)
	rec = ws.recv()
	rec = open_doc(ws, app_id)
	rec = get_script(ws)
	newscript = rec["result"]["qScript"] + addword
	#print(newscript)
	ws.send((json.dumps({"handle": 1,
		"method": "SetScript",
		"params": {
			"qScript": f"{newscript}"
		},
		"outKey": -1,
		"id": 3})))
	#print(ws.recv())

swap_script("3e9b8155-1823-44c3-86e7-1abc025a3e2c", "words")