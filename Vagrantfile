Vagrant.configure("2") do |config|
  config.vm.define "devcsr1" do |devcsr1|
    devcsr1.vm.box = "iosxe/16.6.1"
    devcsr1.vm.network "forwarded_port", guest: 22, host: 2201
    devcsr1.vm.network "forwarded_port", guest: 161, host: 1161, protocol: "udp"
  end
  config.vm.define "devcsr2" do |devcsr2|
    devcsr2.vm.box = "iosxe/16.6.1"
    devcsr2.vm.network "forwarded_port", guest: 22, host: 2202
    devcsr2.vm.network "forwarded_port", guest: 161, host: 2161, protocol: "udp"

  end

# Should be able to auto-provision, but potentially raise condition waiting for VM to bootup
# https://github.com/hashicorp/vagrant/issues/6526
#
#  config.vm.provision "ansible" do |ansible|
#    ansible.playbook = "main.yml"
#    ansible.inventory_path = "./dev"
#    ansible.config_file = "./ansible.cfg"
#  end

end

