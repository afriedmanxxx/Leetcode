str1 = " Hello my name is   Bob"


# add list to dict with amount letter repeat
def list_elements_to_dict_with_letter_count(in_str):
    dict = {}
    for l in in_str.lower().replace(" ", ''):
        if l not in dict:
            dict[l] = 1
        else:
            dict[l] += 1
    print(dict)
    top2 = (sorted(dict.values(), reverse=True))[:2]
    print(top2)
    for l, n in dict.items():
        if n in top2:
            print(f"letter \"{l}\" repeats {n} times and it's top repeated.")
    return dict


print(list_elements_to_dict_with_letter_count(str1))


