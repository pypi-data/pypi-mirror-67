import time, datetime

from .server import HTTPServerAPI
from .security import BasicSecurityHTTPWrapper

import json

http = HTTPServerAPI()
security = BasicSecurityHTTPWrapper("U5GH7KL00HEA")

received_data = []

@http.url("/")
def index():
    # Example of data to send
    urlList = ['/', '/validate_account', '/send', '/send/secured']
    serverVersion = "v1"
    servertime = datetime.datetime.now().strftime("%H:%M:%S.%f %d/%m/%Y")

    answer = {
        "urls": urlList,
        "server_version": serverVersion,
        "server_time": servertime
    }

    # The answer can be a dict
    return answer


@http.url("/validate_account/<account>", method=['GET'])
def validate_account(account, **kwargs):  # -> ** to get the request object
    # Example of accounts id
    valid_account = ['487', '880', '198']

    try:
        if account in valid_account:
            message = "Valid account"
        else:
            raise

    except:
        message = "Invalid account"

    # The answer can be a str too
    return json.dumps(message)

@http.url("/send")
def send_unsecure(**kwargs):
    """
        Here the query don't need to be identified

    """

    # Fetch the request
    req = kwargs['request']

    print("Is the url secured ? " + str(req.secured))
    print("Is the client authenticated ? " + str(req.authenticated))
    print("Here is the payload :" + str(req.content))
    req.content.pop("token", None) # Remove token
    received_data.append(req.content)

    print("Current received data : " + str(received_data))

    # Return smth
    return json.dumps({"received": True})


@http.url("/send/secured")
@security.secure
def send_secure(**kwargs):
    """
        Here the query must be identified with a token passphrase equal to "U5GH7KL00HEA"
    """

    # Fetch the request
    req = kwargs['request']

    print("Is the url secured ? " + str(req.secured))
    print("Is the client authenticated ? " + str(req.authenticated))
    print("Here is the payload :" + str(req.content))
    req.content.pop("token", None)  # Remove token
    received_data.append(req.content)

    print("Current received data : " + str(received_data))

    # Return smth
    return json.dumps({"received": True})


http.run()



"""

    Client side :
    
import request # librairy pip install request

r = request.post("http://127.0.0.1:8005/")
r.content  # -> Content received

r = request.post("http://127.0.0.1:8005/validate_account/123")
# 404 error because we post

r = request.get("http://127.0.0.1:8005/validate_account/123")
r.content  # -> Invalid account

r = request.get("http://127.0.0.1:8005/validate_account/880")
r.content  # -> Valid account

r = request.post("http://127.0.0.1:8005/send", json={"hereisakey":"hereisamessage"})
r.content  # -> {"received": true}

r = request.post("http://127.0.0.1:8005/send/secured", json={"hereisakey":"hereisamessage"})
# 403 error -> We don't have "token" key with the U5GH7KL00HEA passphrase

r = request.post("http://127.0.0.1:8005/send/secured", json={"token":"U5GH7KL00HEA", "hereisakey":"hereisamessage"})
r.content  # -> {"received": true}

r = request.post("http://127.0.0.1:8005/send/secured", json={"token":"NotTheGoodKey", "hereisakey":"hereisamessage"})
# 403 error -> The key is wrong

"""
