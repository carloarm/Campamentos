import pymongo
import json
from urllib.parse import urlparse
from cgi import parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer

class handler_class(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', '*')    
        self.end_headers()
    def do_GET(self):
        url = self.path
        parsed = urlparse(url)

        #http://127.0.0.1:9000/?latitud=1&longitud=0&radio=100&p=0,0

        latitude = parse_qs(parsed.query)['latitud'][0]
        longit = parse_qs(parsed.query)['longitud'][0]
        radious = parse_qs(parsed.query)['radio'][0]
        print("Latitud (" + latitude + ") " + "Longitud ("+longit+")" + "Radio ("+radious+")")

        from pymongo import MongoClient
        client = MongoClient()
        db = client.primer
        # Creamos la conex
        db = client.database
        camps = db.camps
        self._set_headers()
        self.wfile.write("[".encode())
        for camp in camps.find():

            camplon = abs(float(camp["LONGITUD"]))
            camplat = abs(float(camp["LATITUD"]))

            radious = abs(float(radious))
            latitude = abs(float(latitude))
            longit = abs(float(longit))

            if ((camplon < longit + radious) & (camplat < latitude + radious)): 
                    self.wfile.write(json.dumps(camp).encode())
                    self.wfile.write(",".encode())

        self.wfile.write("{}]".encode())
    def do_HEAD(self):
        self._set_headers()
    def do_POST(self):
        self._set_headers()
        
def run(server_class=HTTPServer, handler_class=handler_class, port=9000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Iniciando server...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()