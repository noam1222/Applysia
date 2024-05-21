import pymongo
from controller import *


# Create a new report
new_report = add_report("2024-05-19", "12:34:11", 10.5, 4, [{'x': 12.34, 'y': 56.78}, {'x': 23.45, 'y': 67.89}])

# Get all reports
all_reports = get_all_reports()
#for report in all_reports:
    #print(report.id, report.date, report.time, report.movement, report.applysia, report.trail_points)

x = get_report_by_applysnum(4)
for rep in x:
    print(rep.time)
#print(x.id)

# Delete report
#delete_report(new_report.id)




