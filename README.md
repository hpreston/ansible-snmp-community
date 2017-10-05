# ansible-snmp-community

## Purpose

Provide a demonstration of a CI/CD pipeline for network devices.

In this scenario we will modify SNMP community strings, test the deployment
of those changes by running an ansible playbook against a local CSR1000v
which is instantiated by vagrant.

Once the local dev testing is completed, the changes will be pushed
to source control, where an automated build pipeline will do the same
against a test environment


## Prerequisites

You will need to download a CSR box image, your proctor will provide the link for this file

```
wget http://<url provided by proctor>/iosxe-16.6.1.box
vagrant box add iosxe/16.6.1 iosxe-16.6.1.box --force
```

## Components



# High Level Flow


1. Clone this repository from your lab VCS server, this will be provided by your
lab administrator

    ```
        git clone http://cleur-gogs.lab.apps.imapex.io/network/ansible-snmp-community.git
    ```

2. Create virtualenv and load dependencies

    ```
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

    ```

3. Modify snmp.yml with the new SNMP strings using your favorite text editor

3. Load local dev CSR

    ```
    vagrant up
    ```
4. Add credentials to your local environment

   ```
   export ANSIBLE_NET_USERNAME=vagrant
   export ANSIBLE_NET_PASSWORD=vagrant
   ```

5. Run tests against dev CSR

    ```
    ansible-playbook -i dev.yml main.yml
    ```

6. After playbook executes as expected, you can commit and push your changes

    ```
    git add snmp.yml
    git commit -m 'changed snmp community strings`
    git push origin master
    ```

7. Monitor build status via the drone console

    [http://cleur-drone.lab.apps.imapex.io/network/ansible-snmp-community](http://cleur-drone.lab.apps.imapex.io/network/ansible-snmp-community)
