
def evaluate_number(argument=None, number=None):
    # no argument = right side, just return it
    if argument is None:
        return number

    left_side = number
    right_side = argument.get("number")
    operator = argument.get("operator")


    if operator != "/":
        instruction = f"int({left_side}) {operator} int({right_side})"
        result = eval(instruction)
    else:
        quotient = float(left_side) / float(right_side)
        int_div = float(left_side) // float(right_side)

        result = int_div if quotient*right_side == left_side else quotient

    return result

def zero(argument=None):
    return evaluate_number(argument=argument, number=0)

def one(argument=None):
    return evaluate_number(argument=argument, number=1)

def two(argument=None):
    return evaluate_number(argument=argument, number=2)

def three(argument=None):
    return evaluate_number(argument=argument, number=3)

def four(argument=None):
    return evaluate_number(argument=argument, number=4)

def five(argument=None):
    return evaluate_number(argument=argument, number=5)

def six(argument=None):
    return evaluate_number(argument=argument, number=6)

def seven(argument=None):
    return evaluate_number(argument=argument, number=7)

def eight(argument=None):
    return evaluate_number(argument=argument, number=8)

def nine(argument=None):
    return evaluate_number(argument=argument, number=9)

def plus(number):
    return {
        "operator": "+",
        "number": number
    }

def times(number):
    return {
        "operator": "*",
        "number": number
    }

def minus(number):
    return {
        "operator": "-",
        "number": number
    }

def divided_by(number):
    return {
        "operator": "/",
        "number": number
    }
    
assert seven(times(five())) == 35
assert four(plus(nine())) == 13
assert eight(minus(three())) == 5
assert six(divided_by(two())) == 3
assert two(divided_by(four())) == 0

