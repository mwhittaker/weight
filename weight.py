"""Weight Loss.

Usage:
  weight.py weigh <weight>
  weight.py weigh <time> <weight>
  weight.py javascript
  weight.py now

Options:
  -h --help     Show this screen.
"""

from docopt import docopt
import datetime
import sys
import time
import os.path

WEIGHT_FILE     = "weight.txt"
JAVASCRIPT_FILE = "weight.js"
TIME_FORMAT     = "%Y-%m-%d-%H:%M" # e.g. 2015-07-15-13:34

def usage():
    return __doc__

def die(msg):
    sys.stderr.write(msg + "\n")
    sys.exit(-1)

def err(s):
    die("Error: " + s)

def datetime_to_epoch(time):
    # http://stackoverflow.com/a/11743262/3187068
    return (time - datetime.datetime(1970, 1, 1)).total_seconds()

def parse_float(s):
    try:
        return float(s)
    except ValueError:
        err("{} is not a float.".format(s))

def parse_time(s):
    try:
        return datetime.datetime.strptime(s, TIME_FORMAT)
    except ValueError:
        err("{} is not a time formatted like 2015-07-15-13:34.".format(s))

def parse_weights(filename):
    if not os.path.isfile(filename):
        return []

    with open(filename, "r") as f:
        return [(int(line.split()[0]), float(line.split()[1])) for line in f]


def record_weight(time, weight):
    weights = parse_weights(WEIGHT_FILE)

    with open(WEIGHT_FILE, "w") as f:
        weights.append((time, weight))
        weights.sort()
        for (time, weight) in weights:
            f.write("{} {}\n".format(time, weight))

def generate_javascript():
    template = """
        $(function () {{
            $('#container').highcharts({{
                chart: {{
                    type: 'line'
                }},
                title: {{
                    text: 'Weight Loss'
                }},
                xAxis: {{
                    categories: [{}]
                }},
                yAxis: {{
                    title: {{
                        text: 'Weight (lb)'
                    }}
                }},
                plotOptions: {{
                    line: {{
                        dataLabels: {{
                            enabled: true
                        }},
                        enableMouseTracking: false
                    }}
                }},
                series: [{{
                    data: [{}]
                }}]
            }});
        }});
    """

    timeweights = parse_weights(WEIGHT_FILE)
    times   = [timeweight[0] for timeweight in timeweights]
    weights = [timeweight[1] for timeweight in timeweights]
    times   = ["'{}'".format(datetime.datetime.fromtimestamp(time).strftime("%b %d, %Y %X")) for time in times]
    weights = ["{}".format(weight) for weight in weights]

    with open(JAVASCRIPT_FILE, "w") as f:
        f.write(template.format(", ".join(times), ", ".join(weights)))

def main(args):
    arg_weight     = args["<weight>"]
    arg_time       = args["<time>"]
    arg_weigh      = args["weigh"]
    arg_javascript = args["javascript"]
    arg_now        = args["now"]

    if arg_weigh:
        # weight.py <weight>
        if arg_time is None:
            record_weight(int(time.time()), parse_float(arg_weight))
        # weight.py <time> <weight>
        else:
            t = int(datetime_to_epoch(parse_time(arg_time)))
            record_weight(t, parse_float(arg_weight))
    elif arg_javascript:
        generate_javascript()
    elif arg_now:
        print time.strftime(TIME_FORMAT)
    else:
        die(usage())

if __name__ == '__main__':
    main(docopt(usage()))
