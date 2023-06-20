import urllib.request
from openpyxl import Workbook

class product:
    def __init__(self,name,imgsrc,price,filename):
        self.name = name
        self.imgsrc= imgsrc
        self.price = price
        self.filename = filename
        
        print('imgsrc',self.imgsrc)
        print(f"{self.filename}.jpg")
        
        
        urllib.request.urletrieve(imgsrc,f"{name}.jpg")
        
    def doMakeExcel(self):
        print("아직...")