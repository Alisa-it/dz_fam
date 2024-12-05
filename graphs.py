import matplotlib.pyplot as plt
import numpy as np
from excel_logic import from_variant
from  utils import *

def define_lst(variant):
    global lst
    lst = from_variant(variant)
    define_schema(lst)


# lst = [20, 0.6, 7, 30, 10, 20, 0.4, 0.01, 0.2, 350, 1, 0.2, 400, 290]

schema = 0

def define_h1(schema, lst, s):

    r = lst[6]
    fi = lst[3]
    fi1 = lst[4]

    match schema:

        case 1:
            h1 = s * ((sin(fi) * sin(fi1)) / (sin(fi) + sin(fi1)))
        case 2:
            h1 = r - sqrt((r**2) - ((s / 2)**2))
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
    return h1

def define_h2():

    return 0

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
    return h3

def define_h4(lst):

    rzb = lst[1]
    return rzb

def define_Rz(schema, lst, s):

    v = lst[9]
    hz = lst[8]
    Kh = 0.96
    Kv = 3.5 * (v**(-0.25))

    h1 = define_h1(schema, lst, s)
    h2 = define_h2()
    h3 = define_h3(schema, lst, s)
    h4 = define_h4(lst)

    rz = (h1 + h2 + h3 + h4) * Kv * (1 + (Kh * hz))
    return rz

def create(schema, lst):

    fig, ax = plt.subplots(2, 2)

    s = np.linspace(0.08, 0.6, 60)

    h1 = []
    h3 = []
    h4 = []
    rz = []

    for i in s:
        h1.append(define_h1(schema, lst, i))
        h3.append(define_h3(schema, lst, i))
        h4.append(define_h4(lst))
        rz.append(define_Rz(schema, lst, i))

        
    ax[0, 0].set_title("Зависимость h1(s)") 
    ax[0, 0].set_xlabel("s, мм/об") 
    ax[0, 0].set_ylabel("h1, мкм") 
    ax[0, 0].plot(s, h1, color ="green") 

    ax[0, 1].set_title("Зависимость h3(s)") 
    ax[0, 1].set_xlabel("s, мм/об") 
    ax[0, 1].set_ylabel("h3, мкм") 
    ax[0, 1].plot(s, h3, color ="blue") 

    ax[1, 0].set_title("Зависимость h4(s)") 
    ax[1, 0].set_xlabel("s, мм/об") 
    ax[1, 0].set_ylabel("h4, мкм") 
    ax[1, 0].plot(s, h4, color ="red")

    ax[1, 1].set_title("Зависимость Rz(s)") 
    ax[1, 1].set_xlabel("s, мм/об") 
    ax[1, 1].set_ylabel("Rz, мкм") 
    ax[1, 1].plot(s, rz, color ="black")

    fig.tight_layout()
    plt.show()      

def define_schema(lst):

    r = lst[6]
    s = lst[11]
    fi = lst[3]
    fi1 = lst[4]

    if ((r >= 0) and (r < s/2)):
        schema = 1
    elif ((fi >= arcsin((s/2)/r)) and (fi1 >= arcsin((s/2)/r))):
        schema = 2
    elif ((fi > arcsin((s/2)/r)) and (fi1 <= arcsin((s/2)/r))):
        schema = 3
    elif ((fi <= arcsin((s/2)/r)) and (fi1 > arcsin((s/2)/r))):
        schema = 4
    elif ((fi < arcsin((s/2)/r)) and (fi1 < arcsin((s/2)/r))):
        schema = 5

    print(f'Schema = {schema}')

    h1 = define_h1(schema, lst, s)
    h2 = define_h2()
    h3 = define_h3(schema, lst, s)
    h4 = define_h4(lst)
    rz = define_Rz(schema, lst, s)

    print(f'h1 = {h1}\nh2 = {h2}\nh3 = {h3}\nh4 = {h4}\nRz = {rz}')

    create(schema, lst)

define_lst(2)
