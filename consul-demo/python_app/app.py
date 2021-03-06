import json
from time import sleep
import pymysql.cursors


import requests
from flask import Flask
app = Flask(__name__)

BASE_CONSUL_URL = 'http://consul1:8500'

PORT = 8080

def get_mysql_host():
    BASE_CONSUL_URL = 'http://consul1:8500/v1/catalog/service/mysqldb'
    result = requests.get(BASE_CONSUL_URL)
    return json.loads(result.text)

def mysql_version():
    host = get_mysql_host()[0]['Node']
    mysql_connection = pymysql.connect(host=host,user="root",password="",db="mysql" )
    cursor = mysql_connection.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    return data



@app.route('/')
def home():
    result = mysql_version()
    if result:
       return "Hello World ... DB connected!!"
    else:
       return "Hello World ... DB connection issue.."


@app.route('/health')
def hello_world():
    data = {
        'status': 'healthy'
    }
    return json.dumps(data)


def register():
    url = BASE_CONSUL_URL + '/v1/agent/service/register'
    data = {
        'name': 'PythonApp',
        'address': 'app1',
        'check': {
            'http': 'http://app1:{port}/health'.format(port=PORT),
            'interval': '10s'
        }
    }
    res = requests.put(
        url,
        data=json.dumps(data)
    )
    return res.text


if __name__ == '__main__':
    sleep(8)
    try:
        print(register())
    except:
        pass
    app.debug = True
    app.run(host="0.0.0.0", port=PORT)
