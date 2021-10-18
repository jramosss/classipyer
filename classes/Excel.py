from typing import List
import xlsxwriter as xl
from xlsxwriter import worksheet

from classes.Song import Song


class Excel:
    def __init__(self,filename : str) -> None:
        self.name = filename
        self.last_cell = 0
        self.last_column = 0

    def insert_column (self,name : str,values,col : int):
        wb = xl.Workbook(self.name)
        ws = wb.add_worksheet()
        ws.write(0,col,name)
        index = 1
        for v in values:
            ws.write(index,col,v)
            index += 1

        wb.close()


    def insert_songs (self,songs_data : List[Song]):
        wb = xl.Workbook(self.name)
        ws = wb.add_worksheet()
        ws.write(0,0,'Artist')
        ws.write(0,1,'Song')
        ws.write(0,2,'Decade')
        row = 1
        for song in songs_data:
            ws.write(row,0,song.artist)
            ws.write(row,1,song.name)
            ws.write(row,2,song.release_date)
            row += 1

        wb.close()




