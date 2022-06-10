import re

path = "./madlib_cli/assets/madlib.txt"


def greeting():
    welcome_msg = "Welcome to Madlib Game.\nin this game you need to " \
                  "insert random words\nand then you will see the whole sentence " \
                  "when you finish.\n** to quit at any time, type 'quit'**"
    print(welcome_msg)


def answers():
    user_answer = []
    questions = ["Adjective", "Adjective", "A First Name", "Past Tense Verb", "A First Name", "Adjective", "Adjective",
                 "Plural Noun", "Large Animal", "Small Animal", "A Girl's Name",
                 "Adjective", "Plural Noun", "Adjective", "Plural Noun", "Number 1-50",
                 "First Name's", "Number", "Plural Noun", "Number", "Plural Noun"]
    for word in questions:
        answer = input(f'{word} >')
        if answer == "quit":
            break
        user_answer.append(answer)
    return user_answer


def read_template(n=path):
    try:
        with open(n) as file2:
            x = file2.read()
            return x
    except FileNotFoundError:
        raise FileNotFoundError


def parse_template(n):
    reg = r'(?<={).*?(?=})'
    reg_list = re.findall(reg, n)
    new_str = re.sub(reg, "", n)
    return new_str, tuple(reg_list)


def merge(n, lst):
    return n.format(*lst)


def new_file(n):
    with open("madlib_cli/assets/new_file..txt", "w") as new_file1:
        new = new_file1.write(n)
        return new


if __name__ == "__main__":

    def decoration():
        def wrap():
            print("=" * 50)
            greeting()
            print("=" * 50)
            print("Please write words for the Game")
            print("=" * 50)
            print("=" * 50)
            reading = read_template(path)
            new_strs, reg_lists = parse_template(reading)
            user_answers = answers()
            merge_file = merge(new_strs, tuple(user_answers))
            new_file(merge_file)
            print("=" * 50)
            print(merge_file)
            print("=" * 50)
            print("Thank you XD")
            print("=" * 50)

        return wrap

    decorater = decoration()
    decorater()
