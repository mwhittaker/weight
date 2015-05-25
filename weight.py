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
from datetime import datetime
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
    return (time - datetime(1970, 1, 1)).total_seconds()

def epoch_to_datetime(seconds):
    return datetime.fromtimestamp(seconds)

def parse_float(s):
    try:
        return float(s)
    except ValueError:
        err("{} is not a float.".format(s))

def parse_time(s):
    try:
        return datetime.strptime(s, TIME_FORMAT)
    except ValueError:
        err("{} is not a time formatted like 2015-07-15-13:34.".format(s))

def parse_weights(filename):
    if not os.path.isfile(filename):
        return []

    with open(filename, "r") as f:
        weights = []
        for line in f:
            parts  = line.split()
            time   = int(parts[0])
            weight = float(parts[1])
            weights.append((time, weight))
        return weights

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
                    type: 'datetime',
                    dateTimeLabelFormats: {{ // don't display the dummy year
                        month: '%e. %b',
                        year: '%b'
                    }},
                    title: {{
                        text: 'Date'
                    }}
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
                        enableMouseTracking: true,
                        marker: {{
                            enabled: true
                        }}
                    }}
                }},
                series: [{{
                    name: 'michael',
                    data: [{}]
                }}]
            }});
        }});
    """

    timeweights = parse_weights(WEIGHT_FILE)

    times   = [timeweight[0] for timeweight in timeweights]
    times   = [epoch_to_datetime(time) for time in times]
    times   = ["Date.UTC({}, {}, {}, {}, {})".format(time.year, time.month, time.day, time.hour, time.minute) for time in times]

    weights = [timeweight[1] for timeweight in timeweights]
    weights = ["{}".format(weight) for weight in weights]

    with open(JAVASCRIPT_FILE, "w") as f:
        f.write(template.format(", ".join("[{}, {}]".format(time, weight) for (time, weight) in zip (times, weights))))

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
        generate_javascript()
    elif arg_javascript:
        generate_javascript()
    elif arg_now:
        print time.strftime(TIME_FORMAT)
    else:
        die(usage())

if __name__ == '__main__':
    main(docopt(usage()))
