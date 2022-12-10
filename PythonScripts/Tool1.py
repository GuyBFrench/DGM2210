import random

import maya.cmds as cmds

def random_placement(min_x, max_x, min_y, max_y, min_z, max_z, num_of_dups):
    sels = cmds.ls(sl=True)

    for sel in sels:
        for i in range(num_of_dups):
            dup = cmds.duplicate(sel, rr=True)[0]

            pos_x = random.uniform(min_x, max_x)
            pos_y = random.uniform(min_y, max_y)
            pos_z = random.uniform(min_z, max_z)

            cmds.xform(dup, worldSpace=True, translation=[pos_x, pos_y, pos_z])

random_placement(10, 8, 13, 52, 12, 33, 150)

def print_name(name1, age1, name2, age2):
    #print(name1 + " is " + str(age1) + " years old and " + name2 + " is " + str(age2) + " years old.")

    print('%s is %i years old and %s is %i years old' % (name1, age1, name2, age2))

print_name('Charles', 12, 'Mary', 14)