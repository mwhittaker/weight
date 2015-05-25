# Weight #

This repository contains code to track and graph my weight over time. The
workhorse of the repository is [`weight.py`](weight.py). Say I just weighed
myself in at 215.8 pounds. I type

    python weight.py weigh 215.8

and `weigh.py` enters a timestamped weight into [`weight.txt`](weight.txt). It
also generates the javascript file [`weight.js`](weight.js) which uses
[highcharts](http://www.highcharts.com/) to generate a graph of my weight over
time. The graph can be viewed at http://mwhittaker.github.io/weight/.
