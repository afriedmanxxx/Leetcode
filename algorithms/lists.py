list_x = [1, 3, 5, 4, 3, 1, 1, -9, 8, -9]


def quantity_positive_sum_negative(x):
    positive = sum(1 for i in x if i > 0)
    negative = sum(i for i in x if i < 0)
    return [positive, negative] if len(x) else []


print(quantity_positive_sum_negative(list_x))


# Bubble sort
def bubble_sort(in_list):
    for i in range(len(in_list)-1, 0, -1):
        for j in range(i):
            if in_list[j] > in_list[i]:
                in_list[i], in_list[j] = in_list[j], in_list[i]
    return in_list


print(bubble_sort(in_list=list_x))


def find_pairs_and_amount(str1):
    pairs = []
    storage = list()

    new_str1 = str1.lower().replace(" ", "")
    for i in new_str1:
        if i in storage:
            storage.remove(i)
            pairs += i
        else:
            storage.append(i)
    print(f"Amount of pairs is {len(pairs)}")
    return pairs


print(find_pairs_and_amount(str1))


def return_unique_elements(x: list):
    result = []
    for i in x:
        if i in result:
            result.remove(i)
        else:
            result.append(i)
    return f"The number of unique numbers is {len(result)} and they are: {sorted(result)}"


print(return_unique_elements(list_x))


def count_pairs(x: list):
    pairs = 0
    new_x = []
    for i in x:
        if i in new_x:
            pairs += 1
            new_x.remove(i)
        else:
            new_x.append(i)
    return f"The number of pairs is {pairs}!"


print(count_pairs(list_x))







