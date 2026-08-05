# Home Lab Setup Notes

## Architecture Overview

**Red Team (Attack Machine):** Kali Linux -- Kali-Offense-Project1
- IP: 192.168.153.128
- Role: Network scanning, traffic generation, simulated attacks
- Tools installed: Nmap, Metasploit, Wireshark, Netcat

**Blue Team (Defense Machine):** Linux Mint -- Mint-Target-Project1
- IP: 192.168.153.129
- Role: Log monitoring, traffic detection, SIEM
- Tools installed: Splunk Enterprise 10.4.1, UFW, Wireshark, tcpdump

**Hypervisor:** VMware
**Network isolation:** Host-only network between VMs (no external internet exposure)

---

## Network Configuration

- Host-only network segment: 192.168.153.0/24
- Kali Linux (attacker): 192.168.153.128
- Linux Mint (defender): 192.168.153.129
- Network traffic stays contained within hypervisor -- no risk to external networks

---

## Completed Exercises

### Exercise 1 - Network Reconnaissance with Nmap
**Date:** July 2026
**Status:** Complete

Commands used:
```
nmap -sn 192.168.153.0/24
nmap -sV 192.168.153.129
nmap -A 192.168.153.129
```

**Lesson:** Even a default Linux install exposes services on the network. Understanding what is running is the first step in reducing attack surface.

---

### Exercise 2 - Splunk SIEM Install and Log Ingestion
**Date:** August 4, 2026
**Status:** Complete

- Installed Splunk Enterprise 10.4.1 on Mint-Target-Project1 (localhost:8000)
- Configured /var/log directory monitor data input (recursive)
- 76,234 events ingested and confirmed in Search dashboard

**Lesson:** Raw log volume is high. Filtering and focused SPL queries are what turn noise into signal.

---

### Exercise 3 - Nmap Attack Detection via UFW and Splunk
**Date:** August 4, 2026
**Status:** Complete

- Ran nmap -sV 192.168.153.129 from Kali-Offense-Project1
- UFW on Linux Mint logged all blocked port probes to /var/log/kern.log
- Broad Splunk search returned 56 events in the scan window
- Focused SPL query isolated 10 clean UFW BLOCK entries pointing to the attacker IP

SPL query used:

    source="/var/log/kern.log" host="joel-virtual-machine" "UFW BLOCK" SRC=192.168.153.128

**Lesson:** A SIEM without focused queries is just storage. The value is in knowing what to look for and writing the query that surfaces it.

