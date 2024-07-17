with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    lowered_content = file_contents.lower()

    words = file_contents.split()

    word_count = len(words)

    char_dict = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }

for char in lowered_content:
    if char.isalpha():
        char_dict[char] += 1

list_of_dicts = [{key: value} for key, value in char_dict.items()]        

sorted_list_of_dicts = []

while list_of_dicts:
    max_value = -1
    max_dict = None
    for d in list_of_dicts:
        value = list(d.values())[0]
        if value > max_value:
            max_value = value
            max_dict = d
    sorted_list_of_dicts.append(max_dict)
    list_of_dicts.remove(max_dict)


print("--- Begin report of books/frankenstein.txt ---")   
print(f"{word_count} words found in the document")
print()
for item in sorted_list_of_dicts:
    char = list(item.keys())[0]
    count = list(item.values())[0]
    print(f"The '{char}' character was found {count} times")
print("--- End report ---")   