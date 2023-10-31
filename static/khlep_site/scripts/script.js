var isVisible = false;

var clickEnable = function () {
    $(".searchButton").css({"background":"white"});
    $(".searchInput").css({"width":"240px", "padding":"0 6px", "visibility":"visible"});
    isVisible = true;
};

var clickDisable = function () {
    $(".searchButton").css({"background":"#27f042"});
    $(".searchInput").css({"width":"0px", "padding":"0", "visibility":"hidden"});
    isVisible = false;
};

$('.map, .searchInput').keypress(function(event){
    var keycode = (event.keyCode ? event.keyCode : event.which);
    if(keycode == '13'){ 
        if (isVisible == false) {
            clickEnable();
        } else {
            clickDisable();
        }
    }
});

$(".searchButton").click(function () {
    if (isVisible == false) {
        clickEnable();
    } else {
        clickDisable();
    }
})
