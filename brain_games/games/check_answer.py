def check_answer(answer):
    if answer is True:
        return 'yes'
    else:
        return 'no'


def calc_answer(number_1, number_2, operator):
    if operator == '+':
        return number_1 + number_2
    if operator == '-':
        return number_1 - number_2
    if operator == '*':
        return number_1 * number_2
