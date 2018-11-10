toollist = comp.GetToolList().values()

path = 'C:\\Users\\Nandita\\Desktop\\test.jpg'

for tool in toollist:
    if tool.GetAttrs()["TOOLS_RegID"] == 'Loader':
        print tool.GetAttrs()['TOOLS_Name']
        tool.SetAttrs({'TOOLS_Name' : 'name_test_01'})
        tool.SetAttrs({'TOOLST_Clip_Name' : path})
        print True
