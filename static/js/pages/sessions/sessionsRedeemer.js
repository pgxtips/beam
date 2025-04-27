async function sessionsRedeemer(){
    await get_controller("/internal/sessions", cbSessions)
}

function cbSessions(data){
    console.log(data)

    let table = $("#sessionTable")
    let body = table.find("tbody")

    const td = (txt) => {
        const cell = document.createElement("td");
        cell.textContent = txt;
        return cell;
    };

    for (let dp of data){
        let session_id = dp.session_id ?? "N/A"
        let created = dp.created ?? "N/A"
        let last_seen = dp.last_seen ?? "N/A"
        let preferences = dp.preferences ?? "N/A"
        let likes = dp.likes ?? "N/A"
        let dislikes = dp.dislikes ?? "N/A"
        let last_recs = dp.last_recs ?? "N/A"
        let model_samples = dp.model_samples ?? "N/A"
        let last_trained = dp.last_trained ?? "N/A"

        let tr = document.createElement("tr")

        tr.append(td(session_id))
        tr.append(td(created))
        tr.append(td(last_seen))
        tr.append(td(likes.length))
        tr.append(td(dislikes.length))
        tr.append(td(preferences.length))

        body.append(tr)
    }

}
