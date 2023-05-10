import chardet

with open('SalesRecords.csv', 'rb') as rawdata:
    result = chardet.detect(rawdata.read(100000))
print(result)
