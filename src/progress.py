import json
import os

DATA_PROGRESS_FILE = "C:\\Temp\\progress.json"

class progress:
    

    def __init__(self):
        if not os.path.exists(DATA_PROGRESS_FILE): 
            self.progress = dict()

        else:

            with open(DATA_PROGRESS_FILE, "r") as f:
                content = f.read()

            if content == "": 
                self.progress = dict()
            else:
                self.progress = json.loads(content)


    def load(self, cba_md5):
        if cba_md5 in self.progress.keys():
            return self.progress[cba_md5]
        else:
            return None
        


    def save(self, cba_md5, page):
        self.progress[cba_md5] = page

        with open(DATA_PROGRESS_FILE, "w") as f:
            f.write(json.dumps(self.progress))