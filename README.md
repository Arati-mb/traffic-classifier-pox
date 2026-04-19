# 🚦 SDN Traffic Classification and Analysis using POX

## 📌 Project Overview

This project implements a **Software Defined Networking (SDN)** based traffic classification and analysis system using the **POX controller** and **Mininet**.

It captures packets from the network, classifies them into:

* TCP
* UDP
* ICMP
* Other

and provides **traffic distribution analysis** before and after a traffic spike.

---

## 🎯 Objectives

* Identify TCP, UDP, ICMP packets
* Maintain packet statistics
* Analyze traffic distribution
* Compare network behavior before and after spike

---

## 🛠️ Technologies Used

* Python
* POX Controller
* Mininet
* OpenFlow Protocol
* Ubuntu (Linux)

---

## 🧠 Working Principle

1. Mininet creates a virtual network (hosts + switch)
2. Switch sends packets to POX controller (PacketIn)
3. Controller:

   * Reads raw packet data
   * Identifies protocol (TCP/UDP/ICMP)
   * Updates counters
4. Traffic is divided into:

   * **Before Spike**
   * **After Spike**
5. Final analysis is displayed when program stops

---

## ⚙️ How to Run

### Step 1: Clean Environment

```bash
sudo mn -c
pkill -f pox
```

### Step 2: Run POX Controller

```bash
cd ~/pox
python3.8 pox.py your_file_name
```

### Step 3: Start Mininet

```bash
sudo mn --controller=remote,ip=127.0.0.1,port=6633 --topo single,3
```

### Step 4: Generate Traffic

```bash
pingall
h1 ping h2
h1 iperf -s -u &
h2 iperf -c 10.0.0.1 -u
```

### Step 5: Stop and View Analysis

Press:

```bash
Ctrl + C
```

---

## 📊 Sample Output

```
=========== BEFORE SPIKE ==========
TYPE     TOTAL     PERCENT     AVG PPS
TCP      0         0.00%       0.00
UDP      0         0.00%       0.00
ICMP     18        36.00%      0.46
OTHER    32        64.00%      0.82

=========== AFTER SPIKE ==========
TCP      12        23.08%      ...
UDP      4         7.69%       ...
```

---

## 🔍 Key Features

* Real-time packet classification
* Safe packet parsing (no crashes)
* Traffic distribution analysis
* Before vs After comparison
* Works with TCP, UDP, ICMP traffic

---

## 📚 Concepts Used

* SDN (Software Defined Networking)
* OpenFlow
* PacketIn events
* Traffic Analysis
* Network Protocols (TCP, UDP, ICMP)

---


