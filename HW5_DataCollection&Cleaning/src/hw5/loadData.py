import json

def load_file(input_file):
    tmp=[]
    with open(input_file) as file:
        for jsonObj in file:
            try:
                jdict=json.loads(jsonObj)
                tmp.append(jdict)
            except ValueError:
                continue
    return tmp
