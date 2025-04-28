async function monitorRedeemer(props){
    console.log(props)
    await get_controller("/internal/get/monitor", cbMonitor, props, false)
}

function cbMonitor(props, data){
    let cpu_usage = data.cpu_usage ?? 0
    let memory_usage = data.memory_usage ?? 0
    let net_in = data.net_in ?? 0
    let net_out = data.net_out ?? 0
    console.log(data)

    const timestamp = new Date().toLocaleTimeString();

    let cpuChart = props.cpuChart
    let memoryChart = props.memoryChart
    let incomingTrafficChart = props.incomingTrafficChart
    let outgoingTrafficChart = props.outgoingTrafficChart

    cpuChart.data.labels.push(timestamp);
    memoryChart.data.labels.push(timestamp);
    incomingTrafficChart.data.labels.push(timestamp);
    outgoingTrafficChart.data.labels.push(timestamp);

    cpuChart.data.datasets[0].data.push(cpu_usage);
    memoryChart.data.datasets[0].data.push(memory_usage);
    incomingTrafficChart.data.datasets[0].data.push(net_in / 1024.0);
    outgoingTrafficChart.data.datasets[0].data.push(net_out / 1024.0);

    // Limit number of points (optional, keep it smooth)
    const maxPoints = 20;
    [cpuChart, memoryChart, incomingTrafficChart, outgoingTrafficChart].forEach(chart => {
        if (chart.data.labels.length > maxPoints) {
            chart.data.labels.shift();
            chart.data.datasets[0].data.shift();
        }
        chart.update();
    });

    $(".loading-state").hide()
}
