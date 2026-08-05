# Cybersecurity Portfolio - Joel Massicot

> Technology and Business Operations Leader | Cybersecurity | US/Dutch Veteran | US-EU Bridge

[![ISC2 CC](https://img.shields.io/badge/ISC2-Certified_in_Cybersecurity-green)](https://www.isc2.org/)
[![Google Cybersecurity](https://img.shields.io/badge/Google-Cybersecurity_Professional-blue)](https://grow.google/certificates/cybersecurity/)
[![Security+](https://img.shields.io/badge/CompTIA-Security%2B_In_Progress-orange)]()

---

## About

19-year entrepreneur and US Marine Corps / Army veteran transitioning into cybersecurity with a focus on SOC operations, threat detection, and security automation.

**Background:** Co-founded and led Masacote Entertainment for 19 years, managing global operations across 30+ countries, building digital platforms, and developing teams under pressure. Now applying that operational discipline to cybersecurity.

**Location:** Breda, Netherlands. Legally authorized to work in both the US and EU (US/Dutch dual citizen) with active knowledge of NIST CSF and EU NIS2 frameworks.

---

## Certifications

| Certification | Issuer | Status |
|---|---|---|
| Certified in Cybersecurity (CC) | ISC2 | Active (Feb 2025 - Feb 2028) |
| Google Cybersecurity Professional Certificate | Google / Coursera | Complete (Jun 2025) |
| Google AI Essentials | Google | Complete (Jan 2026) |
| Google Prompting Essentials | Google | Complete (Mar 2025) |
| CompTIA Security+ (SY0-701) | CompTIA | In Progress |

---

## Repository Structure

```
cybersecurity-portfolio/
|- home-lab/        Home lab setup, SIEM configuration, network architecture
|- security-tools/  Python scripts for threat detection and security analysis
|- automation/      Automation scripts for security monitoring workflows
|- write-ups/       Lab write-ups, CTF notes, LinkedIn articles
```

---

## Home Lab

**Architecture:**
- Red Team (Attack): Kali Linux -- Kali-Offense-Project1, 192.168.153.128 -- Nmap, Metasploit, Wireshark
- Blue Team (Defense): Linux Mint -- Mint-Target-Project1, 192.168.153.129 -- Splunk Enterprise 10.4.1, UFW
- Network isolation: VMware host-only network, no external route, clean lab environment

**Completed exercises:**
- Network reconnaissance with Nmap (complete)
- Splunk Enterprise 10.4.1 install and /var/log ingestion -- 76,234 events ingested (complete - Aug 4, 2026)
- Nmap -sV service version detection from Kali, detected via UFW and Splunk -- 10 UFW BLOCK events isolated (complete - Aug 4, 2026)

**SPL query used for Nmap detection:**
```
source="/var/log/kern.log" host="joel-virtual-machine" "UFW BLOCK" SRC=192.168.153.128
```

**Queued next exercises:**
- Metasploit exploitation attempt -- detect in Splunk
- Custom SPL alert rules triggering on attacker behavior
- Firewall rule hardening
- Packet capture and analysis with Wireshark

---

## Published Work

| Article | Platform | Date |
|---|---|---|
| [How I Detected a Network Attack in My Home Lab Using Splunk and Nmap](https://www.linkedin.com/pulse/how-i-detected-network-attack-my-home-lab-using-splunk-joel-massicot-uwoce/) | LinkedIn Pulse | Aug 5, 2026 |

---

## Skills

- **Frameworks:** NIST CSF, CIS Controls, OWASP
- **SIEM:** Splunk Enterprise (log ingestion, SPL queries, threat detection)
- **Tools:** Nmap, Metasploit, Wireshark, UFW, Splunk
- **Languages:** Python (in progress), Bash
- **Platforms:** Linux (Kali, Mint), VMware, Windows
- **Concepts:** Network reconnaissance, log analysis, threat detection, incident response fundamentals

---

## Connect

- LinkedIn: [Joel Massicot](https://www.linkedin.com/in/joelmassicot/)
- Location: Breda, Netherlands
- Work authorization: US and EU
