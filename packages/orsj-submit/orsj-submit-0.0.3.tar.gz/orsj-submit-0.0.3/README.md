## Description

Web application of "submitting papers" in ORSJ.

ORSJ: The Operations Research Society of Japan

http://www.orsj.or.jp/

## OS

mac, ubuntu

## Usage

### Step 1

Copy setting file.

```
$ orsj-submit setting
```

### Step 2

Modify setting file.

```
$ edit setting.yml
```

### Step 3

Start redis server.

```
$ orsj-submit redis
```

### Step 4

In annother shell, set environment.

```
$ export MAIL_USER=XXX
$ export MAIL_PASSWD=XXX
$ export SECRET_KEY=XXX
```

### Step 5

start web application.

```
$ orsj-submit run
```

## Using docker

Must modify setting.yml & start_cmd of orsj.tgz.

```bash
wget -qO- <URL of orsj.tgz> | tar zxf -
docker run -d -u root -p 80:80 -e MAIL_USER=XXX -e MAIL_PASSWD=XXX -e SECRET_KEY=XXX \
  -v $PWD/orsj:/orsj -w /orsj --name orsj tsutomu7/scientific-python ash start_cmd
```
