class Tools:
    """Classe com metodos de classe responsáveis 
    por formatar os nomes dos arquivos, e juntar-los 
    ao caminho de diretórios.

    Author:
        bcarsoft
    """

    @classmethod
    def get_name(cls, name) -> str:
        """Metodo de classe para retirar o nome do arquivo 
        de uma URL.

        Args:
            name (str): o link url para retirar o nome.

        Returns:
            str: o nome retirado.
        """
        if not name:
            return name
        name = list(name)
        name.reverse()
        for i in range(name.__len__()):
            if name[i] == '/':
                break
        name = name[: i]
        name.reverse()
        return ''.join(i for i in name)

    @classmethod
    def join_dirs(cls, dir_1, dir_2) -> str:
        """Esse metódo junta o caminho de diretório 
        ao arquivo a ser baixado.

        Args:
            dir_1 (str): diretório.
            dir_2 (str): nome do arquivo.

        Returns:
            str: caminho do arquivo.
        """
        if not dir_1 or not dir_2:
            return dir_1
        dir_1 += '/' + dir_2 if not dir_1[-1] == '/' else dir_2
        return dir_1
