"""
To run and debug locally.
"""
import os

from wiki.web import create_app

app = create_app(os.path.dirname(__file__) + '/content')
app.run(debug=True, host='127.0.0.1', port=5000)
