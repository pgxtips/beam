async function datasourceRedeemer(){
    await get_controller("/internal/get/datasource", cbDatasource, {}, true)
}

function cbDatasource(props, data){
    console.log(data)
    let source_type = data.source_type ?? "N/A" 
    let source_data = data.source_data ?? "N/A"  
    let attributes = data.attributes ?? []

    let content_column = data.content_column ?? "N/A"  
    let tag_column = data.tag_column ?? "N/A"  

    $("#selectInput").val(source_type)

    switch (source_type){
        case "demo":
            selectDemo()
            $("#fileNameDisplay").text(source_data)
            break;
        case "file":
            selectFile()

            $("#fileNameDisplay").text(source_data)
            $("#selectContentCont").show()
            $("#selectTagCont").show()
            break;
        case "database":
            selectDatabase()
            $("#databaseInput").val(source_data)
            break;
    }

    // build attributes of content and tag selects
    for (let attr of attributes) {
        let op1 = document.createElement("option")
        let op2 = document.createElement("option")

        $(op1).val(attr)
        $(op1).text(attr)

        $(op2).val(attr)
        $(op2).text(attr)

        $("#selectContent").append(op1)
        $("#selectTag").append(op2)
    }

    $("#selectContent").val(content_column)
    $("#selectTag").val(tag_column)

    $(".saveButtons").hide()
    $(".loading-state").hide()
}

function cbAttributes(data){

    $("#selectContentCont").show()
    $("#selectTagCont").show()
    $("#saveButtons").show()

    console.log(data)
    let keys = data.keys


    $("#selectContent").html("")
    $("#selectTag").html("")

    // build attributes of content and tag selects
    for (let attr of keys) {
        let op1 = document.createElement("option")
        let op2 = document.createElement("option")

        $(op1).val(attr)
        $(op1).text(attr)

        $(op2).val(attr)
        $(op2).text(attr)

        $("#selectContent").append(op1)
        $("#selectTag").append(op2)
    }

    $(".saveButtons").hide()
    $(".loading-state").hide()
}


function cbFormPost(data){
    console.log("form post complete")
    console.log(data)

    $("#saveButtons").hide()
}
