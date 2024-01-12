from twttr import shorten

def test_shorten():
    assert shorten('twitter') == 'twttr'
    assert shorten('TwitteR') == 'TwttR'
    assert shorten('TwItteR') == 'TwttR'
    assert shorten('twitter?') == 'twttr?'
    assert shorten('twitter.,2') == 'twttr.,2'