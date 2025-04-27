async function datasourceRedeemer(){
    await get_controller("/internal/datasource", cbDatasource)
}

function cbDatasource(data){
    console.log(data)
    let source_type = data.source_type ?? "N/A" 
    let source_data = data.source_data ?? "N/A"  
    let content_column = data.content_column ?? "N/A"  
    let tag_column = data.tag_column ?? "N/A"  
}
