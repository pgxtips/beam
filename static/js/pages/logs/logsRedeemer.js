async function logsRedeemer(){
    await get_controller("/internal/logs", cbLogs, {})
}

function cbLogs(props, data){
    console.log(data)
    let table = $("#logsTable")
    let body = table.find("tbody")

    const td = (txt) => {
        const cell = document.createElement("td");
        cell.textContent = txt;
        return cell;
    };

    for (let dp of data) {
        let ts = dp.timestamp ?? "N/A"
        let type = dp.type ?? "N/A"
        let sid = dp.session_id ?? "N/A"
        let msg = dp.message ?? "N/A"
        let details = JSON.stringify(dp.details) ?? "N/A"

        let tr = document.createElement("tr")

        tr.append(td(ts))
        tr.append(td(type))
        tr.append(td(sid))
        tr.append(td(msg))
        tr.append(td(details))

        body.append(tr)
    }

    $(".loading-state").hide()
}
