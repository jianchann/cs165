from app import app, db, models, redis_store, utils

import requests
import os
import uuid
import datetime
import jwt
from random import shuffle
from flask import Flask, jsonify, send_file, g, render_template, redirect, request, session, url_for

@app.route('/api/test')
def test_api():
    return jsonify({'msg': 'HELLO WORLD'})
