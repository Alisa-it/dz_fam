import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons
import numpy as np
from excel_logic import from_variant
from  utils import *

def define_lst(variant):
    global lst, var_nums
    lst, var_nums = from_variant(variant)
    
schema = 0
variant = 1

def define_h1(schema, lst, s):

    r = lst[6]
    fi = lst[3]
    fi1 = lst[4]

    match schema:

        case 1:
            h1 = s * ((sin(fi) * sin(fi1)) / (sin(fi) + sin(fi1)))
        case 2:
            h1 = r - sqrt(abs((r**2) - ((s / 2)**2)))
        case 3:
            fi0 = arccos((r - (s * sin(fi1))) / r) - fi1
            a = r * ((cos(fi1) - cos(fi0)) / (tg(fi1)))
            h1 = r * (1 - cos(fi1)) + (a * tg(fi1))
        case 4:
            fi0 = arccos((r - (s * sin(fi))) / r) - fi
            a = r * ((cos(fi) - cos(fi0)) / (tg(fi)))
            h1 = r * (1 - cos(fi)) + (a * tg(fi))
        case 5:
            b = (((s - (r * (sin(fi) + sin(fi1)))) * tg(fi1)) - (r * (cos(fi1) - cos(fi)))) / (tg(fi) + tg(fi1))
            h1 = (r * (1 - cos(fi))) + (b * tg(fi))
    return h1 * 1000

def define_h2(lst, s):
    t = lst[10]
    hb = lst[14]
    rzi = lst[0]
    j = 400 
    py = 0.0027*(t**1.20)*(s**0.75)*(hb**1.3) 
    pyr = 0.0027*((t - (rzi/1000))**1.20)*(s**0.75)*(hb**1.3)
    h2 = (py - pyr) / j
    return h2
 

def define_h3(schema, lst, s):

    r = lst[6]
    fi = lst[3]
    fi1 = lst[4]
    ro = lst[7]
    sigb = lst[12]
    sigt = lst[13]

    ts = 0.75 * sigb
    bs = 0.5 * ro * (1 - (ts / sqrt((ts**2) + (sigt**2))))
    
    match schema:

        case 1:
            h3 = bs / ((1 / tg(fi)) + (1 / tg(fi1)))
        case 2:
            h3 = (bs * ((2 * s) + bs)) / (32 * r)
        case 3:
            h3 = bs / ((1 / tg(fi1)) + ((2 * r) / s))
        case 4:
            h3 = bs / ((1 / tg(fi)) + ((2 * r) / s))
        case 5:
            h3 = bs / ((1 / tg(fi)) + (1 / tg(fi1)))
    return h3 * 1000

def define_h4(lst):

    rzb = lst[1]
    return rzb 

def define_Rz(schema, lst, s):

    v = lst[9]
    hz = lst[8]
    Kh = 0.96
    Kv = 3.5 * (v**(-0.25))

    h1 = define_h1(schema, lst, s)
    h2 = define_h2(lst, s)
    h3 = define_h3(schema, lst, s)
    h4 = define_h4(lst)

    rz = (h1 + h2 + h3 + h4) * Kv * (1 + (Kh * hz))
    return rz     

def change_variant(label):
        variant = {}

        for num in var_nums:
            variant[str(num)] = num

        create(variant[label])

def define_schema():
    
    global schema

    r = lst[6]
    s = lst[11]
    fi = lst[3]
    fi1 = lst[4]

    if ((r >= 0) and (r < s/2)):
        schema = 1
    elif ((fi >= arcsin(s/2/r)) and (fi1 >= arcsin(s/2/r))):
        schema = 2
    elif ((fi > arcsin(s/2/r)) and (fi1 <= arcsin(s/2/r))):
        schema = 3
    elif ((fi <= arcsin(s/2/r)) and (fi1 > arcsin(s/2/r))):
        schema = 4
    elif ((fi < arcsin(s/2/r)) and (fi1 < arcsin(s/2/r))):
        schema = 5

    print(f'Schema = {schema}')

    h1 = define_h1(schema, lst, s)
    h2 = define_h2(lst, s)
    h3 = define_h3(schema, lst, s)
    h4 = define_h4(lst)
    rz = define_Rz(schema, lst, s)

    print(f'h1 = {h1}\nh2 = {h2}\nh3 = {h3}\nh4 = {h4}\nRz = {rz}')

def create(variant):
    
    define_lst(variant)
    
    fig, ax = plt.subplots(2, 3, figsize=(10, 6.5))
    rax = plt.axes([0.9, 0.1, 0.1, 0.85], facecolor='white')
    radio = RadioButtons(rax, tuple(var_nums))

    define_schema()

    s = np.linspace(0.08, 0.4, 60)

    h1 = []
    h2 = []
    h3 = []
    rz = []

    for i in s:
        h1.append(define_h1(schema, lst, i))
        h2.append(define_h2(lst, i))
        h3.append(define_h3(schema, lst, i))
        rz.append(define_Rz(schema, lst, i))

        
    ax[0, 0].set_title("Зависимость h1(s)") 
    ax[0, 0].set_xlabel("s, мм/об") 
    ax[0, 0].set_ylabel("h1, мкм") 
    ax[0, 0].plot(s, h1, color ="green") 

    ax[0, 1].set_title("Зависимость h2(s)") 
    ax[0, 1].set_xlabel("s, мм/об") 
    ax[0, 1].set_ylabel("h2, мкм") 
    ax[0, 1].plot(s, h2, color ="red")

    ax[1, 0].set_title("Зависимость h3(s)") 
    ax[1, 0].set_xlabel("s, мм/об") 
    ax[1, 0].set_ylabel("h3, мкм") 
    ax[1, 0].plot(s, h3, color ="blue") 

    ax[1, 1].set_title("Зависимость Rz(s)") 
    ax[1, 1].set_xlabel("s, мм/об") 
    ax[1, 1].set_ylabel("Rz, мкм") 
    ax[1, 1].plot(s, rz, color ="black")

    ax[0, 2].set_axis_off()
    ax[1, 2].set_axis_off()

    fig.text(0.7, 0.55, f'Вариант {variant}\n\nRzi = {lst[0]} мкм\nRzb = {lst[1]} мкм\nλ = {lst[2]}°\nϕ = {lst[3]}°\nϕ1 = {lst[4]}°\nγ = {lst[5]}°\nr = {lst[6]} мм\nρ = {lst[7]} мм\nhz = {lst[8]} мм\nv = {lst[9]} м/мин\nt = {lst[10]} мм\ns = {lst[11]} мм/об\n', fontsize = 12)
    fig.text(0.7, 0.3, f'h1 = {'{:f}'.format(define_h1(schema, lst, lst[11]))} мкм\nh2 = {'{:f}'.format(define_h2(lst, lst[11]))} мкм\nh3 = {'{:f}'.format(define_h3(schema, lst, lst[11]))} мкм\nh4 = {define_h4(lst)} мкм\nRz = {'{:f}'.format(define_Rz(schema, lst, lst[11]))} мкм', fontsize = 12)
    fig.canvas.manager.set_window_title(f'Домашнее задание ФАМО. Вариант №{variant}')
    fig.tight_layout()
    
    radio.on_clicked(change_variant)
    plt.show() 

create(variant)
