cat9k-soar
----------
Application Hosting on the Catalyst 9K, an interface to Splunk Phantom security orchestration, automation and response (SOAR)

![](./documentation/images/code_for_catalyst_logo.png)

This project uses the application hosting feature of the Catalyst 9K as a distributed platform for gathering and pushing security data to Phantom. This structured data can be combined with other enrichment sources, and as a trigger for automating incident response within Splunk Phantom.

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/joelwking/cat9k-soar)

### Technology Value

Application hosting at the network edge, on the Cisco Catalyst 9300 series switches, enables the network manager to deploy applications on an x86 CPU for the purpose of analyzing and gathering telemetry about traffic on the network. Container based applications can be developed and tested using Docker on Linux systems, then deployed on the Catalyst 9300 series switches, providing the network and security operations a distributed cyber security interface to the enterprise security orchestration, automation and response (SOAR) platform.

The `cat9k-soar` project is a sample code base for ingesting data collected at the network edge as security incidents, managed and acted upon by Splunk Phantom.

### Components

* **SOAR**: The acronym SOAR, Security Orchestration, Automation and Response is a process and concept of managing contextual data associated with cyber attacks and security related incidents. The SOAR platform **Splunk Phantom** is fundamental to this solution. World Wide Technology has developed both apps and data ingest [software](https://github.com/joelwking/Phantom-Cyber) for the **Splunk Phantom** platform, which is used in this solution.

* **Linux Containers**: Specifically Docker, enables building software solutions using containerization shortens development cycles and decreases the barriers to deploying apps on the target systems. In this solution, applications are developed and packaged on Linux systems and then installed on the network edge running on Catalyst 9300 series switches.

* **Application Hosting**: The Cisco Catalyst 9300 series switch now supports application hosting using reserved memory and CPU, running as a separate Linux process, isolated from the IOS XE operating system. This solution is beneficial to the network manager as it does not require separate computing machines to run the software on the network edge. 

* **Catalyst 9K SOAR**: The Python software contained in this solution includes foundational code to create security events (Phantom *containers*) and security data (Phantom *artifacts*) on the Splunk Phantom platform. Within the `library` directory, there are two sub-directories, `hello_phantom` and `snort`, which can be deployed as apps on the Catalyst 9300 series.

#### Topology Diagram

This topology diagram illustrates that multiple apps can be installed and executed on the Catalyst 9300 series, using the REST API interface on a Splunk Phantom instance to ingest structured data, gleaned from the network edge, to the SOAR platform for analysis and action by the security operations center.

![](./documentation/images/cat9k-soar_topology.png)

#### Software

The file `library/connector/base_connector.py` contains a Python class *SOAR*, which is imported and referenced as a Python superclass by the `library/hello_phantom/hello.py` and `library/snort/snort.py` apps.  The `base_connector.py` imports [https://github.com/joelwking/Phantom-Cyber/blob/master/REST_ingest/PhantomIngest.py](https://github.com/joelwking/Phantom-Cyber/blob/master/REST_ingest/PhantomIngest.py) which uses the Python `requests` module to interact with the Phantom REST APIs. 

> ___
> ##### hello_phantom

> This Docker app is a basic 'hello world' example which creates an event (container) in Phantom, then exits. It can be used as a template to develop your own data collection applications as telemetry to Splunk Phantom.

> ___
> ##### snort

> This Docker app installs, configures and executes Snort. [Snort](https://www.snort.org) is an open-source, network intrusion detection system (NIDS). The Snort configuration file enables alerts to be written to a CSV file. Alerts written to the file are processed by `snort.py` and used to create events (containers) and artifacts in CEF (Common Exchange Format) format. The shell `snort.sh` starts both Snort and the Python program.

> Using Snort to act as an intrusion detection system integrated with Software Defined Networking (SDN) concepts have been demonstrated as a  Security-Defined Routing use case. Refer to the  [cybergamut](http://cybergamut.com/2014/10/technical-tuesday-28-october-2014-software-defined-networking-by-joel-king-of-world-wide-technology/) talk and [slides](https://www.slideshare.net/joelwking/security-defined-routingcybergamutv11) as well as a [video demonstration ](https://www.youtube.com/watch?v=KvZuklmi9uU).

___

### Status

Alpha 1.0 - The base functionality of the software has been tested and Phantom containers and artifacts can be created by the software running in Docker containers in a Linux host, to a Phantom community instance (version 4.5.15922) deployed in Amazon Web Services (AWS). Additional testing scheduled for the [DevNet Sandbox](https://developer.cisco.com/site/sandbox/) as reservations become available mid-September 2019. 

### Installation

Information on installing and configuring Splunk Phantom is available by joining the Phantom Community or through training.

* Phantom Community https://my.phantom.us/
* Administering Phantom https://www.splunk.com/en_us/training/courses/introduction-to-phantom.html

At a minimum, the REST Data Source app will need to be enabled and configured on the Phantom instance. This app is a custom REST handler to allow push/ingest data such as events and artifacts into Phantom.

Build instructions for each app in the `library` directory are included the `README.md` file.

Instructions for deploying the app(s) are available on DevNet as [Application Hosting in the Enterprise](https://developer.cisco.com/docs/app-hosting).

### Configuration

The `base_connector` class SOAR attempts to load a configuration file, by default, using the program name and '.yml' or by a YAML file specified as the first argument to the program. Sample configuration and credential inputs are read from the YAML file in the respective directories, for example, `library/hello_phantom/hello.yml` specifies the IP address and API key for the Phantom instance.

Optionally, variables can be specified and are imported. For example, `snort_constants.py` specifies an interval to wait for new input to arrive in the alert file.

Refer to the README specified for each app for additional information on configuring the app.

### Usage

First review the [README](./library/hello_phantom/README.md) from the `hello_phantom` app. Then review the `snort` [README](./library/snort/README.md) and watch the following video demonstration.

[![Video Demonstration](./documentation/images/video_icon.png)](https://vimeo.com/359849536)

### Known issues

Use the the [Issue Tracker](https://github.com/joelwking/cat9k-soar/issues), to open a new issue or provide feedback. 

  * The DevNet Sandbox restricts access to the Internet from the sandbox labs, limiting access to an instance of Phantom deployed in AWS/cloud or the Internet.
  * Note the [restrictions](https://developer.cisco.com/docs/app-hosting/#!getting-cat9k-setup) on Catalyst hardware and software.
  * The app-hosting service utilizes meta data that will be present only when the Docker save command uses the  *image_name:tag* format. 

### Getting help

If you have questions, concerns, bug reports, etc., please file an issue in this repository's [Issue Tracker](https://github.com/joelwking/cat9k-soar/issues).

### Getting involved

This repository highlights the emerging technical skills for a new kind of network engineer who must have a basic understanding of applications, programming and infrastructure, both on-prem and in a cloud. Additionally, enabling the network to be a source of telemetry data will be instrumental in improving the security posture of any organization. This solution provides a network engineer with access to a framework which enables skill development in the following areas:

* Python programming
* Source Control Management systems (Git)
* Linux
* Cloud, Virtualization and Containers (Docker)

We encourage all network and security operations engineers to use this repository as a guide and framework to develop and enable additional use cases and enable additional functionality

Refer to the instructions on how to contribute in [CONTRIBUTING](./CONTRIBUTING.md).

### Credits and references

1. Code for Catalyst Challenge: https://blogs.cisco.com/developer/code-for-catalyst-challenge-is-now-open
2. Snort official documents: https://www.snort.org/#get-started
3. White paper on app hosting: https://www.cisco.com/c/dam/en/us/products/collateral/switches/catalyst-9300-series-switches/white-paper-c87-742415.pdf
4. Snort formatting the alert file output: https://users.du.se/~hjo/cs/common/books/Log%20Parser/9781932266528.PDF
5. Snort.conf output options: https://searchitchannel.techtarget.com/feature/Snortconf-output-options
6. Learn more about Snort Configuration File: https://www.sciencedirect.com/topics/computer-science/snort-configuration-file
7. Using Snort for intrusion detection: https://www.techrepublic.com/article/using-snort-for-intrusion-detection/
8. Common Event Format: https://kc.mcafee.com/resources/sites/MCAFEE/content/live/CORP_KNOWLEDGEBASE/78000/KB78712/en_US/CEF_White_Paper_20100722.pdf
