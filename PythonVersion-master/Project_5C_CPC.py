# Phillipe Shin
# 01/21/2019
# SMART Data Visualization
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import csv  # This section sets up the program and reads the file into values[][]
import sys
import math
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from matplotlib.patches import ConnectionPatch
import numpy as np

class project(object):
    def API(self, values):
        self.ReadFile(values)
        self.createCPCinOne(values)

    def ReadFile(self, values):
        with open('input.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            count = 0
            for line in csv_reader:
                values.append([])
                line = list(line)
                for i in line:
                    values[count].append(i)
                count = count + 1

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # TASK 5 Part A : Draw All Graphs in CPC separately
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def createCPCinOne(self, values):                                                   # This is the "core" method of this task. Calculates CPC values and draws the graph
        xCoords, yCoords = [], []                                                       # Stores the X and Y coordinates
        totalX, totalY, currentClass = 0, 0, 1
        xLength = len(values)                                                           # Number of rows

        fig = plt.figure(figsize=(7, 7))                                                # Sizing the subplots and spacing
        fig.subplots_adjust(hspace=0.5)
        plt.title("Collocated Paired Coordinates")
        plt.xlabel("X")
        plt.ylabel("Y")

        for i in range(1, (xLength - 1)):                                               # Exclude IDS from data
            yLength = len(values[i])                                                    # Number of columns
            for j in range(1, (yLength - 1)):                                           # Exclude IDs from data
                if (int(values[i][yLength - 1]) == currentClass):                       # Process each class
                    if ((len(xCoords)) <= (len(yCoords))):                              # X-values for graph
                        totalX = float(values[i][j]) + float(totalX)
                        xCoords.append(float(totalX))                                   # Store the current total X distance
                    else:                                                               # Y-values for graph
                        totalY = float(values[i][j]) + float(totalY)
                        yCoords.append(float(totalY))                                   # Store the current total Y distance
                else:
                    plt.plot(xCoords, yCoords, '--o', label="Class: " + str(currentClass))
                    xCoords.clear()                                                     # Reset everything for next class
                    yCoords.clear()
                    totalX, totalY = 0, 0
                    currentClass = currentClass + 1
                    xCoords.append(float(values[i][j]))                                 # Store the first x-value of next class
                    totalX = float(values[i][j])
        plt.plot(xCoords, yCoords, '--o', label="Class: " + str(currentClass))
        plt.legend()
        plt.show()                                                                      # Displays the figure

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    values = [[]]
    obj = project()
    obj.API(values)


if __name__ == '__main__':
    main()
