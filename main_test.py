"""
Unit test
"""
import main


def add_test():
    """Unit test function"""
    var1 = 3
    var2 = 3
    result = main.add(var1, var2)
    if result == 6:
        verified = True
    else:
        verified = not True

    return verified


print(add_test())
