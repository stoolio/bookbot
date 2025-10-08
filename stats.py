def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    for char in text:
        lchar = char.lower()
        if lchar in char_count:
            char_count[lchar] += 1
        else:
            char_count[lchar] = 1
    return char_count

def sort_on_num(item):
    return item["num"]

def sort_char_count(char_count):
    chars = []
    for char in char_count:
        chars.append({"name": char, "num":char_count[char]})
    chars.sort(reverse=True, key=sort_on_num)
    return chars