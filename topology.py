import time

from mininet.topo import Topo
from mininet.net  import Mininet
from mininet.cli import CLI
from mininet.node import RemoteController
from mininet.log import setLogLevel


class CustomTopo(Topo):
    "Custom DataCenter topology"

    def build(self):
        # Add hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        
        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')

        # Add host links
        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s3)
        self.addLink(h4, s4)
        self.addLink(h5, s5)

        # Add edge links
        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s2, s4)
        self.addLink(s3, s5)
        self.addLink(s4, s5)


if __name__ == '__main__':
    net = Mininet( topo=CustomTopo(), controller=RemoteController, autoSetMacs = True )
    net.addController(
        name='c1',
        controller=RemoteController,
        ip='127.0.0.1',
        protocol='tcp',
        port=6653
    )
    net.start()
    setLogLevel( 'info' )

    time.sleep(1)

    net.get('h1').sendCmd('python host.py h1')
    net.get('h2').sendCmd('python host.py h2')
    net.get('h3').sendCmd('python host.py h3')
    net.get('h4').sendCmd('python host.py h4')
    net.get('h5').sendCmd('python host.py h5')

    CLI(net)

    net.stop()
