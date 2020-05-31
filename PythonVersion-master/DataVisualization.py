import tkinter as tk
import csv
import matplotlib

from tkinter.filedialog import (askopenfilename, asksaveasfilename)

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


class TopFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, bg='white', height=45, pady=3)
        self.master = master

        # Create and set all widgets for this frame
        self.createButtons()
        self.createOptionMenu()
        self.createRadioButtons()

    def createButtons(self):
        # create button widgets
        self.browseButton = tk.Button(self, text='Browse')
        self.updateButton = tk.Button(self, text='Update')
        # layout the widgets
        self.browseButton.grid(row=0, column=0)
        self.updateButton.grid(row=1, column=0)

    def createOptionMenu(self):
        # create label & option menu widgets
        self.meaningLabel = tk.Label(self, text='Meaning of Weights:')
        self.weightMeaning = tk.StringVar(self)
        self.weightMeaning.set("distance between nodes")  # default value of drop down
        self.dropDown1 = tk.OptionMenu(self, self.weightMeaning, "distance between nodes", "frequency of communication",
                                       "frequency of visits")
        # layout widgets
        self.meaningLabel.grid(row=0, column=2, padx=(50, 0))
        self.dropDown1.grid(row=0, column=3)

    def createRadioButtons(self):
        # create label & radio buttons widgets
        self.similarityLabel = tk.Label(self, text='Higher Value of the Weight indicates:')
        self.var1 = tk.IntVar()
        self.similarityButton1 = tk.Radiobutton(self, text="higher similarity", variable=self.var1, value=1)
        self.similarityButton2 = tk.Radiobutton(self, text="higher dissimilarity", variable=self.var1, value=2)
        # layout widgets
        self.similarityLabel.grid(row=0, column=4, padx=(50, 0))
        self.similarityButton1.grid(row=1, column=4, sticky='w', padx=(60, 0))
        self.similarityButton2.grid(row=2, column=4, sticky='w', padx=(60, 0))


