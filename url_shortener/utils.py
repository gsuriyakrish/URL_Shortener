import logging
from url_shortener.core import application


# Log the logs
logging.basicConfig(filename=application.config['LOG'])


def get_logger():
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    return log


# Serializing the output data for response
def json_response(data, message, status, headers={}):
    serialized = {'status': status, 'message': message, 'response_output': data}
    headers["Content-Type"] = "application/json"
    headers["Access-Control-Allow-Origin"] = "*"
    headers["Access-Control-Allow-Credentials"] = "True"

    for key in headers.keys():
        value = headers.pop(key)
        headers[str(key)] = str(value)

    return {
        'statusCode': status,
        'headers': headers,
        'body': serialized
    }
