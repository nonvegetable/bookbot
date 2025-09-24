def no_of_words(text):
    num_words = text.split()
    print(f"Found {len(num_words)} total words")

def no_of_characters(text):
    characters = text.lower()
    freq = {}
    for c in characters:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    return freq

def sort_on(items):
    return items["num"]

def chars_dict_to_sorted_items(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num":num_chars_dict[ch]})
        sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list