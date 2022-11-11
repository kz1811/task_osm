import pytest
from framework.utils.json_parser import JsonParser
from framework.utils.config_parser import ConfigParser
from tests_project.files.test_data import EMAIL


@pytest.fixture(scope='function',
                params=JsonParser().get_json(ConfigParser().get_config()['search_test_data'])['tests'])
def get_search_data(request):
    if ConfigParser().get_config()['identified'] == "true":
        request.param['test_data']['email'] = EMAIL
    return request.param


@pytest.fixture(scope='function',
                params=JsonParser().get_json(ConfigParser().get_config()['reverse_test_data'])['tests'])
def get_reverse_data(request):
    if ConfigParser().get_config()['identified'] == "true":
        request.param['test_data']['email'] = EMAIL
    return request.param
