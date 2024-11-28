from mininet.topo import Topo  
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSSwitch
from mininet.topo import Topo

class VLANHost(Host):
	def config(self, vlan=100, **params):
        	"""Configure VLANHost with a VLAN."""
        	r = super(Host, self).config(**params)
        	intf = self.defaultIntf()
        	self.cmd('ifconfig %s inet 0' % intf)
        	self.cmd('vconfig add %s %d' % (intf, vlan))
        	self.cmd('ifconfig %s.%d inet %s' % (intf, vlan, params['ip']))
        	newName = '%s.%d' % (intf, vlan)
        	intf.name = newName
        	self.nameToIntf[newName] = intf
        	return r

class MyTopo(Topo):  
	"Simple topology with VLAN support."
    	def __init__(self):
        	"Create custom topology."

	        # Initialize topology
	        Topo.__init__(self)

	        h1 = self.addHost( 'H1', mac='00:00:00:00:15:98', ip='192.170.50.11/24' )
	        h2 = self.addHost( 'H2', mac='00:00:00:00:15:99', ip='192.170.50.12/24' )
	        SERVER1 = self.addHost( 'Sv1', mac='00:00:00:00:16:00', ip='20.0.0.2/8' )
	        SERVER2 = self.addHost( 'Sv2', mac='00:00:00:00:16:01', ip='40.0.0.2/8' )
	        SERVER3 = self.addHost( 'Sv3', mac='00:00:00:00:16:02', ip='60.0.0.2/8' )

	        Switch1 = self.addSwitch( 'Switch1', cls=OVSSwitch )
	        Switch2 = self.addSwitch( 'Switch2', cls=OVSSwitch )
	        Switch3 = self.addSwitch( 'Switch3', cls=OVSSwitch )
	        Switch4 = self.addSwitch( 'Switch4', cls=OVSSwitch )
	        Switch5 = self.addSwitch( 'Switch5', cls=OVSSwitch )

	        self.addLink( h1, Switch4 )
	        self.addLink( h2, Switch5 )
	        self.addLink( SERVER1, Switch1 )
	        self.addLink( SERVER2, Switch1 )
	        self.addLink( SERVER3, Switch1 )
	        self.addLink( Switch1, Switch2 )
	        self.addLink( Switch1, Switch3 )
	        self.addLink( Switch2, Switch4 )
	        self.addLink( Switch2, Switch5 )
	        self.addLink( Switch3, Switch4 )
	        self.addLink( Switch3, Switch5 )
	        self.addLink( Switch4, Switch5 )

topos = { 'mytopo': ( lambda: MyTopo() ) }
