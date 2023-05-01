import ssl
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

publish = {
	"handle": 1,
	"method": "Publish",
	"params": {
		"qStreamId": "2a63aa89-1af5-4e1c-9c18-bbcc612b188b",
		"qName": "Vered_Order Model Process"
	}
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

def swap_script(app_id):
	uri = f"wss://{engine_endpoint}:4747/app"
	ws = websocket.create_connection(uri, sslopt=certs, header=engine_header, verify=False)
	rec = ws.recv()
	rec = open_doc(ws, app_id)
	ws.send(json.dumps(getDocList))
	receieve = json.loads(ws.recv())
	print(rec)
	# rec = get_script(ws)
	# newscript = addword + rec["result"]["qScript"]
	# print(newscript)
	# #print(newscript)
	# ws.send((json.dumps({"handle": 1,
	# 	"method": "SetScript",
	# 	"params": {
	# 		"qScript": f"{newscript}"
	# 	}})))
	ws.close()

swap_script("806f17e1-b58c-4b39-8728-cb5188cd462a")

# pip install websocket-client