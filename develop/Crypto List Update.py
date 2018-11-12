crypto_string_list = '"Husky - Main Geo.Husky - V13-RS.4-Cabin.Cabin.Extra_1.Frame_3.Cache.Null_10.Body_01_27", "Husky - Main Geo.Husky - V13-RS.4-Cabin.Cabin.Frame_5.Symmetry_4.Cache.Symmetry_5.Side_panel", "Husky - Main Geo.Husky - V13-RS.4-Cabin.Cabin.Doors - Static elements_0.Cache.Doors - Static elements_1.Door_Down Hinge.Body_05_21", "Husky - Main Geo.Husky - V13-RS.2-Back-Cover.Back-Cover.Frame_0.WC1-Husky-T4F-rear_cowling_v1:_41061163:1:_41061163:_41017132:1:_41017132:_Body1", "Husky - Main Geo.Husky - V13-RS.4-Cabin.Cabin.New-Part", "Husky - Main Geo.Husky - V13-RS.4-Cabin.Cabin.Frame_5.Symmetry_4.Cache.Symmetry_5.Body Elements_11.Body_013_15", "Husky - Main Geo.Husky - V13-RS.2-Back-Cover.Back-Cover.Frame_0.WC1-Husky-T4F-rear_cowling_v1:_41061163:1:_41061163:_41061156:1:_41061156:_41016908:1:_41016908:_Body1.1", "Husky - Main Geo.Husky - V13-RS.4-Cabin.Cabin.Frame_5.Symmetry_4.Cache.Symmetry_5.Body Elements_11.Body_08_22", "Husky - Main Geo.Husky - V13-RS.4-Cabin.Cabin.Door R - Orbit.Door R.Group_1.Body Elements_8.Body_013_11", "Husky - Main Geo.Husky - V13-RS.2-Back-Cover.Back-Cover.Symmetry_0.Cache.Null_3.WC1-Husky-T4F-rear_cowling_v1:_41061796:1:_41061796:_41017177:1:_41017177:_Body1.1", "Husky - Main Geo.Husky - V13-RS.4-Cabin.Cabin.Door R - Orbit.Door R.Group_1.Lock-Mechanism_0.Body_09_15.Hinge.1_0.Cylinder_0.Cache.Cylinder_0", "Husky - Main Geo.Husky - V13-RS.4-Cabin.Cabin.Door R - Orbit.Door R.Group_1.Lock-Mechanism_0.Body_08_17", "Husky - Main Geo.Husky - V13-RS.4-Cabin.Cabin.Frame_5.Symmetry_4.Cache.Symmetry_5.Body Elements_11.Body_07_22", "Husky - Main Geo.Husky - V13-RS.4-Cabin.Cabin.Door R - Orbit.Door R.Group_1.Lock-Mechanism_0.Body_09_15"'

crypto_list = crypto_string_list.split(',')

crypto_new_stringlist = ''

for sel in crypto_list:
    new_sel = sel.replace('"Husky - ', '"Geo.Husky - ')
    crypto_new_stringlist = crypto_new_stringlist + ',' + new_sel

print crypto_new_stringlist
