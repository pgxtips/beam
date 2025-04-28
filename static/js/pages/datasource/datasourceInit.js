var hasChanged = false

$(document).ready(async function(){

    $("select, input").change(function(event){
        $("#saveButtons").show()
    })


    $("#fileInputButton").click(async function(event){
        $("#fileInput").click()
    })
    
    $("#fileInput").change(async function(event){
        let filename = event.currentTarget.files[0].name
        $("#fileNameDisplay").text(filename)
    })


    $("#submitButton").click(async function(event){
        event.preventDefault()
        console.log("uploading")

        let formEl = document.getElementById("datasourceForm")
        console.log(formEl)

        let formData = new FormData(formEl)

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
    $("#databaseInput").attr("disabled", "true")

    $("#fileNameDisplay").text("DEMO_FILE.json")
    $("#fileInputCont").show()
    $("#databaseInputCont").hide()
}

function selectFile(){
    $("#databaseInput").attr("disabled", "true")

    $("#fileInputButton").removeAttr("disabled")
    $("#selectContent").removeAttr("disabled")
    $("#selectTag").removeAttr("disabled")

    $("#fileInputCont").show()
    $("#databaseInputCont").hide()
}

function selectDatabase(){
    $("#fileInputButton").attr("disabled", "true")

    $("#databaseInput").removeAttr("disabled")
    $("#selectContent").removeAttr("disabled")
    $("#selectTag").removeAttr("disabled")

    $("#databaseInputCont").show()
    $("#fileInputCont").hide()
}
