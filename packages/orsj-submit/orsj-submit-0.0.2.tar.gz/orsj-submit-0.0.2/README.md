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