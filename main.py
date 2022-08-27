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

BANREQUESTS_HTML = """
<link href="http://fonts.cdnfonts.com/css/gost-type-a" rel="stylesheet">

<p style="
        font-family:'GOST type A';
        color:#ff0000;
        font-size:80px;
        font-weight:bold
        "
    >
    Запросов на бан: <br>
    <span id="banrequests"></span>
</p>

<script>

    function update_banrequests(value){

        let bans_as_dict = JSON.parse(value);

        let bans_as_list = Object.keys(bans_as_dict).map(
            (key) => { return [key, bans_as_dict[key]] }
        );

        bans_as_list.sort(
            (first, second) => { return second[1] - first[1]}
        );

        let bans_content = [];

        for (const item of bans_as_list) {
            bans_content.push(`${item[0]}: ${item[1]}`);
        };

        const ban_block = document.getElementById('banrequests');
        ban_block.innerHTML = bans_content.join('<br>');
    }

    function get_banrequests() {
        let request = new XMLHttpRequest();

        request.addEventListener( "load", function(event) {
            if(event.target.status == 200){
                update_banrequests(event.target.responseText);
            } else {
                console.log(event);
            }
        });

        request.open("GET", 'http://localhost:8080/banrequests', true);
        request.send(null);
    };

    window.addEventListener("load", function(event) {
        setInterval(get_banrequests, 1000);
    });

</script>
"""

BANADMIN_HTML = """
<form method="post">

    <label for="username">Username:</label><br>
    <input type="text" id="username" name="username"><br>

    <input type="submit" value="В бан!">
</form>
"""


@bottle.route("/current_time")
def current_time():
    return str(datetime.datetime.now())


@bottle.route("/banrequests")
def get_ban_requests():
    bottle.response.content_type = "application/json"
    return json.dumps({"self": 0})


@bottle.route("/banadmin")
def show_ban_admin_page():
    return BANADMIN_HTML


@bottle.route("/show_banrequests")
def show_ban_requests():
    return BANREQUESTS_HTML


@bottle.route("/")
def index():
    return INDEX_HTML


bottle.run(host="localhost", port=8080)
