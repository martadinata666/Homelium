setTimeout(function() {
    var elem = document.getElementById("alert");
    elem.style.animation="spin2 4s linear infinite";
    elem.parentNode.removeChild(elem);
}, 5000);