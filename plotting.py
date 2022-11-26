import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def animate(i):
    pullData = open("twitter-out.txt", "r").read()
    lines = pullData.split('\n')

    xar = []
    yar = []
    color = "black"
    x = 0
    y = 0

    for l in lines[-200:]:
        x += 1
        if "1" in l:
            y += 1
        elif "0" in l:
            y -= 1
        if y < 0:
            color = 'red'
        else:
            color = 'green'
        xar.append(x)
        yar.append(y)

    ax1.clear()
    plt.ylabel('Sentiment Value')
    plt.xlabel('Number of Tweets')
    ax1.plot(xar, yar, color=color)


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()