class CenterFrame(tk.Frame):

    def __init__(self, master, bottomFrame):
        tk.Frame.__init__(self, bg='gray1', padx=3, pady=3)
        self.master = master
        self.createCenterFrameSections()
        self.bottomFrame = bottomFrame

        # create cpc from Phillipe
        #self.values = [[]]
        #self.cpcAPI()
        #self.spcAPI()

    def createCenterFrameSections(self):
        # create the center widgets
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.ctr_left = tk.Frame(self, bg='gray', width=100)
        self.ctr_mid = tk.Frame(self, bg='white')
        self.ctr_right = tk.Frame(self, bg='gray', width=100)

        self.ctr_left.grid(row=0, column=0, sticky="ns")
        self.ctr_mid.grid(row=0, column=1, sticky="nsew")
        self.ctr_right.grid(row=0, column=2, sticky="ns")

    def saveFile(self):
        file = asksaveasfilename(filetypes=(("PNG Image", "*.png"), ("All Files", "*.*")),
                              defaultextension='.png', title="Save")
        if file:
            plt.savefig(file)

    def openFile(self):
        self.file = askopenfilename()
        print(self.file)
        #show default graph
        for widget in self.ctr_mid.winfo_children():                # Clears widgets on the frame
            widget.destroy()
        for widget in self.bottomFrame.winfo_children():                # Clears widgets on the bottom frame
            widget.destroy()
        values = [[]]
        self.ReadFile1(values,self.file)
        self.createSeperateSPC(values)


    def cpcAPI(self):
        for widget in self.ctr_mid.winfo_children():                # Clears widgets on the frame
            widget.destroy()
        for widget in self.bottomFrame.winfo_children():                # Clears widgets on the bottom frame
            widget.destroy()
        values = [[]]
        self.ReadFile1(values,self.file)
        self.createCPCinOne(values)

    def cpcAPI2(self):
        for widget in self.ctr_mid.winfo_children():                # Clears widgets on the frame
            widget.destroy()
        for widget in self.bottomFrame.winfo_children():                # Clears widgets on the bottom frame
            widget.destroy()
        values = [[]]
        self.ReadFile1(values,self.file)
        self.createSeperateCPC(values)

    def spcAPI(self):
        for widget in self.ctr_mid.winfo_children():                # Clears widgets on the frame
            widget.destroy()
        for widget in self.bottomFrame.winfo_children():                # Clears widgets on the bottom frame
            widget.destroy()
        self.values = [[]]
        self.ReadFile2()
        self.createSPC()

    def spcAPI2(self):
        plt.close('all')
        for widget in self.ctr_mid.winfo_children():                # Clears widgets on the frame
            widget.destroy()
        for widget in self.bottomFrame.winfo_children():                # Clears widgets on the bottom frame
            widget.destroy()
        values = [[]]
        self.ReadFile1(values,self.file)
        self.createSeperateSPC(values)

    def ReadFile1(self,values,file):  # Reads values into 2d array
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            count = 0
            for line in csv_reader:
                values.append([])
                line = list(line)
                for i in line:
                    values[count].append(i)
                count = count + 1
        csv_file.close()

    def ReadFile2(self):  # Reads values into 2d array
        with open('input2.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            count = 0
            for line in csv_reader:
                self.values.append([])
                line = list(line)
                for i in line:
                    self.values[count].append(i)
                count = count + 1
        csv_file.close()



    def setToolbar(self, graph):
        toolbar1 = NavigationToolbar2Tk(graph, self.bottomFrame)
        toolbar1.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def createSPC(self):
        values = [row[:] for row in self.values]
        print("")
        print("The matrix has been converted into x and y coordinates")
        ogX = []
        ogY = []
        first = []
        second = []
        xNums = 0
        yNums = 0
        totalx = 0
        totaly = 0

        for i in range(len(values)):
            for j in range(len(values[i])):
                if (int(values[i][j]) > 0):
                    if (xNums <= yNums):                                                            # X-values for graph
                        totalx = int(values[i][j]) + int(totalx)  # Total  distance x
                        first.append(int(totalx))
                        ogX.append(int(values[i][j]))                                               # Original x-values (for SPC)
                        xNums = xNums + 1
                    else:                                                                           # Y-values for graph
                        totaly = int(values[i][j]) + int(totaly)  # Total  distance y
                        second.append(int(totaly))
                        ogY.append(int(values[i][j]))                                               # Original y-values (for SPC)
                        yNums = yNums + 1

                else:
                    continue

        print("CPC Values")                                                                         # Printing coordinate pairs
        for m in range(len(first)):
            print("(" + str(first[m]) + "," + str(second[m]) + ")")

        print("\n SPC values")
        for m in range(len(ogX)):
            print("(" + str(ogX[m]) + "," + str(ogY[m]) + ")")

        fig = plt.figure()                                                                          # Creating the sub plot and plot points
        p1 = fig.add_subplot(131)
        p2 = fig.add_subplot(132)
        p3 = fig.add_subplot(133)

        p1.plot(ogX[0], ogY[0])
        p2.plot(ogX[1], ogY[1])

        xy = (ogX[0], ogY[0])                                                                       # These are for original values to be graphed in SPC
        ab = (ogX[1], ogY[1])
        cd = (ogX[2], ogY[2])
        con = ConnectionPatch(xyA=ab, xyB=xy, coordsA="data", coordsB="data",
                              axesA=p2, axesB=p1, color="purple")
        p2.add_artist(con)

        p1.plot(ogX[0], ogY[0], 'ro', markersize=10)                                                # Plot the SPC points on each graph
        p2.plot(ogX[1], ogY[1], 'ro', markersize=10)
        p3.plot(ogX[2], ogY[2], 'ro', markersize=10)

        print("\nPrinting the SPC for the first two coordinate pairs")
        #plt.show()
        spc = FigureCanvasTkAgg(fig, self.ctr_mid)  # A tk.DrawingArea.
        spc.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.setToolbar(spc)

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # TASK 5 Part A raw All Graphs in SPC separately
    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def drawSPC(self, currentClass, fig, ogX, ogY):                                                 # Draws the CPC by resizing the figure and creating the graph
        for currentIndex in range(len(ogX)):
            n = len(fig.axes)
            for b in range(n):
                fig.axes[b].change_geometry(currentClass, len(ogX), b + 1)                          # Resizing (row, column, position)
            ax = fig.add_subplot(currentClass, len(ogX), n + 1)

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
            ax.plot(ogX[currentIndex], ogY[currentIndex], 'r')                                      # Plotting the graph
            pax = fig.axes[n]

            if (currentIndex > 0):
                xy = (
                ogX[currentIndex - 1], ogY[currentIndex - 1])                                       # These are for original values to be graphed in SPC
                ab = (ogX[currentIndex], ogY[currentIndex])
                con = ConnectionPatch(xyA=ab, xyB=xy, coordsA="data", coordsB="data",
                                      axesA=fig.axes[n], axesB=fig.axes[n - 1], color="purple")
                pax.add_artist(con)
                pax.plot(ogX[currentIndex], ogY[currentIndex], 'ro', markersize=10)                 # Plot the SPC points on each graph
            else:
                pax.plot(ogX[currentIndex], ogY[currentIndex], 'ro', markersize=10)                 # Plot the SPC points on each graph

    def createSeperateSPC(self,values):  # Read and process csv values
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
        dividedSPC = FigureCanvasTkAgg(fig, self.ctr_mid)  # A tk.DrawingArea.
        dividedSPC.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.setToolbar(dividedSPC)





    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def createCPCinOne(self,values):
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
        cpc = FigureCanvasTkAgg(fig, self.ctr_mid)  # A tk.DrawingArea.
        cpc.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.setToolbar(cpc)

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # TASK 5 Part A : Draw All Graphs in CPC separately
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
        ax.plot(xCoords, yCoords, '--bo')

    def createSeperateCPC(self,values):                                                 # This is the "core" method of this task. Calculates CPC values and draws the graph
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
        dividedCPC = FigureCanvasTkAgg(fig, self.ctr_mid)  # A tk.DrawingArea.
        dividedCPC.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.setToolbar(dividedCPC)



class BottomFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, bg='white', height=45, pady=3)
        self.master = master


