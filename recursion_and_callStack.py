"""
Recursion(遞迴) := A Function that calls itself... until is doesn't

e.g.
def open_box(): 
    if ball: 
        return ball
    open_box()
"""
# ======================================================================

"""
call stack(函式依序呼叫)
"""
# e.g. call func1時，會依序執行func3 -> func2 -> func1
def func3(): 
    print("three")

def func2(): 
    func3()
    print("two")

def func1(): 
    func2()
    print("one")

func1()
# ======================================================================
"""
factorial
"""
def factorial(n): 
    if n == 1: 
        return 1
    return n * factorial(n-1)

fac = factorial(5)
print(fac)