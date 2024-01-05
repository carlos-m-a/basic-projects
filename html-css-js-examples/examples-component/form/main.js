function form_submitted() {
    document.getElementById("processing_request").style.display = "block"
    document.getElementById("submitbutton").disabled = true
    document.getElementById("submitbutton").style.cursor = "not-allowed"
    document.getElementById("name").style.cursor = "not-allowed"
    document.getElementById("password").style.cursor = "not-allowed"
    document.getElementById("number").style.cursor = "not-allowed"
    document.getElementById("file").style.cursor = "not-allowed"
    document.getElementById("commit").style.cursor = "not-allowed"
    
}


function main(){
    // function1()
}

window.addEventListener("load", main, false);