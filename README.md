# ansible-ios-portbounce

## Scenario

Occasionally it becomes necessary to bounce a port a Cisco device (e.g shutdown followed by no shutdown)

## Solution

We will use an ansible playbook to bounce the port while checking for additional conditions to be met before performing
the bounce (e.g port is err-disabled)

## Setup

Create a virtualenv and install the requirements

    pip install -r requirements.txt

## Usage

Credentials will be taken from your current environment, so make sure to set them

    export ANSIBLE_NET_USERNAME=admin
    export ANSIBLE_NET_PASSWORD=cisco

You can execute the playbook directly with something similar to:

     ansible-playbook -i <ip of switch>, -e interface=GigabitEthernetX/Y -vvv portbounce.yaml


***NOTE*** using this method, you must specify the trailing ',' after the hostname/ip