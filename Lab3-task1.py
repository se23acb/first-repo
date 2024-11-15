#!/usr/bin/python

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


def topology():
    "Create a network."
    net = Mininet_wifi()

    info("*** Creating nodes\n")
    #TODO add stations and  access points
    


    c1 = net.addController('c1')
    net.setPropagationModel(model="logDistance", exp=5)
    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()
    #TODO add link and plot graph
    

 
    #TODO create a mobility scenario
    #net.plotGraph(min_x=-20, min_y=-10, max_x=90, max_y=70)
    
    info("*** Starting network\n")
    net.build()
    #TODO start aps
    
    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()
