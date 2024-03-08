def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot_pos = array[0]

    left = []
    right = []
    center = []
    for el in array:
        if el == pivot_pos:
            center.append(el)
        elif el < pivot_pos:
            left.append(el)
        else:
            right.append(el)
    return quick_sort(left) + center + quick_sort(right)


def finding_nums(array, p):
    sorted_arr = quick_sort(array)
    for i in range(len(sorted_arr) - 2):
        j = i + 1
        k = len(sorted_arr) - 1
        while j < k:
            if  sorted_arr[j] + sorted_arr[k] == p-array[i]:
                return True
            elif  sorted_arr[j] + sorted_arr[k] < p-array[i]:
                j += 1
            else:
                k -= 1
    return False




