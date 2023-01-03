def three_args(var1, var2,var3):
    res_dict = locals()
    print(*(f'{key} = {value}' for key, value in res_dict.items() if value))

three_args(1, 20, 55)