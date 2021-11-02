# put your python code here
def multiply(*args):
    total = 1
    if args:
        for number in args:
            total *= number
        return total
    return None
