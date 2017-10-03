Vagrant.configure("2") do |config|
  config.vm.define "devcsr" do |devcsr|
    devcsr.vm.box = "iosxe/16.6.1"
    devcsr.vm.network "forwarded_port", guest: 22, host: 2201
  end
  config.vm.define "prodcsr" do |prodcsr|
    prodcsr.vm.box = "iosxe/16.6.1"
    prodcsr.vm.network "forwarded_port", guest: 22, host: 2202
  end
end
