import requests
from core.model.file import File


class Download:
    """Onde é feito o Download.

    Author:
        bcarsoft
    """

    @classmethod
    def make_download(cls, file: File) -> bool:
        """Esse metodo de classe retorna o método
        que realiza o download do arquivo.

        Args:
            file (File): parametro de arquivo a ser enviado
            para download.

        Returns:
            bool: True se o arquivo foi baixado.
        """
        return cls._get_file(url=file.link, ende=file.way)

    @classmethod
    def _get_file(cls, url: str, ende: str) -> bool:
        """Esse metodo privado de classe realiza de fato o 
        download do arquivo.

        Args:
            url (str): link do arquivo a ser baixado.
            ende (str): caminho do arquivo.

        Returns:
            bool: True se o arquivo foi baixado.
        """
        resposta = requests.get(url)
        if resposta.status_code == requests.codes.OK:
            with open(ende, 'wb') as novo_arquivo:
                novo_arquivo.write(resposta.content)
            return True
        else:
            resposta.raise_for_status()
            return False
