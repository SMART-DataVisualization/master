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
        self.createCPC(values)

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
    # TASK 5 Part A
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def drawCPC(self, currentClass, fig, xCoords, yCoords):                             # Draws the CPC by resizing the figure and creating the graph
        n = len(fig.axes)
        for b in range(n):
            fig.axes[b].change_geometry(n + 1, 1, b + 1)                                # Resizing (row, column, position)
        ax = fig.add_subplot(n + 1, 1, n + 1)

        yMin = min(yCoords) - 1
        yMax = max(yCoords) + 1
        plt.ylim(float(yMin), float(yMax))
        ax.set_xlabel('x')                                                              # Styling the graph
        ax.set_ylabel('y')
        ax.set_title("CPC for Class: " + str(currentClass))
        ax.plot(xCoords, yCoords, '--bo')                                               # Plotting the graph

    def createCPC(self, values):                                                        # This is the "core" method of this task. Calculates CPC values and draws the graph
        xCoords, yCoords = [], []                                                       # Stores the X and Y coordinates
        totalX, totalY, currentClass = 0, 0, 1
        xLength = len(values)                                                           # Number of rows

        fig = plt.figure(figsize=(7, 7))                                                # Sizing the subplots and spacing
        fig.subplots_adjust(hspace=.5)
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
                    self.drawCPC(currentClass, fig, xCoords, yCoords)                   # Draw the CPC
                    xCoords.clear()                                                     # Reset everything for next class
                    yCoords.clear()
                    totalX, totalY = 0, 0
                    currentClass = currentClass + 1
                    xCoords.append(float(values[i][j]))                                 # Store the first x-value of next class
                    totalX = float(values[i][j])
        self.drawCPC(currentClass, fig, xCoords, yCoords)                               # Draws the last CPC
        fig.tight_layout()
        plt.show()                                                                      # Displays the figure


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    values = [[]]
    obj = project()
    obj.API(values)


if __name__ == '__main__':
    main()
