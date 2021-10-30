import matplotlib.pyplot as plt
import numpy as np
divisions=["div_A","div_B","div_C","div_D","div_E"]
division_average_marks=[70,82,73,65,68]

plt.bar(divisions,division_average_marks, color='green')
plt.title("bar graph")
plt.xlabel("divisions")
plt.ylabel("marks")
plt.show()