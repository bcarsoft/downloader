from tools.message import Message


class SingMessage:
    """Singleton Message.

    Author:
        liverp
    """

    _instance = None

    def __init__(self) -> None:
        """Construtor.
        """
        pass

    @classmethod
    def message(cls) -> Message:
        """Esse método estatico retorna ou cria uma instancia da 
        classe Message.

        Returns:
            Message: instancia de Message.
        """
        if not cls._instance:
            cls._instance = Message()
        return cls._instance
