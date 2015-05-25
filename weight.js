
        $(function () {
            $('#container').highcharts({
                chart: {
                    type: 'line'
                },
                title: {
                    text: 'Weight Loss'
                },
                xAxis: {
                    categories: ['May 24, 2015 22:55:04', 'May 24, 2015 22:55:38', 'May 24, 2015 22:55:40', 'May 24, 2015 22:58:58', 'May 24, 2015 23:07:05']
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
                        enableMouseTracking: false
                    }
                },
                series: [{
                    data: [120.0, 120.0, 120.0, 120.0, 120.0]
                }]
            });
        });
    