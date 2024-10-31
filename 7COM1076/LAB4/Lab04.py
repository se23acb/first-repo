#!/usr/bin/python
import sys
from mininet.node import Controller
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI_wifi
from mn_wifi.net import Mininet_wifi

def topology(plot):
    "Create a network."
    net = Mininet_wifi(controller=Controller)

    info("*** Creating nodes\n")
    #TODO: Task1, For CW you can amend the following 6 six lines to reflect the CW requirements 
    sta1 = net.addStation('sta1', mac='00:00:00:00:00:02', ip='10.0.0.2/8',position='10,40,0')
    sta2 = net.addStation('sta2', mac='00:00:00:00:00:03', ip='10.0.0.3/8',position='60,40,0')
    TCPS = net.addStation('TCPS', mac='00:00:00:00:00:04', ip='10.0.0.4/8',position='20,20,0')
    UDPS = net.addStation('UDPS', mac='00:00:00:00:00:05', ip='10.0.0.5/8',position='60,20,0')
    ap1 = net.addAccessPoint('ap1', mac ='00:00:00:00:10:02', ssid='ssid-ap1', mode='g', channel='1',position='15,30,0', band='5')
    ap2 = net.addAccessPoint('ap2', mac ='00:00:00:00:10:03', ssid='ssid-ap2', mode='g', channel='6', position='55,30,0', band='5')
    c1 = net.addController('c1')

    net.setPropagationModel(model="logDistance", exp=5)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Creating links\n")
    #TODO: Task2 You can add links here to reflect the cw requirements ( connecting physical links from one AP to another ) 
    net.addLink(ap1, ap2)
 
    #TODO: Task3 (This is where you add mobility to your nodes. Change the variable values below to reflect CW requirements )
    net.plotGraph(min_x=-20, min_y=-10, max_x=90, max_y=70)
    net.startMobility(time=0)
    net.mobility(sta1, 'start', time=5, position='10,40,0') 
    net.mobility(sta1, 'stop', time=15, position='60,40,0')
    net.mobility(sta2, 'start', time=16, position='60,40,0')
    net.mobility(sta2, 'stop', time=25, position='10,40,0')
    net.stopMobility(time=30)

    info("*** Starting network\n")
    net.build()
    c1.start()
    #TODO: Task4 (This is where you turn your APs on) 
    ap1.start([c1])
    ap2.start([c1])

    info("*** Running CLI\n")
    CLI_wifi(net)

    info("*** Stopping network\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    plot = False if '-p' in sys.argv else True
    topology(plot)
