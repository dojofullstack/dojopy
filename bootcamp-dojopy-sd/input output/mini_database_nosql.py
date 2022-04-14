import json

# crud_select = 'read'
# key = 'username'

# crud_select = 'write'
# key = 'pelicula'
# value = 'spiderman'

# crud_select = 'update'
# key = 'password'
# value = 'homerosimpson'

# crud_select = 'delete'
# key = 'pelicula'

crud_select = sys.argv[1]
key = sys.argv[2]
value = ''
if len(sys.argv) > 3:
    value = sys.argv[3]


"""mini base datos no SQL """
if crud_select == 'read':
    with open('/home/henry/dojopy/bootcamp-dojopy-lm/input output/database.json') as file:
        data = file.read()
    data = json.loads(data)
    result =  data.get(key)
    print(result)

if crud_select == 'write' or crud_select == 'update':
    with open('/home/henry/dojopy/bootcamp-dojopy-lm/input output/database.json') as file:
        data = file.read()
    data = json.loads(data)
    data[key] = value

    with open('/home/henry/dojopy/bootcamp-dojopy-lm/input output/database.json', 'w') as file:
        json.dump(data, file, indent=4)

if crud_select == 'delete':
    with open('/home/henry/dojopy/bootcamp-dojopy-lm/input output/database.json') as file:
        data = file.read()
    data = json.loads(data)
    data.pop(key)

    with open('/home/henry/dojopy/bootcamp-dojopy-lm/input output/database.json', 'w') as file:
        json.dump(data, file, indent=4)
