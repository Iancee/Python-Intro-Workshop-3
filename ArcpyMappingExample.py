#Script to update data in a map and export a new pdf

# esri documentation for updating layers https://desktop.arcgis.com/en/arcmap/10.3/analyze/arcpy-mapping/layer-class.htm

import os
import arcpy

#Set this variable so we can overwrite the pdf when we export a new version of the map
arcpy.env.overwriteOutput = True

#Set up a map document variable
mxd = arcpy.mapping.MapDocument(r"C:\Users\ian.conroy\Desktop\Bay Geo Classes\Python Class\Intro Class Fall\Session 3\SampleMap.mxd")

new_data_fld = r"C:\Users\ian.conroy\Desktop\Bay Geo Classes\Python Class\Output_Folder\Location_Analysis"

#This returns a list of the layers in the dataframe you specify [0] selects the first dataframe
df = arcpy.mapping.ListDataFrames(mxd)[0]


#Use a loop to loop through all the layers in the map, test if it's a feature layer, then update it's source
for lyr in df:
    if lyr.isFeatureLayer == True:
        print lyr.name, 'replacing data source'
        lyr.replaceDataSource(new_data_fld, "SHAPEFILE_WORKSPACE")
        
    else:
        print 'skipped', lyr.name

#This resets the dataframe extent to the new version of the layers
df.zoomToSelectedFeatures()

#Save and export a new version of the map
mxd.save()
arcpy.mapping.ExportToPDF(mxd, r"C:\Users\ian.conroy\Desktop\Bay Geo Classes\Python Class\Intro Class Fall\Session 3\SampleMap.pdf")
