#MAKE SURE ALL REQUIRED CORE FILES ARE IN SAME DIRECTORY
import pandas as pd
import numpy as np
from heapq import *

#A-Star*******************************************************************

class Elevation(object):
    def __init__(self, sLat, sLong, startpoint_eln, dLat, dLong, endpoint_eln):
        self.sLat=sLat
        self.sLong=sLong
        self.startpoint_eln=startpoint_eln
        self.dLat=dLat
        self.dLong=dLong
        self.endpoint_eln=endpoint_eln

    def heuristic(self, a, b):
        return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

    def astar(self, array, start, goal):
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        close_set = set()
        came_from = {}
        gscore = {start: 0}
        fscore = {start: self.heuristic(start, goal)}
        oheap = []
        heappush(oheap, (fscore[start], start))
        while oheap:

            current = heappop(oheap)[1]

            if current == goal:
                data = []
                while current in came_from:
                    data.append(current)
                    current = came_from[current]
                return data

            close_set.add(current)
            for i, j in neighbors:
                neighbor = current[0] + i, current[1] + j
                tentative_g_score = gscore[current] + self.heuristic(current, neighbor)
                if 0 <= neighbor[0] < array.shape[0]:
                    if 0 <= neighbor[1] < array.shape[1]:
                        if array[neighbor[0]][neighbor[1]] == 1:
                            continue
                    else:
                        # array bound y walls
                        continue
                else:
                    # array bound x walls
                    continue

                if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                    continue

                if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                    came_from[neighbor] = current
                    gscore[neighbor] = tentative_g_score
                    fscore[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
                    heappush(oheap, (fscore[neighbor], neighbor))
        return False

    def compute(self,):
        dfile = open("Reformatted_Elevation4.txt", "r")
        area_matrix = np.arange(2000)
        lat_arr = np.linspace(40.29805556,42.88583333,40) #rows
        long_arr = np.linspace(-101.30027778,-94.72638889,50) #columns
        eln_arr = np.arange(2000,dtype="float64")

        for i in range (0,2000): #for elevation
            line = dfile.readline()
            current_latitude, current_longitude, current_elevation = line.split(",")
            eln_arr[i]=float(current_elevation)

        temp_eln_arr = eln_arr #Copy of Actual Elevation Array
        temp_eln_arr2 = np.arange(2000, dtype="int32") #Elevation Matrix in 0s and 1s

        for i in range(0,2000):
            if temp_eln_arr[i] < min(self.startpoint_eln, self.endpoint_eln):
                temp_eln_arr2[i] = 1
            elif temp_eln_arr[i]>max(self.startpoint_eln, self.endpoint_eln):
                temp_eln_arr2[i] = 1
            else:
                temp_eln_arr2[i] = 0

        eln_reshaped_arr = temp_eln_arr2.reshape(40,50)
        path1 = self.astar(eln_reshaped_arr, (self.sLat, self.sLong), (self.dLat, self.dLong))
        if path1 == 0:
            flag = 0
            while flag != 1:
                eln_min = min(self.startpoint_eln, self.endpoint_eln) - 50
                eln_max = max(self.startpoint_eln, self.endpoint_eln) + 50
                for i in range(0, 2000):
                    if temp_eln_arr[i] < eln_min:
                        temp_eln_arr2[i] = 1
                    elif temp_eln_arr[i] > eln_max:
                        temp_eln_arr2[i] = 1
                    else:
                        temp_eln_arr2[i] = 0
                eln_reshaped_arr = temp_eln_arr2.reshape(40, 50)
                path1 = self.astar(eln_reshaped_arr, (self.sLat, self.sLong), (self.dLat, self.dLong))
                if path1 == 0:
                    flag = 0
                else:
                    flag = 1

        path1.append(tuple((self.sLat, self.sLong)))
        lattitude_arr = lat_arr.tolist()
        longitude_arr = long_arr.tolist()
        elev_cord = []
        for key in path1:
            elev_cord.append(list(((round(lattitude_arr[key[0]], 7)), round(longitude_arr[key[1]], 7))))

        for i in range(0,2000):
            temp_eln_arr2[i] = 0
        eln_reshaped_arr = temp_eln_arr2.reshape(40,50)

        path2 = self.astar(eln_reshaped_arr, (self.sLat, self.sLong), (self.dLat, self.dLong))
        path2.append(tuple((self.sLat, self.sLong)))
        elev_cord2 = []
        for key in path2:
            elev_cord2.append(list(((round(lattitude_arr[key[0]], 7)), round(longitude_arr[key[1]], 7))))

        return elev_cord ,elev_cord2

