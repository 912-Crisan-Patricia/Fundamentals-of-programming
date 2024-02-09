def add_plane(params,list):
    '''
    Adds a plane to list
    :param params: command line params
    :param list: list of planes
    :return: -
    '''
    tokens=params.split(',')
    if len(tokens)!=4:
        raise ValueError("Invalid number of parameters")
    for plane in list:
        if plane['code']==tokens[0]:
            raise ValueError("Code already exists")
    list.append({'code': tokens[0], 'duration': tokens[1],'departure city': tokens[2], 'destination city': tokens[3]})
    #print(list)

def test_add():
    addlist=[]
    add_plane('1,2,3,4',addlist)
    assert addlist==[{'code': '1', 'duration': '2', 'departure city': '3', 'destination city': '4'}]

def modify_duration(params, list):
    '''
    Modifies duration of given plane
    :param params: command line params
    :param list: list of planes
    :return: -
    '''

    for plane in list:
        print(plane)

    tokens=params.split(',')
    for plane in list:
        if plane['code']==tokens[0]:
            plane['duration']=tokens[1]

    print("New list:")
    for plane in list:
        print(plane)


def test_modify():
    addlist = []
    add_plane('1,2,3,4', addlist)
    modify_duration('1,5',addlist)
    assert addlist==[{'code': '1', 'duration': '5', 'departure city': '3', 'destination city': '4'}]


def change_destination(params,list):

    for plane in list:
        print(plane)
    tokens=params.split(',')
    if len(tokens[1])<3:
        raise ValueError("New destination not correct")
    for plane in list:
        if plane['destination city']==tokens[0]:
            plane['destination city'] = tokens[1]
    print("New list")
    for plane in list:
        print(plane)



def display_planes(params,list):

    for plane in list:
        print(plane)

    newlist=[]

    for plane in list:
        if plane['destination city']==params:
            newlist.append(plane)

    sorted_list= sorted(newlist,key=lambda x: x['duration'])

    print("New list")
    for plane in sorted_list:
        print(plane)

def increase(params,list):

    for plane in list:
        print(plane)

    tokens=params.split(',')
    for plane in list:
        if plane['code']==tokens[0]:
            plane['duration']=str(int(plane['duration'])+ int(tokens[1]))
    print("New list >")
    for plane in list:
        print(plane)


def procent(params,list):
    for plane in list:
        print(plane)

    for plane in list:
        plane['duration']=str( int(plane['duration']) + (int(plane['duration'])/100*int(params)))

    print("new list")
    for plane in list:
        print(plane)


def split_command(command):
    tokens=command.split(' ',1)
    return tokens[0],'' if len(tokens)==1 else tokens[1]

def menu():
    print("1.Add plane ")
    print("2.Modify duration of plane ")
    print("3.Change all destinations of a city")
    print("4.Display all planes ordered by duration and given a destination ")


def populate_list(list):
    add_plane('P0001,20,Oradea,Cluj', list)
    add_plane('P0002,25,Oradea,Bucuresti', list)
    add_plane('P0003,40,Oradea,Milano', list)
    add_plane('P0004,20,Milano,Cluj', list)
    add_plane('P0005,20,Atena,Cluj', list)

    for plane in list:
        print(plane)


def start():
    list=[]
    command_dict={'add':add_plane,'modify':modify_duration,'change':change_destination,
                  'display':display_planes,'increase':increase,'procent':procent}
    exit=False
    populate_list(list)
    while not exit:
        menu()
        command=input("Input choice here >")
        command_word,command_params=split_command(command)

        if command_word in command_dict:
            try:
                command_dict[command_word](command_params,list)
            except ValueError as ve:
                 print(ve)
        elif command_params=='' and command_word!='exit':
            print('Invalid input')
        elif 'exit'==command_word:
            exit=True
        else:
            print("Invalid input")

start()