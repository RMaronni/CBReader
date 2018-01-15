import os
from cb import cb
from zipfile import ZipFile
import hashlib


extract_folder = "C:\\Temp\\cbz\\"


class cbz(cb):

    def load_file(self):

        if not os.path.exists(extract_folder): os.mkdir(extract_folder)
        
        with ZipFile(self.file_path, 'r') as cbz:
            cbz.extractall(extract_folder)

        self.img_list = os.listdir(extract_folder)
        self.img_list.sort()

        self.index_first = 0
        self.index_last = len(self.img_list)-1
        self.index_current = self.index_first


    