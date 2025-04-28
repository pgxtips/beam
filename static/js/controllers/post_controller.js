/**
*  @param {string} endpoint - api endpoint url
*  @param {fn} callback - callback function after request concludes
*  @param {Object} data - json data for post 
*/
async function post_controller(endpoint, callback, data){
    if (data instanceof FormData) post_form(endpoint, callback, data)
    else post_json(endpoint, callback, data)
}

async function post_form(endpoint, callback, formData) {
    try {
        let req = await fetch(endpoint, {
            method: "POST",
            body: formData
        })
        let json = await req.json()
        return callback(json)
    } catch(e) {
        console.log("Error: " + e)
    }
}

async function post_json(endpoint, callback, data) {
    try {
        let req = await fetch(endpoint, {
            method: "POST",
            body: JSON.stringify(data),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        })
        let json = await req.json()
        return callback(json)
    } catch(e) {
        console.log("Error: " + e)
    }
}

function process_inputs(){
}
