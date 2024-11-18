#!/usr/bin/python
import sys
from mininet.node import Controller
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi

#python func to configure wireless network topology
def topology():
    info("**creating network**\n")
    net = Mininet_wifi()

    #channel=1 specifies freq within 2.4GHz, band=5 allows AP to operate on freq band 5GHz
    #mode='g' configure AP to operate at IEEE 802.11g mode (speeds upto 54mbps on 2.4GHz)
    #failMode='standalone' allows AP to operate when connection to controller is lost
    info("**creating nodes**\n")
    ap1 = net.addAccessPoint('AP1', mac='00:00:00:00:00:00', ssid='AP1', mode='g', channel='1', position='30,117.5', band='5', range=35)
    ap2 = net.addAccessPoint('AP2', mac='00:00:00:00:00:01', ssid='AP2', mode='g', channel='1', position='60,117.5', band='5', range=35)
    ap3 = net.addAccessPoint('AP3', mac='00:00:00:00:00:02', ssid='AP3', mode='g', channel='1', position='80,117.5', band='5', range=35)
    ap4 = net.addAccessPoint('AP4', mac='00:00:00:00:00:03', ssid='AP4', mode='g', channel='1', position='135,55', band='5', range=50)
    ap5 = net.addAccessPoint('AP5', mac='00:00:00:00:00:04', ssid='AP5', mode='g', channel='1', position='135,40', band='5', range=50)
    sta1 = net.addStation('STA1', mac='00:00:00:00:00:10', ip='192.168.50.11/24', position='15,115', range=20, min_v=1, max_v=5)
    sta2 = net.addStation('STA2', mac='00:00:00:00:00:11', ip='192.168.50.12/24', position='20,130', range=20, min_v=5, max_v=10)
    sta3 = net.addStation('STA3', mac='00:00:00:00:00:12', ip='192.168.50.13/24', position='140,10', range=20, min_v=2, max_v=7)
    c0 = net.addController('c0') #control for the OpenFlow switches
    net.setPropagationModel(model="logDistance", exp=5) #define the rate of signal loss in the network model

    info("**configuring wifi nodes**\n")
    net.configureWifiNodes()
    net.addLink(ap1, ap2)
    net.addLink(ap2, ap3)
    net.addLink(ap3, ap4)
    net.addLink(ap4, ap5)
    net.plotGraph(min_x=-20, min_y=-10, max_x=200, max_y=180)

    net.startMobility(time=0)
    net.mobility(sta1, 'start', time=10, position='15,115')
    net.mobility(sta1, 'stop', time=20, position='115,10')
    net.mobility(sta2, 'start', time=30, position='20,130')
    net.mobility(sta2, 'stop', time=60, position='150,10')
    net.mobility(sta3, 'start', time=25, position='140,10')
    net.mobility(sta3, 'stop', time=60, position='15,110')
    net.stopMobility(time=120)

    info("**starting network**\n")
    net.build()
    c0.start()
    ap1.start([c0]) #start APs based on configurations from the controller
    ap2.start([c0])
    ap3.start([c0])
    ap4.start([c0])
    ap5.start([c0])

    info("**running CLI**\n")
    CLI(net) #allows interaction with network on a terminal

    info("**stopping network**\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    plot = False if '-p' in sys.argv else True
    topology()
