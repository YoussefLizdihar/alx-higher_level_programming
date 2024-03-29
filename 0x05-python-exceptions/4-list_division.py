#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    r = []
    R = 0
    for i in range(list_length):
        try:
            R = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            R = 0
        except ZeroDivisionError:
            print("division by 0")
            R = 0
        except (TypeError, ValueError):
            print("wrong type")
            R = 0
        finally:
            r.append(R)
    return r
