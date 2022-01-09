from flask import Flask
from flask_restful import Api
from database.db import init_db
from resources.routes import init_routes

import os


app = Flask(__name__)
api = Api(app)
app.config['MONGODB_SETTINGS'] = {
    'db':'d42',
    # 'host': os.environ['MONGODB_HOSTNAME'],
    'host':'localhost',
    'port': 27017,
    'username':os.environ.get('MONGODB_USERNAME'),
    'password':os.environ.get('MONGODB_PASSWORD')
}



init_db(app)

init_routes(api)



if __name__ == '__main__':
    app.run(debug=True)
