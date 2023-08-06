import json
import ssl

# HTTP
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

# Local import
from .utils import list_split
from .map import RouteMap

__version__ = "0.2.1"


class HTTPServerAPI(object):
    """
        HTTP Server which create a ThreadingHTTPServer.

        Documentation about Python's HTTPServer : https://docs.python.org/3/library/http.server.html
    """

    def __init__(self, host="127.0.0.1", port=8050, **options):
        """
            Constructor for the server and some options

        :param host: Host for the server. Must match the SSL if present
        :param port: Port for the server
        :param options:
                    - SSL : Bool -> Activate the SSL
                    - SSLContext : SSLContext -> Wrapper
        """
        self.host = host
        self.port = port

        # Map
        self.map = RouteMap(**options)

        # SSL
        self.ssl = options.pop("ssl", False)
        self.sslContext = options.pop("sslContext", None)

        if self.ssl and self.sslContext is None:
            self.sslContext = ssl.create_default_context()
            self.sslContext.check_hostname = False
            self.sslContext.verify_mode = ssl.CERT_NONE

        # HTTP Server
        self.rest_handler = RestHandler  # Must not be initialized
        self.rest_handler.map = self.map
        self.httpd = ThreadingHTTPServer((self.host, self.port), self.rest_handler)

    def run(self):
        """
            Start the HTTP Server

            If SSL is activated, it will wrap the socket
        """
        if self.ssl:
            self.httpd.socket = self.sslContext.wrap_socket(self.httpd.socket, server_side=True)

        print("Server is listenning on {}:{}".format(self.host, str(self.port)))
        self.httpd.serve_forever()

    def url(self, rule: str, **kwargs):
        """
            Bind a definition on a url with options

            Add method to authorize GET or both -> @http.url("/", method=['GET','POST']

            Add ** to the definition's param to handle the request content

            Here is how you can add variables in the url
                - <int:varname> : Match an int
                - <str:varname> : Match a str
                - <varname>     : Match everything

                IMPORTANT NOTE 1: if you bind /<int:var>, /<str:var> and /<var> IT WILL WORKS.
                            The third one should never be reached. In a future update, this may be solved

                IMPORTANT NOTE 2: The variable name must match with the parameters. Otherwise when the definitions will
                            be hit, it will raise a TypeError. In a future update, this may be solved


            See example.py for a basic example

        :param rule: Path or route to bind the definition on
        :param kwargs: See the SecurityWrapper, the Map or the Route for the options getters
                - Important options :
                        - method : See Route

        :return: Wrapped function
        """
        def wrapper(function):
            self.map.add_route(rule, function, **kwargs)
            return function
        return wrapper


class HTTPRequest(object):
    """
        Request Object to share to the definition

        The decorated definition MUST have a ** parameter to receive the request under **kawrgs['request']

    """

    def __init__(self):
        self.content = {}
        self.header = {}

        # Security
        self.strict = False
        self.authenticated = False
        self.secured = False


class RestHandler(BaseHTTPRequestHandler):
    """
        HTTP Handler for the HTTPServerAPI

        Contains the three methods : HEAD, GET, POST
        Following the route's method, it will execute the corresponding method

        Variables :
            - Map : Map of routes
            - server_version : The server that the header will put in. I changed it here mostly for security reasons

    """
    server_version = "HTTPServerAPI/" + __version__

    map = None

    def _set_headers(self):
        """
            Method to set default header type
        """
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        """
            Overwritten default method to handle HEAD
        """
        self._set_headers()

    # GET
    def do_GET(self):
        """
            Overwritten default method to handle GET

            Query the answer with the self.build_answer
        """
        answer = self.build_answer("GET")

        if answer is False:
            return

        # Answer the client
        self._set_headers()
        self.wfile.write(answer.encode('utf-8'))

    # POST
    def do_POST(self):
        """
            Overwritten default method to handle POST

            Query the answer with the self.build_answer
        """
        # Drop non-json query
        if self.headers['Content-Type'] != 'application/json':
            self.send_response(400)
            self.end_headers()
            return

        answer = self.build_answer("POST")

        if answer is False:
            return

        # Answer the client
        self._set_headers()
        self.wfile.write(answer.encode('utf-8'))

    def build_answer(self, method):
        """
            Find the route and build the answer returned by the Route

            The main difference between POST and GET method here is the allowed method in the route

        :return: JSON serialized in a string
                - In case of error, return False
        """
        # Convert the message to something readable
        message = json.loads(self.rfile.read(int(self.headers['content-length'])))

        route = self.map.find_matching_rule(self.path, method=method)

        # Route doesn't exist
        if route is None:
            self.send_response(404)
            self.end_headers()
            return False

        # Create HTTPRequest Object
        httpr = HTTPRequest()
        httpr.content = message
        httpr.headers = self.headers.__dict__

        # Answer
        args = list_split(self.path, route.forbidden_elements)
        answer = route.execute(args, request=httpr)

        # There is no return method in the definition
        if answer is None:
            self.send_response(500)
            self.end_headers()
            print("There is no return in the definition or the return is None")
            return False

        # The answer has returned False
        elif not answer:
            self.send_response(403)
            self.end_headers()
            return False

        # Forbidden / Unauthorized access
        if httpr.secured and not httpr.authenticated and httpr.strict:
            self.send_response(403)
            self.end_headers()
            return False

        # Reformat code if dict
        if isinstance(answer, dict):
            answer = json.dumps(answer)

        # if the final answer is not str, something went bad
        if not isinstance(answer, str):
            self.send_response(500)
            self.end_headers()
            print("The provided return must be a str or a dict")
            return False

        return answer
