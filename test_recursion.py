def test_rec(x):
    if x == 1:
        return 1
    else:
        return x * test_rec(x -1)
