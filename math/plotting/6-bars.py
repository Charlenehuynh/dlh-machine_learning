#!/usr/bin/env python3
''' lot a stacked bar graph'''
import numpy as np
import matplotlib.pyplot as plt


def bars():
    ''' number of fruit various people possess'''
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))
    plt.ylabel("Quantity of Fruit")
    labels = ['Farrah', 'Fred', 'Felicia']
    x = np.arange(len(labels))
    width = 0.5
    apples = fruit[0]
    bananas = fruit[1]
    oranges = fruit[2]
    peaches = fruit[3]
    plt.bar(x, apples, width=width, color='red', label='apples')
    plt.bar(x, bananas, bottom=apples, width=width,
            color='yellow', label='bananas')
    plt.bar(x, oranges, bottom=bananas + apples,
            width=width, color='#ff8000', label='oranges')
    plt.bar(x, peaches, bottom=oranges + bananas + apples,
            width=width, color='#ffe5b4', label='peaches')
    plt.xticks(x, labels)
    plt.yticks(np.arange(0, 81, 10))
    plt.legend(loc='upper right')
    plt.ylim(0, 80)
    plt.title("Number of Fruit per Person")
    plt.show()


bars()
