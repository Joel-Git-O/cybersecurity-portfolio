# Write-ups

Lab exercise documentation, CTF notes, and LinkedIn article drafts.

---

## Published

### Home SIEM Lab - Nmap Attack Detection via Splunk and UFW
**Status:** Published -- Aug 5, 2026
**Article:** [How I Detected a Network Attack in My Home Lab Using Splunk and Nmap](https://www.linkedin.com/pulse/how-i-detected-network-attack-my-home-lab-using-splunk-joel-massicot-uwoce/)

What was covered:
- Installed Splunk Enterprise 10.4.1 on Linux Mint (Mint-Target-Project1, 192.168.153.129)
- Configured /var/log ingestion -- 76,234 events
- Ran nmap -sV from Kali-Offense-Project1 (192.168.153.128)
- UFW blocked and logged all port probes to /var/log/kern.log
- SPL query isolated 10 clean UFW BLOCK events from the attacker IP

SPL query:

    source="/var/log/kern.log" host="joel-virtual-machine" "UFW BLOCK" SRC=192.168.153.128

---

## Planned Write-ups

| Title | Type | Status |
|---|---|---|
| Network Reconnaissance with Nmap - What the defender sees | Lab Write-up | Planned |
| Metasploit detection in Splunk | Lab Write-up | Planned |
| Custom SPL alert rules - triggering on attacker behavior | Lab Write-up | Planned |
| File Integrity Monitoring - Building a Python FIM tool | Tool Write-up | Planned |
| CompTIA Security+ Study Notes - Domain 2: Threats and Vulnerabilities | Study Notes | In progress |

---

## CTF Notes

*Hack The Box (HTB) write-ups will be added here as exercises are completed.*

Account: HTB active (joel.massicot@zohomail.eu)

---

## Resources

- [Hack The Box](https://www.hackthebox.com/)
- [TryHackMe](https://tryhackme.com/)
- [Splunk Free](https://www.splunk.com/en_us/download/splunk-enterprise.html)
- [NIST CSF](https://www.nist.gov/cyberframework)
# Write-ups

Lab exercise documentation, CTF notes, and LinkedIn article drafts.

---

## In Progress

### Home SIEM Lab - Splunk on Linux Mint
**Status:** In progress
**Goal:** Install Splunk Free on Linux Mint, ingest system logs, detect Nmap traffic from Kali Linux, visualize in dashboards.
**Planned article:** "How I built a home SIEM to monitor my network"

---

## Planned Write-ups

| Title | Type | Status |
|---|---|---|
| How I built a home SIEM to monitor my network | LinkedIn Article | Planned (post-Splunk exercise) |
| Network Reconnaissance with Nmap - What the defender sees | Lab Write-up | Planned |
| File Integrity Monitoring - Building a Python FIM tool | Tool Write-up | Planned |
| CompTIA Security+ Study Notes - Domain 2: Threats & Vulnerabilities | Study Notes | In progress |

---

## CTF Notes

*Hack The Box (HTB) write-ups will be added here as exercises are completed.*

Account: HTB active (joel.massicot@zohomail.eu)

---

## Resources

- [Hack The Box](https://www.hackthebox.com/)
- [TryHackMe](https://tryhackme.com/)
- [Splunk Free](https://www.splunk.com/en_us/download/splunk-enterprise.html)
- [NIST CSF](https://www.nist.gov/cyberframework)
