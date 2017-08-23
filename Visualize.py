import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
# from matplotlib import style

# style.use("fivethirtyeight")

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

xs = []
ys = []

showing_datapoints = 5000
DATA_BASE_PATH = "./CollectedData/"
file_prefix = "test"

# br_path = os.path.join(DATA_BASE_PATH, file_prefix,file_prefix + "_BIO_summary")
br_path = os.path.join(DATA_BASE_PATH, file_prefix,file_prefix + "_BIO_breathing")


def animate(i):
    ax.clear()
    ys = []
    flag = 0
    with open(br_path, "r") as f:
        for line in f:
            if (flag == 0):
                flag += 1
                continue
            line = line[:-1]
            split = line.split(",")
            try:
                ys.append(float(split[3]))
            except:
                pass


    yss = ys[-showing_datapoints:]
    xss = range(showing_datapoints)
    ax.plot(xss,yss)

ani = animation.FuncAnimation(fig, animate, interval = 1)
plt.show()
