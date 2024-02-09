'''

Welcome to the future. The age of Python is long gone. After the roaring 2000s reigned by Java, from the ashes of the two decade empire ruled by Python, another language takes over the realm: Mamba. Mamba is minimalist and allows writing simple math instructions in the form of function calls defined syntactically as follows:

function_name(p1,p2,...,pn)=p1(+|-)p2(+|-)p3(+|-)...(+|-)pn

Let's consider the following Mamba functions as examples:
add(a,b)=a+b
negate(param)=-param
alternate_sum(first,second,third,fourth)=first-second+third-fourth

You are employed by the establishment to write, in the now obsolete Python language, a program that evaluates Mamba functions. You will implement the commands below, so that users can run them repeteadly and in any order:

1.
add function_name(p1,p2,...,pn)=p1(+|-)p2(+|-)p3(+|-)...(+|-)pn
This adds the given Mamba function to you program [2p]. For example:
add add(a,b)=a+b
add alternate_sum(first,second,third,fourth)=first-second+third-fourth

2.
list function_name
This displays the correct Python code of the given function to the console (whitespace not required) [2p]. An error is displayed if the function was not previously defined [1p]. For example:
list add should display def add(a,b): return a+b
list alternate_sum should display def alternate_sum(first,second,third,fourth): return first-second+third-fourth

3.
eval function_name(actual_parameters)
This displays on the console the result of calling the function with the given parameters [2p]. In case the function definition contains an error, a message is displayed on the console [1p]. For example:
eval add(1,2) will print 3
eval alternate_sum(1,2,3,4) will print -2
'''


def split_command(command):
    tokens=command.split(' ',1)
    tokens[0]=tokens[0].strip().lower()
    return tokens[0],'' if len(tokens)==1 else tokens[1].strip().lower()

def add_function(item_list,command_params):
    name=command_params.split('(',1)
    params=name[1].split('=',1)
    item_list.append({'Name':name[0],'Parameters':'('+params[0],'Result':params[1]})
    print(item_list)

def list_function(item_list,command_params):
    ok=0
    for index in range(len(item_list)):
        if item_list[index]['Name']==command_params:
            ok=1
            print(item_list[index]['Name']+item_list[index]['Parameters']+'='+item_list[index]['Result'])
    if ok==0:
        raise ValueError("Function not defined")


def eval_function(item_list, command_params):
    name, actual_params = command_params.split('(', 1)
    name = name.strip()
    actual_params = actual_params.rstrip(')')

    if name in item_list:
        try:
            mamba_function = item_list[name]
            eval_str = f"{mamba_function['Name']}{mamba_function['Parameters']}={mamba_function['Result']}"
            result = eval(eval_str, {}, actual_params)
            print(result)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"Error: Function '{name}' not defined.")


def start():
    item_list=[]
    exit=False
    command_dict={"add":add_function ,"list":list_function,"eval":eval_function}
    while not exit:
        print("1.add function name")
        print("2.list function name")
        print("3.eval function name")
        print("4.exit")

        command=input("Enter your choice: ").strip().lower()
        command_word,command_params=split_command(command)
        if command_params=='' and command_word!='exit':
            print("Invalid command")
        elif command_word in command_dict:
            try:
                command_dict[command_word](item_list,command_params)
            except ValueError as ve:
                print(ve)
        elif command_word=='exit':
            exit=True
        elif command_word not in command_dict:
            print("Invalid command")

start()

