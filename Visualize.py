import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.signal import butter, lfilter, freqz
import os
import numpy as np
import scipy.fftpack

# from matplotlib import style

# style.use("fivethirtyeight")

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y



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
        self.ysfilter = []
        self.ysdiff = []
        self.flag = False
        self.showing_datapoints = 1000
        self.T = 1.0 / 800.0
        self.fig, self.ax = plt.subplots(2, 1)
        # filter para
        self.order = 1
        self.fs = 10
        self.cutoff = 0.3
        self.filterwindowwidth = 1000
        self.filterdiff = []

        plt.ion()
        plt.show(block = False)



    def animate(self, data, two = False):
        oridata = data
            # if (len(data) == 0):
            #     return
            # self.ax.set_ylim(ylim)
            # background = self.fig.canvas.copy_from_bbox(self.ax.bbox)
        t = type(oridata)
        try:
            if (t is float or t is int):
                self.ys.append(data)
            elif(t is list):
                if (len(oridata) <= 0):
                    return
                else:
                    if (len(self.ys) > 0):
                        self.ysdiff.append(float(oridata[0]) - self.ys[-1])
                    diffdata =  np.diff(np.array(data)).tolist()
                    self.ysdiff += diffdata
                    self.ys += oridata
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
        # self.ax[2].clear()
        # self.ax[3].clear()
        # visulize the raw data
        # breath diff
        # yss = np.diff(self.ys)
        yss = self.ys
        xss = np.array(range(len(yss)))

        if (len(self.ys) >= self.showing_datapoints):
            self.ys = self.ys[-self.showing_datapoints:]
            self.ysdiff = self.ysdiff[-self.showing_datapoints:]
            # tmpx = np.linspace(0.0, (self.showing_datapoints - 1) * self.T, self.showing_datapoints)
            # tmpy = np.interp(tmpx, np.array(range(len(self.ys))) * self.T, self.ys)
            # yf = scipy.fftpack.fft(tmpy)
            # xf = np.linspace(0.0, 1.0 / (2.0 * self.T), self.showing_datapoints // 2)
            # self.ax[1].plot(xf, 2.0/self.showing_datapoints * np.abs(yf[:self.showing_datapoints//2]))
        if (len(self.ys) >= self.filterwindowwidth):
            tmp = butter_lowpass_filter(self.ys[-self.filterwindowwidth:], self.cutoff, self.fs, self.order)
            self.ysfilter += tmp.tolist()
            if (len(self.ysfilter) > self.showing_datapoints):
                self.ysfilter = self.ysfilter[-self.showing_datapoints:]
            yss3 = self.ysfilter[100:]
            xss3 = np.array(range(len(yss3))) / 18
            self.ax[0].plot(xss3, yss3)
            self.ax[0].set_ylim([400, 600])
            self.ax[0].set_ylabel("Bits")
            self.ax[0].set_xlabel("Time/s")
            self.filterdiff = np.diff(self.ysfilter)
            yss4 = self.filterdiff[100:]
            xss4 = np.array(range(len(yss4)))/18
            self.ax[1].plot(xss4, yss4)
            self.ax[1].set_ylim([-10,10])
            self.ax[1].set_ylabel("Diff of Bits")
            self.ax[1].set_xlabel("Time/s")
        #
        # yss = self.ys
        # xss = np.array(range(len(yss)))
        # self.ax[0].plot(xss,yss)
        # self.ax[0].set_ylim([400,600])
        #
        #
        # yss2 = self.ysdiff
        # xss2 = np.array(range(len(yss2)))
        # self.ax[1].set_ylim([-15,15])
        # self.ax[1].plot(xss2,yss2)


        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        plt.pause(0.00001)
        # if (not self.flag):
        #     print "show"
        #     self.flag = True
        #     plt.show()

    # ani = animation.FuncAnimation(fig, animate, interval = 1)
    # plt.show()
