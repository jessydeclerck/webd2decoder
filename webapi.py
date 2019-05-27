#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_sockets import Sockets
from decoder import decoder
import json
import logging

logger = logging.getLogger("webapi")

app = Flask(__name__)
sockets = Sockets(app)


@app.route('/decoder/fromclient', methods=['POST'])
def decode_from_client():
    return jsonify(decoder.readMsg(request.get_data(as_text=True), True))


@app.route('/decoder/fromserver', methods=['POST'])
def decode_from_server():
    return jsonify(decoder.readMsg(request.get_data(as_text=True), False))


@sockets.route('/decoder')
def echo_socket(ws):
    while not ws.closed:
        try:
            message = json.loads(ws.receive())
            logger.debug("Message received %s", message)
            ws.send(json.dumps(
                decoder.readMsg(message['data'], message['fromclient'])))
        except json.decoder.JSONDecodeError as err:
            logger.error(err)
            ws.send("Error while parsing data from json")
        except:
            logger.error("Error while processing data")
            ws.send("Error")


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    port = int(os.environ.get('PORT', 5000))
    server = pywsgi.WSGIServer(('', port), app, handler_class=WebSocketHandler)
    server.serve_forever()
