from os import environ

from docker_env import get_environment

def test_variable_value():
    environ['VARIABLE'] = 'test_content'
    assert get_environment('VARIABLE') == 'test_content'

def test_file_variable(tmp_path):
    file_path = tmp_path.joinpath('test_file')
    file = file_path.open(mode='w', encoding='utf-8')
    file.write('test_content')
    file.close()
    environ['TEST_FILE'] = str(file_path.absolute())
    assert get_environment('TEST') == 'test_content'

def test_default():
    assert get_environment('DOES_NOT_EXIST', 'default') == 'default'

def test_value_precedence_over_file(tmp_path):
    file_path = tmp_path.joinpath('test_file')
    file = file_path.open(mode='w', encoding='utf-8')
    file.write('file_content')
    file.close()
    environ['PRECEDENCE'] = 'variable_content'
    assert get_environment('PRECEDENCE') == 'variable_content'

def test_file_custom_encoding(tmp_path):
    file_path = tmp_path.joinpath('test_file')
    file = file_path.open(mode='w', encoding='utf-32')
    file.write('test_content_with_🌍')
    file.close()
    environ['ENCODING_FILE'] = str(file_path.absolute())
    assert get_environment('ENCODING', encoding='utf-32') == 'test_content_with_🌍'
