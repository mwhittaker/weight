
        $(function () {
            $('#container').highcharts({
                chart: {
                    type: 'line'
                },
                title: {
                    text: 'Weight Loss'
                },
                xAxis: {
                    type: 'datetime',
                    dateTimeLabelFormats: { // don't display the dummy year
                        month: '%e. %b',
                        year: '%b'
                    },
                    title: {
                        text: 'Date'
                    }
                },
                yAxis: {
                    title: {
                        text: 'Weight (lb)'
                    }
                },
                plotOptions: {
                    line: {
                        dataLabels: {
                            enabled: true
                        },
                        enableMouseTracking: true,
                        marker: {
                            enabled: true
                        }
                    }
                },
                series: [{
                    name: 'michael',
                    data: [[Date.UTC(2015, 5, 24, 23, 45), 215.8], [Date.UTC(2015, 5, 25, 7, 43), 214.0], [Date.UTC(2015, 5, 25, 9, 35), 214.8], [Date.UTC(2015, 5, 25, 10, 50), 216.4], [Date.UTC(2015, 5, 25, 11, 26), 215.6], [Date.UTC(2015, 5, 25, 13, 17), 214.0], [Date.UTC(2015, 5, 25, 15, 15), 213.0], [Date.UTC(2015, 5, 25, 21, 4), 213.8], [Date.UTC(2015, 5, 26, 8, 13), 211.4], [Date.UTC(2015, 5, 26, 9, 12), 212.0], [Date.UTC(2015, 5, 26, 9, 53), 211.6], [Date.UTC(2015, 5, 26, 11, 47), 213.4], [Date.UTC(2015, 5, 26, 20, 30), 214.6], [Date.UTC(2015, 5, 26, 21, 26), 214.2], [Date.UTC(2015, 5, 27, 7, 39), 211.6], [Date.UTC(2015, 5, 27, 23, 46), 214.4], [Date.UTC(2015, 5, 28, 7, 5), 212.2], [Date.UTC(2015, 5, 28, 22, 14), 214.0], [Date.UTC(2015, 5, 30, 11, 35), 211.8], [Date.UTC(2015, 5, 31, 0, 42), 211.6], [Date.UTC(2015, 5, 31, 10, 12), 211.4], [Date.UTC(2015, 5, 31, 20, 0), 211.4], [Date.UTC(2015, 6, 2, 22, 12), 211.8], [Date.UTC(2015, 6, 6, 10, 26), 208.8], [Date.UTC(2015, 6, 8, 22, 36), 210.8], [Date.UTC(2015, 6, 9, 7, 15), 208.6], [Date.UTC(2015, 6, 9, 23, 2), 210.0], [Date.UTC(2015, 6, 12, 7, 28), 206.6], [Date.UTC(2015, 6, 13, 9, 55), 205.6], [Date.UTC(2015, 6, 15, 21, 56), 207.6]]
                }]
            });
        });
    