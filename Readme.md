# Get all cookies from www.allin.com.br using seletium

## Install

### Get geckodriver (firefox)

It may vary, but look here: https://www.google.com/search?channel=fs&client=ubuntu&q=install+geckodriver

As loong as geckodriver excecutale is on  your PATH you are ready to go

### Pip & Pipenv

Install pip and pipenv. For example:

```Shell
sudo apt install python3-pip
sudo pip3 install pipenv
```

### Install dependencies

On project root folder run:

```Shell
pipenv install # install deps localy
```

### Run

```Shell
pipenv shell     # apply activate python env libs
python scrap.py https://allin.com.br/  # fire to any website
```