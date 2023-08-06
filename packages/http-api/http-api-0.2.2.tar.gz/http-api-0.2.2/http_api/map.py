import re

# Local import
from .utils import rule_to_regex


class RouteMap(object):
    """
        Map which contains the available routes

    """

    def __init__(self, **options):
        """
            Constructor for the route Map

        :param options:
            - ignorecase : Ignorecase for the matchign rules
        """
        self.routes = []

        self.ignorecase = options.pop("ignorecase", False)
        assert isinstance(self.ignorecase, bool)

    def add_route(self, rule: str, function, **kwargs) -> (Exception, bool):
        """
            Add a route to the RouteMap. This method check if the regex doesn't exist already


        :param rule: The path of the route which we be accessed
        :param function: The function which will be executed
        :param kwargs: Options mostly
        :return: True if working as intended
        """

        assert isinstance(rule, str)

        if not rule.startswith("/"):
            raise ValueError("Url must start with a leading slash")

        regex, args, forbidden = rule_to_regex(rule)
        route = Route(rule, regex, args, forbidden, function, **kwargs)

        if self.find_matching_rule(route.regex, route.method) is not None:
            raise Exception("The rule already exist with this method")

        if len(args) != function.__code__.co_argcount:
            raise Exception("Arguments provided don't match")

        self.routes.append(Route(rule, regex, args, forbidden, function, **kwargs))

        return True

    def find_matching_rule(self, query, method="POST"):
        """
            Find and return the path matching a route

        :param query: The rule/path
        :param method: If we look for post or get route
        :return: A Route object or None
        """
        for r in self.routes:

            if self.ignorecase:
                if bool(re.search(r.regex, query, re.IGNORECASE)):
                    if method in r.method:
                        return r
            else:
                if bool(re.search(r.regex, query)):
                    if method in r.method:
                        return r
        return None

    def __repr__(self):

        routes = ""
        for r in self.routes:
            routes += r.__repr__() + ", "

        return "RouteMap({})[{}]".format(len(self.routes), routes[:-1])


class Route(object):
    """
        Route Object containing informations about the URL

    """

    def __init__(self, rule: str, regex: str, arguments: list, forbidden_elements: list, function, **options):
        """
            Constructor of the Route. Contains some cehkup values

        :param rule: The rule/path
        :param regex: The regex which match the rule/path
        :param arguments: The arguments of the definitions and path
        :param forbidden_elements: A list to make the split easier when returning args
        :param function: The function that the route will execute
        :param options:
                    - method=[''] => List containing GET or/and POST to prevent one of thoses (or none) for accessing
                                    the url
        """
        self.rule = rule
        self.function = function

        self.regex = regex
        self.arguments = arguments  # Order provided by the rule
        self.forbidden_elements = forbidden_elements

        self.function_argscount = function.__code__.co_argcount
        self.function_arguments = list(function.__code__.co_varnames)  # Order coded in the function

        # Options
        self.method = options.pop("method", ['POST'])

    def execute(self, args, **kwargs):
        """
            Execute the function of the Route

        :param args: The function's arguments. Raise assert if the definition doesn't match the given params in rule
        :param kwargs: Params to pass to the function. HTTPRequest is one of thoses
        :return: The output of the definition which will be returned to the RestHandler
        """
        # Right amount of args
        assert len(args) == self.function_argscount

        # Order arguments
        wargs = []

        if self.arguments == self.function_arguments:
            wargs = args
        else:
            for x in self.function_arguments:
                for y in self.arguments:
                    if x == y:
                        wargs.append(args[self.arguments.index(y)])

        if not isinstance(wargs, tuple):
            wargs = tuple(wargs)

        try:
            output = self.function(*wargs, **kwargs)
        except TypeError:
            output = self.function(*wargs)

        if output is None or not output:
            # The query has been dropped
            return False

        return output

    def __repr__(self):
        return "Route(\"{}\")".format(self.rule)




