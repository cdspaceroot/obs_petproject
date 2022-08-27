import datetime

import bottle


INDEX_HTML = """
<link href="http://fonts.cdnfonts.com/css/gost-type-a" rel="stylesheet">

<p style="
        font-family:'GOST type A';
        color:#ff0000;
        font-size:80px;
        font-weight:bold
        "
    >
    Текущее время: <span id="current_time"></span>
</p>
"""


@bottle.route("/current_time")
def current_time():
    return str(datetime.datetime.now())


@bottle.route("/")
def index():
    return INDEX_HTML


bottle.run(host="localhost", port=8080)
