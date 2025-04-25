async function get_controller(endpoint, callback){
    try {
        let req = await fetch(endpoint)
        let json = await req.json()
        return callback(json)
    } catch(e) {
        console.log("Error: " + e)
    }
}
