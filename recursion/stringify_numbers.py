obj1 = {
    "num": 2,
    "test": [],
    "data": {
        "val": 4,
        "info": {
            "time": 'Noon',
            "random": 44
        }
    }
}


def stringifyNumbers(obj):
    # TODO
    for key in obj:
        if type(obj[key]) is dict:
            stringifyNumbers(obj[key])
        elif type(obj[key]) is int:
            obj[key] = str(obj[key])
            
    return obj

print(stringifyNumbers(obj1))
