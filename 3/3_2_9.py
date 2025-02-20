def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"
    print('test abs1 pass')

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"
    print('test abs2 pass')

if __name__ == "__main__":
    test_abs2()
    test_abs1()
    print("Everything passed")