def get_num_words(s):
    return len(s.split())


def get_num_characters(s):
    num_characters = {}
    for char in s:
        char = char.lower()
        if char in num_characters:
            num_characters[char] += 1
        else:
            num_characters[char] = 1
    return num_characters


def sort_on(dict):
    return dict["num"]


def get_sorted_list(dict):
    sorted_list = []
    for k in dict:
        sorted_list.append({"char": k, "num": dict[k]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
