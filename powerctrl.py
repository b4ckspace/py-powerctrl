import serial
import time

class Powerctrl:

    def __init__(self, port, baud=9600):
        self.serial = serial.Serial(port, baud)
        self.ports = [0 for x in xrange(8)]

    def port_set(self, port, value):

        if port < 0 or port > 7:
            raise Exception("Invalid port range")
        
        if value != 1 and value != 0:
            raise Exception("Invalid port value")

        self.ports[port] = value
        self.send("sp%d.%d" % (port,value))

    def port_get(self, port):

        if port < 0 or port > 7:
            raise Exception("Invalid port range")

        return self.ports[port]

    def port_on(self, port):
        self.port_set(port, 1)

    def port_off(self, port):
        self.port_set(port, 0)

    def everything_set(self, value):
        
        if value != 1 and value != 0:
            raise Exception("Invalid port value")

        self.ports = [value for x in xrange(8)]
        self.send("sa%d" % (value))

    def everything_on(self):
        self.everything_set(1)

    def everything_off(self):
        self.everything_set(0)

    def send(self, cmd):
        print cmd
        self.serial.write(cmd+'\r\n')

