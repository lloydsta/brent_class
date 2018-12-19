def adder(var_0, var_1):
    """Adds the two variables"""
    return var_0 + var_1

x = adder(1,3)
#print(x)

def birthday(bday_int, bday_string):
    """1st parameter is a number, 2nd will be a string"""
    to_add = bday_int + 10
    print(bday_string + " " + 'is ' + str(to_add))

birthday(1984, 'lloyd')
