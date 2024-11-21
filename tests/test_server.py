import pytest
import requests
from server import OllamaServer, determine_sentiment, count_sentiments_list

def test_ollama_localhost():
    server = OllamaServer('127.0.0.1', '11434')
    response = server.send_prompt('phi3:mini', 'What is your name?')
    assert isinstance(response, str)

def test_ollama_bad_url():
    server = OllamaServer('host.that.does.not.exist', '1326403162')
    with pytest.raises(requests.exceptions.RequestException):
        response = server.send_prompt('phi3:mini', 'What is your name?')

def test_determine_sentiment():
    mock_response = """\
The reviewer mentioned both positive and negative aspects but overall the\
review does not seem to be exactly neutral. The positive aspects seem to\
be more present than the negative aspects so the review appears to be positive."""

    expected = 'positive'
    result = determine_sentiment(mock_response)
    assert result == expected

def test_count_sentiments_list():
    mock_product = [
            'positive',
            'negative',
            'neutral',
            'positive',
            'negative',
            'negative',
            ]
    expected = {
            'Negative' : 3,
            'Positive' : 2,
            'Neutral' : 1,
            }
    results = count_sentiments_list(mock_product)
    assert results == expected
