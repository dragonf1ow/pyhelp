import matplotlib.pyplot as plt
import numpy as np

phi = np.linspace(0, 2.*np.pi, 100) # linspace генерирует равномерно распределенные значения в заданном диапазоне
#                   начало   конец    кол-во значений
fmt = '[marker][line][color]'    #для редакции формы размера и цвета линий

fig, ax = plt.subplots()



line1, =ax.plot(phi, np.sin(phi), ":r", label="hui")
line1.set_dash_capstyle("round")
line2, =ax.plot(phi, np.cos(phi), "-^C9", label="hui")
line2.set_dash_capstyle("projecting")

plt.show()
print("proverka")