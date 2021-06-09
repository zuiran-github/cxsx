import json


def writeNewCity(list):
    filename = 'allScenic.json'
    with open(filename, 'r') as file:
        a = file.read()
        if len(a) != 0:
            alllist = json.loads(a)
            try:
                alllist = dict(**alllist, **list)
            except:
                for key,value in list.items():
                    alllist[key] = value
    with open(filename, 'w') as file:
        json.dump(alllist, file)


if __name__ == '__main__':
    list = {'4':'6','0':'6'}
    writeNewCity(list)