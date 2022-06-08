import re

def greeting():
    x = "Welcome to Madlib Game.\nin this game you need to " \
        "insert random words\nand then you will see the whole sentence " \
        "when you finish.\n** to quit at any time, type 'quit'**"
    print(x)

def decore(func1,func2):
    def wrap():
        print("="*40)
        func1()
        print("="*40)
        print("Please write words for the Game")
        print("="*40)
        func2()
        print("="*40)
    return wrap

def read_template(n):
    try:
        with open(n) as file:
            x = file.read()
            return x
    except FileNotFoundError:
        raise FileNotFoundError


def parse_template(n):
    reg = r'(?<={).*?(?=})'
    reg_list = re.findall(reg, n)
    new_list = re.sub(reg, "", n)
    return new_list, tuple(reg_list)



def answers(path):
    with open(path , 'r') as file:
        x = file.read()
    pass



def merge(n, lst):
    return n.format(*lst)


#read_template("./assets/dark_and_stormy_night_template.txt")
parse_template('It was a {Adjective} and {Adjective} {Noun}.')
#merge("It was a {} and {} {}.", ("dark", "stormy", "night"))

#decorater = decore(greeting,answers)
#decorater()
