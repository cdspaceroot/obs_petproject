import datetime
import json

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

<script>

    function update_time(value){
        document.getElementById('current_time').innerHTML = value;
    }

    function get_time() {
        let request = new XMLHttpRequest();

        request.addEventListener( "load", function(event) {
            if(event.target.status == 200){
                update_time(event.target.responseText);
            } else {
                console.log(event);
            }
        });

        request.open("GET", 'http://localhost:8080/current_time', true);
        request.send(null);
    };

    window.addEventListener("load", function(event) {
        setInterval(get_time, 1000);
    });

</script>
"""


@bottle.route("/current_time")
def current_time():
    return str(datetime.datetime.now())


@bottle.route("/banrequests")
def get_ban_requests():
    bottle.response.content_type = "application/json"
    return json.dumps({"self": 0})


@bottle.route("/")
def index():
    return INDEX_HTML


bottle.run(host="localhost", port=8080)
