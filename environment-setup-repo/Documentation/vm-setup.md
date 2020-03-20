# Configuring a new VM for training
Assuming a linux machine

## Install Docker

*Instructions extracted from this site: https://docs.docker.com/install/linux/docker-ce/ubuntu/*

1. Update the package index: 
    
    `sudo apt-get update`
1. Allow https for apt repositories: 
    
    `sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common`
1. Add Docker's GPG key:

    `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`
1. Add the repository for docker **stable** releases:

    `sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"`
1. Update the package index again:

    `sudo apt-get update`
1. Install the latest version of _Docker Engine - Community_ and _containered_

    `sudo apt-get install docker-ce docker-ce-cli containerd.io`
1. Verify that Docker was installed properly

    `sudo docker run hello-world`

## Install CUDA/INVIDIA

### Pre-install activities
_Instructions extracted from https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#pre-installation-actions_

1. Verify you have a CUDA-Capable GPU

    `lspci | grep -i nvidia`

1. Verify you have a supported version of linux
    
    `uname -m && cat /etc/*release`

1. Verify you have `gcc` installed

    `gcc --version`

    * If you do not, you can run these commands to install it:
        
        `sudo apt update; sudo apt install build-essential; sudo apt-get install manpages-dev`

1. Verify you have the "Correct Kernel Headers and Development Packages Installed"

    `uname -r`

    * If you do not, you can run this command (Ubuntu) to install them.

        `sudo apt-get install linux-headers-$(uname -r)`


### Install the CUDA Toolkit

_Script below for Ubuntu 18.04 x86_64 - find latest here: https://developer.nvidia.com/cuda-downloads_

`wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin`

`sudo mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600`

`wget http://developer.download.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda-repo-ubuntu1804-10-1-local-10.1.243-418.87.00_1.0-1_amd64.deb`

`sudo dpkg -i cuda-repo-ubuntu1804-10-1-local-10.1.243-418.87.00_1.0-1_amd64.deb`

`sudo apt-key add /var/cuda-repo-10-1-local-10.1.243-418.87.00/7fa2af80.pub`

`sudo apt-get update`

`sudo apt-get -y install cuda`

### Post-Install Activities

_Instructions extracted from here: https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#post-installation-actions_

1. Add to the PATH variables

    `export PATH=/usr/local/cuda-10.1/bin:/usr/local/cuda-10.1/NsightCompute-2019.1${PATH:+:${PATH}}`

    `export LD_LIBRARY_PATH=/usr/local/cuda-10.1/lib64\${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}`

1. POWER9 Setup (Failed on our first install, but CUDA functioned properly)

    1. Enable the NVIDIA Persistence Daemon

        `sudo systemctl enable nvidia-persistenced`


## Install NVIDIA Docker Support

_Instructions extracted from here: https://github.com/NVIDIA/nvidia-docker_

1. Install NVIDIA Docker

    `distribution=$(. /etc/os-release;echo $ID$VERSION_ID)`

    `curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -`

    `curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list`

    `sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit`

    `sudo systemctl restart docker`

1. Confirm installation succeeded

    `docker run --gpus all nvidia/cuda:9.0-base nvidia-smi`

---
---

***Removed the below previously written documentation***

## Install MiniConda

1. In the VM's root folder, run the following command to install Miniconda, which is a lightweight version of Anaconda for managing conda environments

    `wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`

1. After the file finishes installing, run the following commands to install Miniconda

    `chmod +x Miniconda3-latest-Linux-x86_64.sh`

    `./Miniconda3-latest-Linux-x86_64.sh`

1. Check that conda is installed:

    `conda info -e`

## Create a new Python Environment
Navigate to the `environment.yaml` file in the repository folder and run:

`conda env create -f environment.yaml`

Activate the new environment:

`conda activate jds-arx-poc`

