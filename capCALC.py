import tkinter as tk
import math

height = 675
width = 800


def grading():
    try:
        inner = float(entry_1.get())
        outer = float(entry_2.get())
        volt = float(entry_v.get())
        layers = int(spin_layers.get())
        e1 = float(scale1.get())
        e2 = float(scale2.get())
        e3 = float(scale3.get())
        e4 = float(scale4.get())
        result_label.place(relx=0.15, relheight=1, relwidth=0.72)

        # calculating thickness of each layer
        epsilon = [e1, e2, e3, e4]
        radii = []
        for i in range(layers-1):
            r = (epsilon[0]*inner)/epsilon[i+1]
            radii.append(r)

        ri = list(map(lambda x: x - inner, radii))
        last = outer - radii[layers-2]
        # print(ri)
        # print(last)

        # cable capacitance
        # voltage difference across each dielectric layer
        # max electric field = V/rln(R/r)
        # e_max & e_min for each layer
        # charging current

        if layers == 2:
            ct = (2*math.pi*8.85*10e-12) / ((1/epsilon[0]) * (math.log(radii[0])/inner) + math.log(outer/inner))
            e_max = volt / (inner * math.log(radii[0] / inner) + radii[0] * math.log(outer / radii[0]))
            v1 = e_max * math.log(radii[0]/inner)
            v2 = e_max * math.log(outer/radii[0])
            e1_max = v1 / (inner * math.log(radii[0] / inner))
            e1_min = v1 / (radii[0] * math.log(radii[0] / inner))
            e2_max = v2 / (radii[0] * math.log(outer / radii[0]))
            e2_min = v2 / (outer * math.log(outer / radii[0]))
            charging_current = 2 * math.pi * 50 * ct * volt
            result = 'thickness of 1st layer: %.2f cm\nthickness of 2nd layer: %.2f cm \nV1 = %.2f KV\nV2 = %.2f KV\n'\
                     'E1 max = %.2f, E1 min = %.2f KV/cm\nE2 max = %.2f, E2 min = %.2f KV/cm\n' \
                     'total capacitance = %f μF/Km\ncharging current = %f A'\
                     % (ri[0], last, v1, v2, e1_max, e1_min, e2_max, e2_min, ct*10e6, charging_current)
        elif layers == 3:
            e_max = volt / (inner * math.log(radii[0] / inner) + radii[0] * math.log(radii[1] / radii[0])
                            + radii[1] * math.log(outer / radii[1]))
            ct = (2*math.pi*8.85*10e-12) / (
                        (1/epsilon[0]) * (math.log(radii[0])/inner) + (1/epsilon[1]) * math.log(outer/inner))
            # print(ct)
            # qc = volt/(1/epsilon[0] * math.log(radii[0]/inner) + 1/epsilon[1] * math.log(radii[1]/radii[0])
            #           + 1/epsilon[2] * math.log(outer/radii[1]))
            '''v1 = qc * math.log(radii[0]/inner)
            v2 = qc * math.log(radii[1]/radii[0])
            v3 = qc * math.log(outer/radii[1])'''
            v1 = e_max * (inner * math.log(radii[0] / inner))
            v2 = e_max * (inner * math.log(radii[1] / radii[0]))
            v3 = e_max * (inner * math.log(outer / radii[1]))
            e1_max = v1 / (inner * math.log(radii[0] / inner))
            e1_min = v1 / (radii[0] * math.log(radii[0] / inner))
            e2_max = v2 / (radii[0] * math.log(radii[1] / radii[0]))
            e2_min = v2 / (radii[1] * math.log(radii[1] / radii[0]))
            e3_max = v3 / (radii[1] * math.log(outer / radii[1]))
            e3_min = v3 / (outer * math.log(outer / radii[1]))
            charging_current = 2 * math.pi * 50 * ct * volt
            # print(charging_current)
            result = 'thickness of 1st layer: %.2f cm\nthickness of 2nd layer: %.2f cm \n' \
                     'thickness of 3rd layer: %.2f cm\nV1 = %.2f KV\nV2 = %.2f KV\nV3 = %.2f KV\n'\
                     'E1 max = %.2f, E1 min = %.2f KV/cm\nE2 max = %.2f, E2 min = %.2f KV/cm\n' \
                     'E3 max = %.2f, E3 min = %.2f KV/cm\n'\
                     'total capacitance = %f μF/Km\ncharging current = %f A' \
                     % (ri[0], ri[1], last, v1, v2, v3, e1_max, e1_min, e2_max, e2_min, e3_max, e3_min, ct*10e6,
                        charging_current)
        else:
            ct = (2*math.pi*8.85*10e-12) / (
                        (1/epsilon[0]) * (math.log(radii[0])/inner) + (1/epsilon[1]) * math.log(radii[1]/radii[0]) +
                        (1/epsilon[2]) * math.log(outer/radii[1]))
            e_max = volt / (inner * math.log(radii[0] / inner) + radii[0] * math.log(radii[1] / radii[0])
                            + radii[1] * math.log(radii[2] / radii[1]) + radii[2] * math.log(outer / radii[2]))
            v1 = e_max * math.log(radii[0] / inner)
            v2 = e_max * math.log(radii[1] / radii[0])
            v3 = e_max * math.log(radii[2]/radii[1])
            v4 = e_max * math.log(outer/radii[2])
            e1_max = v1 / (inner * math.log(radii[0] / inner))
            e1_min = v1 / (radii[0] * math.log(radii[0] / inner))
            e2_max = v2 / (radii[0] * math.log(radii[1] / radii[0]))
            e2_min = v2 / (radii[1] * math.log(radii[1] / radii[0]))
            e3_max = v3 / (radii[1] * math.log(radii[2] / radii[1]))
            e3_min = v3 / (radii[2] * math.log(radii[2] / radii[1]))
            e4_max = v4 / (radii[2] * math.log(outer / radii[2]))
            e4_min = v4 / (outer * math.log(outer / radii[2]))
            charging_current = 2 * math.pi * 50 * ct * volt
            result = 'thickness of 1st layer: %.2f cm\nthickness of 2nd layer: %.2f cm\n' \
                     'thickness of 3rd layer: %.2f cm\nthickness of 4th layer: %.2f cm\n' \
                     'V1 = %.2f KV\nV2 = %.2f KV\nV3 = %.2f KV\nV4 = %.2f KV' \
                     'E1 max = %.2f, E1 min = %.2f KV/cm\nE2 max = %.2f, E2 min = %.2f KV/cm\n' \
                     'E3 max = %.2f, E3 min = %.2f KV/cm\nE4 max = %.2f, E4 min = %.2f KV/cm\n' \
                     'total capacitance = %f μF/Km\ncharging current = %f A' \
                     % (ri[0], ri[1], ri[2], last, v1, v2, v3, v4, e1_max, e1_min, e2_max, e2_min, e3_max, e3_min, e4_max,
                        e4_min, ct*10e6, charging_current)
        results.set(result)

    except:
        result_label.place(relx=0.15, relheight=1, relwidth=0.72)
        results.set('\n\nthere is a problem please try again')


