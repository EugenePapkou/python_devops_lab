#!/bin/bash
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
pyenv update
echo "export PATH="/home/student/.pyenv/bin:$PATH"; eval "$(pyenv init -)"
; eval "$(pyenv virtualenv-init -)"" >> /home/student/.bash_profile 
source
pyenv update
yum -y install -y gcc gcc-c++ make git patch openssl-devel zlib-devel readline-devel sqlite-devel bzip2-devel 
#yum -y install libffi-devel

pyenv install 2.7
pyenv install 3.5.0
pyenv virtualenv 2.7 python_2
pyenv virtualenv 3.5.0 python_3

