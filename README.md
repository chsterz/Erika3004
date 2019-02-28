# THIS REPOSITORY IS OLD

You are looking at a fork of the software project that is no longer actively worked on. 

**Instead, please have a look at [this repository](https://github.com/Chaostreff-Potsdam/erika3004) where 
we moved the sources instead.** 

# Erika3004

Lets build a secret chat system using 2 of these.


## Installation 

### Install python3
```
sudo apt-get install python3
```

### Install pip package manager for python
```
sudo apt-get install python3-pip
```

### Install necessary packages
```
pip3 install -r requirements.txt
```


## ASCII art

### Create ASCII art for printout

* install Imagemagick's convert tool
```
sudo apt install imagemagick 
```
* install jp2a
```
sudo apt install jp2a
```
* convert png files on the command line like this: 
  * leave one dimension unspecified to keep teh original ratio
```
convert ubuntu-logo32.png jpg:- | jp2a - --width=80 --height=80
```

### Print ASCII art programmatically 

TODO 

* Rendering strategies:
  * LineByLine
    * render the given image line by line 
  * Interlaced (TODO)
    * render the given image, every odd line first, every even line later
  * PerpendicularSpiralOutward (TODO)
    * render the given image, spiralling outward from the middle while going parallel to X or Y axis all the time
  * PerpendicularSpiralInward (TODO)
    * render the given image, spiralling inward to the middle while going parallel to X or Y axis all the time
  * RandomDotFill (TODO)
    * render the given image, printing one random letter at a time
  * NaturalSpiralOutward (TODO)
    * render the given image, starting from the middle, following as close a natural spiral as possible
  * NaturalSpiralInward (TODO)
    * render the given image, towards the middle, following as close a natural spiral as possible


## Testing

### Run unit tests

For now, call this in bash: 
```
./run_unittests.sh
```


### Run integration tests

For now, call this in bash: 
```
./run_integrationtests.sh
```