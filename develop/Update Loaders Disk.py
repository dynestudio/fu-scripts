# v0.1 wip 03

import os

# new disk to use
disk = 'D:'

# get main tools list
toollist = comp.GetToolList().values()

# find loaders nodes
for tool in toollist:
    if tool.GetAttrs()["TOOLS_RegID"] == 'Loader':
        # get original times
        globalIn = tool.GlobalIn[comp.CurrentTime]
        globalOut = tool.GlobalIn[comp.CurrentTime]
        trimIn = tool.ClipTimeStart[comp.CurrentTime]
        trimOut = tool.ClipTimeEnd[comp.CurrentTime]

        # get loader path
        loaderPath = tool.GetAttrs("TOOLST_Clip_Name")
        loaderPathClean = loaderPath[1]

        # split original loader path
        loaderPathSplit = loaderPathClean.split(os.sep)

        # added new disk
        new_disk = loaderPathSplit[0] = disk + '\\'

        # join new path
        path = os.path.join(*loaderPathSplit)

        # replace loader path
        tool.Clip = path

        # update loader times
        tool.GlobalIn = globalIn
        tool.GlobalOut = globalOut
        tool.ClipTimeStart = trimIn
        tool.ClipTimeEnd = trimOut
