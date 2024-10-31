import matplotlib.pyplot as plt
import numpy as np
from excel_logic import from_variant
from  utils import *

def define_lst(variant):
    global lst
    lst = from_variant(variant)
    create_graph(lst)

scheme = "0"
Kh = 0.96
lst_bol = False

def schema_definition(s, r, φ, φ1):
    φ0 = 0
    A = 0
    if φ == φ1:
        if s > 2 * r * sin(φ1):
            scheme = 5
        else:
            scheme = 2

    elif φ > φ1:
        φ0 = grad(arccos((r - s * sin(φ1)) / r) - math.radians(φ1))
        A = (r * (cos(φ1) - cos(φ0))) / tg(φ1)
        if s < 2 * r * sin(φ1):
            scheme = 2
        elif s > sin(φ) + r * sin(φ1) + A:
            scheme = 5
        else:
            scheme = 3

    elif φ < φ1:

        fi0 = grad(arccos((r - s * sin(φ)) / r) - math.radians(φ))
        A = (r * (cos(φ1) - cos(φ0 * 180 / 3.1416))) / tg(φ)

        if s < 2 * r * sin(φ):
            scheme = 2
            
        elif s > r * sin(φ) + r * sin(φ1) + A:
            scheme = 5
        else:
            scheme = 4
    return(scheme, φ0)

def h1_definition(s):

    scheme, φ0 = schema_definition(s, lst[7-1], lst[4-1], lst[5-1])

    r = lst[7-1]
    φ = lst[4-1]
    φ1 = lst[5-1]

    match scheme:
        case (1):
            h1 = s * (((sin(φ)) * sin(φ1)) / (sin(φ) * cos(φ1) + sin(φ1) * cos(φ)))
        case (2):
            h1 = r - sqrt(math.pow(r, 2) - math.pow((s / 2), 2))
        case (3):
            h1 = r * (1 - cos(φ0))
        case (4):
            h1 = r * (1 - cos(φ0))
        case (5):
            x1 = (s - r * (sin(φ) + sin(φ1))) * tg(φ1)
            x2 = r * tg(φ) * (cos(φ1) - cos(φ))
            x3 = tg(φ) + tg(φ1)
            B = (x1 - x2) / x3
            h1 = r * (1 - cos(φ)) + B * tg(φ)
    return (h1*1000)

def h3_definition(s):
    r = lst[7-1]
    φ = lst[4-1]
    φ1 = lst[5-1]
    ρ = lst[8-1]
    σ_b = lst[13-1]
    σ_t = lst[14-1]

    τ_s = 0.75 * σ_b
    x1 = math.sqrt(math.pow(τ_s,2)+math.pow(σ_t,2))
    b_s = 0.5 * (1000 * ρ * (1 - (τ_s / x1)))
    scheme, fi0 = schema_definition(s, lst[7-1], lst[4-1], lst[5-1])
    if scheme == 1 or scheme == 5:
        h3 = b_s / ((1 / tg(φ)) + 1 / tg(φ1))
    elif scheme == 2:
        h3 = (b_s * (2 * s + b_s)) / (32 * r)
    elif scheme == 3:
        h3 = b_s / ((1 / tg(φ1)) + (2 * (r / s)))
    elif scheme == 4:
        h3 = b_s / ((1 / tg(φ)) + ((2 * r) / s))
    else:
       h3 = 0
    return (h3 * 1000)

def Rz_definition(h1, h3):
    Kv = 3.5 * (math.pow(lst[10-1], -0.25))
    h4 = lst[1]
    hz = lst[8] / 1000
    Rz = (h1 + h3 + h4) * Kv * (1 + (Kh * hz))
    return (Rz)

def create_graph(lst):
    
    plt.figure(figsize=(10, 6)) 
    plt.get_current_fig_manager().set_window_title('Домашнее задание по дисциплине "Финишные и абразивные методы обработки"')
     
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    xRz = []
    yRz = []

    for i in np.arange(0.08, 0.61, 0.01):
        x1.append(round(i, 3))
        y1.append(h1_definition(round(i, 3)))

        x2.append(round(i, 3))
        y2.append(h3_definition(round(i, 3)))

        xRz.append(round(i, 3))
        yRz.append(Rz_definition(h1_definition(round(i, 3)), h3_definition(round(i, 3))))

    plt.subplots_adjust(left=0.1, right=1, top=0.9, bottom=0.1, wspace=0.4, hspace=0.4)

    ax1 = plt.subplot(1, 3, 1)
    plt.plot(x1, y1, "r", label="h1(s)")
    ax1.set_xlabel("s, мм/об")
    ax1.set_ylabel('h1, мкм')
    plt.legend()

    text_1 = (f'Параметры при s = {str(lst[11])} мм/об:\n-  h1 = {str(round(h1_definition(lst[12-1]), 3))} мкм\n-  h3 = {str(round(h3_definition(lst[12-1]),3))} мкм\n-  h4 = {str(round(lst[1],3))} мкм\n-  Rz = {str(round((Rz_definition(h1_definition(lst[12-1]),h3_definition(lst[12-1]))),3))} мкм.')
    plt.text(-0.5, -0.3, text_1, ha='left', transform=plt.gca().transAxes)
    plt.legend()

    ax2 = plt.subplot(1, 3, 2)
    plt.plot(x2, y2, label="h3(s)")
    ax2.set_xlabel("s, мм/об")
    ax2.set_ylabel('h2, мкм')
    plt.legend()

    ax3 = plt.subplot(1, 3, 3)
    plt.plot(xRz, yRz, label="Rz(s)", color="green")
    ax3.set_xlabel("s, мм/об")
    ax3.set_ylabel('Rz, мкм')
    plt.legend()

    plt.tight_layout()
    plt.show()
