import os

toollist = comp.GetToolList().values()

tool = []

path = 'C:\\Users\\Nandita\\Desktop\\test.jpg'

for tool in toollist:
    #print tool.GetAttrs()["TOOLS_RegID"]
    if tool.GetAttrs()["TOOLS_RegID"] == 'Loader':
        #print tool.GetAttrs()
        tool.SetAttrs({'TOOLS_Name' : 'name test 02'})
        tool.SetAttrs({'TOOLST_Clip_Name' : path})
        print True

        #print 'this is the name: ' + str(tool.name)
    if tool.GetAttrs("TOOLS_RegID") == "Loader":
        loaderPath = tool.GetAttrs("TOOLST_Clip_Name")
        loaderPathClean = loaderPath[1]

        tool.SetAttrs({'TOOLB_PassThrough' : True})
        tool.SetAttrs({'TOOLB_PassThrough' : False})

        #tool.SetAttrs({loaderPath[1] : path})

'''

{'TOOLNT_Region_End': {1.0: 999999999.9999}, 'TOOLIT_AltClip_Height': {1.0: 0.0}, 'TOOLB_HoldOutput': False, 'TOOLST_AltClip_FormatID': {}, 'TOOLIT_Clip_TrimIn': {1.0: 0.0}, 'TOOLI_Number_o_Inputs': 0.0, 'TOOLB_CacheToDisk': False, 'TOOLIT_Clip_AspectMode': {1.0: 0.0}, 'TOOLIT_Clip_ExtendLast': {1.0: 0.0}, 'TOOLNT_Clip_End': {1.0: 0.0}, 'TOOLIT_Clip_Width': {1.0: 1152.0}, 'TOOLS_Name': 'plant01', 'TOOLIT_AltClip_Length': {1.0: 1.0}, 'TOOLB_Selected': True, 'TOOLB_CtrlWZoom': False, 'TOOLBT_Clip_Saving': {1.0: False}, 'TOOLBT_Clip_Reverse': {1.0: False}, 'TOOLI_ImageWidth': 1152.0, 'TOOLNT_Region_Start': {1.0: 0.0}, 'TOOLIT_Clip_TimeCode': {1.0: 0.0}, 'TOOLIT_AltClip_Width': {1.0: 0.0}, 'TOOLB_Locked': False, 'TOOLB_ShowControls': True, 'TOOLNT_Clip_Start': {1.0: 0.0}, 'TOOLI_ImageHeight': 648.0, 'TOOLB_PassThrough': False, 'TOOLIT_Clip_TrimOut': {1.0: 0.0}, 'TOOLIT_Clip_ImportMode': {1.0: 0.0}, 'TOOLIT_Clip_StartFrame': {1.0: 5582.0}, 'TOOLBT_Clip_IsMultiFrame': {1.0: False}, 'TOOLIT_Clip_Length': {1.0: 1.0}, 'TOOLS_RegID': 'Loader', 'TOOLST_AltClip_FormatName': {}, 'TOOLB_Visible': True, 'TOOLB_NameSet': True, 'TOOLST_Clip_Name': {1.0: 'C:\\Users\\Nandita\\Desktop\\2] 5582.jpg'}, 'TOOLIT_Clip_PullOffset': {1.0: 0.0}, 'TOOLI_ID': 1.0, 'TOOLI_ImageDepth': 5.0, 'TOOLI_ImageField': -1.0, 'TOOLN_LastFrameTime': 0.03125, 'TOOLBT_Clip_Loop': {1.0: False}, 'TOOLBT_AltClip_IsMultiFrame': {1.0: False}, 'TOOLST_Clip_FormatName': {1.0: 'JpegFormat'}, 'TOOLIT_Clip_InitialFrame': {1.0: 5582.0}, 'TOOLST_AltClip_Name': {1.0: ''}, 'TOOLN_ImageAspectX': 1.0, 'TOOLNT_EnabledRegion_End': {1.0: 1000000000.0}, 'TOOLN_ImageAspectY': 1.0, 'TOOLBT_Clip_IsPreviewSaver': {1.0: False}, 'TOOLIT_Clip_ExtendFirst': {1.0: 0.0}, 'TOOLIT_Clip_Height': {1.0: 648.0}, 'TOOLST_Clip_FormatID': {1.0: 'JpegFormat'}, 'TOOLST_Clip_KeyCode': {1.0: ''}, 'TOOLIT_AltClip_StartFrame': {1.0: 5582.0}, 'TOOLNT_EnabledRegion_Start': {1.0: -1000000000.0}}

'''

# bg = comp.Background
