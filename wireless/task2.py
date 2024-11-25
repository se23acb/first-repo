import sys
from mininet.log import setLogLevel, info
from mn_wifi.link import wmediumd, adhoc
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi
from mn_wifi.wmediumdConnector import interference

def topology( args ):
    "Create a network."
    net = Mininet_wifi( link=wmediumd, wmediumd_mode=interference ) 
    # Mininet_wifi func with wireless links specified 
    # simulate signal interference of wireless devices in range transmiting simultanoeusly

    info( "*** Creating nodes\n" )
    sta1 = net.addStation( 'STA1', ip6='2024::11', mac='00:00:00:00:01:11', position='20,10,0', range=30, antennaGain=5, antennaHeight=1 )
    sta2 = net.addStation( 'STA2', ip6='2024::12', mac='00:00:00:00:01:12', position='45,10,0', range=30, antennaGain=6, antennaHeight=2 )
    sta3 = net.addStation( 'STA3', ip6='2024::13', mac='00:00:00:00:01:13', position='70,10,0', range=30, antennaGain=7, antennaHeight=3 )
    net.setPropagationModel( model="logDistance", exp=4 )

    info( "*** Configuring nodes\n" )
    net.configureNodes()

    info( "*** Creating links\n" )
    # testing 'batman_adv', 'batmand', 'olsrd' manet protocol
    net.plotGraph( min_x=-20, min_y=-40, max_x=120, max_y=90 )
    net.addLink( sta1, cls=adhoc, intf='STA1-wlan0', ssid='adhocUH', mode='g', channel=5, ht_cap='HT40+', proto='batman_adv' )
    net.addLink( sta2, cls=adhoc, intf='STA2-wlan0', ssid='adhocUH', mode='g', channel=5, ht_cap='HT40+', proto='batman_adv' )
    net.addLink( sta3, cls=adhoc, intf='STA3-wlan0', ssid='adhocUH', mode='g', channel=5, ht_cap='HT40+', proto='batman_adv' )
    
    info( "*** Starting network\n" )
    net.build()

    info( "*** Running CLI\n" )
    CLI( net )

    info( "*** Stopping network\n" )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology( sys.argv )
