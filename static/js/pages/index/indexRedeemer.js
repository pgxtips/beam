async function indexRedeemer(){
    await get_controller("/internal/get/index", cbIndex, {}, true)
}

function cbIndex(props, data){
    let rec_requests = data.rec_requests ?? "N/A"
    let active_sessions = data.active_sessions ?? "N/A"
    let system_status = data.system_status ?? "N/A"

    console.log($("#recRequests"))

    $("#recRequests").html(rec_requests)
    $("#activeSessions").html(active_sessions)
    $("#systemStatus").html(system_status)

    console.log(data)
    $(".loading-state").hide()
}
