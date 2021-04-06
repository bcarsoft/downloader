import requests
from core.model.file import File


class Download:
    """Onde é feito o Download.

    Author:
        bcarsoft
    """

    @classmethod
    def make_download(cls, file: File) -> bool:
        return cls._get_file(url=file.link, ende=file.way)

    @classmethod
    def _get_file(cls, url: str, ende: str):
        resposta = requests.get(url)
        if resposta.status_code == requests.codes.OK:
            with open(ende, 'wb') as novo_arquivo:
                novo_arquivo.write(resposta.content)
            return True
        else:
            resposta.raise_for_status()
            return False
