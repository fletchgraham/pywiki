"""
To run and debug locally.
"""
import os
from os import path
from shutil import copyfile

from wiki.web import create_app

content_dir = path.join(path.dirname(__file__), 'content')

if not path.exists(content_dir):
    os.mkdir(content_dir)
    copyfile('config.example.py', './content/config.py')

app = create_app(content_dir)
app.run(debug=True, host='127.0.0.1', port=5000)
