Vagrant.configure("2") do |config|
  config.vm.define "devcsr1" do |devcsr1|
    devcsr1.vm.box = "iosxe/16.6.1"
    devcsr1.vm.network "forwarded_port", guest: 22, host: 2201
  end
  config.vm.define "devcsr2" do |devcsr2|
    devcsr2.vm.box = "iosxe/16.6.1"
    devcsr2.vm.network "forwarded_port", guest: 22, host: 2202
  end
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "main.yml"
    ansible.inventory_path = "./dev"
  end
end

