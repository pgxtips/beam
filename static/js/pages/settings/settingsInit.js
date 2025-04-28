$(document).ready(async function(){

    $("select, input").change(function(event){
        console.log("input changed")
        $("#saveButtons").show()
    })

    $("#batchSizeInput").change(function(event){
        let batch_size = $("#batchSizeInput").val()
        $("#displayBatchSize").text(batch_size)
    })

    await settingsRedeemer()
})
