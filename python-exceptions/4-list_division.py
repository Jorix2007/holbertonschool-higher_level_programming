#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element two lists.
    """
    new_list = []
    for i in range(list_length):
        div_result = 0
        try:
            # Attempt to perform the division
            div_result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            # Always append the result (either the quotient or 0)
            new_list.append(div_result)
    return new_list
