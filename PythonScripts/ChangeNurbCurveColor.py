import maya.cmds as cmds

def ChangeColor(color):
    sels = cmds.ls(sl=1)
    for sel in sels:
        shape = cmds.listRelatives(sel)
        cmds.setAttr(shape[0] + ".overrideEnabled", 1)
        cmds.setAttr(shape[0] + ".overrideColor", color)

ChangeColor(29)