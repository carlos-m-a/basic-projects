
function function1(e) {
    document.getElementById("change-me").innerHTML = e;
}

function function2() {
    // do something again
}



function main(){
    function1("I’ve been changed authomatically at loading!")

    function2()
}

window.addEventListener("load", main, false);