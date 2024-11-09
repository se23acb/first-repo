#!/usr/bin/python
import sys
from mininet.node import Controller
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


def topology():
    info("***Create a network.\n")
    net = Mininet_wifi()

    info("*** Creating nodes\n")
    #TODO add stations and  access points
    sta1 = net.addStation('sta1', mac='00:00:00:00:00:02', ip='10.0.0.2/8', position='10,55,0', range=20, min_v=1, max_v=5, passwd='123', authmode='wpa2')
    sta2 = net.addStation('sta2', mac='00:00:00:00:00:03', ip='10.0.0.3/8', position='45,40,0', range=20, min_v=5, max_v=10, passwd='123', authmode='wpa2')
    sta3 = net.addStation('sta3', mac='00:00:00:00:00:04', ip='10.0.0.4/8', position='5,50,0', range=20, min_v=2, max_v=7, passwd='123', authmode='wpa2')
    #TCPS = net.addStation('TCPS', mac='00:00:00:00:00:04', ip='10.0.0.4/8', position='20,20,0', range=20)
    #UDPS = net.addStation('UDPS', mac='00:00:00:00:00:05', ip='10.0.0.5/8', position='60,20,0', range=20)
    ap1 = net.addAccessPoint('ap1', mac='00:00:00:00:10:02', ssid='ssid-ap1', mode='g', channel='1', position='10,60,0', band='5', range=35, failMode="standalone", passwd='123', authmode='wpa2')
    ap2 = net.addAccessPoint('ap2', mac='00:00:00:00:10:03', ssid='ssid-ap2', mode='g', channel='1', position='40,60,0', band='5', range=35, failMode="standalone", passwd='123', authmode='wpa2')
    ap3 = net.addAccessPoint('ap3', mac='00:00:00:00:10:04', ssid='ssid-ap3', mode='g', channel='1', position='25,45,0', band='5', range=35, failMode="standalone", passwd='123', authmode='wpa2')
    ap4 = net.addAccessPoint('ap4', mac='00:00:00:00:10:05', ssid='ssid-ap4', mode='g', channel='1', position='45,35,0', band='5', range=50, failMode="standalone", passwd='123', authmode='wpa2')
    ap5 = net.addAccessPoint('ap5', mac='00:00:00:00:10:06', ssid='ssid-ap5', mode='g', channel='1', position='80,18,0', band='5', range=50, failMode="standalone", passwd='123', authmode='wpa2')

    c1 = net.addController('c1')
    net.setPropagationModel(model="logDistance", exp=5)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()
    #TODO add link and plot graph
    net.addLink(ap1, ap2)
    net.addLink(ap2, ap3)
    net.addLink(ap3, ap4)
    net.addLink(ap4, ap5)

    net.plotGraph(max_x=150, max_y=150)
 
    #TODO create a mobility scenario
    net.startMobility(time=0)
    net.mobility(sta1, 'start', time=10, position='10,45,0')
    net.mobility(sta1, 'stop', time=20, position='60,20,0')
    net.mobility(sta2, 'start', time=30, position='60,40,0')
    net.mobility(sta2, 'stop', time=60, position='0,90,0')
    net.mobility(sta3, 'start', time=25, position='5,50,0')
    net.mobility(sta3, 'stop', time=60, position='40,0,0')
    net.stopMobility(time=60)
    #net.plotGraph(min_x=-20, min_y=-10, max_x=90, max_y=70)
    
    info("*** Starting network\n")
    net.build()
    c1.start()
    #TODO start aps
    ap1.start([c1])
    ap2.start([c1])
    ap3.start([c1])
    ap4.start([c1])
    ap5.start([c1])

    

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    plot = False if '-p' in sys.argv else True
    topology()
