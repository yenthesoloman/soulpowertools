import maya.cmds as cmds

sqList = cmds.ls('combined_*'+'*_INIT')
sqList.remove('combined_GE01_INIT')
cmds.select(sqList)

for each in sqList:
  cmds.setAttr('smplBs_'+each+'.envelope', 0)
