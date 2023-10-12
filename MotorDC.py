import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import serial.tools.list_ports
import control as ctrl
import numpy as np
from matplotlib import pyplot as plt
import serial, time
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import collections, time
from simple_pid import PID


def main():
    root = Tk()
    gui = Proyecto(root)
    gui.root.mainloop()
    return None


class Proyecto:
    def __init__(self, root):
        self.root = root
        self.root.geometry("913x576")
        self.root.resizable(width=False, height=False)
        self.root.title("Lectura de sensor GUI")
        tk.Label(self.root, text="Seleccione puerto de comunicación.", bg='#A42F16', font=("MS Shell Dlg 2", 10)).place(
            x=10, y=40)
        self.selec_port = ttk.Combobox(self.root, values=[''])
        self.selec_port.place(x=45, y=70)
        self.actualizar = tk.Button(self.root, text="Actualizar puertos", command=self.update_ports)
        self.actualizar.place(x=45, y=110)
        tk.Label(self.root, text="Seleccione tiempo de muestreo.", bg='#A42F16', font=("MS Shell Dlg 2", 10)).place(
            x=10, y=150)
        self.selec_bd = ttk.Combobox(self.root, values=['1200', '2400', '9600', '14400', '56000', '115200'])
        self.selec_bd.current(2)
        self.selec_bd.place(x=45, y=180)
        self.conectar_p = tk.Button(self.root, text="Conectar", command=self.conexion_serial)
        self.conectar_p.place(x=70, y=250)

        # -----------------------------------------------------------------------------------------------------
        self.panel_datos = Frame(self.root, width=661, height=521)
        self.panel_datos.pack(fill='both', expand=1)
        self.panel_datos.place(x=240, y=10)
        self.panel_datos.config(bg='#E0CBC7')

        #self.fig = plt.figure()
        #self.ax = self.fig.add_subplot(1, 1, 1)
        self.fig, self.ax = plt.subplots()
        self.x_d1 = []
        self.y_d1 = []
        self.y2_d2 = []

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.panel_datos)
        self.canvas.get_tk_widget().pack()
        self.canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

        #-----------------------------------CONTROL--------------------------------------------------------------
        self.setpoint = 100.0
        #--------------------------------SetSetpoint-------------------------------------------------------------
        self.textSP = ttk.Label(self.root, text="Ingrese SetPoint:").place(x=45, y=370)
        self.setSP = Entry(self.root)
        self.setSP.place(x=45, y=400)
        self.entrySP = ttk.Button(self.root, text="Actualizar SP", command=self.actializarSP)
        self.entrySP.place(x=50, y=430)

    def actializarSP(self, event=None):
        self.setpoint = float(self.setSP.get())


    def update_ports(self, event=None):
        self.ports = list(serial.tools.list_ports.comports())
        if self.ports:
            for self.p in self.ports:
                self.selec_port.set(self.p.name)
        else:
            messagebox.showerror(message="No hay puertos disponibles", title="Alerta!")

    def conexion_serial(self, event=None):
        self.conectar = serial.Serial(port=self.selec_port.get(), baudrate=self.selec_bd.get(), timeout=1,
                                      write_timeout=1)
        self.conectar.close()
        self.conectar.open()
        try:
            self.conectar.write('a'.encode())
            time.sleep(1)
            self.conectar.write('b'.encode())
            messagebox.showinfo(message="Conexión serial completada.", title="Conexión")
            self.selec_port['state'] = tk.DISABLED
            self.selec_bd['state'] = tk.DISABLED
            self.actualizar['state'] = tk.DISABLED
            self.conectar_p['state'] = tk.DISABLED
            self.datos = 30.0;
            def animate(i):
                self.controladorPID(self.datos)
                self.datos = self.conectar.readline().decode().strip()
                self.datos = float(self.datos)
                self.x_d1.append(i)
                self.y_d1.append(self.datos)
                self.y2_d2.append(self.setpoint)
                self.ax.clear()
                self.ax.plot(self.x_d1, self.y_d1, label='Señal del Motor')
                self.ax.plot(self.x_d1, self.y2_d2, label='SetPoint')
                self.ax.legend()
            ani = animation.FuncAnimation(self.fig, animate, frames=1000, interval=100, cache_frame_data=False)
            self.canvas.draw()
        except serial.SerialException:
            messagebox.showinfo(message="Cerrando graficas", title="Alerta")


    def controladorPID(self, cs):
        pid = PID(0.65, 0.65, 0.065)
        pid.setpoint = self.setpoint * (255/100)
        pid.auto_mode = True
        pid.output_limits = (0, 255)
        cv = pid(cs)
        output_str = f"{cv}\n"
        self.conectar.write(output_str.encode())
        print(cv)
        time.sleep(0.2)

    def tomar_datos(self, event=None):
        self.temp.setvar(self.conectar.readline())


if __name__ == "__main__":
    main()