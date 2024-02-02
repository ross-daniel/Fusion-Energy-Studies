import GUI as gui
from GUI import MainFrame
from GUI import ChamberWidget
import snap7

root = gui.root

if __name__ == "__main__":
    main_frame = MainFrame(root, 4)
    main_frame.grid()
    root.mainloop()
