#Script to loop through a folder of shapefiles and clip them using an input buffer
import os
import arcpy

#Set environmental workspace
arcpy.env.workspace = r"C:\Users\ian.conroy\Desktop\Bay Geo Classes\Python Class\GIS_Data\SF_SHPs"

#Set location for output of geoprocessing tools
output_folder = r"C:\Users\ian.conroy\Desktop\Bay Geo Classes\Python Class\Output_Folder"

#Create folder path of the folder that will be created to store the clipped shapefiles
location_analysis_fld = os.path.join(output_folder, 'Location_Analysis')

#Use the os module to create a new folder
os.mkdir(location_analysis_fld)

#Get a list of the shapefiles that will be looped through
shp_list = arcpy.ListFeatureClasses()

#Input shapefile of the point of interest
starting_point = r"C:\Users\ian.conroy\Desktop\Bay Geo Classes\Python Class\GIS_Data\Point_of_Interest.shp"

#Create buffer of point of interest
print('Creating buffer')
starting_point_buffer = os.path.join(location_analysis_fld, 'Location_buffer.shp')
arcpy.Buffer_analysis(starting_point, starting_point_buffer, "1 Mile")

for shp in shp_list:
    #Clipping all our shapefiles
    print('Clipping', shp)
    clip_shp = os.path.join(location_analysis_fld, shp[:-4] + '_Clipped.shp')
    arcpy.Clip_analysis(shp, starting_point_buffer, clip_shp)
