import pytest
import graph

def test_organize_sentiment_data():
    mock_versions = ['product1', 'product2']
    mock_product1 = [
            'positive',
            'negative',
            'neutral',
            'positive',
            'negative',
            'negative',
            ]
    mock_product2 = [
            'negative',
            'negative',
            'neutral',
            'positive',
            ]
    mock_sentiments_dict = { 
                            'product1' : mock_product1,
                            'product2' : mock_product2,
                            }

    expected = {
            'Negative' : [3, 2],
            'Positive' : [2, 1],
            'Neutral' : [1, 1],
            }

    results = graph.organize_sentiment_data(mock_sentiments_dict, mock_versions)

    assert results == expected
