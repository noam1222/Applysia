from reportModel import Report
from mongoengine import connect
import matplotlib.pyplot as plt

mydict = {"date": "ababababa", "time": "Highway 37", "applysia": int("3"), "movement": float("4.3"),
          "trail_points": [(1, 2), (1, 1), (1, 3)]}

def add_report(date, time, movement, applysia, trail_points):
    report = Report(
        date=date,
        time=time,
        movement=movement,
        applysia=applysia,
        trail_points=trail_points
    )
    report.save()
    return report

#print(add_report("afafafaf", "test2", 4.5, 2, [{'x': 1, 'y': 2}, {'x': 3, 'y': 4}, {'x': 5, 'y': 6}]))

# returns cursor with all reports, to access individually iterate over cursor
def get_all_reports():
    return Report.objects()

# receives 2 strings as input representing date + time, returns cursor
def get_report_by_date_and_time(date, time):
    return Report.objects(date-date, time=time)


# receives string input representing wanted date, returns cursor
def get_report_by_date(date):
    return Report.objects(date=date)


# receives string! input representing wanted time
def get_report_by_time(time):
    return Report.objects(time=time)


# receives int!, returns info on wanted applysia
def get_report_by_applysnum(num):
    return Report.objects(applysia=num)


def delete_reports_by_date(date):
    reports_to_delete = Report.objects(date=date)
    reports_to_delete.delete()


# returns num of deleted items, deletes all reports of applysia #num
def delete_reports_by_applysia(num):
    reports_to_delete = Report.objects(applysia=num)
    reports_to_delete.delete()

delete_reports_by_applysia(2)


def delete_unique_report(date, time):
    reports_to_delete = Report.objects(date=date, time=time)
    reports_to_delete.delete()

# if we want a function that deletes the whole collection of reports
# def delete_reports():

#given array of points, get a trail of movement
def plot_trail(points):
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    plt.plot(x, y, marker='o', linestyle='-')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Trail of Points')
    plt.grid(True)
    plt.show()

# Example usage:
#points = [(1, 2), (3, 4), (5, 6), (7, 8)]
#plot_trail(points)