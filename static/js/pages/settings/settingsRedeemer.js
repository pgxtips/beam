async function settingsRedeemer(){
    await get_controller("/internal/settings", cbSettings)
}

function cbSettings(data){
    let model_type = data.model_type ?? "N/A"
    let batch_size = data.batch_size ?? "N/A"
    let auto_training = data.auto_training ?? "N/A"
    let training_interval = data.training_interval ?? "N/A"
    let ui_theme = data.ui_theme ?? "N/A"

    console.log(data)
}
