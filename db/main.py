import pymongo
from controller import *
from widgets.report.exports import *

# Create a new report
#delete_reports_by_applysia(3)
#delete_reports_by_applysia(4)
#delete_reports_by_applysia(9)
#delete_reports_by_applysia(6)
#delete_reports_by_applysia(2)

# new_rep = add_report("27/05/24", "13:00", 6, [{"x": i * 0.05, "y": i} for i in range(120)], [i for i in range(12)])
# new_rep = add_report("27/05/24", "14:00", 4, [{"x": i * 0.05, "y": i} for i in range(120)], [i+2 for i in range(12)])
# new_rep = add_report("27/05/24", "15:00", 2, [{"x": i * 0.05, "y": i} for i in range(120)], [i+4 for i in range(12)])

# test for export to excel function

new_rep = {
    'date': "27/05/24",
    'time': "13:00",
    'movement': 0.86666666666,
    'applysia': 6,
    'trail_points': [{'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 731.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 729.5}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.5}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.5}, {'x': 709.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.5}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 729.5}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 729.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 729.5}, {'x': 709.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 729.5}, {'x': 709.5, 'y': 729.5}, {'x': 709.5, 'y': 730.0}, {'x': 710.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 729.0}, {'x': 710.0, 'y': 729.5}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 729.5}, {'x': 710.0, 'y': 729.5}, {'x': 710.5, 'y': 729.5}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.0, 'y': 730.0}, {'x': 709.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 729.5}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 729.5}, {'x': 709.0, 'y': 731.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 729.5}, {'x': 709.5, 'y': 731.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.5, 'y': 729.5}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 729.5}, {'x': 710.0, 'y': 729.5}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.0, 'y': 731.0}, {'x': 710.0, 'y': 730.5}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.5}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}],
    'movement_every_five': [i for i in range(12)]
}
#export_report_to_word(new_rep)
#export_report_to_excel(new_rep)
#reports = [{'date': '22/08/24', 'movement': 0.26666666666666666, 'applysia': 0, 'trail_points': [{'x': 710.5, 'y': 730.0}, {'x': 710.5, 'y': 729.0}, {'x': 710.5, 'y': 729.5}, {'x': 710.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.5}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 729.0}, {'x': 709.5, 'y': 729.5}, {'x': 710.5, 'y': 729.5}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.5}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.5}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.5}, {'x': 709.5, 'y': 730.0}, {'x': 710.5, 'y': 730.0}, {'x': 710.0, 'y': 730.5}, {'x': 710.5, 'y': 730.0}, {'x': 709.5, 'y': 730.5}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.5}, {'x': 709.5, 'y': 730.5}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 729.5}, {'x': 710.0, 'y': 729.5}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 729.5}, {'x': 709.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 729.5}, {'x': 710.0, 'y': 729.5}, {'x': 710.0, 'y': 729.5}, {'x': 710.0, 'y': 729.5}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 729.5}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 729.0}, {'x': 709.5, 'y': 729.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.5}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.5}, {'x': 709.5, 'y': 730.0}, {'x': 710.5, 'y': 729.5}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.5}, {'x': 710.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 729.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.5}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.5}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 729.5}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 729.5}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.5}, {'x': 710.0, 'y': 729.5}, {'x': 710.0, 'y': 729.5}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 729.5}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.5}, {'x': 710.0, 'y': 729.5}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 729.5}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 729.0}, {'x': 1028.0, 'y': 678.0}, {'x': 1026.0, 'y': 684.5}, {'x': 1020.5, 'y': 694.5}, {'x': 1021.0, 'y': 698.0}, {'x': 1020.5, 'y': 705.0}, {'x': 1021.5, 'y': 717.5}, {'x': 1019.0, 'y': 728.5}, {'x': 1021.0, 'y': 733.0}, {'x': 1019.5, 'y': 736.5}, {'x': 1020.0, 'y': 740.5}, {'x': 1021.5, 'y': 745.0}, {'x': 1023.0, 'y': 744.5}, {'x': 1024.0, 'y': 745.0}, {'x': 1026.0, 'y': 746.5}, {'x': 1028.5, 'y': 748.0}, {'x': 1053.5, 'y': 749.5}, {'x': 1060.5, 'y': 748.5}, {'x': 1068.5, 'y': 749.0}, {'x': 1074.0, 'y': 748.5}, {'x': 1081.0, 'y': 750.0}, {'x': 1141.5, 'y': 746.5}, {'x': 1147.0, 'y': 745.0}, {'x': 1149.5, 'y': 744.5}, {'x': 1154.5, 'y': 695.0}, {'x': 1151.5, 'y': 684.5}, {'x': 1294.5, 'y': 607.5}, {'x': 1294.5, 'y': 607.0}, {'x': 1295.0, 'y': 607.0}, {'x': 1295.0, 'y': 608.0}, {'x': 1295.0, 'y': 607.0}, {'x': 1295.5, 'y': 606.5}, {'x': 1296.0, 'y': 607.5}, {'x': 1294.5, 'y': 608.0}, {'x': 1293.5, 'y': 607.5}, {'x': 1294.5, 'y': 607.0}, {'x': 1294.0, 'y': 607.0}, {'x': 1295.0, 'y': 607.0}, {'x': 1294.5, 'y': 607.5}, {'x': 1295.0, 'y': 607.5}, {'x': 1294.5, 'y': 607.0}, {'x': 1295.0, 'y': 606.0}, {'x': 1293.5, 'y': 607.0}, {'x': 1295.0, 'y': 607.0}, {'x': 1293.5, 'y': 607.5}, {'x': 1295.0, 'y': 608.0}, {'x': 1296.0, 'y': 608.0}, {'x': 1294.5, 'y': 606.5}, {'x': 1295.0, 'y': 608.0}, {'x': 727.0, 'y': 573.5}, {'x': 729.0, 'y': 574.0}, {'x': 725.0, 'y': 571.5}, {'x': 723.5, 'y': 571.0}, {'x': 724.5, 'y': 572.0}, {'x': 720.5, 'y': 572.0}, {'x': 720.0, 'y': 572.0}, {'x': 722.0, 'y': 572.0}, {'x': 720.5, 'y': 571.0}, {'x': 719.5, 'y': 574.5}, {'x': 720.0, 'y': 575.5}, {'x': 723.0, 'y': 576.5}, {'x': 722.0, 'y': 576.0}, {'x': 719.5, 'y': 575.0}, {'x': 719.5, 'y': 572.5}, {'x': 718.0, 'y': 572.0}, {'x': 717.0, 'y': 572.0}, {'x': 716.0, 'y': 574.0}, {'x': 716.5, 'y': 574.0}, {'x': 716.5, 'y': 574.0}, {'x': 715.5, 'y': 574.0}, {'x': 714.5, 'y': 573.5}, {'x': 715.0, 'y': 576.5}, {'x': 715.0, 'y': 576.0}, {'x': 714.0, 'y': 576.0}, {'x': 713.5, 'y': 575.5}, {'x': 712.0, 'y': 574.0}, {'x': 711.5, 'y': 572.0}, {'x': 710.5, 'y': 575.5}, {'x': 710.5, 'y': 577.0}, {'x': 709.5, 'y': 577.5}, {'x': 709.0, 'y': 576.0}, {'x': 707.5, 'y': 576.5}, {'x': 706.0, 'y': 575.5}, {'x': 706.0, 'y': 572.0}, {'x': 705.5, 'y': 577.0}, {'x': 1200.5, 'y': 678.5}, {'x': 1201.5, 'y': 678.0}, {'x': 1204.5, 'y': 679.0}, {'x': 1204.0, 'y': 680.5}, {'x': 1203.0, 'y': 683.0}, {'x': 1204.5, 'y': 683.0}, {'x': 1201.5, 'y': 687.0}, {'x': 1201.5, 'y': 691.5}, {'x': 1203.0, 'y': 689.5}, {'x': 1202.5, 'y': 701.5}, {'x': 1200.0, 'y': 705.0}, {'x': 1200.0, 'y': 709.5}, {'x': 1200.0, 'y': 712.0}, {'x': 1197.5, 'y': 722.0}, {'x': 1198.5, 'y': 724.5}, {'x': 1197.0, 'y': 726.0}, {'x': 1198.0, 'y': 727.5}], 'movement_every_five': [0.0, 0.016666666666666666, 0.016666666666666666, 0.03333333333333333, 0.016666666666666666, 0.016666666666666666, 0.016666666666666666, 0.03333333333333333, 0.016666666666666666, 0.03333333333333333, 0.03333333333333333, 0.03333333333333333]},  {'date': '22/08/24', 'movement': 0.25, 'applysia': 2, 'trail_points': [{'x': 727.0, 'y': 573.5}, {'x': 729.0, 'y': 574.0}, {'x': 725.0, 'y': 571.5}, {'x': 723.5, 'y': 571.0}, {'x': 724.5, 'y': 572.0}, {'x': 720.5, 'y': 572.0}, {'x': 720.0, 'y': 572.0}, {'x': 722.0, 'y': 572.0}, {'x': 720.5, 'y': 571.0}, {'x': 719.5, 'y': 574.5}, {'x': 720.0, 'y': 575.5}, {'x': 723.0, 'y': 576.5}, {'x': 722.0, 'y': 576.0}, {'x': 719.5, 'y': 575.0}, {'x': 719.5, 'y': 572.5}, {'x': 718.0, 'y': 572.0}, {'x': 717.0, 'y': 572.0}, {'x': 716.0, 'y': 574.0}, {'x': 716.5, 'y': 574.0}, {'x': 716.5, 'y': 574.0}, {'x': 715.5, 'y': 574.0}, {'x': 714.5, 'y': 573.5}, {'x': 715.0, 'y': 576.5}, {'x': 715.0, 'y': 576.0}, {'x': 714.0, 'y': 576.0}, {'x': 713.5, 'y': 575.5}, {'x': 712.0, 'y': 574.0}, {'x': 711.5, 'y': 572.0}, {'x': 710.5, 'y': 575.5}, {'x': 710.5, 'y': 577.0}, {'x': 709.5, 'y': 577.5}, {'x': 709.0, 'y': 576.0}, {'x': 707.5, 'y': 576.5}, {'x': 706.0, 'y': 575.5}, {'x': 706.0, 'y': 572.0}, {'x': 705.5, 'y': 577.0}], 'movement_every_five': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.08333333333333333, 0.08333333333333333, 0.08333333333333333]}, {'date': '22/08/24', 'movement': 0.25, 'applysia': 5, 'trail_points': [{'x': 1294.5, 'y': 607.5}, {'x': 1294.5, 'y': 607.0}, {'x': 1295.0, 'y': 607.0}, {'x': 1295.0, 'y': 608.0}, {'x': 1295.0, 'y': 607.0}, {'x': 1295.5, 'y': 606.5}, {'x': 1296.0, 'y': 607.5}, {'x': 1294.5, 'y': 608.0}, {'x': 1293.5, 'y': 607.5}, {'x': 1294.5, 'y': 607.0}, {'x': 1294.0, 'y': 607.0}, {'x': 1295.0, 'y': 607.0}, {'x': 1294.5, 'y': 607.5}, {'x': 1295.0, 'y': 607.5}, {'x': 1294.5, 'y': 607.0}, {'x': 1295.0, 'y': 606.0}, {'x': 1293.5, 'y': 607.0}, {'x': 1295.0, 'y': 607.0}, {'x': 1293.5, 'y': 607.5}, {'x': 1295.0, 'y': 608.0}, {'x': 1296.0, 'y': 608.0}, {'x': 1294.5, 'y': 606.5}, {'x': 1295.0, 'y': 608.0}], 'movement_every_five': [0.0, 0.0, 0.0, 0.0, 0.0, 0.08333333333333333, 0.08333333333333333, 0.08333333333333333, 0.0, 0.0, 0.0, 0.0]}, {'date': '22/08/24', 'movement': 0.6666666666666666, 'applysia': 7, 'trail_points': [{'x': 710.5, 'y': 730.0}, {'x': 710.5, 'y': 729.0}, {'x': 710.5, 'y': 729.5}, {'x': 710.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.5}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 729.0}, {'x': 709.5, 'y': 729.5}, {'x': 710.5, 'y': 729.5}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.5}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.5}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.5}, {'x': 709.5, 'y': 730.0}, {'x': 710.5, 'y': 730.0}, {'x': 710.0, 'y': 730.5}, {'x': 710.5, 'y': 730.0}, {'x': 709.5, 'y': 730.5}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.5}, {'x': 709.5, 'y': 730.5}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 729.5}, {'x': 710.0, 'y': 729.5}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 729.5}, {'x': 709.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 729.5}, {'x': 710.0, 'y': 729.5}, {'x': 710.0, 'y': 729.5}, {'x': 710.0, 'y': 729.5}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 729.5}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 729.0}, {'x': 709.5, 'y': 729.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.5}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.5}, {'x': 709.5, 'y': 730.0}, {'x': 710.5, 'y': 729.5}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.5}, {'x': 710.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 729.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.5}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.5}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 729.5}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 729.5}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.5}, {'x': 710.0, 'y': 729.5}, {'x': 710.0, 'y': 729.5}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 729.5}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.5, 'y': 730.5}, {'x': 710.0, 'y': 729.5}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 710.0, 'y': 730.0}, {'x': 709.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 729.5}, {'x': 709.5, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 709.0, 'y': 730.0}, {'x': 709.5, 'y': 730.0}, {'x': 710.0, 'y': 729.0}], 'movement_every_five': [0.0, 0.08333333333333333, 0.08333333333333333, 0.08333333333333333, 0.08333333333333333, 0.0, 0.0, 0.08333333333333333, 0.08333333333333333, 0.08333333333333333, 0.08333333333333333, 0.0]}, {'date': '22/08/24', 'movement': 0.08333333333333333, 'applysia': 9, 'trail_points': [{'x': 1028.0, 'y': 678.0}, {'x': 1026.0, 'y': 684.5}, {'x': 1020.5, 'y': 694.5}, {'x': 1021.0, 'y': 698.0}, {'x': 1020.5, 'y': 705.0}, {'x': 1021.5, 'y': 717.5}, {'x': 1019.0, 'y': 728.5}, {'x': 1021.0, 'y': 733.0}, {'x': 1019.5, 'y': 736.5}, {'x': 1020.0, 'y': 740.5}, {'x': 1021.5, 'y': 745.0}, {'x': 1023.0, 'y': 744.5}, {'x': 1024.0, 'y': 745.0}, {'x': 1026.0, 'y': 746.5}, {'x': 1028.5, 'y': 748.0}, {'x': 1053.5, 'y': 749.5}, {'x': 1060.5, 'y': 748.5}, {'x': 1068.5, 'y': 749.0}, {'x': 1074.0, 'y': 748.5}, {'x': 1081.0, 'y': 750.0}, {'x': 1141.5, 'y': 746.5}, {'x': 1147.0, 'y': 745.0}, {'x': 1149.5, 'y': 744.5}, {'x': 1154.5, 'y': 695.0}, {'x': 1151.5, 'y': 684.5}], 'movement_every_five': [0.0, 0.0, 0.0, 0.08333333333333333, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}, {'date': '22/08/24', 'movement': 0.08333333333333333, 'applysia': 10, 'trail_points': [{'x': 1200.5, 'y': 678.5}, {'x': 1201.5, 'y': 678.0}, {'x': 1204.5, 'y': 679.0}, {'x': 1204.0, 'y': 680.5}, {'x': 1203.0, 'y': 683.0}, {'x': 1204.5, 'y': 683.0}, {'x': 1201.5, 'y': 687.0}, {'x': 1201.5, 'y': 691.5}, {'x': 1203.0, 'y': 689.5}, {'x': 1202.5, 'y': 701.5}, {'x': 1200.0, 'y': 705.0}, {'x': 1200.0, 'y': 709.5}, {'x': 1200.0, 'y': 712.0}, {'x': 1197.5, 'y': 722.0}, {'x': 1198.5, 'y': 724.5}, {'x': 1197.0, 'y': 726.0}, {'x': 1198.0, 'y': 727.5}], 'movement_every_five': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.08333333333333333]}]
draw_path_video(new_rep, output_file="path_animation.gif", fps=2)

# new_rep = add_report("27/05/24", "13:00", 3, [{"x": i * 0.05, "y": i} for i in range(120)], [i for i in range(12)])
# new_rep = add_report("27/05/24", "14:00", 3, [{"x": i * 0.05, "y": i} for i in range(120)], [i+1 for i in range(12)])
# new_rep = add_report("27/05/24", "12:00", 3, [{"x": i * 0.05, "y": i} for i in range(120)], [i for i in range(12)])
# new_rep = add_report("27/05/24", "16:00", 3, [{"x": i * 0.05, "y": i} for i in range(120)], [i + 1 for i in range(12)])
# new_rep = add_report("27/05/24", "20:00", 3, [{"x": i * 0.05, "y": i} for i in range(120)], [i for i in range(12)])

# new_rep = add_report("27/05/24", "12:00", 4, [{"x": i * 0.05, "y": i} for i in range(120)], [i for i in range(12)])
# new_rep = add_report("27/05/24", "13:00", 4, [{"x": i * 0.05, "y": i} for i in range(120)], [i for i in range(12)])
# new_rep = add_report("27/05/24", "14:00", 4, [{"x": i * 0.05, "y": i} for i in range(120)], [i+1 for i in range(12)])
# new_rep = add_report("27/05/24", "15:00", 4, [{"x": i * 0.05, "y": i} for i in range(120)], [i for i in range(12)])
# new_rep = add_report("27/05/24", "16:00", 4, [{"x": i * 0.05, "y": i} for i in range(120)], [i+2 for i in range(12)])

# new_rep = add_report("27/05/24", "12:00", 9, [{"x": i * 0.05, "y": i} for i in range(120)], [i for i in range(12)])
# new_rep = add_report("27/05/24", "13:00", 9, [{"x": i * 0.05, "y": i} for i in range(120)], [i for i in range(12)])
# new_rep = add_report("27/05/24", "14:00", 9, [{"x": i * 0.05, "y": i} for i in range(120)], [i+1 for i in range(12)])
# new_rep = add_report("27/05/24", "15:00", 9, [{"x": i * 0.05, "y": i} for i in range(120)], [i-1 for i in range(12)])
# new_rep = add_report("27/05/24", "16:00", 9, [{"x": i * 0.05, "y": i} for i in range(120)], [i for i in range(12)])

# x = get_average_report_of_all("27/05/24", "12:00", "16:00")
# print(x)
# Get all reports
# all_reports = get_all_reports()
# for report in all_reports:
# print(report.id, report.date, report.time, report.movement, report.applysia, report.trail_points)
# y = get_all_reports()
# print(y)
# x = get_filtered_reports("2024-05-11","12:34:00", "12:34:13", 12, False)
# print(x)

# print(x.id)

"""code for installing nescesary packages"""
# import sys
# import subprocess

# def install(package):
#    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# try:
#    import openpyxl
#    import xlwt
# except ImportError as e:
#    print(f"Error: {e}")
#    print("Attempting to install missing packages...")
#    install('openpyxl')
#    install('xlwt')
#    print("Packages installed. Please rerun the script.")
#    sys.exit(1)

# print("All necessary libraries are installed.")
