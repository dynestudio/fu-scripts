# Crypto List Update - v0.1 wip 02

"""

# get main tools list
toollist = comp.GetToolList().values()

# find cryptomatte nodes
for tool in toollist:
    if tool.GetAttrs()["TOOLS_RegID"] == 'Fuse.Cryptomatte':
        print tool.GetAttrs()

"""


crypto_string_list = '"Husky - Main Geo.Husky - V13-RS.4-Cabin.Cabin.Door R - Orbit.Door R.Group_1.Window_0.Window", "Husky - Main Geo.Husky - V13-RS.4-Cabin.Cabin.Windows.Front-Window", "Husky - Main Geo.Husky - V13-RS.4-Cabin.Cabin.Door R - Orbit.Door R.Group_1.Body Elements_8.Window"'

crypto_list = crypto_string_list.split(',')

crypto_new_stringlist = ''

for sel in crypto_list:
    new_sel = sel.replace('"Husky - ', '"Geo.Husky - ')
    crypto_new_stringlist = crypto_new_stringlist + ',' + new_sel

print crypto_new_stringlist
