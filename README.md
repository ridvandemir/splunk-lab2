# splunk-lab2

Objective

The Distributed Splunk Environment Lab project aimed to build a comprehensive distributed setup of Splunk. The primary focus was on deploying and configuring various Splunk components, including a Search Head, Indexers, Forwarders (Intermediate, Universal and Heavy), and a Deployment Server, to create a scalable and efficient environment for log collection and analysis. This lab was designed to improve my 'splunk-lab' project by adding Search Peer and Intermediate Forwarders and managing log forwarding with Deployment Server.

Skills Learned

- Proficiency in deploying and managing a distributed Splunk architecture, including Search Head, Indexers, and Forwarders.
- Practical experience in setting up and configuring Heavy Forwarders to enhance log ingestion workflows.
- Hands-on knowledge of ingesting data from Linux and Windows systems using Universal Forwarders.
- Understanding and implementation of various Splunk data input mechanisms, such as file monitoring, scripted inputs, and real-time network inputs.
- Practical knowledge of using a Deployment Server to centrally manage and configure Splunk Forwarders.

Tools Used

- Virtual Machines/Cloud: To simulate a distributed Splunk environment.
- Splunk Enterprise: For log management, indexing, and querying.
- Splunk Universal Forwarder: For collecting logs from endpoint systems and sending them to search peers.
- Splunk Heavy Forwarder: For preprocessing and advanced routing of log data.
- Deployment Server: For centralized configuration and management of Splunk Forwarders.
- VS Code: To connect and manage Linux and Windows servers.

Network Diagram

![splunk_lab2 drawio](https://github.com/user-attachments/assets/e30c7b1f-6626-401b-b8ee-0905c1b7c8dc)

Steps

1-Installation and Setup of Virtual Machines
- For the Linux machines, Ubuntu 22.04 and for the Windows machine Windows 10 were installed on VirtuelBox as virtual machines.
- As a network ‘NAT Network' was selected and static IP address was determined on each virtual machine.
- After installing virtual machines, I saw that they were reachable with the ‘ping’ command.
- Splunk Enterprise was installed as Indexer, Seach Head, Deployment Server and Heavy Forwarder on the Linux machines.
- Universal Forwarder was installed on Linux and Windows 10 machine to send logs to Splunk.
- I created 'lab2' app under $SPLUNK_HOME/etc/apps/ to manage forwarding effectively.

2-Indexers
- First, I changed the IP address to static IP and added 'splunk' user.
  - sudo nano /etc/netplan/00-installer-config.yaml
    - IP1:192.168.2.19, IP2:192.168.2.20
  - sudo adduser splunk
- I installed Splunk and ran it.
  - sudo dpkg -i <splunk.deb folder>
  - sudo chown -R splunk:splunk *
  - sudo –u splunk bash #I switched to splunk user
  - $SPLUNK_HOME/bin/splunk start –accept-license
- I activated 'boot start'.
  - sudo $SPLUNK_HOME/bin/splunk enable boot-start -user splunk
- I configured Indexers to get the logs from Splunk components. For this purpose, I created inputs.conf and indexes.conf under $SPLUNK_HOME/etc/apps/<>/local directory.

3-Search Head
- First, I changed the IP address to static IP and added 'splunk' user.
  - sudo nano /etc/netplan/00-installer-config.yaml
    - IP:192.168.2.21
  - sudo adduser splunk
- I installed Splunk and ran it.
  - sudo dpkg -i <splunk.deb folder>
  - sudo chown -R splunk:splunk *
  - sudo –u splunk bash #I switched to splunk user
  - $SPLUNK_HOME/bin/splunk start –accept-license
- I activated 'boot start'.
  - sudo $SPLUNK_HOME/bin/splunk enable boot-start -user splunk
- Now that I installed Search Head on a seperate machine, I must connect Indexers to Search Head. So that I can run the query in my Indexer. For this purpose, I created distsearch.conf along with inputs.conf, outputs.conf and web.conf under $SPLUNK_HOME/etc/apps/lab/local directory.

4-Deployment Server
- First, I changed the IP address to static IP and added 'splunk' user.
  - sudo nano /etc/netplan/00-installer-config.yaml
    - IP:192.168.2.9
  - sudo adduser splunk
- I installed Splunk and ran it.
  - sudo dpkg -i <splunk.deb folder>
  - sudo chown -R splunk:splunk *
  - sudo –u splunk bash #I switched to splunk user
  - $SPLUNK_HOME/bin/splunk start –accept-license
- I activated 'boot start'.
  - sudo $SPLUNK_HOME/bin/splunk enable boot-start -user splunk

5-Heavy Forwarder
- First, I changed the IP address to static IP and added 'splunk' user.
  - sudo nano /etc/netplan/00-installer-config.yaml
    - IP:192.168.2.29
  - sudo adduser splunk
- I installed Splunk and ran it.
  - sudo dpkg -i <splunk.deb folder>
  - sudo chown -R splunk:splunk *
  - sudo –u splunk bash #I switched to splunk user
  - $SPLUNK_HOME/bin/splunk start –accept-license
- I activated 'boot start'.
  - sudo $SPLUNK_HOME/bin/splunk enable boot-start -user splunk

6-Intermediate Forwarders
- First, I changed the IP address to static IP and added 'splunkfwd' user.
  - sudo nano /etc/netplan/00-installer-config.yaml
    - IP1:192.168.2.30, IP2:192.168.2.31
  - sudo adduser splunkfwd
- I installed Splunk Forwarder and ran it.
  - sudo dpkg -i <splunkforwarder.deb folder>
  - sudo chown -R splunkfwd:splunkfwd *
  - sudo –u splunkfwd bash #I switched to splunkfwd user
  - $SPLUNK_HOME/bin/splunk start –accept-license
- I activated 'boot start'.
  - sudo $SPLUNK_HOME/bin/splunk enable boot-start -user splunkfwd

7-Splunk Forwarder on Linux machines
- First, I changed the IP address to static IP and added 'splunkfwd' user.
  - sudo nano /etc/netplan/00-installer-config.yaml
    - IP1:192.168.2.10, IP2:192.168.2.11
  - sudo adduser splunkfwd
- I installed Splunk Forwarder and ran it.
  - sudo dpkg -i <splunkforwarder.deb folder>
  - sudo chown -R splunkfwd:splunkfwd *
  - sudo –u splunkfwd bash #I switched to splunkfwd user
  - $SPLUNK_HOME/bin/splunk start –accept-license
- I activated 'boot start'.
  - sudo $SPLUNK_HOME/bin/splunk enable boot-start -user splunkfwd
- I planed to monitor scripted inputs from first Linux machine and security logs from second Linux machine. For this purpose, I created inputs.conf and outputs.conf under $SPLUNK_HOME/etc/apps/lab/local directory for each of them. I created this 'lab' under apps to manage forwarding effectively. We should also remember to place scripts under $SPLUNK_HOME/etc/apps/lab/bin directory. I used a random log generating script for this lab.

8-Splunk Forwarder on Windows machine
- First, I changed the IP address to static IP.
  - Internet Settings>Change Adapter Options>Ethernet>Properties>IPv4 Properties>Manual
    - IP:192.168.2.12
- I installed Splunk Forwarder
  - Deployment Server> Host/IP: 192.168.2.9, Port:8089
  - Receiving Server> Host/IP: 192.168.2.20, Port:9997
- I then configured inputs.conf under $SPLUNK_HOME/etc/apps/lab/local directory

