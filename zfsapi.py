import json
from bottle import route, run
from zfslib.zpool import zpool_status
@route('/status')
def index():
    return json.dumps(zpool_status()) 

run(host='localhost', port=8080, server='paste')

