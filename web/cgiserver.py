# -*- coding: utf-8 -*-
from http.server import HTTPServer, CGIHTTPRequestHandler

class Handler(CGIHTTPRequestHandler):
    cgi_directories = ["/cgi"]

PORT = 8000
httpd = HTTPServer(("", PORT), Handler)
httpd.serve_forever()
