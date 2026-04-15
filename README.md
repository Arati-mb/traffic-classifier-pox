#  Traffic Classification using POX (SDN)

##  Project Overview

This project implements a **Traffic Classifier** using the POX Software Defined Networking (SDN) controller. It monitors network traffic in real-time and classifies packets into different types based on protocol.

---

##  Objectives

* Classify network traffic into:

  * **ICMP (Ping)**
  * **UDP (iperf)**
  * **TCP (HTTP / wget)**
* Understand SDN architecture using POX and Mininet
* Analyze real-time packet flow in a network
---

##  Technologies Used

* **Python 3.8**
* **POX Controller**
* **Mininet Network Emulator**
* **OpenFlow Protocol**

---

##  How It Works

* The POX controller listens for **PacketIn events**
* Each incoming packet is analyzed
* Based on protocol type:

  * ICMP → Printed as *ICMP Packet*
  * UDP → Printed as *UDP Packet*
  * TCP → Printed as *TCP Packet*
* Other packets (like ARP) are classified as *Other Packet*

---

---

## ▶️ How to Run

###  Start POX Controller

```
cd ~/pox
python3.8 pox.py forwarding.l2_learning traffic_classifier
```

---

### Start Mininet

```
sudo mn --controller=remote,ip=127.0.0.1,port=6633 --topo single,3
```

---

###  Test Connectivity

```
pingall
```

---

###  Generate Traffic

#### ICMP (Ping)

```
h1 ping h2
```

#### UDP (iperf)

```
h1 iperf -s -u &
h2 iperf -c 10.0.0.1 -u
```

#### TCP (HTTP)

```
h1 python3 -m http.server 80 &
h2 wget http://10.0.0.1
```

---

## Expected Output

In POX controller terminal:

```
ICMP Packet
UDP Packet
TCP Packet
```


