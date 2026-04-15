from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.packet import ethernet, ipv4, tcp, udp, icmp

log = core.getLogger()

def _handle_PacketIn(event):
    packet = event.parsed

    if not packet.parsed:
        log.info("Incomplete packet")
        return

    ip_packet = packet.find('ipv4')

    if not ip_packet:
        log.info("Other Packet")
        return

    if ip_packet.protocol == ipv4.ICMP_PROTOCOL:
        log.info("ICMP Packet")

    elif ip_packet.protocol == ipv4.TCP_PROTOCOL:
        log.info("TCP Packet")

    elif ip_packet.protocol == ipv4.UDP_PROTOCOL:
        log.info("UDP Packet")

    else:
        log.info("Other Packet")

def launch():
    def start_switch(event):
        log.info("Switch connected")
        event.connection.addListeners(globals())

    core.openflow.addListenerByName("ConnectionUp", start_switch)
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
