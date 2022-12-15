import maya.cmds as cmds

def SequentialRenamer(name):
    try:
        name = str(name)
        sels = cmds.ls(sl=True)
        formatCheck = name.find("#")
        if formatCheck < 1:
            print("This function requires a properly formatted string to work.")
            return
        num = name.count("#")
        chars = ("#" * num)
        properCheck = name.find(chars)
        if properCheck < 1:
            print("The input string needs to be in proper format with all # symbols together.")
            return
        x = name.partition(chars)
        pre = x[0]
        suffix = x[2]
        i = 100
        for sel in sels:
            replace = str(i)
            x = replace.zfill(num)
            i += 1
            cmds.rename(sel, pre + x + suffix)
    except:
        print("An error occurred, please select objects to rename and input a properly formatted string.")

SequentialRenamer("Arm_####_Jnt")