// ============================================
// As of Chart.js v2.5.0
// http://www.chartjs.org/docs
// ============================================





var ctx = document.getElementById("chart-bars").getContext("2d");
//=================================================================

var chart    = document.getElementById('chart-line').getContext('2d'),
    gradient = chart.createLinearGradient(0, 0, 0, 450);

gradient.addColorStop(0, 'rgba(214, 51, 132, 0.7)');
gradient.addColorStop(0.5, 'rgba(214, 51, 132, 0.8)');
gradient.addColorStop(1, 'rgba(214, 51, 132, 0.7)');


var data  = {
    labels: [ '0', '6hrs ago', '5hrs ago', '4hrs ago', '3hrs ago', '2hrs ago', '1hrs ago' , 'Now'],
    datasets: [{
			//label: 'Custom Label Name',
			backgroundColor: gradient,
			pointBackgroundColor: '#164c35',
			borderWidth: 3,
			borderColor: 'rgba(214, 51, 132)',
			data: [50, 55, 80, 81, 54, 50,50, 55, 80, 81, 54, 50,50, 55, 80, 81, 54, 50,50, 55, 80, 81, 54, 50]
    }]
};



var options = {
	responsive: true,
	maintainAspectRatio: true,
	animation: {
		easing: 'easeInOutQuad',
		duration: 520
	},
	scales: {
		xAxes: [{
			gridLines: {
				color: 'rgba(200, 200, 200, 0.05)',
				lineWidth: 1
			}
		}],
		yAxes: [{
			gridLines: {
				color: 'rgba(200, 200, 200, 0.2)',
				lineWidth: 1
			}
		}]
	},
	elements: {
		line: {
			tension: 0.4
		}
	},
	legend: {
		display: false
	},
	point: {
		backgroundColor: 'white'
	},
	tooltips: {
		titleFontFamily: 'Open Sans',
		backgroundColor: 'rgba(0,0,0,0.3)',
		titleFontColor: 'red',
		caretSize: 5,
		cornerRadius: 2,
		xPadding: 10,
		yPadding: 10
	}
};


var chartInstance = new Chart(chart, {
    type: 'line',
    data: data,
		options: options
});

var chartInstance = new Chart(chartx, {
    type: 'bars',
    data: data,
		options: options
});