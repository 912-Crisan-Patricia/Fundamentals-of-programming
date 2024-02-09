def add_animal(params, list):
    for animal in list:
        print(animal)
    tokens=params.split(',')
    if len(tokens)!=4:
        raise ValueError("Invalid number of parameters")
    for animal in list:
        if animal['code']==tokens[0]:
            raise ValueError("Code already exists")
    list.append({'code': tokens[0], 'name': tokens[1],'type': tokens[2], 'species': tokens[3]})


def test_add():
    addlist=[]
    add_animal('1,2,3,4',addlist)
    assert addlist==[{'code': '1', 'name': '2', 'type': '3', 'species': '4'}]

def modify_type(params, list):
    for animal in list:
        print(animal)
    tokens=params.split(',')
    if len(tokens)!=2:
        raise ValueError("Invalid number of parameters")
    for animal in list:
        if animal['code']==tokens[0]:
            animal['type']=tokens[1]
            print(list)
            return
    raise ValueError("Code does not exist")

def test_modify():
    modifylist=[{'code': '1', 'name': '2', 'type': '3', 'species': '4'}]
    modify_type('1,5',modifylist)
    assert modifylist==[{'code': '1', 'name': '2', 'type': '5', 'species': '4'}]

def change_type(params, list):
    for animal in list:
        print(animal)
    tokens=params.split(',')
    for animal in list:
        if animal['species']==tokens[0]:
            animal['type']=tokens[1]
    print("modified changes:")
    for animal in list:
        print(animal)

def display_animals(params,list):
    for animal in list:
        print(animal)
    newlist=[]
    for animal in list:
        if animal['type']==params:
            newlist.append(animal)

    sortedlist=sorted(newlist, key= lambda x: x['name'],reverse=True)

    print("New list")
    for animal in sortedlist:
        print(animal)



def populate_list(list):
    add_animal('Z01,John,carnivore,lion',list)
    add_animal('Z02,Alex,carnivore,zebra',list)
    add_animal('Z03,Michael,herbivore,monkey',list)
    add_animal('Z04,Andrei,herbivore,lion',list)
    add_animal('Z05,George,carnivore,zebra',list)


def menu():
    print("1. Add an animal")
    print("2. Modify type of an animal")
    print("3. Change type of an entire species")
    print("4. Display animals in ascending order based on type")
    print("4. Exit")


def split_command(command):
    tokens=command.split(' ',1)
    return tokens[0],'' if len(tokens)==1 else tokens[1]


def start():
    list=[]
    populate_list(list)
    command_dict={'1': add_animal,'2': modify_type,'3':change_type,'4':display_animals}
    exit=False
    while not exit:
        menu()
        command=input("Enter command: ")
        command_word,command_params=split_command(command)
        if command_word in command_dict:
            try:
                command_dict[command_word](command_params, list)
            except ValueError as ve:
                print(ve)
        elif command_params=='' and command_word!='exit':
            print("Invalid command")
        elif command_word=='exit':
            exit=True
        else:
            print("Invalid command")

start()

