from os.path import expanduser, isdir
from core.model.file import File
from core.singleton.singleton import Singleton as Sing
from core.singleton.singmessage import SingMessage as SMsg
from tools.tools import Tools
from tkinter import Tk, Frame, Label, Entry, Button
from tkinter import Spinbox, Text, messagebox
from tkinter.constants import LEFT
from tkinter.filedialog import askdirectory


class GetFile:
    """Classe Responsável pela interface 
    gráfica do projeto.

    Author:
        bcarsoft
    """

    _font_titulo = ('Arial', 18, 'bold')
    _font_normal = ('Arial', 15)
    _font_butt = ('Arial', 12)
    _back_g = '#2f2f2f'
    _file = File()
    _dir_init = expanduser('~')

    def __init__(self):
        """Construtor da Interface Gráfica.
        """
        self.window = Tk()
        self.window.minsize(640, 512)
        self.window.title('Downloader')
        self.window['bg'] = self._back_g

        self.title_frame = Frame(self.window)
        self.title_frame['bg'] = self._back_g
        self.title_frame.pack()

        self.label_title = Label(self.title_frame)
        self.label_title['font'] = self._font_titulo
        self.label_title['text'] = 'Get Files from Internet'
        self.label_title['fg'] = '#ffffff'
        self.label_title['bg'] = self._back_g
        self.label_title.pack(pady=10)

        self.link_frame = Frame(self.window)
        self.link_frame['bg'] = self._back_g
        self.link_frame.pack()

        self.label_link = Label(self.link_frame)
        self.label_link['font'] = self._font_normal
        self.label_link['bg'] = self._back_g
        self.label_link['fg'] = '#ffffff'
        self.label_link['text'] = 'Link URL*'
        self.label_link.pack()

        self.entry_link = Entry(self.link_frame)
        self.entry_link['width'] = 50
        self.entry_link['font'] = self._font_normal
        self.entry_link.bind('<Button-1>', self.clear_url)
        self.entry_link.pack()

        self.way_frame = Frame(self.window)
        self.way_frame['bg'] = self._back_g
        self.way_frame.pack()

        self.label_way = Label(self.way_frame)
        self.label_way['text'] = 'Select Directory*'
        self.label_way['fg'] = '#ffffff'
        self.label_way['bg'] = self._back_g
        self.label_way['font'] = self._font_normal
        self.label_way.pack()

        self.entry_way = Entry(self.way_frame)
        self.entry_way['font'] = self._font_normal
        self.entry_way['width'] = 43
        self.entry_way.pack(side=LEFT)

        self.butt_way = Button(self.way_frame)
        self.butt_way['font'] = self._font_butt
        self.butt_way['text'] = 'Select'
        self.butt_way['width'] = 6
        self.butt_way['fg'] = '#ffffff'
        self.butt_way['bg'] = '#d40003'
        self.butt_way.bind('<Button-1>', self.get_folder)
        self.butt_way.pack(side=LEFT)

        self.spn_frame = Frame(self.window)
        self.spn_frame['bg'] = self._back_g
        self.spn_frame.pack()

        self.label_spiner = Label(self.spn_frame)
        self.label_spiner['text'] = 'How Many Files* '
        self.label_spiner['font'] = self._font_normal
        self.label_spiner['fg'] = '#ffffff'
        self.label_spiner['bg'] = self._back_g
        self.label_spiner.pack(side=LEFT)

        self.spiner_files = Spinbox(self.spn_frame)
        self.spiner_files['width'] = 5
        self.spiner_files['values'] = tuple(i for i in range(123))
        self.spiner_files['font'] = self._font_normal
        self.spiner_files.pack(side=LEFT)

        self.label_digits = Label(self.spn_frame)
        self.label_digits['font'] = self._font_normal
        self.label_digits['text'] = ' Digits '
        self.label_digits['bg'] = self._back_g
        self.label_digits['fg'] = '#ffffff'
        self.label_digits.pack(side=LEFT)

        self.spiner_digits = Spinbox(self.spn_frame)
        self.spiner_digits['font'] = self._font_normal
        self.spiner_digits['width'] = 5
        self.spiner_digits['values'] = tuple(i for i in range(1, 8))
        self.spiner_digits.pack(side=LEFT)

        self.label_init = Label(self.spn_frame)
        self.label_init['font'] = self._font_normal
        self.label_init['bg'] = self._back_g
        self.label_init['fg'] = '#ffffff'
        self.label_init['text'] = ' From '
        self.label_init.pack(side=LEFT)

        self.spiner_from = Spinbox(self.spn_frame)
        self.spiner_from['font'] = self._font_normal
        self.spiner_from['values'] = tuple(i for i in range(123))
        self.spiner_from['width'] = 5
        self.spiner_from.pack(side=LEFT)

        self.files_frame = Frame(self.window)
        self.files_frame['bg'] = self._back_g
        self.files_frame.pack()

        self.label_files = Label(self.files_frame)
        self.label_files['font'] = self._font_normal
        self.label_files['text'] = 'Files Downloaded'
        self.label_files['fg'] = '#ffffff'
        self.label_files['bg'] = self._back_g
        self.label_files.pack()

        self.text_files = Text(self.files_frame)
        self.text_files['width'] = 61
        self.text_files['font'] = self._font_butt
        self.text_files['fg'] = '#2c5e9a'
        self.text_files['height'] = 10
        self.text_files['bd'] = 2
        self.text_files.pack()

        self.down_frame = Frame(self.window)
        self.down_frame['bg'] = self._back_g
        self.down_frame.pack()

        self.butt_down = Button(self.down_frame)
        self.butt_down['font'] = self._font_butt
        self.butt_down['text'] = 'Make Download'
        self.butt_down['width'] = 15
        self.butt_down['fg'] = '#ffffff'
        self.butt_down['bg'] = '#2c5e9a'
        self.butt_down.bind('<Button-1>', self.make_download)
        self.butt_down.pack(pady=30)

        self.window.mainloop()

    def get_folder(self, evt):
        """Pega o caminho da pasta.

        Args:
            evt (event): evento do mouse - botão 1.
        """
        road = self.entry_way.get()
        directory = askdirectory(
            initialdir=self._dir_init if not isdir(road) else road
        )
        self.entry_way.delete(0, 'end')
        self.entry_way.insert(0, directory)

    def clear_url(self, evt):
        """Limpa entry de URL.

        Args:
            evt (event): evento do mouse - botão 1.
        """
        self.entry_link.delete(0, 'end')

    def make_download(self, evt):
        """Tenta realizar o download requeido.

        Args:
            evt (event): evento do mouse - botão 1.
        """
        self.file.quantity = int(self.spiner_files.get())
        self.text_files.delete('1.0', 'end')
        if self.file.quantity < 1:
            messagebox.showwarning(title='Problem with size',
                                   message='File\'s number invalid, it must be great than 0')
            return
        if self.file.quantity < int(self.spiner_from.get()):
            messagebox.showwarning(title='Problem with first file',
                                   message='File\'s initial must be smaller than quantity')
            return
        self.file.link = self.entry_link.get()
        self.file.way = self.entry_way.get()
        # extra
        digits = int(self.spiner_digits.get())
        from_t = int(self.spiner_from.get())
        self.file.quantity += 1 if from_t > 0 else 0
        # extra File
        arquivo = File()
        arquivo.quantity = self.file.quantity
        self.file.way = Tools.join_dirs(
            dir_1=self.file.way, dir_2=Tools.get_name(self.file.link))
        # downloading and inserts to Text
        for i in range(from_t, self.file.quantity):
            try:
                zeros = digits - str(i).__len__()
                arquivo.link = self.file.link.format(zeros * '0' + str(i))
                arquivo.way = self.file.way.format(zeros * '0' + str(i))
                self.text_files.insert(f'{i}.0', arquivo.way + '\n')
                downloaded = Sing.get_service().validate_file(file=arquivo)
                if not downloaded:
                    messagebox.showerror(
                        title='It found an error',
                        message=SMsg.message().msg
                    )
                    return
            except Exception as ex:
                messagebox.showerror(
                    title='Excepction Found',
                    message=str(ex) + '\n' + arquivo.way
                )
                return
        else:
            messagebox.showinfo(
                title='Success', message='All Files Downloaded!')

    @property
    def file(self):
        return self._file
