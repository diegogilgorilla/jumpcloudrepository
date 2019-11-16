import hashlib
import base64
import json


class Utils:

    """
    Method that encode a string in SHA512 and return it encode in base 64
    :param data: string to be encode to SHA512 and base 64
    return string encode in SHA512 and Base 63
    """
    @staticmethod
    def convert_sha_512_encode(data):
        return base64.b64encode(hashlib.sha512(data.encode('utf-8')).digest()).decode('UTF-8')

    """
    Method that convert a string into JSON
    :param text: string to be covert
    return JSON
    """
    @staticmethod
    def convert_to_json(text):
        try:
            return json.loads(text)
        except ValueError:
            return None

    """
    Method that convert milliseconds to seconds
    :param milliseconds: int to be convert
    return int in seconds
    """
    @staticmethod
    def convert_millisecond_to_second(milliseconds):
        return milliseconds/1000
