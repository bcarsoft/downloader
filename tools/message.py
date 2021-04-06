class Message:

    def __init__(self):
        self._msg = ''

    @property
    def msg(self) -> str:
        return self._msg

    @msg.setter
    def msg(self, msg: str) -> None:
        self._msg = msg
