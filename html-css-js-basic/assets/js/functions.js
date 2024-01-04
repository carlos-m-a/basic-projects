function buttonclick() {
    document.getElementById("change-me").innerHTML = "Changed when button clicked";
}

async function call_API_endpoint(url){
    try {
        response = await fetch(url);
        return response;
    } catch (err) {
        console.log(err);
    }
}

async function example_call_API_and_wait_result(url){
    response = await call_generate_API_endpoint(url)
    if(response.status >= 100 && response.status < 200){
        window.alert("informational response")
    }else if(response.status >= 200 && response.status < 300){
        window.alert("successful")
    } else if(response.status >= 300 && response.status < 400){
        window.alert("redirection")
    } else if(response.status >= 400 && response.status < 500){
        window.alert("client error")
    }else if(response.status >= 500){
        window.alert("server error ")
    } else {
        window.alert("HTTP ERROR: ")
    }
}