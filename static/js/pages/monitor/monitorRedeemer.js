async function monitorRedeemer(){
    await get_controller("/internal/monitor", cbMonitor)
}

function cbMonitor(data){
    let cpu_usage = data.cpu_usage ?? "N/A"
    let memory_usage = data.memory_usage ?? "N/A"
    let incoming_traffic = data.incoming_traffic ?? "N/A"
    let outgoing_traffic = data.outgoing_traffic ?? "N/A"
    let average_response_time = data.average_response_time ?? "N/A"
    console.log(data)
}
