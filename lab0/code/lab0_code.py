'''
Maisong Francis

This document contains the code used to buffer MN State Trails in two different environments: Jupyter Notebooks in ArcPro and in ArcGIS Online. 

'''

# Buffer MN State Trails Shapefile 50 meters on each side 
# Buffer total size: 100 meters



# ArcPro environment

in_feature = r"C:\Users\msong\Desktop\GIS5572\lab0\shp_trans_state_trails_minnesota\state_trails_minnesota.shp"
out_feature = "MNstate_trails_buff_50m_jupyter"
buff_dist = "50 meters"

arcpy.analysis.Buffer(in_feature, 
                      out_feature,
                      buff_dist)



# --------------------------------------------------------------------------------------
# ArcGIS Online environment

from arcgis.gis import GIS
from arcgis import features

gis = GIS("home")


# Title: shp_trans_state_trails_minnesota | Type: Feature Service | Owner: leex6165_UMN
trails = gis.content.get("d1c3c8c8448a4158859a83df2169b028")

# buffer state trails by 100 m (50 m on each side)
features.use_proximity.create_buffers(trails, 
                                      distances = [50], 
                                      units = "Meters", 
                                      output_name = "MNstate_trails_buff_50m_arconline")



# Map buffered state trails
#
# Title: MNstate_trails_buff_50m_arconline | Type: Feature Service | Owner: leex6165_UMN
trails_50m = gis.content.get("bae6c3d7807c4525b713b74c3d504028")
trails_50m

map1 = gis.map("Minnesota")

map1.add_layer(trails_50m)
map1.add_layer(item)

# View Map
map1
