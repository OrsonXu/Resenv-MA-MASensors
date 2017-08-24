import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
import numpy as np
import scipy.fftpack

# from matplotlib import style

# style.use("fivethirtyeight")

class RealtimeVis:
    # xs = []
    # ys = []
    #
    # showing_datapoints = 5000
    # DATA_BASE_PATH = "./CollectedData/"
    # file_prefix = "test"
    #
    # # br_path = os.path.join(DATA_BASE_PATH, file_prefix,file_prefix + "_BIO_summary")
    # br_path = os.path.join(DATA_BASE_PATH, file_prefix,file_prefix + "_BIO_breathing")
    #
    # flag = False

    def __init__(self):
        # self.fig = plt.figure()
        # self.ax = self.fig.add_subplot(1,1,1)
        self.xs = []
        self.ys = []
        self.flag = False
        self.showing_datapoints = 500
        self.T = 1.0 / 800.0
        plt.ion()
        plt.show(block = False)

    def animate(self,data, two = False):
        if (not two):
            self.fig, self.ax = plt.subplots(1,1)
        else:
            self.fig, self.ax = plt.subplots(2,1)
            # if (len(data) == 0):
            #     return
            # self.ax.set_ylim(ylim)
            # background = self.fig.canvas.copy_from_bbox(self.ax.bbox)
        t = type(data)
        try:
            if (t is float or t is int):
                self.ys.append(data)
            elif(t is list):
                if (len(data) <= 0):
                    return
                else:
                    self.ys += data
        except:
            pass
        # ys = []
        # flag = 0
        # with open(br_path, "r") as f:
        #     for line in f:
        #         if (flag == 0):
        #             flag += 1
        #             continue
        #         line = line[:-1]
        #         split = line.split(",")
        #         try:
        #             ys.append(float(split[3]))
        #         except:
        #             pass
        self.ax[0].clear()
        self.ax[1].clear()
        # visulize the raw data
        # breath diff
        # yss = np.diff(self.ys)
        yss = self.ys
        xss = np.array(range(len(yss))) * self.T

        if (len(self.ys) > self.showing_datapoints):
            self.ys = self.ys[-self.showing_datapoints:]
            tmpx = np.linspace(0.0, (self.showing_datapoints - 1) * self.T, self.showing_datapoints)
            tmpy = np.interp(tmpx, np.array(range(len(self.ys))) * self.T, self.ys)
            yf = scipy.fftpack.fft(tmpy)
            xf = np.linspace(0.0, 1.0 / (2.0 * self.T), self.showing_datapoints // 2)
            self.ax[1].plot(xf, 2.0/self.showing_datapoints * np.abs(yf[:self.showing_datapoints//2]))

        yss = self.ys
        xss = np.array(range(len(yss))) * self.T
        self.ax[0].plot(xss,yss)


        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        plt.pause(0.00001)
        # if (not self.flag):
        #     print "show"
        #     self.flag = True
        #     plt.show()

    # ani = animation.FuncAnimation(fig, animate, interval = 1)
    # plt.show()
