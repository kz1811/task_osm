import xml.parsers.expat
from urllib.parse import quote_plus
from framework.exceptions.exceptions import WrongValueException, WrongFormatException
import xmltodict
import json


class Steps:

    def add_parameters(self, url, params):

        for i in params.keys():
            if quote_plus(i) != i:
                raise WrongValueException(f'Parameter should contains latin letters only; got {i} instead.')

            url += f"{i}={quote_plus(params[i])}&"

        return url[:-1]

    def get_search_response_data(self, format_type, response):

        if format_type in ['json', 'jsonv2']:
            try:
                result = json.loads(response.content)
                if type(result) == dict:
                    result = [result, ]
            except json.decoder.JSONDecodeError:
                raise WrongFormatException(f'Response format does not meet the requirement; should be {format_type}')

        elif format_type == 'xml':
            try:
                result = xmltodict.parse(response.content, attr_prefix='')['searchresults']['place']
                if type(result) == dict:
                    result = [result, ]
            except xml.parsers.expat.ExpatError:
                raise WrongFormatException(f'Response format does not meet the requirement; should be {format_type}')

        else:
            if format_type in ['geojson', 'geocodejson']:
                raise RuntimeError(f'Format {format_type} does not supported')
            else:
                raise WrongValueException(f"{response.json()['error']['message']}")

        return result

    def is_response_valid(self, response, params, expected_data):

        resp_format = params.get('format')
        if resp_format is None:
            resp_format = 'xml'

        data = self.get_search_response_data(format_type=resp_format, response=response)

        if type(expected_data) == dict:
            expected_data = [expected_data, ]

        limit = len(data)
        if (limit is not None) and (len(expected_data) > limit):
            return False
        else:
            for i in range(len(expected_data)):
                for param in expected_data[i].keys():
                    if str(expected_data[i][param]) != str(data[i].get(param)):
                        return False

        return True

