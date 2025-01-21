# splunk-lab2

Objective

The Distributed Splunk Environment Lab project aimed to build a comprehensive distributed setup of Splunk. The primary focus was on deploying and configuring various Splunk components, including a Search Head, Indexers, Forwarders (Intermediate, Universal and Heavy), and a Deployment Server, to create a scalable and efficient environment for log collection. This lab was designed to improve my 'splunk-lab' project by adding Search Peer and Intermediate Forwarders and managing log forwarding with Deployment Server.

Skills Learned

- Proficiency in deploying and managing a distributed Splunk architecture, including Search Head, Indexers, and Forwarders.
- Practical experience in setting up and configuring Heavy Forwarders to enhance log ingestion workflows.
- Hands-on knowledge of ingesting data from Linux and Windows systems using Universal Forwarders.
- Practical knowledge of using a Deployment Server to centrally manage and configure Splunk Forwarders.
- Understanding and implementation of various Splunk data input mechanisms, such as file monitoring, scripted inputs, and real-time network inputs.

Tools Used

- Virtual Machines/Cloud: To simulate a distributed Splunk environment.
- Splunk Enterprise: For log management, indexing, and querying.
- Splunk Universal Forwarder: For collecting logs from endpoint systems and sending them to search peers.
- Splunk Heavy Forwarder: For preprocessing and advanced routing of log data.
- Deployment Server: For centralized configuration and management of Splunk Forwarders.
- VS Code: To connect and manage Linux and Windows servers.

Network Diagram

![splunk_lab2 drawio](https://github.com/user-attachments/assets/23d953be-b44c-458e-88f1-fb6517c8427f)

Steps

1-Installation and Setup of Virtual Machines
- For the Linux machines, Ubuntu 22.04 and for the Windows machine Windows 10 were installed on VirtuelBox as virtual machines.
- As a network ‘NAT Network' was selected and static IP address was determined on each virtual machine.
- After installing virtual machines, I saw that they were reachable with the ‘ping’ command.
- Splunk Enterprise was installed as Indexer, Seach Head, Deployment Server and Heavy Forwarder(HF) on the Linux machines.
- Universal Forwarder(UF) was installed on Linux and Windows 10 machine to send logs to Intermediate Forwarder(IF) and then to Indexer1.

2-Splunk Configuration Setup
- First, I deployed an app $SPLUNK_HOME/etc/apps/forward-to-indexer2 to send the internal logs of Seach Head and Deployment Server.
- Then, I configured Search Head for the distributed environment. I created 'distsearch.conf' along with inputs.conf and web.conf under $SPLUNK_HOME/etc/system/local directory.
- I then configured deployment clients, so that they can phone to Deployment Server. For this purpose, I created 'deploxmenclients.conf' under $SPLUNK_HOME/etc/apps/deployment-client app.
- After that, I configured the Universal Forwarders and Intermediate Forwarders to interact each other shown in the diagram by pushing the apps through Deployment Server. At this point, I created 'serverclass.conf' under $SPLUNK_HOME/etc/system/local to send the app that I wanted.
- According to the use cases I configured indexes.conf for each Indexer. For this lab, UF1 sends script output, UF2 sends linux secure logs, UF3 sends windows system logs and HF sends network logs.
- When sending logs to Indexer, using Splunk Add-ons for certain use cases would be very beneficial.

3-Indexers
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
- I configured Indexers creating inputs.conf and indexes.conf to get the logs from Splunk components. Indexer1 gets the logs from Universal Forwarders. Indexer2 gets the logs from Syslog.

4-Search Head
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
- I configured Search Head creating inputs.conf and indexes.conf.

5-Deployment Server
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
- After connecting the clients to Deployment Server, I assigned the apps to the clients and created a server class for each app pushing.

6-Heavy Forwarder
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
- I used Heavy Forwarder to send the network logs to Indexer2. As a network logs, I sent OPNSense firewall logs through port 514.

7-Intermediate Forwarders
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
- I configured those Intermediate Forwarders through Deployment Server.

8-Splunk Forwarder on Linux machines
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
- I monitored scripted inputs from first Linux machine and security logs from second Linux machine. I configured those Universal Forwarders through Deployment Server.

9-Splunk Forwarder on Windows machine
- First, I changed the IP address to static IP.
  - Internet Settings>Change Adapter Options>Ethernet>Properties>IPv4 Properties>Manual
    - IP:192.168.2.12
- I installed Splunk Forwarder
  - Deployment Server> Host/IP: 192.168.2.9, Port:8089
  - Receiving Server> Host/IP: 192.168.2.20, Port:9997
- I monitored system logs from Windows machine and configured this Universal Forwarder through Deployment Server.

NOT: 
- As a best practice, when working with the directory/file under $SPLUNK_HOME, we should change the ownership of directory/file from root to splunk/splunkfwd.
- For network logs, it is recommended to use syslog collector to send the logs to Heavy Forwarder.
