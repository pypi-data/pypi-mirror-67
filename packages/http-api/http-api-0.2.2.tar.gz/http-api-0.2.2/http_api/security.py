class AbstractSecurityHTTPWrapper(object):
    """
        Abstract (should be) Security wrapper for the HTTP_API object

        => DO NOT USE THIS CLASS DIRECTLY. CHECK BasicSecurityHTTPWrapper

        The process should be quite easy to implement and modify as inheritance
        Here is what to do if you want to customize the wrapper :
            - Override check method
            - Override secure method if you want to send more datas to HTTPRequest or other object
                > Example : return the id of the user authenticated
            - Override __init__ if you want to add more options or set custom parameters


        => DO NOT USE THIS CLASS DIRECTLY. CHECK BasicSecurityHTTPWrapper

    """

    def __init__(self, **options):
        """
            Constructor with basics options. Does nothing else

        :param options:
            - strict : Immediately return 403 if set to True, if not, the wrapped function could still work
        """

        # Options
        self.strict = options.pop("strict", True)

    def check(self, *security_args):
        """
            Method to verify if the given authentication_token is valid with the implemented security (none here)

                For an example, see BasicSecurityHTTPWrapper's check method

        :param security_args: The provided token or anything to validate the user. Could be a list or dict
        :return: Return True or False
        """
        print("There is something wrong. You did not implemented 'check' method ")

        return False

    def secure(self, function):
        """
            Decorator to wrap the function to secure.

            Here nothing really happens

        :param function: Function for decorator
        :return: Wrapped function
        """

        print("There is something wrong. You did not implemented 'secure' method ")

        def wrapper(**kwargs):
            return function(**kwargs)
        return wrapper


class BasicSecurityHTTPWrapper(AbstractSecurityHTTPWrapper):

    def __init__(self, passphrase, **options):
        """
            Constructor for a with basic options for authentication purpose

        :param passphrase: passphrase or list of passphrases to valid query
        :param options:
            - auth_keyword : The keyword to search in the HTTPRequest's content as a authentication header
            - auth_method : Gives the options to
        """

        super().__init__(**options)
        self.passphrase = passphrase

        # Options
        self.auth_keyword = options.pop("auth_keyword", "token")
        self.auth_method = options.pop("auth_method", "token")  # Options pre-made -> token and list

    def check(self, security_args):
        """
            Check if the provided argument match the auth_method and the passphrase

        :param security_args: Provided authentication token
        :return: True if the authentication is valid
        """

        # One token for all authentication
        if self.auth_method == "token":
            return security_args == self.passphrase

        # List of passphrase
        elif self.auth_method == "list":
            return security_args in self.passphrase

        # Option not implemented !!
        else:
            return False

    def secure(self, function):
        """
            Decorator to wrap the function to secure.

            Get the HTTPRequest via the wrapper's kwargs and check the token given
                If something goes wrong, set the authenticated as false

        :param function: Function for decorator
        :return: Wrapped function
        """
        def wrapper(*wargs, **kwargs):
            authenticated = False

            try:
                # Check the authentication keyword
                authenticated = self.check(kwargs['request'].content[self.auth_keyword])

                # Get the HTTPRequest
                req = kwargs['request']
                req.authenticated = authenticated

                # Set the options
                kwargs['request'].strict = self.strict
                kwargs['request'].secured = True

            except:
                # If something went wrong, set as not authenticated
                kwargs['request'].authenticated = False

            if not authenticated:
                return False

            try:
                # Return the function. The only modified item is the HTTPRequest
                return function(**kwargs)
            except TypeError:
                # Return the function. This is executed when the function can't handle kwargs
                return function()



        return wrapper
