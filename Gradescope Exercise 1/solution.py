import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np

filename = 'stroke_separable.csv'

def load_data(filename):
    data = pd.read_csv(filename)
    age = data['age_years'].tolist()
    hg = data['blood_pressure_mmhg'].tolist()
    cls = data['stroke'].tolist()
    return (age, hg, cls)

def perceptron(age, hg, cls):
    random.seed(10)
    lr = 0.1
    w0 = random.randint(-10, 10)
    w_age = random.randint(-10,10)
    w_hg = random.randint(-10,10)
    x=0

    for i in range(100000000):

        dot = w0 + w_age * age[x] + w_hg*hg[x]
        if cls[x] == 0:
            if dot >= 0:
                w0 = w0 - 0.1
                w_age = w_age - 0.1*age[x]
                w_hg = w_hg - 0.1*hg[x]
        elif cls[x] == 1:
            if dot < 0:
                w0 = w0 + 0.1
                w_age = w_age + 0.1*age[x]
                w_hg = w_hg + 0.1*hg[x]

        if x == len(age) - 1:
            x=0
        else:
            x=x+1
    return w0, w_age, w_hg

age, hg, cls = load_data(filename)
w0, w_age, w_hg = perceptron(age, hg, cls)
print(w0)
print(w_age)
print(w_hg)

colours = []
y_values = []
x_values = []

for i in range(30,80):
    line_value = (-w0 - i * w_age)/w_hg
    y_values.append(line_value)
    x_values.append(i)

for i in range(0, len(cls)):
    if cls[i] == 0:
        colours.append("red")
    else:
        colours.append("green")

plt.scatter(age, hg, c = colours)
plt.scatter(x_values, y_values, color = 'blue')
plt.show()




