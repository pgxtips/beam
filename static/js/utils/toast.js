function createToast(json, headerMsg, msg){

    let status = json.status
    let statusMsg = json.status_msg

    let header = ""

    switch (status){
        case 200:
            header += "Success"
            break

        case 404:
            header += "Not Found"
            break

        case 500:
            header += "Internal Error"
            break
        default:
            header += "Unknown"
            break
    }

    header += " - " + headerMsg


    const template = $(`
        <div class="toast" role="alert" aria-live="assertive" aria-atomic="true">
          <div class="toast-header">
            <img src="/img/logo.png" style="width: 6%;" class="rounded me-2" alt="...">
            <strong class="me-auto">beam - ${header}</strong>
            <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
          </div>
          <div class="toast-body">
            ${statusMsg ? statusMsg + " - " : ""} ${msg}
          </div>
        </div>
   `)

    $(".toast-container").append(template)

    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(template)
    toastBootstrap.show()
}
