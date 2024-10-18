from math import sin, cos, tan, asin, acos, sqrt
mark = 'Д16'
group = 'Алюминиевый сплав'
sig_b = 400
sig_02 = 290
delt = 9
hb = 1050
e1 = 72
mu1 = 0.33
km = 0.95
rzi = 20
rzb = 0.6
lamb = 7
phi = 30
phi1 = 10
gamma = 20
r = 0.4
ro = 0.01
hz = 0.2
v = 350
t = 1
s = 0.2

sh = 0

if (r >= 0) and (r <= (s/2)):
    sh = 1
    print('Схема 1')
    b = (s - r * (sin(phi) + cos(phi1)) - (r * (cos(phi1) - cos(phi)) / tan(phi1))) * (tan(phi1) / (tan(phi) + tan(phi1)))
    h1 = r * (1 - cos(phi)) + b * tan(phi)

elif (phi >= asin(s/2/r)) and (phi1 >= asin(s/2/r)):
    sh = 2
    print('Схема 2')
    h1 = r - sqrt((r ** 2) - ((s / 2) ** 2))

elif (phi > asin(s/2/r)) and (phi1 <= asin(s/2/r)):
    sh = 3
    print('Схема 3')
    phi0 = acos((r - s * sin(phi1)) / r) - phi1
    a = (r * (cos(phi1) - cos(phi0))) / tan(phi1)
    h1 = r * (1 - cos(phi1)) + a * tan(phi1)

elif (phi <= asin(s/2/r)) and (phi1 > asin(s/2/r)):
    sh = 4
    print('Схема 4')
    phi0 = acos((r - s * sin(phi)) / r) - phi
    a = (r * (cos(phi) - cos(phi0))) / tan(phi)
    h1 = r * (1 - cos(phi)) + a * tan(phi)

elif (phi < asin(s/2/r)) and (phi1 < asin(s/2/r)):
    sh = 5
    print('Схема 5')
    b = ((s - r * (sin(phi) + sin(phi1))) * tan(phi1) - r * (cos(phi1) - cos(phi))) / (tan(phi) + tan(phi1))
    h1 = r * (1 - cos(phi) + b * tan(phi))

h2 = 0  # узнать

tao_s = 0.75 * sig_b

b_s = 0.5 * ro * (1 - ((tao_s) / (sqrt((tao_s ** 2) + (sig_02 ** 2)))))

match (sh):
    case (1):
        h3 = b_s / (1 / tan(phi) + (1 / tan(phi1)))
    case (2):
        h3 = (b_s * ((2 * s) + b_s))/ (32 * r)
    case (3):
        h3 = b_s / ((1 / tan(phi1)) + (2 * r) / s)
    case (4):
        h3 = b_s / ((1 / tan(phi)) + (2 * r) / s)
    case (5):
        h3 = b_s / (1 / tan(phi) + (1 / tan(phi1)))

h4 = rzb

kv = 3.5 * (v ** (-0.25))
kh = 0.96

rz = (h1 + h2 + h3 + h4) * kv * (1 + (kh * hz))

print(f'h1 = {h1}, h2 = {h2}, h3 = {h3}, h4 = {h4}, Kv = {kv}, Rz = {rz}')