def user_input_range(n, ll):
    for i in range(n + 1):
        ll.append(i)
    return ll


def which_comp(n, ll):
    comp = None
    if n == 1:
        comp = [i for i in ll]
        print(comp)
    elif n == 2:
        comp = "set_comp"
    elif n == 3:
        comp = "dict_comp"
    return comp


ll = user_input_range(5, [])
which_comp(1, ll)