def inter_sheath():
    try:
        inner = float(entry_1.get())
        outer = float(entry_2.get())
        volt = float(entry_v.get())
        layers = int(spin_layers.get())
        result_label.place(relx=0.15, relheight=1, relwidth=0.72)
        r = []
        # radius = []
        for i in range(layers):
            ans = pow(outer/inner, i/layers) * inner
            r.append(ans)

        alpha = pow(outer/inner, 1/layers)
        v = []
        denimenator = 0
        num = 0
        for i in range(layers):
            denimenator += pow(alpha, i)
            num = denimenator
        for i in range(layers - 1):
            num -= pow(alpha, layers - i - 1)
            v.append(((pow(alpha, i + 1)) * num * volt) / denimenator)
        Emax = [(volt - v[0])/(inner * math.log(alpha))]
        Emin = [(volt - v[0])/(r[1] * math.log(alpha))]
        v.append(0)
        r.remove(r[0])
        for i in range(layers - 1):
            if i == layers - 1:
                ans = abs((v[layers - 2])/r[layers - 2])
                Emax.append(ans)
                ans = abs((v[layers - 2])/outer)
                Emin.append(ans)
            elif i == layers - 2:
                ans = abs((v[layers - 3] - v[layers - 2])/(r[layers - 3] * math.log(alpha)))
                Emax.append(ans)
                ans = abs((v[layers - 3] - v[layers - 2]) / (r[layers - 2] * math.log(alpha)))
                Emin.append(ans)
            else:
                ans = abs((v[i] - v[i+1])/(r[i] * math.log(alpha)))
                Emax.append(ans)
                ans = (v[i] - v[i+1])/(r[i + 1] * math.log(alpha))
                Emin.append(ans)
        if layers == 2:
            result = 'position of layer: %.2f cm\ninter-sheath voltage of layer is: %.2f kV\n' \
                     'Emax 1: %.2f ,Emin 1: %.2f kV/cm\n' \
                     'Emax 2: %.2f ,Emin 2: %.2f kV/cm\n' \
                     % (r[0], v[0], Emax[0], Emin[0], Emax[1], Emin[1])
            results.set(result)
        elif layers == 3:
            result = 'position of 1st layer: %.2f cm\nposition of 2nd layer: %.2f cm\n' \
                     'inter-sheath voltage of 1st layer is: %.2f kV\ninter-sheath voltage of 2nd layer is: %.2f kV\n'\
                     'Emax 1: %.2f ,Emin 1: %.2f kV/cm\n' \
                     'Emax 2: %.2f ,Emin 2: %.2f kV/cm\n' \
                     'Emax 3: %.2f ,Emin 3: %.2f kV/cm\n' \
                     % (r[0], r[1], v[0], v[1], Emax[0], Emin[0], Emax[1], Emin[1], Emax[2], Emin[2])
            results.set(result)
        else:  # 4 layers
            result = 'position of 1st layer: %.2f cm\nposition of 2nd layer: %.2f cm\nposition of 3rd layer: %.2f cm\n'\
                     'inter-sheath voltage of 1st layer is: %.2f kV\ninter-sheath voltage of 2nd layer is: %.2f kV\n' \
                     'inter-sheath voltage of 3rd layer is: %.2f kV\n' \
                     'Emax 1: %.2f ,Emin 1: %.2f kV/cm\n' \
                     'Emax 2: %.2f ,Emin 2: %.2f kV/cm\n' \
                     'Emax 3: %.2f ,Emin 3: %.2f kV/cm\n' \
                     'Emax 4: %.2f ,Emin 4: %.2f kV/cm\n' \
                     % (r[0], r[1], r[2], v[0], v[1], v[2], Emax[0], Emin[0], Emax[1], Emin[1], Emax[2], Emin[2]
                        , Emax[3], Emin[3])
            results.set(result)
    except:
        result_label.place(relx=0.15, relheight=1, relwidth=0.72)
        results.set('\n\nthere is a problem please try again')


