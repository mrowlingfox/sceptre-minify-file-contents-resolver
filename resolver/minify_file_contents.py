from sceptre.resolvers import Resolver

class MinifyFileContents(Resolver):
    """
    Resolver for the contents of a file.
    :param argument: Absolute path to file.
    :type argument: str
    """

    def __init__(self, *args, **kwargs):
        super(MinifyFileContents, self).__init__(*args, **kwargs)

    def resolve(self):
        """
        Retrieves the contents of a file at a given absolute file path.
        :returns: Contents of file.
        :rtype: str
        """
        try:
            with open(self.argument, "r") as file:
                return file.read()
        except (EnvironmentError, TypeError) as e:
            raise e
