async function get_controller(endpoint, callback, props){
    try {
        let req = await fetch(endpoint)
        let json = await req.json()
        return callback(props, json)
    } catch(e) {
        console.log("Error: " + e)
    }
}
