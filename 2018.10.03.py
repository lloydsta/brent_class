list = [1, 1, 3, 6, 7, 9, 10, 2, 2, 1, 5]

# for x in list:
#     if list[x] == 2:
#         print('True')
#     else:
#         print('False')

def twentyTwo():
    for x in range(len(list)-1):
        if list[x] == 2:
            if list[x+1] == 2:
                #print("True-nested")
                return True
                break
            else:
                return False
        else:
            return False

print(twentyTwo())


    #     if list[1] == 2:
    #         print("True")
    #     elif list[x-1] == 2:
    #         print("True")
    #     else:
    #         print("False")
    # else:
    #     print("False")
