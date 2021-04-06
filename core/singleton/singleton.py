from core.service.service import Service


class Singleton:
    """Singleton para o Service do projeto.

    Author:
        bcarsoft
    """

    _instance = None

    def __init__(self):
        """Construtor.
        """
        pass

    @classmethod
    def get_service(cls) -> Service:
        """Esse metodo de classe retorna ou 
        cria uma nova instancia de service.

        Returns:
            Service: instancia de Service.
        """
        if not cls._instance:
            cls._instance = Service()
        return cls._instance
