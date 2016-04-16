# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "simulator"

   config.vm.provider "virtualbox" do |vb|
     # Display the VirtualBox GUI when booting the machine
     vb.gui = true
  
     # Customize the amount of memory on the VM:
     vb.memory = "4096"
   end
  # Bash Script
  #  config.vm.provision :shell, :path => "script.sh" # runs script file
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update

    # install programs
    echo "---------------INSTALLING PACKAGES---------------"
    declare -a program=(
      "chromium-browser"
      "curl" "git""vim" "terminator" "htop"
      "python" "python-setuptools" "python-pip" "python-dev")
    for i in "${program[@]}"
      do
         echo "Installing $i ..."
         apt-get -y install "$i"
      done
  
    echo "---------------INSTALLING BUILD TOOLS---------------"
sudo apt-get install build-essential libxmu-dev libxmu6 libxi-dev libxine-dev libalut-dev freeglut3 freeglut3-dev cmake libogg-dev libvorbis-dev libxxf86dga-dev libxxf86vm-dev libxrender-dev libxrandr-dev zlib1g-dev libpng12-dev 
sudo apt-get build-dep plib
sudo apt-get build-dep torcs

  
    # install pip python packages
    echo "---------------INSTALLING PYTHON PACKAGES---------------"
    declare -a py=(
        "flask"
        "virtualenv"
        "requests"
        "ipython[all]")

    for i in "${py[@]}"
      do
         echo "Installing $i ..."
         pip install "$i"
      done


    # upgrade and clean up
    sudo apt-get upgrade -y
    # sudo apt-get dist-upgrade -y
    sudo apt-get autoremove -y
    sudo apt-get autoclean -y

  SHELL
end
