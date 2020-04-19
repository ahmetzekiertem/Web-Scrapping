
from xlsxwriter import Workbook     # neccessary import



# make workbook

workbook = Workbook('first_file.xlsx')



# add work sheet

worksheet = workbook.add_worksheet()


# write function - parameters - ( row,column, value )

for row in range(200):
    worksheet.write(row,0,'Row Number')
    worksheet.write(row,1,row)


# close workbook

workbook.close()
