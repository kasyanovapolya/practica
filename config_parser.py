from tabulate import tabulate

file1 = open('config1.txt', 'r', encoding='cp1251', errors='ignore', newline='')
file2 = open('config2.txt', 'r', encoding='cp1251', errors='ignore', newline='')

def parametersExtractor(file):
    lines = file.readlines()
    params = {}
    for line in lines:
        newline = line.replace('\t',' ')
        fchar = newline[0]
        if fchar == '#' or fchar =='\r' or fchar == ' ':
            continue
        splitline = newline.split()
        if len(splitline) > 1:
            params[splitline[0]] = splitline[1]
        else:
            params[splitline[0]] = '–'
    return params

config1 = parametersExtractor(file1)
config2 = parametersExtractor(file2)

keys1 = list(config1.keys())
keys2 = list(config2.keys())
allkeys = list(keys1)

for key in keys2:
    if key not in allkeys:
        allkeys.append(key)

result = []
for key in allkeys:
    value1 = config1[key] if key in keys1 else '–'
    value2 = config2[key] if key in keys2 else '–'
    result.append([key, value1, value2])

resultable = tabulate(result, headers=['Parameters', 'Config 1', 'Config 2'])
resultfilename = 'comparison.txt'

try:
  file = open(resultfilename, 'x')
except PermissionError:
    print(f'No access permissions for {resultfilename}')
except FileExistsError:
    print(f'File {resultfilename} already exists')
except Exception as err:
    print(f'Unexpected error opening {resultfilename} is',repr(err))
else:
  with file:
    file.write(resultable)