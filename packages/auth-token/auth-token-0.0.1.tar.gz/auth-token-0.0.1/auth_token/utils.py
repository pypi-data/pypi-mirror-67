
class Response:
    """Object Response

    """
    def __init__(
        self,
        status_code: int = None,
        message: str = None,
        token: str = None,
        error: list = None
            ):

        self.status_code = status_code
        self.message = message
        self.token = token
        self.error = error


class Payload:
    """Payload Response

    """
    def __init__(
        self,
        exp: int = None,
        iat: str = None,
        sub: str = None,
        uuid: str = None,
        error: str = None
            ):

        self.exp = exp
        self.iat = iat
        self.sub = sub
        self.uuid = uuid
        self.error = error
