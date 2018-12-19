# string = "AbcDefgHijkL"
# uppercase = 0
# lowercase = string - uppercase
#
#
# for x in string:
#     if string[x].isupper():
#         uppercase += 1
#     else:
#         continue

# ======================================

# numbers = [1,2,3,4]
# double = []
# blah = [(n*2) for n in numbers if n%2 == 1]
#
# print(blah)


# ======================================

# numbers = [1,2,3,4]
# double = []
# blah = [for n in numbers ("odd") if n%2 == 1 else "even" if n%2 == 0]
#
# print(blah)

# =====================================


# factorial

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

print(fact(10))
