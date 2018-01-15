import os
from cb import cb
from zipfile import ZipFile
import hashlib




class cbz(cb):

    def load_file(self):

        if not os.path.exists(self.extract_folder): os.mkdir(self.extract_folder)
        
        with ZipFile(self.file_path, 'r') as cbz:
            cbz.extractall(self.extract_folder)

        self.img_list = os.listdir(self.extract_folder)
        self.img_list.sort()

        self.index_first = 0
        self.index_last = len(self.img_list)-1
        self.index_current = self.index_first


    