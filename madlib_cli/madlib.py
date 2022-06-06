def read_template(n):
    try:
        file = open(n)
        x = file.read()
        return x
    except FileNotFoundError:
        return "missing.txt"
    finally:
        file.close()


def parse_template(n):
    return n.format({}, {}, {})


def merge():
    return 1


#read_template("/dark_and_stormy_night_template.txt")