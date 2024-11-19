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
        
        # Add hosts and switches with VLAN support
        h1 = self.addHost('h1', mac='00:00:00:00:00:01', ip='10.10.10.11/24')
        h2 = self.addHost('h2', mac='00:00:00:00:00:02', ip='10.10.10.12/24')
        h3 = self.addHost('h3', mac='00:00:00:00:00:03', ip='10.10.10.13/24')
        h4 = self.addHost('h4', mac='00:00:00:00:00:04', ip='10.10.10.14/24')
        server = self.addHost('server', mac='00:00:00:00:00:05', ip='10.10.10.15/24', cls=VLANHost, vlan=100)
        client = self.addHost('client', mac='00:00:00:00:00:06', ip='10.10.10.16/24', cls=VLANHost, vlan=100)
        # Add switches
        switch1 = self.addSwitch('s1', cls=OVSSwitch, failmode='standalone', stp=True)
        switch2 = self.addSwitch('s2', cls=OVSSwitch, failmode='standalone', stp=True)
        switch3 = self.addSwitch('s3', cls=OVSSwitch, failmode='standalone', stp=True)
        switch4 = self.addSwitch('s4', cls=OVSSwitch, failmode='standalone', stp=True)
        # Add links
        self.addLink(h1, switch1)
        self.addLink(h2, switch1)
        self.addLink(h3, switch1)
        self.addLink(h4, switch4)
        self.addLink(server, switch1)
        self.addLink(client, switch4)
        self.addLink(switch1, switch2)
        self.addLink(switch1, switch3)
        self.addLink(switch2, switch4)
        self.addLink(switch3, switch4)

topos = { 'mytopo': (lambda: MyTopo()) }

