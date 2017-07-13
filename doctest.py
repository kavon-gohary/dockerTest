"""
This is the module docstring pylint wants
"""
def cycle_length(n: int) -> int:
    assert n > 0
    c = 1
    pay = "jay"
    while n >1:
        if (n % 2) == 0:
            n = (n // 2)
        else:
            n = (3 * n) + 1
        c += 1
    assert c > 0

    return pay


print(cycle_length(5))
