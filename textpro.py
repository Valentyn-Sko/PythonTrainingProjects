def sentence_marker(phrase):
    text = phrase.capitalize()
    if 'How' not in text:
        text = text + '?'
    else:
        text = text + '.'
    return text


def main():
    result = ''
    input_str = ''
    while input_str != "\end":
        input_str = input("Say something: ")
        result = result + sentence_marker(input_str) + ' '
    print(result)

main()
