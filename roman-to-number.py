def int_to_rome(x):
    number = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    roman = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    i = 12
    roman_numeral = ''
    while x != 0:
        if number[i]<=x:
            roman_numeral += roman[i]
            x = x - number[i]
        else:
            i -= 1

    return roman_numeral

print(int_to_rome(1000)) 