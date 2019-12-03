# ADD NEW FILES HERE
__all__ = ["views", "bank","branch","bankaccount"]

from app import app, utils
import requests
import os
from flask import Flask, jsonify, send_file, g, render_template, redirect, request, session, url_for

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def route_frontend(path):
    # ...could be a static file needed by the front end that
    # doesn't use the `static` path (like in `<script src="bundle.js">`)
    file_path = os.path.join(app.static_folder, path)
    if os.path.isfile(file_path):
        return send_file(file_path)
    # ...or should be handled by the SPA's "router" in front end
    else:
        if app.debug:
            # change this to the Network address of the Vue app
            return requests.get('{}{}'.format(utils.get_env_variable("FRONTEND_URL"), path)).text
        index_path = os.path.join(app.static_folder, 'index.html')
        return send_file(index_path)
