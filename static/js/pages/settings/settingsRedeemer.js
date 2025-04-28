async function settingsRedeemer(){
    await get_controller("/internal/get/settings", cbSettings, {})
}

function cbSettings(props, data){
    let model_type = data.model_type ?? "N/A"
    let batch_size = data.batch_size ?? "N/A"
    let auto_training = data.auto_training ?? "N/A"
    let training_interval = data.training_interval ?? "N/A"
    let ui_theme = data.ui_theme ?? "N/A"

    $("#selectModelInput").val(model_type)
    $("#batchSizeInput").val(batch_size)
    $("#selectAutoTrainingInput").val(auto_training)
    $("#selectIntervalInput").val(training_interval)
    $("selectUIThemeInput").val(ui_theme)
    

    $(".loading-state").hide()
    console.log(data)
}
