/**
*  @param {string} endpoint - api endpoint url
*  @param {fn} callback - callback function after request concludes
*  @param {Object} data - json data for post 
*  @param {boolean} send_toast - bool to create toasts
*/
async function post_controller(endpoint, callback, data, send_toast){
    try {
        let json;

        if (data instanceof FormData) json = await post_form(endpoint, data)
        else json = await post_json(endpoint, data)

        let status = json.status

        if (send_toast){ createToast(json, endpoint, "successfully made request") }

        return callback(json)
    } catch (e) {
        createToast(0, endpoint, e)
        console.log("Error: " + e)
    }
}

async function post_form(endpoint, formData) {
    try {
        let req = await fetch(endpoint, {
            method: "POST",
            body: formData
        })
        let json = await req.json()

        return json
    } catch(e) {
        console.log("Error: " + e)
        return e
    }
}

async function post_json(endpoint, data) {
    try {
        let req = await fetch(endpoint, {
            method: "POST",
            body: JSON.stringify(data),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        })
        let json = await req.json()
        return json
    } catch(e) {
        console.log("Error: " + e)
        return e
    }
}
