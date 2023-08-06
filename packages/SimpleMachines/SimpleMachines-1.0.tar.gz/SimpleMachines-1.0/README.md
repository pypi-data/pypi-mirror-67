## Simple Machines Package
### Project Motivation
This package is created for basic calculations of simple machines.
All the systems are considered in the simplest system that work with
one load and force. All other factors like friction, weigth of systems etc.
are ignored.

Simple machines have these atrributes in common:
* P
* F

Distribution have these method in common:
* findStrGain()
* calculate_load_distance()
* calculate_force_distance()
* calculate_energy()
* calculate_power()

### Install
#### Dependencies
No additional install is required rather than Python software.
#### User Installation
You can use pip install method.
* pip install SimpleMachines

### File Descriptions
* **SimpleMachines.py**: This file holds the general properties of a simple machines. All simple machine classes are inherited from this SimpleMachine class.
* **lever.py**: It includes lever simple machine.
* **pulley.py**: It includes the pulley simple machine.
* **licence.txt**: licence file
* **setup.cfg**: This is used to setup package.
* **README.md**: The file that you are currently reading.

### Licences and Acknowledgements
Thanks to Udacity for data science course that encourages me to build a package and improve my skills.
