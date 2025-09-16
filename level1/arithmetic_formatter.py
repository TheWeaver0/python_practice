def arithmetic_arranger(problems, show_answers=False):
    line1 = line2 = line3 = line4 = ''
    if len(problems) > 5:
        return 'Error: Too many problems.'

    for idx, problem in enumerate(problems):
        if problem.find('+') != -1:
            op = '+'
            pos = problem.find('+')
            a = problem[:pos-1]
            b = problem[pos+2:]
            if a.isdigit() and b.isdigit(): 
                a = int(problem[:pos-1])
                b = int(problem[pos+2:])
            else:
                return 'Error: Numbers must only contain digits.'
          
            result = a + b
        elif problem.find('-') != -1:
            op = '-'
            pos = problem.find('-')
            a = problem[:pos-1]
            b = problem[pos+2:]
            if a.isdigit() and b.isdigit(): 
                a = int(problem[:pos-1])
                b = int(problem[pos+2:])
            else:
                return 'Error: Numbers must only contain digits.'
          
            result = a - b
        else:
          return "Error: Operator must be '+' or '-'."     
        len_result = max(len(str(a)), len(str(b))) + 2
        if len_result > 6:
            return 'Error: Numbers cannot be more than four digits.'
        
        line1 += ''.join([' ' for i in range(len_result - len(str(a)))]) + str(a)
        
        if idx != len(problems)-1:
            line1 +=  ''.join([' ' for i in range(4)])
        line2 += op+''.join([' ' for i in range(len_result - len(str(b))-1)]) + str(b) 

        if idx != len(problems)-1:
            line2 +=  ''.join([' ' for i in range(4)])

        line3 += ''.join(['-' for i in range(len_result)])

        if idx != len(problems)-1:
            line3 +=  ''.join([' ' for i in range(4)])

        line4 += ''.join([' ' for i in range(len_result - len(str(result)))]) + str(result)

        if idx != len(problems)-1:
            line4 +=  ''.join([' ' for i in range(4)])

    if show_answers:
        problems = line1+'\n'+line2+'\n'+line3+'\n'+line4
    else:
        problems = line1+'\n'+line2+'\n'+line3
    return problems

print(arithmetic_arranger(["3801 - 2", "123 + 49"]))