#!/usr/bin/env bash
wget http://netprog.cisco.com/vagrant_box/iosxe-16.6.1.box
vagrant box add iosxe/16.6.1 iosxe-16.6.1.box --force