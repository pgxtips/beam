console.log("data source init")

var hasChanged = false

$(document).ready(async function(){

    $("select, input").change(function(event){
        console.log("input changed")
        $("#saveButtons").show()
    })

    $("#submitButton").click(async function(event){
        event.preventDefault()
        console.log("uploading")

        let formEl = document.getElementById("datasourceForm")
        console.log(formEl)
        let formData = new FormData(formEl)
        console.log(formData)
        
        function cbPost(data){
            console.log("post complete")
            console.log(data)
        }

        await post_controller("/internal/post/datasource", cbPost, formData)
    })
       
    $("#selectInput").change(function(event){
        let selected = $("#selectInput :selected")
        let option = Number(selected.val())

        switch(option){
            case 1:
                selectDemo()
                break;
            case 2:
                selectFile()
                break;
            case 3:
                selectDatabase()
                break;
        }
    });

    await datasourceRedeemer()
})


function selectDemo(){
    $("#fileInputButton").attr("disabled", "true")
    $("#selectContent").attr("disabled", "true")
    $("#selectTag").attr("disabled", "true")
    $("#fileNameDisplay").text("DEMO_FILE.json")
    $("#fileInputCont").show()
    $("#databaseInputCont").hide()
}

function selectFile(){
    $("#fileInputButton").removeAttr("disabled")
    $("#fileInputCont").show()
    $("#databaseInputCont").hide()
}

function selectDatabase(){
    $("#databaseInputCont").show()
    $("#fileInputCont").hide()
}
