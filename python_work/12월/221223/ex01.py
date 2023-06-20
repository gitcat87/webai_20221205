from mywork import MyWorkBook

mwb = MyWorkBook()



cnt =input("몇 행으로 출력하시겠습니까?")
cnt = int(cnt)+1

mwb.setCnt(cnt)
mwb.doSave()
mwb.doLoad()


from openpyxl import Workbook, load_workbook



