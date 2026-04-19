from pox.core import core
import pox.openflow.libopenflow_01 as of
import time

log = core.getLogger()

types = ["TCP", "UDP", "ICMP", "OTHER"]

before = {t: 0 for t in types}
after  = {t: 0 for t in types}

packet_counter = 0
SPLIT_POINT = 30

start_time = time.time()


#  SAFE RAW CLASSIFICATION (NO POX PARSER USED)
def classify_packet(data):
    try:
        if len(data) < 14:
            return "OTHER"

        eth_type = int.from_bytes(data[12:14], "big")

        # IPv4
        if eth_type == 0x0800 and len(data) >= 34:
            proto = data[23]

            if proto == 1:
                return "ICMP"
            elif proto == 6:
                return "TCP"
            elif proto == 17:
                return "UDP"

        return "OTHER"

    except:
        return "OTHER"


def _handle_PacketIn(event):
    global packet_counter

    data = event.ofp.data
    ptype = classify_packet(data)

    packet_counter += 1

    if packet_counter <= SPLIT_POINT:
        before[ptype] += 1
    else:
        after[ptype] += 1

    log.info("%s Packet", ptype)

    #  Forward packet safely
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)


def print_table(title, stats, duration):
    total = sum(stats.values())

    log.info("\n=========== %s ==========", title)
    log.info("TYPE     TOTAL     PERCENT     AVG PPS")

    for t in types:
        count = stats[t]
        percent = (count / total * 100) if total > 0 else 0
        pps = (count / duration) if duration > 0 else 0

        log.info("%-8s %-10d %.2f%%     %.2f",
                 t, count, percent, pps)


def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)

    log.info(" Running... Press Ctrl+C to see results")

    def shutdown():
        end_time = time.time()
        total_time = end_time - start_time

        before_time = total_time / 2
        after_time = total_time / 2

        print_table("BEFORE SPIKE", before, before_time)
        print_table("AFTER SPIKE", after, after_time)

    core.addListenerByName("DownEvent", lambda e: shutdown())
