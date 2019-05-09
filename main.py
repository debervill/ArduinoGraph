import serial
import logging
import re
import matplotlib.pyplot as plt
import time
import pylab


def main():
    print("1")
    logging.basicConfig(filename='ard.log',
                        level=logging.DEBUG,
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S')
    logging.info("Program Started")

    splitPattern = '\W*\d{1}.\d{2}'

    serPort = serial.Serial('COM3')
    res = serPort.readline()


    fig = plt.gcf()
    fig.suptitle("Графики перемещения по осям X, Y,Z")
    gs = fig.add_gridspec(2, 2)

    ax = fig.add_subplot(gs[0, 0])
    ax.set_title("Перемещение по Х")

    ay = fig.add_subplot(gs[0, 1])
    ay.set_title("Перемещеение по Y")

    az = fig.add_subplot(gs[1, 0])
    az.set_title("Перемещеение по Z")

    fig.show()

    x, y,z, dot = [], [],[], []
    i = 0
    while 1>0:
        logging.warning(serPort.readline().decode('UTF-8'))
        data = re.findall(splitPattern, serPort.readline().decode('UTF-8'))
        logging.warning(data)
        i = i + 1
        dot.append(i)
        x.append(float(data[0]))
        y.append(float(data[1]))
        z.append(float(data[2]))

        ax.plot(dot, x, color='b')
        ay.plot(dot, y, color='r')
        az.plot(dot, z, color='g')

        fig.canvas.draw()

        time.sleep(0.1)


if __name__ == '__main__':
    main()
