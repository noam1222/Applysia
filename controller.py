import json
from reportModel import Report
from mongoengine import connect
import matplotlib.pyplot as plt


def add_report(date, time, movement, applysia, trail_points, movement_array):
    report = Report(
        date=date,
        time=time,
        movement=movement,
        applysia=applysia,
        trail_points=trail_points,
        movement_every_five=movement_array
    )
    report.save()
    return report

#print(add_report("afafafaf", "test2", 4.5, 2, [{'x': 1, 'y': 2}, {'x': 3, 'y': 4}, {'x': 5, 'y': 6}]))

# returns cursor with all reports, to access individually iterate over cursor
def get_all_reports():
    reports = Report.objects()
    return [report.to_mongo().to_dict() for report in reports]

# receives 2 strings as input representing date + time, returns cursor
def get_report_by_date_and_time(date, time):
    reports = Report.objects(date=date, time=time)
    return [report.to_mongo().to_dict() for report in reports]

def get_filtered_reports(date, start, end, movement, geq):
    """first filter reports by given date"""
    reports = Report.objects(date=date)

    """filter reports by time range"""
    reports = reports.filter(time__gte=start, time__lte=end)

    """filter reports by movement field"""
    if geq:
        reports = reports.filter(movement__gte=movement)
    else:
        reports = reports.filter(movement__lte=movement)

    return [report.to_mongo().to_dict() for report in reports]



# receives string input representing wanted date, returns cursor
def get_report_by_date(date):
    reports = Report.objects(date=date)
    return [report.to_mongo().to_dict() for report in reports]


# receives string! input representing wanted time
def get_report_by_time(time):
    reports = Report.objects(time=time)
    return [report.to_mongo().to_dict() for report in reports]


# receives int!, returns info on wanted applysia
def get_report_by_applysnum(num):
    reports = Report.objects(applysia=num)
    return [report.to_mongo().to_dict() for report in reports]

# return reports that is an average of ALL aplysias
def get_average_report_of_all(date, time):
    reports = get_report_by_date_and_time(date, time)

    if not reports:
        return json.dumps({})

    total_movement = 0
    movement_every_five_min_totals = [0] * 12
    trail_points = []

    # Calculate the total movement and sum of each index in movement_every_five_min
    for report in reports:
        total_movement += report['movement']

        for i, value in enumerate(report['movement_every_five']):
            movement_every_five_min_totals[i] += value

        # Convert trail_points to arrays of integers
        #the inner arrarys are arrays of tuples
        trail_points.extend([[[float(point['x']), float(point['y'])] for point in report['trail_points']]])

    # Calculate averages
    average_movement = total_movement / len(reports)
    average_movement_every_five_min = [total / len(reports) for total in movement_every_five_min_totals]

    # Create the average report dictionary
    average_report = {
        "date": date,
        "time": time,
        "movement": average_movement,
        "trail_points": trail_points,
        "movement_every_five_min": average_movement_every_five_min
    }

    return average_report


def delete_reports_by_date(date):
    reports_to_delete = Report.objects(date=date)
    reports_to_delete.delete()


# returns num of deleted items, deletes all reports of applysia #num
def delete_reports_by_applysia(num):
    reports_to_delete = Report.objects(applysia=num)
    reports_to_delete.delete()


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