from mininet.topo import Topo
class MyTopo( Topo ):
    "simple topology example"
    def __init__( self ):
        "create custom topo"

        Topo.__init__( self )

        Host1 = self.addHost( 'h1', mac='00:00:00:00:00:11', ip='192.168.40.10/24' )
        Host2 = self.addHost( 'h2', mac='00:00:00:00:00:12', ip='192.168.40.11/24' )
        Server1 = self.addHost( 'sv1', mac='00:00:00:00:00:90', ip='20.0.0.2/8' )
        Server2 = self.addHost( 'sv2', mac='00:00:00:00:00:91', ip='40.0.0.2/8' )
	Server3 = self.addHost( 'sv3', mac='00:00:00:00:00:92', ip='60.0.0.2/8' )

        Switch1 = self.addSwitch( 's1' )
        Switch2 = self.addSwitch( 's2' )
        Switch3 = self.addSwitch( 's3' )
        Switch4 = self.addSwitch( 's4' )
        Switch5 = self.addSwitch( 's5' )

        self.addLink( Host1, Switch4 )
        self.addLink( Host2, Switch5 )
        self.addLink( Server1, Switch1 )
        self.addLink( Server2, Switch1 )
        self.addLink( Server3, Switch1 )
        self.addLink( Switch1, Switch2 )
        self.addLink( Switch1, Switch3 )
        self.addLink( Switch2, Switch4 )
	self.addLink( Switch2, Switch5 )
	self.addLink( Switch3, Switch4 )
	self.addLink( Switch3, Switch5 )
	self.addLink( Switch4, Switch5 )

topos = { 'mytopo': ( lambda: MyTopo() ) }
