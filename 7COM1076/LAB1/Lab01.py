from mininet.topo import Topo  
class MyTopo( Topo ):  
    "Simple topology example."
    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches TODO
        
	
	
        # Add links TODO 
	
	
topos = { 'mytopo': ( lambda: MyTopo() ) } 
