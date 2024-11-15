#!/usr/bin/env python
import sys

from mininet.log import setLogLevel, info
from mn_wifi.link import wmediumd, adhoc
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi
from mn_wifi.wmediumdConnector import interference


def topology(args):
    "Create a network."
    net = Mininet_wifi(link=wmediumd, wmediumd_mode=interference)
    info("*** Creating nodes\n")
    #TODO Add 3 stations
    sta1 = net.addStation('sta1', ip6='fe80::1', position='10,10,0', range=50)
    sta2 = net.addStation('sta2', ip6='fe80::2', position='50,10,0', range=50)
    sta3 = net.addStation('sta3', ip6='fe80::3', position='90,10,0', range=50)
    net.setPropagationModel(model="logDistance", exp=4)

    info("*** Configuring nodes\n")
    net.configureNodes()

    info("*** Creating links\n")
    # MANET routing protocols supported by the following protocols:
    # 'babel', 'batman_adv', 'batmand', 'olsrd', 'olsrd2'
    #TODO Add links and plot graph
    net.plotGraph(max_x=150, max_y=150)
    net.addLink(sta1, cls=adhoc, intf='sta1-wlan0', ssid='adhocNet', mode='g', channel=5, ht_cap='HT40+', proto='batmand')
    net.addLink(sta2, cls=adhoc, intf='sta2-wlan0', ssid='adhocNet', mode='g', channel=5, ht_cap='HT40+', proto='batmand')
    net.addLink(sta3, cls=adhoc, intf='sta3-wlan0', ssid='adhocNet', mode='g', channel=5, ht_cap='HT40+', proto='batmand')
    

    info("*** Starting network\n")
    net.build()
    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    topology(sys.argv)
