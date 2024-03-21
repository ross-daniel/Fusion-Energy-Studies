#import GUI as gui
#from GUI import MainFrame
#from GUI import ChamberWidget
import PLC as plc

#root = gui.root

if __name__ == "__main__":
    #main_frame = MainFrame(root, 2)
    #main_frame.grid()
    #root.mainloop()
    plc.read_data(50)
