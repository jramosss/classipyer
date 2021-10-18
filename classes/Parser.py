import os
import sys
from pandas import read_excel

class Parser:
    def __init__(self,path : str) -> None:
        self.excel_name = self.declare_path(path)

    def declare_path (self,path : str):
        ex = os.path.exists(path)
        if not ex:
            print('Invalid path!')
            sys.exit(1)
        if '.xlsx' not in path:
            print('Not an excel file!')
            sys.exit(1)
        return path

    def get_songs (self):
        excel = read_excel(self.excel_name)
        return excel.get('Song')
    
    def get_artists (self):
        excel = read_excel(self.excel_name)
        return excel.get('Artist')

