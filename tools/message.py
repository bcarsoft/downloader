class Message:
    """Classe que recebe mensagens que 
    serão exibidas em algum dos métodos do modulo
    messagebox.

    Author:
        bcarsoft
    """

    def __init__(self):
        """Construtor.
        """
        self._msg = ''

    @property
    def msg(self) -> str:
        return self._msg

    @msg.setter
    def msg(self, msg: str) -> None:
        self._msg = msg
