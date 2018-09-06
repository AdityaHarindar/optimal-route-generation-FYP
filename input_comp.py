#MAKE SURE ALL REQUIRED CORE FILES ARE IN SAME DIRECTORY
import numpy as np
#to resize pycharm output
import pandas as pd
from elevation import Elevation

class Input(object) :
    def __init__(self, input_source_lat, input_source_long, input_dest_lat, input_dest_long):
        self.input_source_latitude = input_source_lat
        self.input_source_longitude = input_source_long
        self.input_dest_latitude = input_dest_lat
        self.input_dest_longitude = input_dest_long

    def compute(self):
        ctr1 = 0 #index of S lat
        ctr11 = 0
        ctr2 = 0 #index of S long
        ctr22 = 0
        ctr3 = 0 #index of D lat
        ctr33 = 0
        ctr4 = 0 #index of D long
        ctr44 = 0
        lat_arr = np.linspace(40.29805556,42.88583333,40) #rows
        long_arr = np.linspace(-101.30027778,-94.72638889,50) #columns
        #print(lat_arr)
        for lat in lat_arr.tolist():
            if self.input_source_latitude == round(lat, 7):
                break
            else:
                ctr1 = ctr1 + 1
        if ctr1 == 40: #approx to nearest greater value
            for lat in lat_arr.tolist():
                if self.input_source_latitude < round(lat, 7):
                    break
                else:
                    #print(lat)
                    ctr11 = ctr11 + 1
            ctr1 = ctr11

        for lon in long_arr.tolist():
            if self.input_source_longitude == round(lon, 7):
                break
            else:
                ctr2 = ctr2 + 1
        if ctr2 == 50:
            for lon in long_arr.tolist():
                if self.input_source_longitude < round(lon, 7):
                    break
                else:
                    ctr22 = ctr22 + 1
            ctr2 = ctr22
        for lat in lat_arr.tolist():
            if self.input_dest_latitude == round(lat, 7):
                break
            else:
                ctr3 = ctr3 + 1
        if ctr3 == 40:
            for lat in lat_arr.tolist():
                if self.input_dest_latitude < round(lat, 7):
                    break
                else:
                    ctr33 = ctr33 + 1
            ctr3 = ctr33
        for lon in long_arr.tolist():
            if self.input_dest_longitude == round(lon, 7):
                break
            else:
                ctr4 = ctr4 + 1
        if ctr4 == 50:
            for lon in long_arr.tolist():
                if self.input_dest_longitude < round(lon, 7):
                    break
                else:
                    print(lon)
                    ctr44 = ctr44 + 1
            ctr4 = ctr44
       # print(ctr1)


        startpoint = (ctr1*50)+ctr2 #index of Elevation for S
        endpoint = (ctr3*50)+ctr4 #index of Elevation for D
        dfile = open("Reformatted_Elevation4.txt","r")
        eln_arr = np.arange(2000, dtype="float64")
        for j in range(0, 2000):
            line = dfile.readline()
            current_latitude, current_longitude, current_elevation = line.split(",")
            eln_arr[j] = float(current_elevation)

        print(ctr1, ctr2, eln_arr[startpoint], ctr3, ctr4, eln_arr[endpoint])

        e = Elevation(ctr1, ctr2, eln_arr[startpoint], ctr3, ctr4, eln_arr[endpoint])
        return e.compute()

# if __name__ == "__main__":
#  i = Input(42.8858332,-101.3002778,42.8855662,-101.3002778)
# print(str(i.compute()))


