def over_easy(string1,string2):
    x = len(string1)
    slice_string2 = string2[-x:]
    if slice_string2 == string1:
        print('True')
    else:
        print('False')

####################################

over_easy('tmare','nightmare')
