import pytest
import time
from pytest_bdd import when, then, parsers

LOCAL_HOST = 'http://127.0.0.1:8088/{}'
DATA = {}
MINIMUM_TIME = 5
MAXIMUM_TIME = 5.4
PORT = 'PORT=8088'


@pytest.fixture
def get_data():
    return DATA


def pytest_runtest_setup():
    DATA['url'] = LOCAL_HOST


def pytest_bdd_before_scenario(request, feature, scenario):
    if scenario.name == 'I want to validate the hash service response immediately':
        DATA['start_time'] = time.time()
    elif scenario.name == 'I want to create a hash with alphanumeric password':
        DATA['hash_numbers'] = 0
        DATA['create_hash'] = False
    elif scenario.name == 'I want to validate the hash service response immediately' or \
            scenario.name == 'I want to validate the fields in the stats response':
        DATA['min_time'] = MINIMUM_TIME
        DATA['max_time'] = MAXIMUM_TIME


def pytest_bdd_after_scenario(request, feature, scenario):
    print('')


@when(parsers.parse('the response status code is "{code}"'))
def when_validate_status_code(get_data, code):
    try:
        condition = get_data['create_hash']
        if condition:
            get_data['hash_numbers'] = get_data['hash_numbers'] + 1
            get_data['create_hash'] = False
        assert get_data['request'].status_code == int(code)
    except Exception:
        assert get_data['request'].status_code == int(code)


@then(parsers.parse('the response status code is "{code}"'))
def then_validate_status_code(get_data, code):
    try:
        condition = get_data['create_hash']
        if condition:
            get_data['hash_numbers'] = get_data['hash_numbers'] + 1
            get_data['create_hash'] = False
        assert get_data['request'].status_code == int(code)
    except Exception:
        assert get_data['request'].status_code == int(code)
