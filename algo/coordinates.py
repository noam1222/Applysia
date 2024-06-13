C00 = (504, 452)
C10 = (509, 632)
C20 = (527, 796)
C30 = (535, 927)
C01 = (623, 448)
C11 = (629, 634)
C21 = (643, 806)
C31 = (658, 951)
C02 = (784, 448)
C12 = (794, 642)
C22 = (802, 824)
C32 = (808, 976)
C03 = (988, 457)
C13 = (983, 650)
C23 = (985, 838)
C33 = (986, 991)
C04 = (1188, 466)
C14 = (1181, 665)
C24 = (1174, 836)
C34 = (1167, 995)
C05 = (1382, 469)
C15 = (1349, 662)
C25 = (1332, 816)
C35 = (1307, 993)

CAGES = {
    1: (C00, C01, C10, C11),
    2: (C01, C02, C11, C12),
    3: (C02, C03, C12, C13),
    4: (C03, C04, C13, C14),
    5: (C04, C05, C14, C15),
    6: (C10, C11, C20, C21),
    7: (C11, C12, C21, C22),
    8: (C12, C13, C22, C23),
    9: (C13, C14, C23, C24),
    10: (C14, C15, C24, C25),
    11: (C20, C21, C30, C31),
    12: (C21, C22, C31, C32),
    13: (C22, C23, C32, C33),
    14: (C23, C24, C33, C34),
    15: (C24, C25, C34, C35)
}

REAL_CAGE_WIDTH = CAGES[4][1][0] - CAGES[4][0][0]
REAL_CAGE_HEIGHT = CAGES[4][2][1] - CAGES[4][0][1]


def get_cage_num(p):
    x, y = p
    for cage, corners in CAGES.items():
        x_left = corners[0][0]
        x_right = corners[1][0]
        y_top = corners[0][1]
        y_bottom = corners[2][1] 
        if x_left <= x <= x_right and y_top <= y <= y_bottom:
            return cage
    return None


def get_point_in_relation_to_cage(p):
    cage = get_cage_num(p)
    if not cage:
        return None
    x, y = p
    x_relate = x - CAGES[cage][0][0]
    y_relate = y - CAGES[cage][0][1]
    return x_relate, y_relate


def norm_point_to_box(p, box_width, box_height):
    x_relate_to_box, y_relate_to_box = get_point_in_relation_to_cage(p)
    width_relation = box_width / REAL_CAGE_WIDTH
    height_relation = box_height / REAL_CAGE_HEIGHT
    return x_relate_to_box * width_relation, y_relate_to_box * height_relation