def permittivity():
    entries = spin_layers.get()
    if entries == '2':
        label_7.place_forget()
        label_8.place_forget()
        scale3.place_forget()
        scale4.place_forget()
    if entries == '3':
        label_7.place(relx=0.5, rely=0.48, relheight=0.13, relwidth=0.19)
        label_8.place_forget()
        scale3.place(relx=0.7, rely=0.465, relheight=0.185, relwidth=0.17)
        scale4.place_forget()

    elif entries == '4':
        label_7.place(relx=0.5, rely=0.48, relheight=0.13, relwidth=0.19)
        label_8.place(relx=0.5, rely=0.66, relheight=0.13, relwidth=0.19)
        scale3.place(relx=0.7, rely=0.465, relheight=0.185, relwidth=0.17)
        scale4.place(relx=0.7, rely=0.655, relheight=0.185, relwidth=0.17)


root = tk.Tk()
slider_1 = tk.DoubleVar()
slider_2 = tk.DoubleVar()
slider_3 = tk.DoubleVar()
slider_4 = tk.DoubleVar()
# slider.trace("r", lambda name, index, mode, slider=slider: permittivity())
spin = tk.IntVar()
results = tk.StringVar()
spin.trace("r", lambda name, index, mode, spin=spin: permittivity())
default_voltage = tk.DoubleVar()
default_voltage.set(25)  # default voltage
root.title("capacitance calc")
canvas = tk.Canvas(root, height=height, width=width, bd=0)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=7)
frame.place(relwidth=1, relheight=0.5)

