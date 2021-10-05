import arcpy		#Here is our Python ArcGIS package
from arcpy import env	#Env class contains all geoprocessing environments
from arcpy.sa import *  #Importing spatial analysis package
import sys		    #sys module (information ab constants, functions, + methods
import os		#os module (functions for editing directories)
 
 
#Check out the Network Analyst extension license
arcpy.CheckOutExtension("Network")
 
#Set environment settings
env.workspace = "C:/data/NewPaltz.gdb"
env.overwriteOutput = True
#tools will execute and overwrite the output dataset
 
 
#Set local variables
network_data_source = "openStreet_nd"	#name of our street layer
layer_name = "serviceArea"			#setting name of service area
travel_mode = "DriveTime"			#Setting drive/time variable
travel_direction = "TRAVEL_FROM"		#Indicates leaving from facility
break_values = "1, 2, 3, 4, 5"		#Setting 1-5 min intervals
inFacilities = "SRFD.gdb\Stations"		#Grabbing station locations
 
#Create the Service Area Layer
sa = arcpy.na.MakeServiceAreaLayer(network_data_source,layer_name, travel_mode, travel_direction, break_values)
outNALayer = sa.getOutput(0)
#Here we create a service area, using the values we just defined.
 
#Get the names of all the sublayers within the service area layer.
subLayerNames = arcpy.na.GetNAClassNames(outNALayer)
 
#Stores the layer names that we will use later
facilitiesLayerName = subLayerNames["Facilities"]
 
#Load the fire stations as facilities 
arcpy.na.AddLocations(outNALayer, facilitiesLayerName, inFacilities, "", "")
 
#Solve the Service Area Layer
arcpy.na.Solve(outNALayer)
