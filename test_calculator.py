from calculator import add

def test_add():
    result1 = add(2, 3)
    result2 = add(-1, 1)
    print(result1)  # should print 5
    print(result2)  # should print 0
    try:
        add('2', 3)
    except TypeError as e:
        print(e)  # should print error message

test_add()