result_frame = tk.Frame(root, bg='#80c1ff', bd=7)
result_frame.place(rely=0.5, relwidth=1, relheight=0.5)

# inner radius
label_1 = tk.Label(frame, text='Inner radius (cm)', font=('Georgia', 12), justify='center', bd=5)
label_1.place(relx=0.15, rely=0.12, relheight=0.13, relwidth=0.19)

entry_1 = tk.Entry(frame, font=('Georgia', 12), justify='center')
entry_1.place(relx=0.35, rely=0.12, relwidth=0.1, relheight=0.13)

# outer radius
label_2 = tk.Label(frame, text='Outer radius (cm)', font=('Georgia', 12), justify='center', bd=5)
label_2.place(relx=0.15, rely=0.3, relheight=0.13, relwidth=0.19)

entry_2 = tk.Entry(frame, font=('Georgia', 12), justify='center')
entry_2.place(relx=0.35, rely=0.3, relwidth=0.1, relheight=0.13)

# number of layers
label_3 = tk.Label(frame, text='no. of layers', font=('Georgia', 12), justify='center', bd=5)
label_3.place(relx=0.15, rely=0.48, relheight=0.13, relwidth=0.19)

spin_layers = tk.Spinbox(frame, font=('Georgia', 12), justify='center', from_=2, to=4, state='readonly',
                         command=lambda: permittivity())
spin_layers.place(relx=0.35, rely=0.48, relheight=0.13, relwidth=0.1)

# permittivity of used dielectric
label_4 = tk.Label(frame, text='Permittivity 1', font=('Georgia', 12), justify='center', bd=5)
label_4.place(relx=0.5, rely=0.12, relheight=0.13, relwidth=0.19)

label_6 = tk.Label(frame, text='Permittivity 2', font=('Georgia', 12), justify='center', bd=5)
label_6.place(relx=0.5, rely=0.3, relheight=0.13, relwidth=0.19)

label_7 = tk.Label(frame, text='Permittivity 3', font=('Georgia', 12), justify='center', bd=5)

label_8 = tk.Label(frame, text='Permittivity 4', font=('Georgia', 12), justify='center', bd=5)

scale1 = tk.Scale(frame, font=('Georgia', 9), from_=1.5, to=5.5, orient='horizontal', resolution=0.1, var=slider_1,
                  sliderlength=20)
scale1.place(relx=0.7, rely=0.085, relheight=0.185, relwidth=0.17)

scale2 = tk.Scale(frame, font=('Georgia', 9), from_=1.5, to=5.5, orient='horizontal', resolution=0.1, var=slider_2,
                  sliderlength=20)
scale2.place(relx=0.7, rely=0.275, relheight=0.185, relwidth=0.17)

scale3 = tk.Scale(frame, font=('Georgia', 9), from_=1.5, to=5.5, orient='horizontal', resolution=0.1, var=slider_3,
                  sliderlength=20)

scale4 = tk.Scale(frame, font=('Georgia', 9), from_=1.5, to=5.5, orient='horizontal', resolution=0.1, var=slider_4,
                  sliderlength=20)


# voltage
label_5 = tk.Label(frame, text='Default voltage (KV)', font=('Georgia', 12), justify='center', bd=5)
label_5.place(relx=0.15, rely=0.65, relheight=0.13, relwidth=0.19)

entry_v = tk.Entry(frame, font=('Georgia', 12), justify='center', textvariable=default_voltage)
entry_v.place(relx=0.35, rely=0.65, relwidth=0.1, relheight=0.13)

# calculation
capacitance_grading = tk.Button(frame, text='Capacitance grading', font=('Georgia', 12), justify='center',
                                command=lambda: grading())
capacitance_grading.place(relx=0.15, rely=0.85, relwidth=0.3, relheight=0.15)

interSheath = tk.Button(frame, text='Inter-sheath', font=('Georgia', 12), justify='center',
                        command=lambda: inter_sheath())
interSheath.place(relx=0.55, rely=0.85, relwidth=0.3, relheight=0.15)

# result
result_label = tk.Label(result_frame, font=('arial', 18), justify='left', bg='#e6e6e6', anchor='n', bd=5,
                        textvariable=results)

root.iconbitmap('cable.ico')
root.mainloop()
