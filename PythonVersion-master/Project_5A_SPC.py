# Phillipe Shin
# 01/21/2019
# SMART Data Visualization
import csv                                                                                          # This section sets up the program and reads the file into values[][]
import matplotlib
from matplotlib.patches import ConnectionPatch
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

class project(object):
    def API(self, values):
        self.ReadFile(values)
        self.sortGraph(values)
        
    def ReadFile(self, values):                                                      
        with open('input.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            count = 0
            for line in csv_reader:
                values.append([])
                line=list(line)
                for i in line:
                    values[count].append(i)
                count = count + 1

    def drawSPC(self, currentClass, fig, ogX, ogY):                                                 # Draws the CPC by resizing the figure and creating the graph
        for currentIndex in range(len(ogX)):
            n = len(fig.axes)
            for b in range(n):
                fig.axes[b].change_geometry(currentClass, len(ogX), b+1)                            # Resizing (row, column, position)
            ax = fig.add_subplot(currentClass, len(ogX), n+1)
                
            ax.set_xlabel("X " + str(currentIndex * 2 + 1))                                         # Styling the graph
            ax.set_ylabel("X " + str(currentIndex * 2 + 2))
            if (currentIndex == 0):
                ax.set_title("SPC for Class: " + str(currentClass))
            xMin = min(ogX) - 1
            xMax = max(ogX) + 1
            yMin = min(ogY) - 1
            yMax = max(ogY) + 1
            plt.xlim(float(xMin), float(xMax))
            plt.ylim(float(yMin), float(yMax))
            ax.plot(ogX[currentIndex], ogY[currentIndex],'r')                                        # Plotting the graph
            pax = fig.axes[n]


            if (currentIndex > 0):
                xy = (ogX[currentIndex - 1], ogY[currentIndex - 1])                                  # These are for original values to be graphed in SPC
                ab = (ogX[currentIndex], ogY[currentIndex])
                con = ConnectionPatch(xyA=ab, xyB=xy, coordsA="data", coordsB="data",
                      axesA=fig.axes[n], axesB=fig.axes[n - 1], color="purple")
                pax.add_artist(con)                                                                                                      
                pax.plot(ogX[currentIndex],ogY[currentIndex],'ro',markersize=10)                     # Plot the SPC points on each graph
            else:
                pax.plot(ogX[currentIndex],ogY[currentIndex],'ro',markersize=10)                     # Plot the SPC points on each graph

    def sortGraph(self, values):                                                                     # Read and process csv values
        ogX, ogY =[], []
        currentClass = 1
        xLength = len(values)                                                                        # Number of rows
        fig = plt.figure(currentClass, figsize=(8, 8))  # Sizing the subplots and spacing

        for i in range(1, (xLength - 1)):                                                            # Exclude IDS from data
            yLength = len(values[i])                                                                 # Number of columns
            for j in range(1, (yLength - 1)):                                                        # Exclude IDs from data
                if (int(values[i][yLength - 1]) == currentClass):                                    # Process each class
                    if ((len(ogX)) <= (len(ogY))):                                                   # X-values for graph
                        ogX.append(float(values[i][j]))                                              # Store the original x-value for graph
                    else:                                                                            # Y-values for graph
                        ogY.append(float(values[i][j]))                                              # Store the original y-value for graph
                else:
                    self.drawSPC(currentClass, fig, ogX, ogY)                                        # Draw the CPC
                    ogX.clear()                                                                      # Reset everything for next class
                    ogY.clear()
                    currentClass = currentClass +1
                    ogX.append(float(values[i][j]))                                                  # Store the first x-value of next class

        self.drawSPC(currentClass, fig, ogX, ogY)                                                    # Draw the last SPC (not included in for loop)
        fig.tight_layout()
        plt.show()                                                                                   # Displays the figure
        
                                                                               
def main():
        values = [[]]
        obj = project()
        obj.API(values)

if __name__ == '__main__':
    main()