class MainApplication(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        root.title('Data Visualization')
        root.geometry('{}x{}'.format(1000, 1000))
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        tk.Frame.__init__(self, master, *args, **kwargs)  # define settings upon initialization
        self.master = master  # reference to the master widget, the tk window

        # Call classes to create frames
        #self.topFrame = TopFrame(self)
        self.bottomFrame = BottomFrame(self)
        self.centerFrame = CenterFrame(self, self.bottomFrame)


        tk.Menu.__init__(self, master)
        self.createMenu()

        # root.grid_rowconfigure(1, weight=1)
        # root.grid_columnconfigure(0, weight=1)

        # Set frames in position
        #self.topFrame.grid(row=0, sticky="ew")
        self.centerFrame.grid(row=1, sticky="nsew")
        self.bottomFrame.grid(row=2, sticky="ew")
        root.config(menu=self.menubar)

    def createMenu(self):
        self.menubar = tk.Menu(self)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New")
        self.filemenu.add_command(label="Open", command=self.centerFrame.openFile)
        self.filemenu.add_command(label="Save", command=self.centerFrame.saveFile)
        #self.filemenu.add_command(label="Save as...")
        self.filemenu.add_command(label="Close")
        self.filemenu.add_separator() # adds a line ---
        self.filemenu.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu) # add the FILE menu

        self.viewmenu = tk.Menu(self.menubar, tearoff=0)
        self.viewmenu.add_command(label="Collocated Paired Coordinates (CPC)", command=self.centerFrame.cpcAPI)
        self.viewmenu.add_command(label="Seperated CPC(s)", command=self.centerFrame.cpcAPI2)
        self.viewmenu.add_separator()  # adds a line ---
        self.viewmenu.add_command(label="Shifted Paired Coordinates (SPC)", command=self.centerFrame.spcAPI)
        self.viewmenu.add_command(label="Seperated SPC(s)", command=self.centerFrame.spcAPI2)
        self.menubar.add_cascade(label="View", menu=self.viewmenu) # add the VIEW menu

        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Undo")
        self.editmenu.add_separator() # adds a line ---
        self.editmenu.add_command(label="Cut")
        self.editmenu.add_command(label="Copy")
        self.editmenu.add_command(label="Paste")
        self.editmenu.add_command(label="Delete")
        self.editmenu.add_command(label="Select All")
        self.menubar.add_cascade(label="Edit", menu=self.editmenu) # add the EDIT menu

        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Help Index")
        self.helpmenu.add_command(label="About...")
        self.menubar.add_cascade(label="Help", menu=self.helpmenu) # add the HELP menu



if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root)
    while True:  # Scrolling on trackpad (Mac) throws error
        try:
            root.mainloop()
            break
        except UnicodeDecodeError:
            pass