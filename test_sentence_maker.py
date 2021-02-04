from sentence_maker import make_sentence


def test_with_one_word():
    input = 'this'
    words = ('this', 'is', 'basket', 'ball', 'basketball',
             'play', 'player', 'a', 'game', 'for')

    result = make_sentence(input=input, words=words)
    assert result == 'this'


def test_with_one_match_per_word():
    input = 'thisisasentence'
    words = ('this', 'is', 'basket', 'ball', 'basketball',
             'play', 'player', 'a', 'game', 'sentence')

    result = make_sentence(input=input, words=words)
    assert result == 'this is a sentence'


def test_with_multi_match_per_word():
    input = 'thisisasentenceforbasketballplayers'
    words = ('this', 'is', 'basket', 'ball', 'basketball',
             'play', 'sentence', 'players', 'a', 'game', 'for')

    result = make_sentence(input=input, words=words)
    assert result == 'this is a sentence for basketball players'
