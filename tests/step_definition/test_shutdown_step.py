from pytest_bdd import given, scenarios
import requests


scenarios('../features/shutdown.feature')


@given('I call POST shutdown service')
def application_put_status_response(get_data):
    url = get_data['url'].format('hash')
    get_data['request'] = requests.post(url, data='shutdown')
