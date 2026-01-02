def get_book_word_count(texts):

    words = texts.split()
    return len(words)

def get_char_count (texts):

    lower_char = texts.lower()
    char_count = {}
    for ch in lower_char:
         if ch not in char_count:
              char_count[ch] = 1
         else:
              char_count[ch] += 1
    return char_count

def sort_char (item):
    return item["num"]
def chars_dict_to_sorted_list(char_count):
     result = []
     for ch in char_count:
          result.append({"char": ch, "num": char_count[ch]})
     result.sort(reverse=True, key=sort_char)
     return result