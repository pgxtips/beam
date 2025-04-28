async function settingsPoster(e){
    e.preventDefault()

    let formEl = document.getElementById("settingsForm")
    let formData = new FormData(formEl)

    await post_controller("/internal/post/settings", cbSettingsPoster, formData, true)
}
