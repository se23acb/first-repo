from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI

class MyTopo( Topo ):  
    "Simple topology example."
    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches TODO
        h1 = self.addHost('H1', ip='50.10.10.10/8')
        h2 = self.addHost('H2', ip='50.10.10.11/8')
        h3 = self.addHost('H3', ip='50.10.10.12/8')
        h4 = self.addHost('VS', ip='50.10.10.20/8')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        self.addLink(h1, s2)
        self.addLink(h2, s2)
        self.addLink(h3, s2)
        self.addLink(s1, s2)
        self.addLink(h4, s1)

topos = { 'mytopo': ( lambda: MyTopo() ) } 
