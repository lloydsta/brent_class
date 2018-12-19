#phone_no = '8082819094'
phone_no = input('Please enter a phone number (no dashes): ')
first_3_digits = phone_no[0] + phone_no[1] + phone_no[2]


if len(phone_no) >= 2 or len(phone_no) <= 15:
    #for x in first_3_digits:
        #if first_3_digits[x] == 7 or int(first_3_digits[x]) == 8 or int(first_3_digits[x]) == 9:

    if '7' in first_3_digits or '8' in first_3_digits or '9' in first_3_digits:
        print('VALID PHONE NUMBER')
    else:
        print('Phone number must start with a 7, 8, or 9')
else:
    print ('Not a valid phone number')
