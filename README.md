# downloader
Get files from internet.

# funcionalidades
Com esse programa, é possível realizar o download de vários 
arquivos da internet, seja música, vídeo ou imagem. Basta que 
o usuário forneça:

* link url - endereço do arquivo na rede;
* caminho da pasta onde ficará o arquivo; 
* quantidade - número de arquivos a serem baixados;
* digitos (se for sequência númerica);
* inicio - no caso de haver sequência, de onde ela começa;

# requerimentos
Aqui a sequência de requerimentos para o funcionamento dessa 
aplicação:

* Python3.x. - [download Python](https://www.python.org)
* Requests - com pip instalado, digite: pip3 install requests
* Tkinter - GUI padrão do Python:
    * distros derivadas debian: sudo apt-get install python3-tk
    * distros derivadas fedora: sudo dnf install python3-tkinter

# imagens
A aparência do programa inicialmente:

![aparencia inicial]()

Como fica após o download realizado:

![download realizado]()

# notas
Ele possuí um testador de exceções e um singleton para mensagem, 
onde, uma vez instanciado, pode ser acessado a parti de outra classe.
