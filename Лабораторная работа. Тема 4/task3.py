def delete(list_, index=None):
    if index is None:
        result_list = list_[:-1]
    else:
        list_before = list_[:index]
        list_after = list_[index+1:]
        result_list = list_before + list_after
    return result_list


print(delete([0, 0, 1, 2], index=0))  # [0, 1, 2]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2, 3]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3, 4]
