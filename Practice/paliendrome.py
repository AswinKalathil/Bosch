string =input("Enter a String : ")
string_lower=string.lower()
rev_string = string_lower[::-1]

if string_lower == rev_string:
    print( f'"{string}" is paliendrome')
else:
    print( f'"{string}" is not paliendrome')