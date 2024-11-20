import pytest
from server import OllamaServer

def test_ollama_localhost():
    server = OllamaServer('127.0.0.1', '11434')
    response = server.send_prompt('phi3:mini', 'What is your name?')
    assert isinstance(response, str)
