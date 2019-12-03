#!/usr/bin/env python
from app import app, db
import os

db.create_all()
if __name__ == '__main__':
    if app.debug:
        app.run(host='0.0.0.0')
    else:
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)
