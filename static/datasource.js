console.log("data source init")

var hasChanged = false

$(document).ready(function(){
       
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

//function selectFile(){
//    console.log("selecting file input")
//    $("#fileInputCont").removeClass("hidden")
//    $("#databaseInputCont").addClass("hidden")
//}
//
//function selectDatabase(){
//    console.log("selecting database input")
//    $("#databaseInputCont").removeClass("hidden")
//    $("#fileInputCont").addClass("hidden")
//}
