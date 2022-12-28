def sun_and_max(*args):
    my_sum = 0
    my_min = [0]

    for element in args:
            my_sum += element
            if element < my_min:
                my_min = element
                return my_sum, my_min
