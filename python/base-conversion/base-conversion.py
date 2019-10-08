def decimal_to_binary(number):
    next_power_of_two, i = 0, 0
    result_string = []
    while next_power_of_two<=number:
        next_power_of_two = 2**i
        i += 1
        
    if i == 1:
        return "0"
    else:
        for a in range(i-2, -1, -1):
            if number//(2**a) == 1:
                result_string.append("1")
                number = number - 2**a
            else:
                result_string.append("0")
    return_string = ""
    for entry in result_string:
        return_string += entry
    return return_string

add1 = lambda x: x + 1

def compose(f, g):
    return lambda x: f(g(x))


def repeated(f, n):
    if n == 0:
        return lambda x: x
    else:
        return compose(f, repeated(f, n - 1))

def plus(x,y):
    return repeated(add1, x)(y)


def make_decimal_to_n_ary_converter(n):
    def make_decimal_to_n_ary(number):
        alphabets = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        next_power_of_n, i = 0, 0
        result_string = []
        while next_power_of_n<=number:
            next_power_of_n = n**i
            i += 1
        print(i)
        if i > 1:
            for a in range(i-2, 0, -1):
                if number//(n**a) != 0:
                    if number//(n**a) <10:
                        result_string.append(str(number//(n**a)))
                        number = number%(n**a)
                    else:
                        result_string.append(alphabets[(number//(n**a))])
                        number = number%(n**a)
                else:
                    result_string.append("0")
        result_string.append(alphabets[number])

                        
        return_string = ""
        for entry in result_string:
            return_string += entry
        return return_string
    return make_decimal_to_n_ary


def hexadecimal_to_decimal(hex_number):
    alphabets = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_list = list(hex_number)
    power = len(number_list)-1
    dec_return = 0
    for number in number_list:
        dec_return += alphabets.index(number) * (16**power)
        power -=1
    return dec_return




def make_n_ary_to_decimal_converter(n):
    def n_ary_to_dec(number):
        alphabets = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        number_list = list(number)
        power = len(number_list)-1
        dec_return = 0
        for digit in number_list:
            dec_return += alphabets.index(digit) * (n**power)
            power -=1
        return dec_return
    return n_ary_to_dec

print(make_n_ary_to_decimal_converter(14)('DABBAD00'))
    
