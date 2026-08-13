# Write-ups and Published Articles

Hands-on documentation of lab exercises, blue team operations, and published technical writing.

---

## Published Articles

| Title | Platform | Date | Topic |
|---|---|---|---|
| [How I Detected a Network Attack in My Home Lab Using Splunk and Nmap](https://www.linkedin.com/pulse/how-i-detected-network-attack-my-home-lab-using-splunk-joel-massicot-uwoce/) | LinkedIn | Aug 5, 2026 | SIEM, Nmap, UFW, Blue Team |

### Article Summary: How I Detected a Network Attack in My Home Lab Using Splunk and Nmap

Full end-to-end blue team exercise covering:

- **Lab setup:** Kali Linux (attacker, 192.168.153.128) vs Linux Mint (defender, 192.168.153.129), VMware host-only isolation
- **Exercise 1:** Nmap reconnaissance scan from Kali targeting Mint
- **Exercise 2:** UFW firewall blocking and logging the Nmap traffic
- **Exercise 3:** Splunk SIEM ingestion of 76,234 /var/log events, SPL query isolating 10 UFW BLOCK events from the Kali source IP

**SPL Detection Query:**
```
index=main sourcetype=syslog "UFW BLOCK" src_ip=192.168.153.128
```

Screenshots included: Splunk dashboard showing 76,234 events ingested, 56 UFW BLOCK events, and 10 events isolated to the Kali source IP.

---

## Lab Write-ups (In Progress)

Additional write-ups will be added as exercises are completed.

| Topic | Status |
|---|---|
| SPL alert rules -- automated detection | Planned |
| Metasploit exploitation + Splunk detection | Planned |
| Log correlation across multiple sources | Planned |
| Python automation for security monitoring | Planned |
| Incident response simulation | Planned |

---

*See [home-lab/](../home-lab/) for the full lab setup and architecture notes.*
