#!/usr/bin/python

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


def topology():
    info("*** Creating network.\n")
    net = Mininet_wifi()

    info("*** Creating nodes\n")
    #TODO add stations and  access points
    sta1 = net.addStation('sta1', mac='00:00:00:00:00:11', ip='192.168.10.11/24', position='105,0', range='116')    
    sta2 = net.addStation('sta2', mac='00:00:00:00:00:22', ip='192.168.10.12/24', position='0,-105', range='116')
    sta3 = net.addStation('sta3', mac='00:00:00:00:00:33', ip='192.168.10.13/24', position='0,345', range='116')
    ap1 = net.addAccessPoint('ap1', wlans=2, ssid='UHWifi', mode='g', channel='1', position='0,0',range='150')
    ap2 = net.addAccessPoint('ap2', wlans=2, ssid='UHWifi', mode='g', channel='1', position='0,300',range='150')
    #ap3 = net.addAccessPoint('ap3', wlans=2, ssid='UHWifi', mode='g', channel='1', position='400,0',range='250')
    c1 = net.addController('c1')

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()
    net.plotGraph(max_x=500, max_y=500)
    net.addLink(sta1, ap1)
    net.addLink(sta2, ap1)
    net.addLink(sta3, ap2)
    net.addLink(ap1, ap2)
    #net.addLink(ap1, ap2)
    #net.addLink(ap2, ap3)
    #net.addLink(ap1, ap3)

    info("*** Starting network\n")
    net.build()
    #TODO start ap1
    ap1.start([c1])
    ap2.start([c1])
    
    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    topology()
