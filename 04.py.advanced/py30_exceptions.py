try:
    5/0
except ZeroDivisionError:
    print('No division by zero!')


while True:
    try:
        x = int(input('Enter your age: '))
    except ValueError:
        print('Oops! That was no valid number. Try again...')
    else:
        print('carry on!')
        break


raise ValueError('some error message')


try:
    raise KeyboardInterrupt
except:
    print('oops')
finally:
    print('all done')
