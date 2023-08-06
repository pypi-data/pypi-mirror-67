import json
from munch import munchify

def ok(req, res):
    """ status ok """
    res.data = json.dumps({"status": "ok"})

def jsonify(req, res):
    """ return json """
    res.json.code = res.status
    res.data = json.dumps(res.json)
    res.content_type = 'application/json'
