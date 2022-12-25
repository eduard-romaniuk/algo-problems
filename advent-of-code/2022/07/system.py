class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return f'f {self.name} {self.size}'


class Dir(File):
    def __init__(self, name, parent=None):
        super().__init__(name, 0)
        self.parent = parent
        self.dirs = {}
        self.files = {}

    def get_dir(self, name):
        if name == '.':
            return self
        if name == '..':
            return self.parent
        return self.dirs[name]

    def add_size(self, size):
        self.size += size
        if self.parent is not None:
            self.parent.add_size(size)

    def _add(self, system_object, collection):
        collection[system_object.name] = system_object
        self.add_size(system_object.size)

    def add_dir(self, directory):
        self._add(directory, self.dirs)

    def add_file(self, file):
        self._add(file, self.files)

    def __str__(self):
        return f'd {self.name} {self.size}'


def sizes(directory: Dir):
    res = [directory.size]
    for d in directory.dirs.values():
        res.extend(sizes(d))
    return res
