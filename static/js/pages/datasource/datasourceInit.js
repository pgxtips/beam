console.log("data source init")

var hasChanged = false

$(document).ready(async function(){
       
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
    $("#fileInputCont").hide()
    $("#databaseInputCont").hide()
}

function selectFile(){
    $("#fileInputCont").show()
    $("#databaseInputCont").hide()
}

function selectDatabase(){
    $("#databaseInputCont").show()
    $("#fileInputCont").hide()
}
