var options1 = {
	type: 'doughnut',
	data: {
	  labels: [ "Good", "Warning","" ],
	  datasets: [
		 {
				  label: '# of Votes',
				  data: [35, 15, 30],
				  backgroundColor: [
					   'rgba(46, 204, 113, 1)',
					  'rgba(255, 164, 46, 1)',
					 'rgba(231, 76, 60, 1)',
				  ],
				  borderColor: [
					  'rgba(255, 255, 255 ,1)',
					  'rgba(255, 255, 255 ,1)',
					  'rgba(255, 255, 255 ,1)'
				  ],
				  borderWidth: 5
			  }
		  ]
	},
	options: {
	 rotation: 1 * Math.PI,
			  circumference: 1 * Math.PI,
			  legend: {
				  display: false
			  },
			  tooltip: {
				  enabled: false
			  },
			  cutoutPercentage: 80
	}
  }
  
  var ctdght1 = document.getElementById('chartJSContainer').getContext('2d');
  new Chart(ctdght1, options1);
  
  var options2 = {
	type: 'doughnut',
	data: {
	 labels: ["", "", ""],
			  datasets: [
				 {
					  data: [8, 1,45],
					  backgroundColor: [
						  "rgba(0,0,0,0)",
						   "rgba(1, 34, 15)",
							"rgba(0,0,0,0)",
					  ],
					   borderColor: [
					  'rgba(0, 0, 0 ,0)',
					   'rgba(1, 34, 15)',
					  'rgba(0, 0, 0 ,0)'
				  ],
				  borderWidth: 3
					
				  }]
	},
	options: {
	  cutoutPercentage: 85,
	   rotation: 1 * Math.PI,
		circumference: 1 * Math.PI,
			  legend: {
				  display: false
			  },
			  tooltips: {
				  enabled: false
			  }
	}
  }
  
  var ctdght = document.getElementById('secondContainer').getContext('2d');
  new Chart(ctdght, options2);