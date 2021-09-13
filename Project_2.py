from random import randint, choices, shuffle, sample, choice
import string

def password_specs(length = 14, min_spec = 0, min_num = 0, min_upper = 0):
    special_characters = randint(min_spec, length-(min_num + min_upper))
    digits = randint(min_num, length-(special_characters + min_upper))
    uppercase = randint(min_upper, length-(special_characters + digits))
    lower_case = length-(special_characters + digits + uppercase)
    return [special_characters, digits, uppercase, lower_case]



def password_gen(length = 14, spec_char = '@!&', repeat = True, min_spec = 0, min_num = 0, min_upper = 0):
    required = [min_upper, min_num, min_spec]
    if sum(required) <= length and (repeat==True or (repeat==False and len(spec_char) >= min_spec)):
        specs = password_specs(length, min_spec, min_num, min_upper)
        if repeat:
            password = choices(string.ascii_lowercase, k=specs[3]) + choices(string.ascii_uppercase, k=specs[2]) + choices(string.digits, k=specs[1]) + choices(spec_char, k=specs[0])
        else:
            ok = True
            while ok:
                if specs[0] > len(spec_char) or specs[1] > len(string.digits) or specs[2] > len(string.ascii_uppercase)or specs[3] > len(string.ascii_lowercase):
                    specs = password_specs(length, min_spec, min_num, min_upper)
                else:
                    ok = False
            password = sample(string.ascii_lowercase, specs[3]) + sample(string.ascii_uppercase, specs[2]) + sample(string.digits, specs[1]) + sample(spec_char, specs[0])
        shuffle(password)
        pass_w = ""
        for i in password:
            pass_w += i
        return pass_w
    print('Invalid specifications!') 


def check_password(password, length, min_spec, min_num, min_upper):
    spec_char = '@!&'
    num_digit = 0
    num_spec_char = 0
    num_upper = 0
    for letter in password:
        if letter in string.digits:
            num_digit += 1
        if letter in string.ascii_uppercase:
            num_upper += 1
        if letter in spec_char:
            num_spec_char += 1
    if num_digit <= min_num and num_spec_char <= min_spec and num_upper <= min_upper and len(password)== length:
        return True
    else:
        return False