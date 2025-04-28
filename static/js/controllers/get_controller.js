async function get_controller(endpoint, callback, props, send_toast){
    try {
        let req = await fetch(endpoint)
        let json = await req.json()

        if (send_toast){ createToast(json, endpoint, "successfully made request") }
        return callback(props, json)
    } catch(e) {
        createToast(0, endpoint, e)
        console.log("Error: " + e)
    }
}
