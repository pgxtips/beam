async function datasourceRedeemer(){
    await get_controller("/internal/get/datasource", cbDatasource, {})
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
        case "1":
            $("#fileNameDisplay").text(source_data)
            selectDemo()
            break;
        case "2":
            $("#fileNameDisplay").text(source_data)
            selectFile()
            break;
        case "3":
            selectDatabase()
            $("#databaseInput").val(source_data)
            break;
    }

    // build attributes of content and tag selects
    for (let [idx, attr] of attributes.entries()) {
        let op1 = document.createElement("option")
        let op2 = document.createElement("option")

        $(op1).val(idx)
        $(op1).text(attr)
        $(op2).val(idx)
        $(op2).text(attr)

        $("#selectContent").append(op1)
        $("#selectTag").append(op2)
    }

    $("#selectContent").val(content_column)
    $("#selectTag").val(tag_column)

    $(".saveButtons").hide()
    $(".loading-state").hide()
}
