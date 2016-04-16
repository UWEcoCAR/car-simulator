# Install VM

## Requires:
* [Vagrant](https://www.vagrantup.com/downloads.html)
* [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
* [VirtualBox  Extension Pack](http://download.virtualbox.org/virtualbox/5.0.10/Oracle_VM_VirtualBox_Extension_Pack-5.0.10-104061.vbox-extpack)

## Info:
The directory contains a `Vagrantfile` which is the build script, and a `package.box` which is the virtual machine image. Vagrant combines these to create and launch an up-to-date virtual machine and launches it in Virtual Box.

## Installation:
* Make sure you install the required software above
* Clone the repo: `git clone https://github.com/UWEcoCAR/UW-Infotainment.git`
* Download the `package.box` (large file) [here](https://drive.google.com/file/d/0B4G8-6r3M_jseU14ZmN2WUdSU0E/view?usp=sharing). Save it in the `VM/` subdirectory of this repo.
* `cd` to the `VM/` directory
* Install the box: `vagrant box add simulator package.box`
* Run `vagrant up` (this will install the latest packages for the dev environment). Vagrant will now start Virtual Box, SSH in and automatically install packages. Hopefully everything updates installs correctly.
* The `package.box` file can now be deleted
* The VM is permanently in the Virtual Box's default directory

## Usage:
* Run `vagrant up` in the `VM/` directory to open the vm
* `vagrant reload`can reload a running vm
* the `--provision` argument will rerun the install scripts in the above commands
* To stop the vm run `vagrant halt`
* to ssh into vm from your os type `vagrant ssh`

## Update:
* Update Vm: `git pull` this repo for the latest `Vagrantfile`
* Run `vagrant up --provision` in the `Vagrantfile` directory

## Uninstall:
* Uninstall Vm: `vagrant destroy` in the `VM/` directory. You will loose you virtual machine, but can reinstall fresh.

# Torcs

## Links
* [**TORCS**](https://sourceforge.net/projects/torcs/files/latest/download)
* [**Server**](https://sourceforge.net/projects/cig/files/SCR%20Championship/Server%20Linux/2.1/scr-linux-patch.tgz/download)

## Requirements
* Torcs torcs-1.3.6 source code
* Hardware accelerated OpenGL (usually provided by your Linux distribution)
* GLUT 3.7 or FreeGlut (better than GLUT for full screen support)
* PLIB 1.8.5 version
* OpenAL
* libpng and zlib (usually provided by your Linux distribution)
* FreeALUT


## Build
* `cd` into the `torcs-1.3.6`
* Configure with by running `./configure`
* make with `sudo make`
* install with `sudo make install`
* add extras with `sudo make datainstall`

## Run
* Simply type `torcs` in a command window
* Note, there are command line options to set default settings
* Note that due to my print tweak explained below, in game info is printed to the console

## Tweak
In `torcs-1.3.6/src` you can tweak the game. Below is a list of files that may be of interest

* In `/drivers` you can edit the different bots. The `human` driver is useful for changing behavior when a human is playing (using arrow keys)
  * I have added a `printf` line in `human.cpp` so that parameters such as speed, rpm, gear and fuel are printed
  * this is the print statement I added :

    `printf("Speed : %0.2f \tYaw : %0.2f\tRPM : %0.2f\tGear : %d\tFuel : %0.2f\n", 3.6*car->_speed_x,yaw_rel, car->_enginerpm, car->_gear, car->_fuel);`

* In `/interfaces/car.h` you can see what a car class is made up of. It has things such as `car->_enginerpm` which will tell you the RPM of the of the car.


# Torcs SCR Server
The server allows you to make custom bots to autonomously drive a level. We have a python wrapper for this server that defines simple driver and car control classes to tweak the bots

## Install
The server is already included in torcs in this repo, but it can be installed or uninstalled with the patch in the `torcs-1.3.6/scr-patch` directory.

## Python server
* source code is in `/python_svr`
* Run the server by typing `python pyclient.py` in the `/python_svr` directory
* The server will wait for a race to start
* the race must have `scr_server_1` as a player for the default pyclient to work
* Once the race starts, the `scr_server_1` should drive on its own

Notes:
* Essentially the `driver.py` will steer to stay in the middle of the road, and increase speed until the `max_speed` limit is reached. Once it is reached, the bot will oscillate around this speed.
* The steering algorithm is `steer = (angle - dist)/self.steer_lock` where angle is the cars angle, dist is distance from ideal path and steer_lock is a constant to prevent over steering.
* The gear shift algorithm is also in the `driver.py`

## Usage
* Start the python server client by typing `python pyclient.py` in the `/python_svr` directory
* Start the game with `torcs`
* In torcs, start a race and make sure `scr_server_1` is a player
* The python server should connect and in game information should be printed to console
