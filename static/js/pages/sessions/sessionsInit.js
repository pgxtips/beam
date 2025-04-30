$(document).ready(async function(){

    $("#sessionTable").on("click", "tr", function(event) {
        console.log("tr clicked")
        loadRowData(event)
    })

    await sessionsRedeemer()
})

function loadRowData(event){
    let el = $(event.currentTarget)
    let sid = el.data("sid")

    let data = SESSION_DATA[sid]

    $("#info-sid").text(data.session_id)
    $("#info-pref").text(data.preferences.join(", "))
    $("#info-likes").text(data.likes.join(", "))
    $("#info-dislikes").text(data.dislikes.join(", "))
    $("#info-activeModel").text()
    $("#info-lastTrain").text(data.last_trained)
    $("#info-modelSamples").text(data.model_samples)
    $("#info-history").text(data.history.join(", "))

    $("#noTableRowsSelectedText").hide()
    $("#sessionInfo").show()
}


