import pytest
import serialize

def test_list_to_file(tmp_path):
    test_list = ['apple', 'pear', 'pineapple']
    test_file = tmp_path / 'list_to_file.txt'
    serialize.list_to_file(test_file, test_list)

    results = []
    with open(test_file, 'r') as file:
        for line in file:
            results.append(line)
    expected = ['apple\n', 'pear\n', 'pineapple\n']
    assert results == expected

def test_list_from_file(tmp_path):
    expected = ['green', 'blue', 'red']
    test_file = tmp_path / 'list_from_file.txt'
    with open(test_file, 'w') as file:
        for item in expected:
            file.write(f"{item}\n")

    results = serialize.list_from_file(test_file)
    assert results == expected

def test_dict_from_file(tmp_path):
    prefixes = ['ccc', 'ddd']
    expected = {
            'ccc' : ['h', 'i', 'j'],
            'ddd' : ['k', 'l', 'm'],
            }
    mock_file1 = tmp_path / 'ccc test.txt'
    with open(mock_file1, 'w') as file:
        file.write('h\ni\nj\n')
    mock_file2 = tmp_path / 'ddd test.txt'
    with open(mock_file2, 'w') as file:
        file.write('k\nl\nm\n')

    results = serialize.dict_from_file(prefixes, 'test', tmp_path)
    assert results == expected

def test_dict_to_file(tmp_path):
    test_dict = {
            'aaa' : ['q', 'r', 's'],
            'bbb' : ['t', 'u', 'v'],
            }
    serialize.dict_to_file(test_dict, 'test', tmp_path)

    expected_file1 = ['q\n', 'r\n', 's\n']
    expected_file2 = ['t\n', 'u\n', 'v\n']

    results_file1 = []
    with open(tmp_path / 'aaa test.txt') as file:
        for line in file:
            results_file1.append(line)
    results_file2 = []
    with open(tmp_path / 'bbb test.txt') as file:
        for line in file:
            results_file2.append(line)

    assert results_file1 == expected_file1
    assert results_file2 == expected_file2
