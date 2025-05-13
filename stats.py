def word_count(text):
    word_conjunction = text.split()
    return len(word_conjunction)

def count_characters(text):
    characters = {}
    for c in text:
        word_lower = c.lower()
        if word_lower in characters:
            characters[word_lower] += 1
        else:
            characters[word_lower] = 1
    return characters

def sort_on(dict):
    return dict["num"]

def sorted_report(dict):
    list = []
    for key, value in dict:
        temp = [key,value]
        list.append(temp)
    return list.sort(reverse=True, key=sort_on)
