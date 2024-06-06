import pymongo
from controller import *

from mongoengine import connect
result = connect(db="applysias", host="mongodb://localhost:27017/")
print(result)

# Create a new report
delete_reports_by_applysia(3)
delete_reports_by_applysia(4)
delete_reports_by_applysia(9)
delete_reports_by_applysia(6)
delete_reports_by_applysia(2)

#new_rep = add_report("27/05/24", "13:00", 6, [{"x": i * 0.05, "y": i} for i in range(120)], [i for i in range(12)])
#new_rep = add_report("27/05/24", "14:00", 4, [{"x": i * 0.05, "y": i} for i in range(120)], [i+2 for i in range(12)])
#new_rep = add_report("27/05/24", "15:00", 2, [{"x": i * 0.05, "y": i} for i in range(120)], [i+4 for i in range(12)])


new_rep = add_report("27/05/24", "13:00", 3, [{"x": i * 0.05, "y": i} for i in range(120)], [i for i in range(12)])
new_rep = add_report("27/05/24", "14:00", 3, [{"x": i * 0.05, "y": i} for i in range(120)], [i+1 for i in range(12)])
new_rep = add_report("27/05/24", "12:00", 3, [{"x": i * 0.05, "y": i} for i in range(120)], [i for i in range(12)])
new_rep = add_report("27/05/24", "16:00", 3, [{"x": i * 0.05, "y": i} for i in range(120)], [i + 1 for i in range(12)])
new_rep = add_report("27/05/24", "20:00", 3, [{"x": i * 0.05, "y": i} for i in range(120)], [i for i in range(12)])

new_rep = add_report("27/05/24", "12:00", 4, [{"x": i * 0.05, "y": i} for i in range(120)], [i for i in range(12)])
new_rep = add_report("27/05/24", "13:00", 4, [{"x": i * 0.05, "y": i} for i in range(120)], [i for i in range(12)])
new_rep = add_report("27/05/24", "14:00", 4, [{"x": i * 0.05, "y": i} for i in range(120)], [i+1 for i in range(12)])
new_rep = add_report("27/05/24", "15:00", 4, [{"x": i * 0.05, "y": i} for i in range(120)], [i for i in range(12)])
new_rep = add_report("27/05/24", "16:00", 4, [{"x": i * 0.05, "y": i} for i in range(120)], [i+2 for i in range(12)])

new_rep = add_report("27/05/24", "12:00", 9, [{"x": i * 0.05, "y": i} for i in range(120)], [i for i in range(12)])
new_rep = add_report("27/05/24", "13:00", 9, [{"x": i * 0.05, "y": i} for i in range(120)], [i for i in range(12)])
new_rep = add_report("27/05/24", "14:00", 9, [{"x": i * 0.05, "y": i} for i in range(120)], [i+1 for i in range(12)])
new_rep = add_report("27/05/24", "15:00", 9, [{"x": i * 0.05, "y": i} for i in range(120)], [i-1 for i in range(12)])
new_rep = add_report("27/05/24", "16:00", 9, [{"x": i * 0.05, "y": i} for i in range(120)], [i for i in range(12)])


x = get_average_report_of_all("27/05/24", "12:00", "16:00")
print(x)
# Get all reports
#all_reports = get_all_reports()
#for report in all_reports:
    #print(report.id, report.date, report.time, report.movement, report.applysia, report.trail_points)
#y = get_all_reports()
#print(y)
#x = get_filtered_reports("2024-05-11","12:34:00", "12:34:13", 12, False)
#print(x)

#print(x.id)