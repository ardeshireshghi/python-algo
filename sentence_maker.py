def make_sentence(input, words):
    current_word = ''
    result = []

    for char in input:
        current_word = f'{current_word}{char}'
        found_word_match = False

        if len(result) > 0 and f'{result[-1]}{current_word}' in words:
            result[-1] = f'{result[-1]}{current_word}'
            found_word_match = True
        elif current_word in words:
            result.append(current_word)
            found_word_match = True

        current_word = '' if found_word_match else current_word
    return ' '.join(result)
