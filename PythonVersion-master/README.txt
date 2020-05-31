This file shows the general format for the interface and how backends will generally be used to the front end.

CLASS - classes will be the frames/section of the window. There will also be one main class that handles creating and
    implementing the frame classes.

Methods/Function - these function serve many roles such as: creating/layout widgets, do actions. Functions can also
    serve as smaller sections of the "bigger frames" since you can essentially put frames in frames.

Widgets - widgets are anything the user will interact with like buttons, labels, canvas's, holders for graphs, etc...





*** This is just an Example to help explain the layout concept when utilizing classes more for modularity. ***
--------------------------------------------------------------------------------------------------------------

Class topFrame()
    def __init__() # Like a constructor, when the class is created, this is usually  called to initialize this classes components
        createWidget()
        ...

    def createWidget()
        doSomething
        ...

    def doSomething()
    .
    .
    .

Class MidFrame()
    def leftSide()
        # widgets
        ...
    def center()
        # graphing
        ...
    def rightSide()
        # more widgets if needed
    .
    .
    .

Class BotFrame()
    .
    .
    .

Class Main()
    .
    .
    .
    # Create frames
    ...
    # Layout frames
    ...


# This is basically what loops tkinter, specifically the root.mainloop does it.
if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()