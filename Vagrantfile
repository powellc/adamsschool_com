# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|
  config.vm.box = "precise64"

  config.vm.customize ["modifyvm", :id, "--memory", 384]
  config.vm.forward_port 80, 8100
  config.vm.network :hostonly, '11.0.0.100'  # Update the fabfile.py if you update this

  config.vm.share_folder("vagrant-root", "/vagrant", ".", :nfs => true)
  config.vm.provision :ansible do |ansible|
    ansible.playbook = "ansible/vagrant.yml"
    ansible.inventory_path = "ansible/local_hosts"
  end
end
