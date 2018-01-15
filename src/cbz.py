import os
from zipfile import ZipFile
from distutils.dir_util import remove_tree
import hashlib


extract_folder = "C:\\Temp\\cbz\\"


class cbz:

    def __init__(self, file_path):
        self.file_path     = file_path
        self.img_list      = None
        self.index_first   = None
        self.index_last    = None
        self.index_current = None
        self.ing_size      = None



    def load_file(self):

        if not os.path.exists(extract_folder): os.mkdir(extract_folder)
        
        with ZipFile(self.file_path, 'r') as cbz:
            cbz.extractall(extract_folder)

        self.img_list = os.listdir(extract_folder)
        self.img_list.sort()

        self.index_first = 0
        self.index_last = len(self.img_list)-1
        self.index_current = self.index_first


    def first_page(self):
        self.index_current = self.index_first
        
        return extract_folder + self.img_list[self.index_current]


    def last_page(self):
        self.index_current = self.index_last
        
        return extract_folder + self.img_list[self.index_current]


    def page(self, index):
        if index > self.index_first and index < self.index_last:
            self.index_current = index
            return extract_folder + self.img_list[self.index_current]


    def next_page(self):
        if self.index_current < self.index_last: self.index_current += 1

        return extract_folder + self.img_list[self.index_current]


    def previous_page(self):
        if self.index_current > self.index_first: self.index_current -= 1

        return extract_folder + self.img_list[self.index_current]


    def current_page(self):
        return extract_folder + self.img_list[self.index_current]


    def get_current_index(self):
        return self.index_current


    def get_md5(self):

        with open(self.file_path, "rb") as f:
            md5 = hashlib.md5(f.read())

        return md5.hexdigest()