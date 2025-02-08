def function_with_uncommon_error(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

result = function_with_uncommon_error(0, 0)
print(result) # This will cause a ZeroDivisionError if the caller doesn't handle the edge case