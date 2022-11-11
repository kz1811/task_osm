import pytest
from tests_project.api.osm_api_wrapper import OSMAPIWrapper
from tests_project.steps.steps import Steps


class TestOSM:

    @pytest.mark.search
    def test_search(self, get_search_data):

        search_data = get_search_data['test_data']
        expected_data = get_search_data['expected']

        if 'q' in search_data.keys():
            response = OSMAPIWrapper().simple_search(search_data)
        else:
            response = OSMAPIWrapper().structured_search(search_data)

        assert Steps().is_response_valid(response, search_data, expected_data), f'Response contains wrong data'

    @pytest.mark.reverse
    def test_reverse_search(self, get_reverse_data):

        search_data = get_reverse_data['test_data']
        expected_data = get_reverse_data['expected']

        response = OSMAPIWrapper().reverse_search(search_data)

        assert Steps().is_response_valid(response, search_data, expected_data), \
            f'Response contains wrong data'
