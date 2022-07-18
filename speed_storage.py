import numpy as np
import datetime
import csv

class speed_storage:
    def __init__(self,file_name:str,entries_before_write:int=1):
        self._initialized_at = self.get_current_time()
        self._last_ran = None
        self._file_name = file_name
        self._entries_before_write = entries_before_write
        self._dl_list = []
        self._ul_list = []
    
    def get_current_time(self)->str:
        now = datetime.datetime.now()
        current_time = now.strftime("%d/%m/%Y %H:%M:%S")
        return current_time

    @property
    def last_ran(self):
        return self._last_ran

    @last_ran.setter
    def last_ran(self,time:str)->None:
        self._last_ran = time

    @property
    def initalized_at(self):
        return self._initialized_at

    @property
    def filename(self)->str:
        return self._file_name
    
    @filename.setter
    def filename(self,name:str)->None:
        self._file_name = name

    @property
    def entries_before_write(self):
        return self._entries_before_write

    @entries_before_write.setter
    def entries_before_write(self,var:int)->None:
        if var > 0:
            self._entries_before_write=var

    @property
    def downloads(self)->list:
        return self._dl_list

    def add_download(self,value:float)->None:
        self._dl_list.append(value)

    @property
    def uploads(self)->list:
        return self._ul_list

    def add_upload(self,value:float)->None:
        self._ul_list.append(value)

    def save_data(self,download:float,upload:float)->None:
        self.add_download(download)
        self.add_upload(upload)
        self.last_ran = self.get_current_time()
        self._save_check()

    def _purge(self):
        self._dl_list = []
        self._ul_list = []

    def _save_check(self):
        if len(self.downloads) >= self.entries_before_write and len(self.uploads) >= self.entries_before_write:
            try:
                with open(self.filename,"r") as rfile:
                    reader = csv.reader(rfile)
                    rows = []
                    for row in reader:
                        if row:
                            rows.append(row)
                    head = rows[0]
                    downloads = rows[1] + self.downloads
                    uploads = rows[2] + self.uploads
            except FileNotFoundError:
                head = self.initalized_at
                downloads = self.downloads
                uploads = self.uploads
            tail = self.last_ran
            with open(self.filename,"w") as wfile:
                writer = csv.writer(wfile)
                writer.writerows((head,downloads,uploads,tail))
            self._purge()
