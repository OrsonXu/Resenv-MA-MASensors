import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
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
        self.fig, self.ax = plt.subplots()
        self.xs = []
        self.ys = []
        self.flag = False
        self.showing_datapoints = 5000
        plt.ion()
        plt.show(block = False)

    def animate(self,data):
        # if (len(data) == 0):
        #     return
        self.ax.clear()
        # self.ax.set_ylim(ylim)
        # background = self.fig.canvas.copy_from_bbox(self.ax.bbox)
        t = type(data)
        try:
            if (t is float or t is int):
                self.ys.append(data)
            elif(t is list):
                if (len(data) <= 0):
                    return
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
        if (len(self.ys) > self.showing_datapoints):
            self.ys = self.ys[-self.showing_datapoints:]
            xss = range(self.showing_datapoints)
        else:
            xss = range(len(self.ys))
        yss = self.ys
        self.ax.plot(xss,yss)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        plt.pause(0.0000001)
        # if (not self.flag):
        #     print "show"
        #     self.flag = True
        #     plt.show()

    # ani = animation.FuncAnimation(fig, animate, interval = 1)
    # plt.show()
