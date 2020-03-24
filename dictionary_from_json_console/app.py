from difflib import get_close_matches
import json

def search_value(str1):
    str1 = str1.lower()
    if str1 in data:
        res = data[str1]
    elif len(get_close_matches(str1, data.keys()))>0:
        print("Did you mean %s instead?" % get_close_matches(str1, data.keys())[0])
        yn = input("\nY/N? \n")
        if yn.lower() == 'y':
            res = data[get_close_matches(str1, data.keys())[0]]
        else:
            res = "We don't have this word"
    else:

        res = "We don't have this word"
    return res


data = json.load(open('data.json'))
word = input("Enter a word: ")

print(search_value(word))


