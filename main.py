import GUI as gui
from GUI import MainFrame
from GUI import ChamberWidget

root = gui.root

if __name__ == "__main__":
    main_frame = MainFrame(root, 6)
    main_frame.grid()
    root.mainloop()