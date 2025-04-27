
$(document).ready(async function(){

    const cpuChart = new Chart(document.getElementById('cpuChart'), {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'CPU %',
                data: [],
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 2,
                fill: false,
            }]
        },
        options: {
            scales: {
                x: { ticks: { color: '#bbb' }, display: false},
                y: { min: 0, max: 100, ticks: { color: '#bbb' } }
            }
        }
    });

    const memoryChart = new Chart(document.getElementById('memoryChart'), {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Memory %',
                data: [],
                borderColor: 'rgba(153, 102, 255, 1)',
                borderWidth: 2,
                fill: false,
            }]
        },
        options: {
            scales: {
                x: { ticks: { color: '#bbb' }, display: false},
                y: { min: 0, max: 100, ticks: { color: '#bbb' } }
            }
        }
    });

    const incomingTrafficChart = new Chart(document.getElementById('incomingTrafficChart'), {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Incoming (KB/s)',
                data: [],
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 2,
                fill: false,
            }]
        },
        options: {
            scales: {
                x: { ticks: { color: '#bbb' }, display: false},
                y: { ticks: { color: '#bbb' } }
            }
        }
    });

    const outgoingTrafficChart = new Chart(document.getElementById('outgoingTrafficChart'), {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Outgoing (KB/s)',
                data: [],
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 2,
                fill: false,
            }]
        },
        options: {
            scales: {
                x: { ticks: { color: '#bbb' }, display: false},
                y: { ticks: { color: '#bbb' } }
            }
        }
    });

    setInterval(async () => {
        await monitorRedeemer({ 
            cpuChart, memoryChart, incomingTrafficChart, outgoingTrafficChart
        })
    }, 2000);

})
