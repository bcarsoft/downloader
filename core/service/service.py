from core.model.file import File
from core.downloder.download import Download as DLoad
from core.singleton.singmessage import SingMessage as SMsg


class Service:
    """Regra de Negócio, onde os parametros do 
    arquivo são testados.

    Author:
        bcarsoft
    """

    def __init__(self):
        """Novo Service.
        """
        pass

    def validate_file(self, file: File) -> bool:
        """Esse método verifica se de fato o arquivo pode
        ser considerado válido para ser baixado.

        Args:
            file (File): instancia de file.

        Returns:
            bool: True se o arquivo foi baixado.
        """
        if not isinstance(file.link, str):
            SMsg.message().msg = 'Instance of link must be str'
            return False
        elif not isinstance(file.way, str):
            SMsg.message().msg = 'Instance of way must be str'
            return False
        elif not isinstance(file.quantity, int):
            SMsg.message().msg = 'Instance of quantity must be int'
            return False
        elif file.quantity < 1:
            SMsg.message().msg = 'Invalid quantity'
            return False
        elif not file.way or not file.link:
            SMsg.message().msg = 'Invalid link or directory'
            return False
        return DLoad.make_download(file=file)
