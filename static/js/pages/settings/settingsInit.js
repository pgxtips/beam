$(document).ready(async function(){

    $("select, input").change(function(event){
        console.log("input changed")
        $("#saveButtons").show()
    })

    await settingsRedeemer()
})
