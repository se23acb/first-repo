#!/usr/bin/python
import sys
from mininet.node import Controller
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi

def topology():
    info("**creating network**\n")
    net = Mininet_wifi()

    info("**creating nodes**\n")
    ap1 = net.addAccessPoint('ap1', mac='00:00:00:00:00:00', ssid='AP1', mode='g', channel='1', position='10,135', band='5', range=35)
    ap2 = net.addAccessPoint('ap2', mac='00:00:00:00:00:01', ssid='AP2', mode='g', channel='1', position='45,100', band='5', range=35)
    ap3 = net.addAccessPoint('ap3', mac='00:00:00:00:00:02', ssid='AP3', mode='g', channel='1', position='75,135', band='5', range=35)
    ap4 = net.addAccessPoint('ap4', mac='00:00:00:00:00:03', ssid='AP4', mode='g', channel='1', position='110,50', band='5', range=50)
    ap5 = net.addAccessPoint('ap5', mac='00:00:00:00:00:04', ssid='AP5', mode='g', channel='1', position='160,50', band='5', range=50)
    sta1 = net.addStation('iphone5', mac='00:00:00:00:00:10', ip='192.168.50.11/24', position='15,115', range=20, min_v=1, max_v=5)
    sta2 = net.addStation('ipad', mac='00:00:00:00:00:11', ip='192.168.50.12/24', position='20,130', range=20, min_v=5, max_v=10)
    sta3 = net.addStation('macbook', mac='00:00:00:00:00:12', ip='192.168.50.13/24', position='140,10', range=20, min_v=2, max_v=7)
    c0 = net.addController('c0')
    net.setPropagationModel(model="logDistance", exp=5)

    info("**configuring wifi nodes**\n")
    net.configureWifiNodes()
    net.addLink(ap1, ap2)
    net.addLink(ap2, ap3)
    net.addLink(ap3, ap4)
    net.addLink(ap4, ap5)
    net.plotGraph(max_x=200, max_y=200)

    net.startMobility(time=0)
    net.mobility(sta1, 'start', time=10, position='15,115')
    net.mobility(sta1, 'stop', time=20, position='115,10')
    net.mobility(sta2, 'start', time=30, position='20,130')
    net.mobility(sta2, 'stop', time=60, position='150,10')
    net.mobility(sta3, 'start', time=25, position='140,10')
    net.mobility(sta3, 'stop', time=60, position='15,120')
    net.stopMobility(time=120)

    info("**starting network**\n")
    net.build()
    c0.start()
    ap1.start([c0])
    ap2.start([c0])
    ap3.start([c0])
    ap4.start([c0])
    ap5.start([c0])

    info("**running CLI**\n")
    CLI(net)

    info("**stopping network**\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    plot = False if '-p' in sys.argv else True
    topology()