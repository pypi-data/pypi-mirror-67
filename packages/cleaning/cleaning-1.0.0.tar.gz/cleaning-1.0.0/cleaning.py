def cleantime(listtest):
    listtestnew = []
    for eachitem in listtest:
        eachitemnew = ''
        if '-' in str(eachitem):
            splitter = '-'
        elif ':' in str(eachitem):
            splitter = ':'
        elif '.' in str(eachitem):
            splitter = '.'
        (mins, seconds) = eachitem.split(splitter)
        eachitemnew = (mins + '.' + seconds)
        listtestnew.append(eachitemnew)
    return listtestnew
