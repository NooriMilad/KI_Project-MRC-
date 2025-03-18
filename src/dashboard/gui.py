from tkinter import Tk, Label, Button, Text, StringVar, Frame
import datetime

class Dashboard:
    def __init__(self, master):
        self.master = master
        master.title("License Plate Recognition Dashboard")

        self.plate_var = StringVar()
        self.status_var = StringVar()
        self.stats = {
            "total_cars": 0,
            "access_granted": 0,
            "access_denied": 0
        }

        self.create_widgets()

    def create_widgets(self):
        self.frame = Frame(self.master)
        self.frame.pack()

        self.webcam_label = Label(self.frame, text="Webcam Feed")
        self.webcam_label.grid(row=0, column=0, columnspan=2)

        self.plate_label = Label(self.frame, textvariable=self.plate_var, font=("Helvetica", 24))
        self.plate_label.grid(row=1, column=0, columnspan=2)

        self.status_label = Label(self.frame, textvariable=self.status_var, font=("Helvetica", 24))
        self.status_label.grid(row=2, column=0, columnspan=2)

        self.stats_text = Text(self.frame, height=10, width=30)
        self.stats_text.grid(row=3, column=0, columnspan=2)

        self.update_button = Button(self.frame, text="Update Display", command=self.update_display)
        self.update_button.grid(row=4, column=0)

        self.quit_button = Button(self.frame, text="Quit", command=self.master.quit)
        self.quit_button.grid(row=4, column=1)

        self.update_statistics()

    def update_display(self, plate, status):
        self.plate_var.set(plate)
        self.status_var.set(status)
        self.update_statistics()

    def update_statistics(self):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.stats["total_cars"] += 1  # Increment total cars for each update
        self.stats_text.delete(1.0, "end")
        self.stats_text.insert("end", f"Current Time: {current_time}\n")
        self.stats_text.insert("end", f"Total Cars: {self.stats['total_cars']}\n")
        self.stats_text.insert("end", f"Access Granted: {self.stats['access_granted']}\n")
        self.stats_text.insert("end", f"Access Denied: {self.stats['access_denied']}\n")

    def log_access(self, granted):
        if granted:
            self.stats["access_granted"] += 1
        else:
            self.stats["access_denied"] += 1

def main():
    root = Tk()
    dashboard = Dashboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()