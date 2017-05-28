# Basic steps for preparing a Python 3 environment

These steps are made for Python 3.
The same results can be achieved for Python 2.7 simply by removing the "3" everywhere.

## Update and Upgrade your system if necessary
Make sure you have a the latest libraries
```
$ sudo apt-get update
```
and are up to date
```
$ sudo apt-get upgrade
```

## Install Python 3 if necessary

If Python 3 is not installed, please do it 
```
$ sudo apt-get install python3 python3-dev python3-setuptools python3-pip
```

## Install ML libraries

* Install basic libraries for ML computations
```
$ sudo apt-get install python3-numpy python3-pandas python3-scipy python3-matplotlib
```
* If you are going to be using advances ML, please install theano
```
sudo pip3 install theano
```
