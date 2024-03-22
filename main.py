#import GUI as gui
#from GUI import MainFrame
#from GUI import ChamberWidget
import PLC as client

#root = gui.root

if __name__ == "__main__":
    #main_frame = MainFrame(root, 2)
    #main_frame.grid()
    #root.mainloop()
    client.read_data(50)
