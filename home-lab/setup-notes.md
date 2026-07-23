# Home Lab Setup Notes

## Architecture Overview

**Red Team (Attack Machine):** Kali Linux
- Role: Network scanning, traffic generation, simulated attacks
- Tools installed: Nmap, Metasploit, Wireshark, Netcat

**Blue Team (Defense Machine):** Linux Mint
- Role: Log monitoring, traffic detection, SIEM (Splunk in progress)
- Tools installed: Wireshark, tcpdump

**Hypervisor:** VMware / VirtualBox
**Network isolation:** Host-only network between VMs (no external internet exposure)

---

## Network Configuration

- Host-only network segment: 192.168.56.0/24
- Kali Linux (attacker): 192.168.56.101
- Linux Mint (defender): 192.168.56.102
- Network traffic stays contained within hypervisor -- no risk to external networks

---

## Completed Exercises

### Exercise 1 - Network Reconnaissance with Nmap
**Date:** July 2026
**Machine:** Kali Linux (attacker) scanning Linux Mint (defender)

Commands used:
```bash
# Host discovery
nmap -sn 192.168.56.0/24

# Service version scan
nmap -sV 192.168.56.102

# OS detection + scripts
nmap -A 192.168.56.102
```

**Results:** Successfully identified open ports and services on the Linux Mint VM.
**Lesson:** Even a default Linux install exposes services on the network. Understanding what's running is the first step in reducing attack surface.

---

## In Progress

### SIEM Setup with Splunk on Linux Mint
- Install Splunk Free (single-instance) on Linux Mint
- Configure Splunk to ingest Linux system logs (/var/log/syslog, /var/log/auth.log)
- Generate network traffic from Kali (Nmap scans, ping sweeps)
- Create Splunk dashboards to detect and visualize the traffic
- Document findings as a LinkedIn article

**Next step:** Download Splunk Free from splunk.com, install on Linux Mint, configure log forwarding

---

## Tools Reference

| Tool | Machine | Purpose |
|---|---|---|
| Nmap | Kali | Network scanning, host discovery, port enumeration |
| Metasploit | Kali | Exploitation framework (learning/lab use only) |
| Wireshark | Both | Packet capture and traffic analysis |
| Splunk | Linux Mint | SIEM - log aggregation and threat detection (in progress) |
| tcpdump | Linux Mint | Command-line packet capture |

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
