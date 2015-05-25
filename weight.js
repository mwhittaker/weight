
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
                    data: [[Date.UTC(2015, 5, 24, 23, 45), 215.8], [Date.UTC(2015, 5, 25, 7, 43), 214.0], [Date.UTC(2015, 5, 25, 9, 35), 214.8]]
                }]
            });
        });
    