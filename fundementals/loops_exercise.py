def break_statement():
    for i in "Python":
        if i == 'h':
            break
        print('Current letter:', i)

    var = 10
    while var > 0:
        var = var - 1
        if var == 5:
            break
        print('Current value is:', var)


def continue_statement():
    for i in "Python":
        if i == 'h':
            continue
        print('Current letter:', i)

    var = 10
    while var > 0:
        var = var - 1
        if var == 5:
            continue
        print('Current value is:', var)


def pass_statement():
    for i in "Python":
        if i == 'h':
            pass
            print('This is pass block')
        print('Current letter:', i)


def else_clause():
    for num in range(10, 20):
        for i in range(2, num):
            if num % i == 0:
                j = num / i
                print('{} equals {} * {}'.format(num, i, j))
                break
        else:
            print(num, 'is a prime number')

    count = 0
    while count < 5:
        print(count)
        count += 1
    else:
        print('it reaches its limit')
