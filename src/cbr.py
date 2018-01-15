import os
from rarfile import RarFile
from cb import cb


class cbr(cb):

    def load_file(self):

        if not os.path.exists(extract_folder): os.mkdir(extract_folder)
        
        with RarFile(self.file_path, 'r') as cbr:
            cbr.extractall(extract_folder)

        self.img_list = os.listdir(extract_folder)
        self.img_list.sort()

        self.index_first = 0
        self.index_last = len(self.img_list)-1
        self.index_current = self.index_first