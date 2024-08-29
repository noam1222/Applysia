# old ones
# C00 = (504, 452)
# C10 = (509, 632)
# C20 = (527, 796)
# C30 = (535, 927)
# C01 = (623, 448)
# C11 = (629, 634)
# C21 = (643, 806)
# C31 = (658, 951)
# C02 = (784, 448)
# C12 = (794, 642)
# C22 = (802, 824)
# C32 = (808, 976)
# C03 = (988, 457)
# C13 = (983, 650)
# C23 = (985, 838)
# C33 = (986, 991)
# C04 = (1188, 466)
# C14 = (1181, 665)
# C24 = (1174, 836)
# C34 = (1167, 995)
# C05 = (1382, 469)
# C15 = (1349, 662)
# C25 = (1332, 816)
# C35 = (1307, 993)

# CAGES = {
#     1: (C00, C01, C10, C11),
#     2: (C01, C02, C11, C12),
#     3: (C02, C03, C12, C13),
#     4: (C03, C04, C13, C14),
#     5: (C04, C05, C14, C15),
#     6: (C10, C11, C20, C21),
#     7: (C11, C12, C21, C22),
#     8: (C12, C13, C22, C23),
#     9: (C13, C14, C23, C24),
#     10: (C14, C15, C24, C25),
#     11: (C20, C21, C30, C31),
#     12: (C21, C22, C31, C32),
#     13: (C22, C23, C32, C33),
#     14: (C23, C24, C33, C34),
#     15: (C24, C25, C34, C35)
# }

CAGES = {
    1: ((547, 453), (625, 451), (563, 600), (630, 598)),
    2: ((672, 450), (782, 448), (678, 607), (788, 610)),
    3: ((822, 450), (984, 457), (827, 618), (982, 630)),
    4: ((1006, 457), (1182, 466), (1004, 627), (1179, 631)),
    5: ((1188, 465), (1352, 468), (1182, 633), (1334, 640)),
    6: ((564, 636), (625, 639), (576, 747), (638, 759)),
    7: ((680, 639), (795, 649), (681, 766), (796, 775)),
    8: ((827, 651), (984, 658), (835, 783), (984, 784)),
    9: ((1001, 657), (1177, 663), (1006, 792), (1169, 792)),
    10: ((1185, 666), (1353, 664), (1180, 781), (1313, 775)),
    11: ((576, 804), (644, 808), (587, 883), (652, 895)),
    12: ((688, 816), (793, 822), (700, 904), (801, 913)),
    13: ((838, 826), (980, 832), (835, 927), (985, 931)),
    14: ((1004, 835), (1169, 838), (1004, 939), (1163, 940)),
    15: ((1179, 829), (1324, 820), (1171, 933), (1278, 937))
}

def get_cage_num(p):
    # Convert x and y to integers
    x, y = int(p[0]), int(p[1])
    for cage, corners in CAGES.items():
        x_left = corners[0][0]
        x_right = corners[1][0]
        y_top = corners[0][1]
        y_bottom = corners[2][1]
        if x_left <= x <= x_right and y_top <= y <= y_bottom:
            return cage
    return None


def get_point_in_relation_to_cage(p, cage):
    if not cage:
        return None
    x, y = int(p[0]), int(p[1])
    x_relate = x - CAGES[cage][0][0]
    y_relate = y - CAGES[cage][0][1]
    return x_relate, y_relate

def get_real_cage_width_and_height(app_num):
    return CAGES[app_num][1][0] - CAGES[app_num][0][0], CAGES[app_num][2][1] - CAGES[app_num][0][1]

def norm_point_to_box(p, box_width, box_height):
    app_num = get_cage_num(p)
    x_relate_to_box, y_relate_to_box = get_point_in_relation_to_cage(p, app_num)
    real_cage_width, real_cage_height = get_real_cage_width_and_height(app_num)
    width_relation = box_width / real_cage_width
    height_relation = box_height / real_cage_height
    return x_relate_to_box * width_relation, y_relate_to_box * height_relation




