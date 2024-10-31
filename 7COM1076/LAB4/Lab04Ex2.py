
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
        Host1 = self.addHost( 'h1' )
        Host2 = self.addHost( 'h2' )
	Host3 = self.addHost( 'h3' )
	Host4 = self.addHost( 'h4' )
	Host5 = self.addHost( 'h5' )
	Host6 = self.addHost( 'h6' )
	Host7 = self.addHost( 'h7' )
	Switch1 = self.addSwitch('s1')
	Switch2 = self.addSwitch('s2')
	Switch3 = self.addSwitch('s3')
	Switch4 = self.addSwitch('s4')
	Switch5 = self.addSwitch('s5')
	Switch6 = self.addSwitch('s6')
        # Add links TODO 
	self.addLink( Host1, Switch1 )
	self.addLink( Host2, Switch1 )
	self.addLink( Host3, Switch1 )
	self.addLink( Switch1, Switch2 )
	self.addLink( Switch2, Switch3 )
	self.addLink( Switch3, Switch4 )
	self.addLink( Switch4, Switch5 )
	self.addLink( Switch5, Switch6 )
	self.addLink( Host4, Switch5 )
	self.addLink( Host5, Switch5 )
        self.addLink( Host6, Switch5 )
	self.addLink( Host7, Switch6 )
	
topos = { 'mytopo': ( lambda: MyTopo() ) } 

