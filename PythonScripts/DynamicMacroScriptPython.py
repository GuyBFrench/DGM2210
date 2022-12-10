import maya.cmds as cmds
import random

citySize = 30.0
cityBuildings = 35
shortBuildingsHeight = 1.1
tallBuildingsHeight = 2.3
cityKeeps = 3
keepsSize = 3.7

cmds.polyCylinder(r=citySize, h=4, sx=60, sy=1, sz=1, ax=(0, 1, 0), rcp=0, cuv=3, ch=1);
cmds.move(0, 1, 0, r=1)
cmds.select('pCylinder1.f[120:179]')
cmds.select('pCylinder1.f[60:119]', add=1)

cmds.delete()

cmds.select('pCylinder1.f[0:59]', r=1)
cmds.polyExtrudeFacet('pCylinder1.f[0:59]', kft=1, ltz=1, d=1, twt=0, tp=1, off=0, tk=0, sma=30)

cmds.polyDisc(s=30, subdivisionMode=3, subdivisions=1, r=(citySize+0.3))
cmds.move(0, 0.15, 0, r=1)
cmds.polyCylinder(r=keepsSize, h=keepsSize, sx=20, sy=1, sz=1, ax=(0, 1, 0), rcp=0)
cmds.move(0, (keepsSize/2), 0, r=1)

cmds.polyCube(w=keepsSize, h=keepsSize, d=keepsSize, sx=1, sy=1, sz=1, ax=(0, 1, 0))
cmds.move(0, keepsSize*1.1, 0, r=1)

for i in range(cityBuildings):

    x = random.uniform(-(citySize/1.4), (citySize/1.4))
    z = random.uniform(-(citySize/1.4), (citySize/1.4))
    cmds.polyCube(w=1, h=shortBuildingsHeight, d=1, sx=1, sy=1, sz=1, ax=(0, 1, 0))

    sels = cmds.ls(sl=1)
    sel = sels[0]

    cmds.xform(sel, ws=1, translation=(x, (shortBuildingsHeight/2), z))

cmds.select(cl=1)


for i in range(cityBuildings):

    x = random.uniform(-(citySize/1.4), (citySize/1.4))
    z = random.uniform(-(citySize/1.4), (citySize/1.4))
    cmds.polyCube(w=1, h=tallBuildingsHeight, d=1, sx=1, sy=1, sz=1, ax=(0, 1, 0))

    sels = cmds.ls(sl=1)
    sel = sels[0]

    cmds.xform(sel, ws=1, translation=(x, (tallBuildingsHeight/2), z))


for i in range(cityKeeps+1):
    x = random.uniform(-(citySize/1.4), (citySize/1.4))
    z = random.uniform(-(citySize/1.4), (citySize/1.4))
    cmds.polyCube(w=keepsSize, h=keepsSize, d=keepsSize, sx=1, sy=1, sz=1, ax=(0, 1, 0))

    sels = cmds.ls(sl=1)
    sel = sels[0]

    cmds.xform(sel, ws=1, translation=(x, (keepsSize/2), z))
