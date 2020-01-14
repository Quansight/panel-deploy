# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|


  # devolopment machine (requires virtualbox)
  # config.vm.define "db_follower", autostart: false
  config.vm.define "dev", primary: true do |dev_config|
    dev_config.vm.provider :'virtualbox' do |vb, override|
      vb.memory = 1024
      vb.cpus = 1
      override.vm.box = "ubuntu/xenial64"
      override.vm.network :private_network, ip: "192.168.33.10"
      override.vm.network "forwarded_port", guest: 5000, host: 5000
    end
  end

  config.vm.synced_folder ".", "/vagrant", type: "rsync",
  rsync__exclude: ['./data/']

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "devops/webserver-dev.yml"
    ansible.verbose = "vvvv"
  end
end