**Published write-up:** [How I Detected a Network Attack in My Home Lab Using Splunk and Nmap](https://www.linkedin.com/pulse/how-i-detected-network-attack-my-home-lab-using-splunk-joel-massicot-uwoce/) -- LinkedIn Pulse, Aug 5, 2026

---

## Queued Next Exercises

- Metasploit exploitation attempt -- detect in Splunk
- Custom SPL alert rules triggering on specific attacker behaviors
- Firewall rule hardening
- Packet capture and analysis with Wireshark
- Vulnerability scan with OpenVAS

---

## Tools Reference

| Tool | Machine | Purpose | Status |
|---|---|---|---|
| Nmap | Kali | Network scanning, host discovery, port enumeration | Active |
| Metasploit | Kali | Exploitation framework (learning/lab use only) | Active |
| Wireshark | Both | Packet capture and traffic analysis | Active |
| Splunk Enterprise 10.4.1 | Linux Mint | SIEM - log aggregation and threat detection | Active (localhost:8000) |
| UFW | Linux Mint | Host firewall and block logging | Active |
| tcpdump | Linux Mint | Command-line packet capture | Active |

---

## Lab Rules

- All exercises run within the isolated host-only network
- No scanning or exploitation outside the lab environment
- All activity documented for portfolio and LinkedIn articles
- Lab configs backed up regularly

---

## References

- [Splunk Free Download](https://www.splunk.com/en_us/download/splunk-enterprise.html)
- [Nmap Reference Guide](https://nmap.org/book/man.html)
- [NIST CSF Framework](https://www.nist.gov/cyberframework)
- [CompTIA Security+ SY0-701 Objectives](https://www.comptia.org/certifications/security)
# Home Lab Setup Notes

## Architecture Overview

**Red Team (Attack Machine):** Kali Linux -- Kali-Offense-Project1
- IP: 192.168.153.128
- Role: Network scanning, traffic generation, simulated attacks
- Tools installed: Nmap, Metasploit, Wireshark, Netcat

**Blue Team (Defense Machine):** Linux Mint -- Mint-Target-Project1
- IP: 192.168.153.129
- Role: Log monitoring, traffic detection, SIEM
- Tools installed: Splunk Enterprise 10.4.1, UFW, Wireshark, tcpdump

**Hypervisor:** VMware
**Network isolation:** Host-only network between VMs (no external internet exposure)

---

## Network Configuration

- Host-only network segment: 192.168.153.0/24
- Kali Linux (attacker): 192.168.153.128
- Linux Mint (defender): 192.168.153.129
- Network traffic stays contained within hypervisor -- no risk to external networks

---

## Completed Exercises

### Exercise 1 - Network Reconnaissance with Nmap
**Date:** July 2026
**Machine:** Kali Linux (attacker) scanning Linux Mint (defender)

Commands used:
```bash
# Host discovery
nmap -sn 192.168.153.0/24

# Service version scan
nmap -sV 192.168.153.129

# OS detection + scripts
nmap -A 192.168.153.129
```

**Results:** Successfully identified open ports and services on the Linux Mint VM.
**Lesson:** Even a default Linux install exposes services on the network. Understanding what's running is the first step in reducing attack surface.

---

### Exercise 2 - Splunk SIEM Install and Log Ingestion
**Date:** August 4, 2026
**Status:** Complete

- Installed Splunk Enterprise 10.4.1 on Mint-Target-Project1 (localhost:8000)
- Configured /var/log directory monitor data input (recursive)
- 76,234 events ingested and confirmed in Search dashboard

```
source="/var/log/*" host="joel-virtual-machine"
```

**Lesson:** Raw log volume is high. Filtering and focused SPL queries are what turn noise into signal.

---

### Exercise 3 - Nmap Attack Detection via UFW and Splunk
**Date:** August 4, 2026
**Status:** Complete

- Ran `nmap -sV 192.168.153.129` from Kali-Offense-Project1
- UFW on Linux Mint logged all blocked port probes to /var/log/kern.log
- Broad Splunk search returned 56 events in the scan window
- Focused SPL query isolated 10 clean UFW BLOCK entries pointing to the attacker IP

**SPL query used:**
```
source="/var/log/kern.log" host="joel-virtual-machine" "UFW BLOCK" SRC=192.168.153.128
```

**Lesson:** A SIEM without focused queries is just storage. The value is in knowing what to look for and writing the query that surfaces it.

**Published write-up:** [How I Detected a Network Attack in My Home Lab Using Splunk and Nmap](https://www.linkedin.com/pulse/how-i-detected-network-attack-my-home-lab-using-splunk-joel-massicot-uwoce/) -- LinkedIn Pulse, Aug 5, 2026

---

## Queued Next Exercises

- Metasploit exploitation attempt -- detect in Splunk
- Custom SPL alert rules triggering on specific attacker behaviors
- Firewall rule hardening
- Packet capture and analysis with Wireshark
- Vulnerability scan with OpenVAS

---

## Tools Reference

| Tool | Machine | Purpose | Status |
|---|---|---|---|
| Nmap | Kali | Network scanning, host discovery, port enumeration | Active |
| Metasploit | Kali | Exploitation framework (learning/lab use only) | Active |
| Wireshark | Both | Packet capture and traffic analysis | Active |
| Splunk Enterprise 10.4.1 | Linux Mint | SIEM - log aggregation and threat detection | Active (localhost:8000) |
| UFW | Linux Mint | Host firewall + block logging | Active |
| tcpdump | Linux Mint | Command-line packet capture | Active |

---

## Lab Rules

- All exercises run within the isolated host-only network
- No scanning or exploitation outside the lab environment
- All activity documented for portfolio and LinkedIn articles
- Lab configs backed up regularly

---

## References

- [Splunk Free Download](https://www.splunk.com/en_us/download/splunk-enterprise.html)
- [Nmap Reference Guide](https://nmap.org/book/man.html)
- [NIST CSF Framework](https://www.nist.gov/cyberframework)
- [CompTIA Security+ SY0-701 Objectives](https://www.comptia.org/certifications/security)
