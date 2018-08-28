class Error(Exception):
    """ Base class for all the application related errors
    """

    pass

    def __init__(self, message, code):
        """ Constructs an application error

        Args:
            message (str): The message of the error
            code (int): A numeric code for the error

        Returns:
            new Error

        Raises:
            None
        """

        self.message = message
        self.code = code

    def __str__(self):
        return "Error [E" + str(self.code) + "]: " + self.message


class LoginNotFound(Error):
    """ Raised if the log in form in the udemy site is not available

        Raise of this error usually means that the Udemy Website changed and the
        bot is no longer compatible, so a patch should be made.
    """

    def __init__(self, message):
        """ Constructs a new LoginNotFoundError

        Args:
            message (str): The message for the error

        Returns:
            new LoginNotFound

        Raises:
            None
        """

        super().__init__(message, 1)

class LoginError(Error):
    """ Raised if the login was not successfully made

        Raise of this error means that the login credentials are invalid    
    """

    def __init__(self, message):
        """ Constructs a new LoginError

        Args:
            message (str): The message for the error

        Returns:
            new LoginError

        Raises:
            None
        """

        super().__init__(message, 2)