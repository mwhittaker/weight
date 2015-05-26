
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
                    data: [[Date.UTC(2015, 5, 24, 23, 45), 215.8], [Date.UTC(2015, 5, 25, 7, 43), 214.0], [Date.UTC(2015, 5, 25, 9, 35), 214.8], [Date.UTC(2015, 5, 25, 10, 50), 216.4], [Date.UTC(2015, 5, 25, 11, 26), 215.6], [Date.UTC(2015, 5, 25, 13, 17), 214.0], [Date.UTC(2015, 5, 25, 15, 15), 213.0], [Date.UTC(2015, 5, 25, 21, 4), 213.8], [Date.UTC(2015, 5, 26, 8, 13), 211.4], [Date.UTC(2015, 5, 26, 9, 12), 212.0], [Date.UTC(2015, 5, 26, 9, 53), 211.6], [Date.UTC(2015, 5, 26, 11, 47), 213.4]]
                }]
            });
        });
    