import pymongo
from controller import *


# Create a new report
delete_reports_by_applysia(4)
new_report = add_report("2024-05-11", "12:34:11", 10.5, 4, [{'x': 12.34, 'y': 56.78}, {'x': 23.45, 'y': 67.89}], [3, 4])
new_report = add_report("2024-05-11", "12:34:13", 11.5, 4, [{'x': 12.34, 'y': 56.78}, {'x': 23.45, 'y': 67.89}], [1, 2])

# Get all reports
#all_reports = get_all_reports()
#for report in all_reports:
    #print(report.id, report.date, report.time, report.movement, report.applysia, report.trail_points)
#y = get_all_reports()
#print(y)
x = get_filtered_reports("2024-05-11","12:34:00", "12:34:13", 12, False)
print(x)

#print(x.id)






