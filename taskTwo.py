#!/usr/bin/env python
import sys
from mininet.net import Mininet
from mininet.node import Controller, OVSController
from mininet.link import TCLink

from mininet.log import setLogLevel, info
from mn_wifi.link import wmediumd, adhoc
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi
from mn_wifi.wmediumdConnector import interference
#from mininet.link import TCLink
#from mininet.node import Controller, OVSKernelAP


def topology(args):
    "Create a network."
    net = Mininet_wifi(link=wmediumd, wmediumd_mode=interference, controller=Controller)
    #net = Mininet(controller=Controller, link=TCLink)
    info("*** Creating nodes\n")
    #TODO Add 3 stations
    #c0 = net.addController('c0')
    #ap1 = net.addAccessPoint('AP1', ssid='ssid-AP1', mode='g', channel='1', position='45,20', range=50)
    sta1 = net.addStation('STA1', ip6='fe47::11', mac='00:00:00:00:00:11', position='20,10,0', range=30, antennaGain=5, antennaHeight=1)
    sta2 = net.addStation('STA2', ip6='fe47::12', mac='00:00:00:00:00:12', position='45,10,0', range=30, antennaGain=6, antennaHeight=2)
    sta3 = net.addStation('STA3', ip6='fe47::13', mac='00:00:00:00:00:13', position='70,10,0', range=30, antennaGain=7, antennaHeight=3)
    net.setPropagationModel(model="logDistance", exp=4)

    info("*** Configuring nodes\n")
    net.configureNodes()

    info("*** Creating links\n")
    # 'babel', 'batman_adv', 'batmand', 'olsrd', 'olsrd2'
    # using batman_adv protocol works fine
    #TODO Add links and plot graph
    net.plotGraph(min_x=-20, min_y=-40, max_x=120, max_y=100)
    net.addLink(sta1, cls=adhoc, intf='STA1-wlan0', ssid='adhocUH', mode='g', channel=5, ht_cap='HT40+', proto='olsrd')
    net.addLink(sta2, cls=adhoc, intf='STA2-wlan0', ssid='adhocUH', mode='g', channel=5, ht_cap='HT40+', proto='olsrd')
    net.addLink(sta3, cls=adhoc, intf='STA3-wlan0', ssid='adhocUH', mode='g', channel=5, ht_cap='HT40+', proto='olsrd')
    
    info("*** Starting network\n")
    net.build()
    #ap1.start([c0])

    #sta1.cmd('iperf -s -u -p 5006 -i1')
    #sta2.cmd('iperf -c' + 'STA1.IP()' + '-u -p 5006 -t 20 -b 1M')
    #for sta in net.stations:
        #sta.cmd('iw dev {}-wlan0 interface add mon0 type monitor' .format(sta.name))
        #sta.cmd('ifconfig mon0 up')

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    topology(sys.argv)
