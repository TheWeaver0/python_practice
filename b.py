def luhn_check(card_number):
    # Remove all non-digit characters
    digits = ''.join(filter(str.isdigit, card_number))
    
    # Check if empty or not all digits (shouldn't happen after filtering)
    if not digits or not digits.isdigit():
        return False
    
    total = 0
    reverse_digits = digits[::-1]
    
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        
        if i % 2 == 1:  # Every second digit (starting from right, index 1, 3, 5...)
            n *= 2
            if n > 9:
                n = n - 9
        total += n
    
    return total % 10 == 0, total

# Test each card number
card_data = [
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

print("Card Number".ljust(25), "Given".ljust(8), "Luhn".ljust(8), "Status".ljust(8), "Total")
print("-" * 55)

for card_number, expected in card_data:
    actual, total = luhn_check(card_number)
    status = "✓" if actual == expected else "✗"
    print(f"{card_number.ljust(25)} {str(expected).ljust(8)} {str(actual).ljust(8)} {str(status).ljust(8)} {total}")