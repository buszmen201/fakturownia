function showResult(str) {
    if (str.length == 0) {
        document.getElementById("livesearch").innerHTML = "";
        document.getElementById("livesearch").style.border = "0px";
        return;
    }


    if (window.XMLHttpRequest) {
        // code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp = new XMLHttpRequest();
    } else {  // code for IE6, IE5
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("livesearch").innerHTML = this.responseText;
            document.getElementById("livesearch").style.border = "1px solid #A5ACB2";
        }
    }
    var url = window.location.href;
    var url = url.split("/")
    xmlhttp.open("GET", url[0] + "//" + url[2] + "/livesearch?q=" + str, true);
    xmlhttp.send();
}

function addNext() {
    $('.search-bar').show();
    $('#livesearch').show().css("border-width", "0px");
}

function chooseThis(cur_node, val){
    cur_node.setAttribute("onClick","removeThis(this, " + val + ")");
    console.log(cur_node);
    $('.search-bar').hide().val("");
    $('#livesearch').hide().html("");
    $(cur_node).insertAfter( "#products_id" );
    val += ", ";
    document.getElementById("products_id").value += val;
}

function removeThis(cur_node, val) {
    var curr = document.getElementById("products_id").value;
    var arr = curr.split(", ");
    console.log(arr);
    var new_vals = ""
    for (var i = 0; i < arr.length; i++) {
        if ( (arr[i] != val) && (arr[i].length > 0) ) {
            console.log(arr[i])
            new_vals += arr[i]
            new_vals += ", ";
        }
    }
    $('p[value=' + val + ']').remove();
    document.getElementById("products_id").value = new_vals;





}

