async function datasourcePoster(){
    await post_controller("/internal/post/datasource", cbDatasource, {}, true)
}

async function send_file(event){
    event.preventDefault()
    console.log("posting file")

    let formEl = document.getElementById("datasourceForm")

    let formData = new FormData(formEl)
    formData.set("file_upload", "true")

    await post_controller("/internal/post/datasource", cbAttributes, formData, true)
}

async function send_form(event){
    event.preventDefault()
    console.log("posting form")

    let formEl = document.getElementById("datasourceForm")

    let formData = new FormData(formEl)

    await post_controller("/internal/post/datasource", cbFormPost, formData, true)
}
