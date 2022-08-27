import datetime

import bottle


@bottle.route("/current_time")
def current_time():
    return str(datetime.datetime.now())


@bottle.route("/")
def index():
    return ""


bottle.run(host="localhost", port=8080)
