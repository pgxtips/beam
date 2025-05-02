$(document).ready(async function(){

    $("select, input").change(function(event){
        console.log("input changed")
        $("#saveButtons").show()
    })

    $("#batchSizeInput").change(function(event){
        let batch_size = $("#batchSizeInput").val()
        $("#displayBatchSize").text(batch_size)
    })

    $("#submitButton").click(async function(event){
        await settingsPoster(event)
    })

    $("#submitButton").click(async function(event){
        await settingsPoster(event)
    })

    $("#deletePKL").click(async function(event){
        await get_controller("/internal/get/deletepkl", cbDeletePKL, {}, true)
    })

    await settingsRedeemer()
})
