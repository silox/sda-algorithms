def foo(x, array=None):
    if array is None:
        array = []
    array.append(x)
    print(array)


foo(10)  # [10]
foo(20)  # [20]
