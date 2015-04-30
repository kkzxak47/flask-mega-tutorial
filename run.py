#!/usr/bin/env python2

import socket
from app import app

if socket.gethostname().startswith('DigitalOcean'):
    app.run(debug=True, host='0.0.0.0')
else:
    app.run(debug=False)

