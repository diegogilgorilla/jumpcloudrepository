from pytest_bdd import given, then, scenarios, parsers
from tests.utils.utils import Utils
import requests
import time


scenarios('../features/hash.feature')

# POST
@given(parsers.parse('I call POST hash service with "{password}" as a "{option}" password'))
def application_response(get_data, password, option):
    if option == 'alpha':
        params = {'password': password, 'format': 'json'}
    else:
        params = {'password': int(password), 'format': 'json'}

    get_data['request'] = requests.post(get_data['url'].format('hash'), json=params)
    get_data['password'] = password
    get_data['create_hash'] = True


@given(parsers.parse('I call POST hash service without password'))
def application_response_without_password(get_data):
    params = {'password': '', 'format': 'json'}
    get_data['request'] = requests.post(get_data['url'].format('hash'), json=params)
    get_data['create_hash'] = True


@then('service response a number')
def validate_response_number(get_data):
    assert get_data['request'].text is not None
    assert get_data['request'].text.isdigit()


@then('service response should response immediately')
def validate_response_seconds(get_data):
    assert (time.time() - get_data['start_time']) < 1


# GET

@given(parsers.parse('I call GET hash service for "{job_identifier}" as id'))
def application_get_hash_response(get_data, job_identifier):
    url = get_data['url'].format('hash/{}').format(job_identifier)
    get_data['request'] = requests.get(url)


@given(parsers.parse('I call GET hash service'))
def application_get_hash_response_without_id(get_data):
    url = get_data['url'].format('hash/{}').format(get_data['request'].text)
    get_data['request'] = requests.get(url)


@then('validate the hash is right encode')
def validate_response_hashcode(get_data):
    util = Utils()
    assert get_data['request'].text == util.convert_sha_512_encode(get_data['password'])


# status

@given('I call GET status service')
def application_get_status_response(get_data):
    url = get_data['url'].format('stats')
    get_data['request'] = requests.get(url)


@then('validate the response is a valid json')
def validate_status_response(get_data):
    util = Utils()
    json = util.convert_to_json(get_data['request'].text)
    assert json is not None
    assert json['TotalRequests'] >= 0
    assert json['AverageTime'] >= 0


@then('validate Total Requests')
def validate_status_response_total(get_data):
    util = Utils()
    json = util.convert_to_json(get_data['request'].text)
    assert json['TotalRequests'] == get_data['hash_numbers']


@then('validate Average Time')
def validate_status_response_average(get_data):
    util = Utils()
    json = util.convert_to_json(get_data['request'].text)
    minimum = json['TotalRequests'] * get_data['min_time']
    maximum = json['TotalRequests'] * get_data['max_time']
    assert json is not None
    assert minimum <= util.convert_millisecond_to_second(json['AverageTime']) <= maximum


@given(parsers.parse('I call POST hash service "{number}" times'))
def application_response_multiple_hash(get_data, number):
    for i in range(int(number)):
        params = {'password': 'Test' + str(i), 'format': 'json'}
        get_data['request'] = requests.post(get_data['url'].format('hash'), json=params)
        assert get_data['request'].status_code == 200
        get_data['hash_numbers'] = get_data['hash_numbers'] + 1


@given('I call POST status service')
def application_post_status_response(get_data):
    url = get_data['url'].format('stats')
    params = {'password': 'It is value', 'format': 'json'}
    get_data['request'] = requests.post(url, json=params)


@given('I call PUT status service')
def application_put_status_response(get_data):
    url = get_data['url'].format('stats')
    params = {'password': 'It is value', 'format': 'json'}
    get_data['request'] = requests.put(url, json=params)

