import cProfile

square = lambda x: x * x

def sum_square(n):
    total = 0

    for i in range(n):
        total += square(i)

    return total

if __name__ == 'main':
    sum_square(5)
