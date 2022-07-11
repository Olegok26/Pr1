def function(x):
    if x < 0:
        return x
    else:
        return x * 2


def main():
    for i in range(-5, 10):
        y = function(i)
        print('function(', i, ') = ', y, sep='')


main()


print()


def print_info(object_name, color, price):
    print('Object:', object_name, sep='\t')
    print('Color:', color, sep='\t')
    print('Price:', price, sep='\t')
    print()


print_info('pen', 'blue', 1)

print_info(object_name='pen',
           color='blue',
           price=1)


print_info(price=5, object_name='cup', color='orange')

print_info('coffee', price=10, color='black')