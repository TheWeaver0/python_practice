"""
- prprocessthe string remove space and -
- reverse the string
- store the odd numbers on their own string
- store the ven numbers on their own string
- convert the odd string numbers into numbers * 2 and substract -9 if a number is >= 10 => summ all of them
- convert the even string numbers into numbers and sum all of them
- sum all of the nubers % 10
- if total % 10 == 0 valid else not valid

"""


def verified_card_number(card_number):
    trans_table = str.maketrans({' ': '', '-':''})
    clean_card_number = card_number.translate(trans_table)
    reversed_card_number = clean_card_number[::-1] 
    # print(f'reversed_card_number: {reversed_card_number}\n')
    even_digits = reversed_card_number[1::2]
    # print(f'even_digits: {even_digits}\n')
    odd_digits = reversed_card_number[::2]
    # print(f'odd_digits: {odd_digits}\n')
    odd_sum = 0
    even_sum = 0
    for odd in odd_digits:
        odd_sum += int(odd)
    for even in even_digits:
        temp = int(even)*2
        if temp>9:
            temp = temp-9
        even_sum += temp
    total = even_sum + odd_sum
    return not(total%10)
    

def main():

    test_cases = [
    ['4111 1111 1111 1111', True],
    ['4111-1111-4555-1191', True],
    ['4539 1488 0343 6467', True],
    ['79927398713', True],
    ['79927398710', False],
    ['1234567812345670', True],
    ['0000 0000 0000 0000', True],
    ['4242 4242 4242 4242', True],
    ['1234 5678 9012 3456', False],
    ['378282246310005', True]
]
    
    for test in test_cases:
        result  = verified_card_number(test[0])
        print(f'{result == test[1]}')



main()