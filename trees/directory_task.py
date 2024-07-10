class Directory:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None

    def __len__(self):
        return len(self.children)


class File:
    def __init__(self, name, data):
        self.name = name
        self.parent = None
        self.data = data

    def __len__(self):
        return len(self.data)


class FileSystem:
    def __init__(self):
        self.root = Directory('/')
        self.current_directory = self.root
        self.files_count = 0

    def create_directory(self, name):
        """
        Vytvori novy adresar v aktualnom adresari.
        """
        directory = Directory(name)
        directory.parent = self.current_directory
        self.current_directory.children.append(directory)

    def create_file(self, name, data):
        """
        Vytvori novy subor v aktualnom adresari.
        """
        # TODO

    def delete_node(self, name):
        """
        Vymaze subor/adresar v aktualnom adresari podla mena.
        Ak neexistuje, metoda vyhodi FileNotFoundError
        """
        # TODO

    def get_children(self):
        """
        Vrati zoznam vsetkych suborov a priecinkov v aktualnom adresari
        """
        return self.current_directory.children

    def list_files(self):
        """
        Sprava sa podobne ako `ls` na unixovych systemoch

        Vypise pod seba vsetky subory a priecinky v aktualnom adresari.
        Pri kazdom je napisane, ci ide o subor alebo adresar.
        Vypis je zoradeny podla atributu name.
        """
        # TODO

    def choose_directory(self, path):
        """
        Sprava sa ako `cd` na unixovych systemoch.

        Vstupi do adresara specifikovany cestou `path`. Ak cesta zacina znakom '/', cesta je
        absolutna, v opacnom pripade relativna. Rozdiel medzi nimi je vysvetleny napriklad
        v tomto kratkom texte https://www.otrekal.info/linux/cesty-v-linuxe/. Su tam vysvetlene aj
        priecinky '.' a '..', ktore som spominal aj na kruzku.
        Mozete ocakavat korektnu path.
        """
        if path.startswith('/'):
            self.current_directory = self.root

        for dirname in path.split('/'):
            if dirname:
                self.choose_directory_one_level(dirname)

    def choose_directory_one_level(self, dirname):
        """
        Vstupi do jedneho adresara
        """
        if dirname == '.':
            return
        if dirname == '..':
            if self.current_directory != self.root:
                self.current_directory = self.current_directory.parent
            return

        for node in self.current_directory.children:
            if node.name == dirname:
                self.current_directory = node
                return

        raise FileNotFoundError

    def print_working_directory(self):
        """
        Sprava sa ako `pwd` na unixovych systemoch.

        Vypise absolutnu cestu ku `self.current_directory` vratane. Zaciatok je v '/' a
        adresare su oddelene '/'.
        """
        result = []
        current_node = self.current_directory
        while current_node is not None:
            result.append(current_node.name)
            current_node = current_node.parent

        return '/'.join(reversed(result))[1:]

    def print_tree(self, root=True):
        """
        Sprava sa podobne ako prikaz `tree`.
        Vypise stromovu strukturu suboroveho systemu.
        Ak je root=True, vypise cely suborovy system,
        inak iba podstrom od aktualneho adresara.
        """
        # print('/' if root or self.current_directory == self.root else '.')
        self.print_tree_rec(self.root if root else self.current_directory, 0)

    def print_tree_rec(self, node, indent, spacing=' '*3):
        print(node.name)
        if isinstance(node, File):
            return
        for i, child in enumerate(node.children):
            print(('│' + spacing) * indent, end='')
            print('└──' if i == len(node.children) - 1 else '├──', end=' ')
            self.print_tree_rec(child, indent + 1, spacing)


# Demo
if __name__ == '__main__':
    fs = FileSystem()
    fs.create_directory('d1')
    fs.create_directory('d2')
    fs.create_file('a', 'hello world')
    fs.choose_directory('d1')
    fs.create_file('b', ['ff', 'gg', 'hh'])
    fs.create_file('c', 42)
    fs.choose_directory('..')
    fs.choose_directory('d2')
    fs.create_directory('d3')
    fs.choose_directory('/')
    fs.create_file('d', not False)
    fs.choose_directory('/d2/d3')
    print(fs.print_working_directory())
    fs.choose_directory(fs.print_working_directory())  # should do nothing
    fs.list_files()
    fs.choose_directory('..')
    fs.create_file('e', True)
    fs.list_files()
    fs.print_tree()
    fs.list_files()
    fs.print_tree(root=False)
    fs.choose_directory('..')
    fs.delete_node('d2')
    fs.delete_node('a')
    fs.print_tree(root=False)
