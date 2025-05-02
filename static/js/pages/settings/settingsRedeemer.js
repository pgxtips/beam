async function settingsRedeemer(){
    await get_controller("/internal/get/settings", cbSettings, {}, true)
}

function cbSettings(props, data){
    let default_model = data.default_model ?? "N/A"
    let batch_size = data.batch_size ?? "N/A"
    let auto_training = data.auto_training ?? "N/A"
    let ui_theme = data.ui_theme ?? "N/A"

    $("#selectModelInput").val(default_model)
    $("#batchSizeInput").val(batch_size)
    $("#displayBatchSize").text(batch_size)
    $("#selectAutoTrainingInput").val(""+auto_training)
    $("#selectUIThemeInput").val(ui_theme)

    $(".loading-state").hide()
    console.log(data)
}

function cbSettingsPoster(data){
    console.log(data)
    $("#saveButtons").hide()
}

function cbDeletePKL(props, data){
    console.log(data)
}

