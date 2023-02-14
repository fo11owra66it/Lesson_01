def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    delimiter = str('&')
    summ_text = one + delimiter + two
    print(summ_text.upper())

get_summ('Learn', 'python')