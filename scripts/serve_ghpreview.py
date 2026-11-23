#!/usr/bin/env python3
"""Serve out-gh under the /DataQ basePath for local preview."""
import http.server, os, functools, sys

ROOT = '/home/z/my-project/site/out-gh'
BASE = '/DataQ'

class H(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        if path.startswith(BASE):
            path = path[len(BASE):] or '/'
        return super().translate_path(path)
    def log_message(self, *a): pass

os.chdir(ROOT)
http.server.ThreadingHTTPServer(('127.0.0.1', 4173), H).serve_forever()
