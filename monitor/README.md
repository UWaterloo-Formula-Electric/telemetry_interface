# Monitor - Read and Store Signals

## Structure

The `Monitor` class contains two methods at the moment. One to simulate live CAN data using an old testing log file, and one to listen to a TCP client.

To change where we are reading data from, we can simply implement a new method and call that function in `main.py` instead, so it is flexible.

## Docker Instructions

```console
$ docker build -t uwfe-monitor .

$ docker run uwfe-monitor
```

## Normal Instructions

```
$ pip install -r requirements.txt
$ python ./app/main.py
```
