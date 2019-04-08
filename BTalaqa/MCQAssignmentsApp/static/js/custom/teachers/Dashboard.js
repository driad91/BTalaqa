$( document ).ready(function() {
    var sumAssignedTests =0;
    var sumSolvedAssignedTests =0;

$('.count-assigned-tests').each(function() {
    sumAssignedTests += parseInt($(this).text());

});
$('.completed-assigned-tests').each(function() {
    sumSolvedAssignedTests += parseInt($(this).text());

});


var ctx = document.getElementById('barchart-assigned-solved').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Total Assigned Tests','Total Assigned Completed Tests'],
        datasets: [{
            label: 'Total # of tests',
            data: [sumAssignedTests,sumSolvedAssignedTests],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',

            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',

            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});


});