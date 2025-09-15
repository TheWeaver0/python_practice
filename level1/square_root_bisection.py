'''
- case 1
- case 0
- normal case

low
high
for max iterations

if mid = (high + low) /2
   m_2 = m**2
   abs(s - m_2) < tolerance
   we found it !
   s > m_2
   low = mid
   s < m_2
   high = mid 


'''

def square_root_bisection(number, tolerance = 1e-7, max_iterations=100):
    root = None
    if number < 0:
         raise ValueError('Square root of negative number is not defined in real numbers')
    if number == 0:
         root = 0
         print(f'square root of {number} is {root}')
    elif number == 1:
         root = 1
         print(f'square root of {number} is {root}')
    else:
         low = 0
         high = max(1, number)
         for _ in range(max_iterations):
            mid = (low + high)/2
            m_2 = mid**2
            if abs(number - m_2) < tolerance:
                root = round(mid)
            elif number > m_2:
                low = mid
            else:
                high = mid
    if root is None:
        print(f"Failed to converge within {max_iterations} iterations.")
    else:
        print(f'square root of {number} is {root}')
    return root
def main():
    N = 49
    square_root_bisection(N)

main()
