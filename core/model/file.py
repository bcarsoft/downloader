class File:
    """Modelo de arquivo que será baixado.

    Author:
        bcarsoft
    """

    def __init__(self):
        """Construtor.
        """
        self._link = ''
        self._way = ''
        self._quantity = ''

    @property
    def link(self) -> str:
        return self._link

    @link.setter
    def link(self, link: str) -> None:
        self._link = link

    @property
    def way(self) -> str:
        return self._way

    @way.setter
    def way(self, way: str) -> None:
        self._way = way

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int) -> None:
        self._quantity = quantity
