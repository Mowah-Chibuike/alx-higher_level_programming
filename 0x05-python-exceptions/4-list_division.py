#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    n = 0
    result = []
    try:
        for i in range(list_length):
            try:
                result.append(my_list_1[i] / my_list_2[i])
                n += 1
            except TypeError:
                print("wrong type")
                result.append(0)
                n += 1
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
                n += 1
    except IndexError:
        print("out of range")
        for i in range(n, list_length):
            result.append(0)
    except Exception:
        pass
    finally:
        return result
