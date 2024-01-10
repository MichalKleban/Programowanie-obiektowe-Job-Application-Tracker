function edit_application(id){
    document.getElementById("applicationForm").action = "/edit_job"
    tableRow = document.getElementById("myRow"+id)
    console.log(tableRow)
    
    company = tableRow.children[1].innerText
    position = tableRow.children[2].innerText
    dateofappy = tableRow.children[3].innerText
    site = tableRow.children[4].innerText
    job_status = tableRow.children[5].innerText
    cv_version = tableRow.children[6].innerText
    mode = tableRow.children[7].innerText
    contract_type = tableRow.children[8].innerText
    job_level = tableRow.children[9].innerText

    document.getElementById("company_name").value = company
    document.getElementById("position").value = position
    document.getElementById("dateofapply").value = dateofappy
    document.getElementById("site").value = site
    document.getElementById("status").value = job_status
    document.getElementById("cv_version").value = cv_version
    document.getElementById("mode").value = mode
    document.getElementById("contract_type").value = contract_type
    document.getElementById("job_level").value = job_level
    
}