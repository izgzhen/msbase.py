import json

def load_json(p: str):
    return json.load(open(p, "r"))

def write_pretty_json(stuff, path: str):
    open(path, 'w').write(json.dumps(stuff, indent=4, sort_keys=True))
