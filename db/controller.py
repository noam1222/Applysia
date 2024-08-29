import json
from datetime import datetime, timedelta

from .reportModel import Report
from mongoengine import connect
import matplotlib.pyplot as plt
import numpy as np


def _get_time_formatted(date, time):
    return datetime.strptime(f"{date} {time}", "%d/%m/%y %H:%M")

def add_report(date, time, applysia, movement, trail_points, movement_array):
    time_format = _get_time_formatted(date, time)
    report = Report(
        date=date,
        time=time_format,
        movement=movement,
        applysia=applysia,
        trail_points=trail_points,
        movement_every_five=movement_array
    )
    report.save()
    return report


# returns cursor with all reports, to access individually iterate over cursor
def get_all_reports():
    reports = Report.objects()
    return [report.to_mongo().to_dict() for report in reports]

# receives 2 strings as input representing date + time, returns cursor
def get_report_by_date_and_time(date, time):
    time_format = _get_time_formatted(date, time)
    reports = Report.objects(date=date, time=time_format).order_by('applysia')

    reports_list = [report.to_mongo().to_dict() for report in reports]
    if len(reports_list) == 0:
        return []

    average_report = get_average_report_of_all(date, time)

    reports_list.insert(0, average_report)

    return reports_list

def get_filtered_reports(date, start, end, movement, geq):

    """first filter reports by given date"""
    reports = Report.objects(date=date)

    """filter reports by movement field"""
    if geq:
        reports = reports.filter(movement__gte=movement)
    else:
        reports = reports.filter(movement__lte=movement)

    """sort by applysia num"""
    reports = reports.order_by('time')

    """filter reports by time range"""
    time_format = "%H:%M"
    start_time = datetime.strptime(start, time_format)
    end_time = datetime.strptime(end, time_format)
    reports = [report for report in reports if start_time.hour <= report.time.hour <= end_time.hour]

    av_report = get_average_report_of_all(date, start, end)

    reports_list = [report.to_mongo().to_dict() for report in reports]
    reports_list.insert(0, av_report)

    return reports_list



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

# given cursor of reports of certain hour, returns average report of that hour
def calc_average_of_hour(date, time,reports_cursor):

    total_movement = 0
    movement_every_five_min_totals = [0] * 12
    trail_points = []

    # Calculate the total movement and sum of each index in movement_every_five_min
    for report in reports_cursor:
        total_movement += report['movement']

        for i, value in enumerate(report['movement_every_five']):
            movement_every_five_min_totals[i] += value

        # Convert trail_points to arrays of integers
        # the inner arrarys are arrays of tuples
        trail_points.extend([{"x": float(point['x']), "y": float(point['y'])} for point in report['trail_points']])

    # Calculate averages
    average_movement = total_movement / len(reports_cursor)
    average_movement_every_five_min = [total / len(reports_cursor) for total in movement_every_five_min_totals]

    # Create the average report dictionary
    average_report = {
        "date": date,
        "time": time,
        "movement": average_movement,
        "applysia": 0,
        "trail_points": trail_points,
        "movement_every_five": average_movement_every_five_min
    }

    return average_report

# return reports that is an average of ALL aplysias
def get_average_report_of_all(date, time, end_time=None):
    time_format = "%H:%M"
    start_time = datetime.strptime(time, time_format)
    if end_time:
        e_time = datetime.strptime(end_time, time_format)

        reports_list = []

        current_time = start_time
        while current_time <= e_time:
            time_string = current_time.strftime("%H:%M")
            time_string = _get_time_formatted(date, time_string)
            reports = Report.objects(date=date, time=time_string)
            if reports:
                hour_average = calc_average_of_hour(date, current_time, reports)
                reports_list.append(hour_average)
            current_time = current_time + timedelta(hours=1)
        if len(reports_list) != 0:
            return reports_list
        else:
            return json.dumps({})

    else:
        time_string = start_time.strftime("%H:%M")
        time_string = _get_time_formatted(date, time_string)
        reports = Report.objects(date=date, time=time_string)
        if reports:
            average_rep = calc_average_of_hour(date, start_time, reports)
            return average_rep
        else:
            return json.dumps({})


def delete_reports_by_date(date):
    reports_to_delete = Report.objects(date=date)
    reports_to_delete.delete()


# returns num of deleted items, deletes all reports of applysia #num
def delete_reports_by_applysia(num):
    reports_to_delete = Report.objects(applysia=num)
    reports_to_delete.delete()


def delete_all_reports_by_date_and_time(date, time):
    reports_to_delete = Report.objects(date=date, time=time)
    reports_to_delete.delete()


def delete_unique_report(date, time, aplysia):
    reports_to_delete = Report.objects(date=date, time=time, applysia=aplysia)
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