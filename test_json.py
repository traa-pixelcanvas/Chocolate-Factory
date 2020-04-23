import json

# Checks for JSONDecode Errors, finds shit like missing brackets
def test_syntax():
    data = None
    with open("config.json") as json_file:
        data = json.loads(json_file.read())
    print(data)
