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

kset = set(config1.keys())
kset.update(config2.keys())

result = []
for k in kset:
    v1 = config1[k] if k in config1.keys() else '–'
    v2 = config2[k] if k in config2.keys() else '–'
    result.append([k, v1, v2])

resultable = tabulate(result, headers=['Parameters', 'Config 1', 'Config 2'])
resultfilename = 'comparison.txt'

try:
  file = open(resultfilename, 'x')
except PermissionError:
    print(f'No access permissions for {resultfilename}')
except FileExistsError:
    print(f'File {resultfilename} is already exists')
except Exception as err:
    print(f'Unexpected error opening {resultfilename} is',repr(err))
else:
  with file:
    file.write(resultable)