import hashlib
from tempfile import mkdtemp
from distutils.dir_util import remove_tree



class cb:

    def __init__(self, file_path):
        self.file_path      = file_path
        self.extract_folder = mkdtemp() + "\\"
        self.img_list       = None
        self.index_first    = None
        self.index_last     = None
        self.index_current  = None
        self.ing_size       = None

        print("CB file: " + self.file_path)
        print("Temp img location: " + self.extract_folder)


    def first_page(self):
        self.index_current = self.index_first
        
        return self.extract_folder + self.img_list[self.index_current]


    def last_page(self):
        self.index_current = self.index_last
        
        return self.extract_folder + self.img_list[self.index_current]


    def page(self, index):
        if index > self.index_first and index < self.index_last:
            self.index_current = index
            return self.extract_folder + self.img_list[self.index_current]


    def next_page(self):
        if self.index_current < self.index_last: self.index_current += 1

        return self.extract_folder + self.img_list[self.index_current]


    def previous_page(self):
        if self.index_current > self.index_first: self.index_current -= 1

        return self.extract_folder + self.img_list[self.index_current]


    def current_page(self):
        return self.extract_folder + self.img_list[self.index_current]


    def get_current_index(self):
        return self.index_current


    def get_md5(self):

        with open(self.file_path, "rb") as f:
            md5 = hashlib.md5(f.read())

        return md5.hexdigest()


    def close(self):
        remove_tree(self.extract_folder, True)
