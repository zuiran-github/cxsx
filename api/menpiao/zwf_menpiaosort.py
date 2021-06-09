


def sortmenpiao(listx):
    lens = []
    alllist = {}
    for key,value in listx.items():
        lens.append({key:len(value)})
    lens.sort(key=lambda x: list(x.values()), reverse=True)
    # print(lens)
    for item in lens:
        key0,value0 = item.popitem()
        alllist[key0] = listx[key0]
    # print(alllist)
    return alllist