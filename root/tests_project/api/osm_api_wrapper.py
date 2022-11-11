from urllib.parse import quote_plus
from framework.api.client_api import ClientApi
from tests_project.steps.steps import Steps
from framework.exceptions.exceptions import KeyIsNotPresentedException
from tests_project.files.test_data import STRUCTURED_SEARCH_PARAMS


class OSMAPIWrapper(ClientApi):

    search_url = '/search?'
    reverse_url = '/reverse?'

    def simple_search(self, params):
        """simple search by free-form string"""

        # # Удаляем лишние параметры структурированного запроса, если они есть
        # # Кодом можно пренебречь, так как присутствие параметра q обнуляет параметры структурированного запроса
        # for param in STRUCTURED_SEARCH_PARAMS:
        #     if params.get(param) is not None:
        #         params.pop(param)

        query_param = params.pop('q')
        url = self.search_url + f"q={quote_plus(query_param)}&"
        url = Steps().add_parameters(url, params)

        response = self.send_get_request(endpoint=url, )

        return response

    def structured_search(self, params):
        """Structured search by parameters 'street', 'city', 'county', 'state', 'country', 'postalcode'."""

        if params.get('q') is not None:
            params.pop('q')

        if set(params.keys()).isdisjoint(set(STRUCTURED_SEARCH_PARAMS)):
            raise KeyIsNotPresentedException('Parameters for structured search was not presented')

        url = Steps().add_parameters(self.search_url, params)

        response = self.send_get_request(endpoint=url, )
        return response

    def reverse_search(self, params):
        """Reverse search by latitude and longitude"""

        if (params.get('lat') is None) or (params.get('lon') is None):
            raise KeyIsNotPresentedException('Required parameter is not presented.')

        url = Steps().add_parameters(self.reverse_url, params)
        response = self.send_get_request(endpoint=url, )

        return response
