$(document).ready(function () {
    $(".ui.dropdown").dropdown({
        on: "hover",
        action: "nothing",
    });
    $("#create_blog").on("click", function () {
        $.ajax({
            type: "get",
            url: "/blog/create_blog/",
            success: function (data) {
                jsonobj = JSON.parse(data);
                if(jsonobj.error == 1) {
                    window.location.href = '/blog/login';
                }else {
                    window.location.href = '/blog/edit/' + jsonobj.id;
                }
            }
        });
    });

});