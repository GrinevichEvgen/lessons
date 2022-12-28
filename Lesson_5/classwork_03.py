def my_func(*args, func_type):
    if func_type == "min":
        return min(args)

    elif func_type == "max":

        return max(args)

    raise "Unknown function"

print(my_func(1,2,3,4,5, func_type="min"))

