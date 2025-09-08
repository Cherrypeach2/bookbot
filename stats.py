def get_num_words(text):
    return len(text.split())

def get_chars_dict(text):
    chars = {}
    lower_case_text = text.lower()
    
    for c in lower_case_text:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
        
    return chars

# Sort Key
def sort_on(items):
    return items["num"]

def get_sorted_char_list(items):
    sorted_list = []
    for char in items:
        character = char
        count = items[char]
        sorted_list.append({"char": character, "num": count})
    
    sorted_list.sort(reverse=True, key=sort_on)
        
    return sorted_list