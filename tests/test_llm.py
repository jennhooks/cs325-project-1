import pytest
from llm import LanguageModel, Servers, UnknownServerException

def test_send_prompt():
    model = LanguageModel('phi3:mini', Servers.OLLAMA)
    response = model.send_prompt('What is your name?')
    assert isinstance(response, str)

def test_send_prompt_unknown_server():
    model = LanguageModel('phi3:mini', "hugging face")
    with pytest.raises(UnknownServerException):
        response = model.send_prompt('What is your name?')
