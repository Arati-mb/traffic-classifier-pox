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

## How to Run

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
```
## Proof of Execution
###  POX Controller Started
<img width="820" height="613" alt="WhatsApp Image 2026-04-16 at 10 41 32 AM" src="https://github.com/user-attachments/assets/35155fbd-90bb-49f1-8985-faf2f0f2e575" />
Controller started + switch connected + background packets detected
```
```
### ICMP Traffic Classification Output in POX Controller

<img width="813" height="619" alt="WhatsApp Image 2026-04-16 at 10 41 52 AM" src="https://github.com/user-attachments/assets/3b939f91-1a67-45de-90c0-a621e0132193" />
```
```
###UDP & TCP Traffic Classification in POX Controller
<img width="496" height="252" alt="WhatsApp Image 2026-04-16 at 10 44 41 AM" src="https://github.com/user-attachments/assets/63f897db-1785-427c-960d-93a24791089b" />
```
```
###Mininet Network Setup and Connectivity Test
<img width="809" height="619" alt="WhatsApp Image 2026-04-16 at 10 45 22 AM" src="https://github.com/user-attachments/assets/8310250c-0d64-4ab0-a15d-f57e0b05a0cf" />
```
```
###ICMP Ping Communication Between Hosts (h1 → h2)
<img width="811" height="613" alt="WhatsApp Image 2026-04-16 at 10 45 45 AM" src="https://github.com/user-attachments/assets/293e90a1-4038-447c-8d84-2ef2091492a4" />
```
```
###UDP Traffic Generation using iperf
<img width="814" height="619" alt="WhatsApp Image 2026-04-16 at 10 46 21 AM" src="https://github.com/user-attachments/assets/7b6a545d-9479-4d55-a147-f91756a5a375" />
```
```
###TCP Traffic (HTTP Communication using wget)
<img width="812" height="608" alt="WhatsApp Image 2026-04-16 at 10 46 42 AM" src="https://github.com/user-attachments/assets/f7302d3d-0457-4b48-a31f-bc94fff3b168" />



















