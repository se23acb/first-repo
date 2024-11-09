#!/usr/bin/python
import sys
#from mininet.node import Controller
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi

def topology(plot):
    "Create a network."
    net = Mininet_wifi()

    info("*** Creating nodes\n")
    #TODO: Task1
    
    


    c1 = net.addController('c1')
    net.setPropagationModel(model="logDistance", exp=5)
    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()
    info("*** Creating links\n")
    #TODO: Task2
     
    #TODO: Task3
     
    c1.start()
    #TODO: Task4
    
    info("*** Starting network\n")
    net.build()
    info("*** Running CLI\n")
    CLI(net)
    info("*** Stopping network\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    plot = False if '-p' in sys.argv else True
    topology(plot)
 
