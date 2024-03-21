import tkinter as tk

root = tk.Tk()


class ChamberWidget(tk.Canvas):
    def __init__(self, parent, chamber_num, vacuum_status=False):
        self.chamber_num = chamber_num
        self.vacuum_status = vacuum_status
        self.parent = parent

        self.row = tk.IntVar(0)
        self.label = tk.StringVar()
        self.label.set("Chamber " + str(chamber_num))

        super().__init__(self.parent, width=150, height=80, bg="white", highlightthickness=0)

        self.create_oval(5, 5, 45, 45, fill="gray", outline="black")
        self.label_id = self.create_text(100, 25, text=str(self.label.get()))
        self.bind("<Button-1>", lambda event: self.pump_chamber())

    def pump_chamber(self):
        if self.vacuum_status:
            print(f"Venting {self.label.get()}")
            self.vacuum_status = False
        else:
            print(f"Pumping {self.label.get()}")
            self.vacuum_status = True


class GateWidget(tk.Canvas):
    def __init__(self, parent, gate_num):
        self.parent = parent
        self.gate_num = gate_num
        super().__init__(self.parent, width=10, height=50, bg="gray", highlightthickness=0)
        self.bind("<Button-1>", lambda event: self.open_gate())

    def open_gate(self):
        print(f"Opening Gate Valve {self.gate_num}")


class MainFrame(tk.Frame):
    def __init__(self, parent, num_chambers):
        super().__init__(parent)

        self.parent = parent

        self.chambers = []
        self.gates = []

        for i in range(num_chambers):
            # create the correct number of chamber widgets and add them to the frame
            chamber = ChamberWidget(self, i+1)
            self.chambers.append(chamber)
            chamber.grid(row=i*2, column=0, padx=10, pady=10)
            # add a gate to the left of the chamber unless it's the last chamber
            if i < num_chambers - 1:
                rectangle = GateWidget(self, i+1)
                self.gates.append(rectangle)
                rectangle.grid(row=i*2+1, column=0, padx=10, pady=10)
