# import modules
from websocket import create_connection, WebSocket

# api attributes
api_key = 'DNwJnXSswWOkrwbjYeYUtWphDjrpnHjr'
host = 'ovs.kontakt.io'
port = '9090'
headers = {
	'Api-key': api_key,
	'Accept': 'application/vnd.com.kontakt+json;version=10'
}
url = f'wss://{host}:{port}/stream?apiKey={api_key}'

# create connection
ws = create_connection(url, header=headers)

ws.send(json.dumps({
    'event': 'subscribe',
    'method': '/presence/stream/0C:8D:DB:D9:0D:5B'
}))
while True:
	result = ws.recv()
	print (result)
