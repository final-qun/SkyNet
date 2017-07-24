$(document).ready(function () {
    $(".dropdown").dropdown();
    $("#save_blog").on("click", function () {
        var $save_msg = $("<a class='ui item'>正在保存</a>");
        $(".right.menu").prepend($save_msg)
        var id = $("#blog-id").attr("data-index");
        var title = $("#title").val();
        var body = $("#body").val();
        $.ajax({
            type: "post",
            url: '../save_blog/' + id,
            data: {
                'title': title,
                'body': body
            },
            success: function (data) {
                $save_msg.text("已保存");
                $save_msg.animate({
                    opacity: 0,
                }, 2000, function () {
                    $(".right.menu").remove($save_msg);
                });
            }

        })
    });
    $('#pub_blog').on('click',function () {
        var id = $("#blog-id").attr("data-index");
        var title = $("#title").val();
        var body = $("#body").val();
        $.ajax({
            type: "post",
            url: '../pub_blog/' + id,
            data: {
                'title': title,
                'body': body
            },
            success: function (data) {
                $save_msg.text("已保存");
                $save_msg.animate({
                    opacity: 0,
                }, 2000, function () {
                    $(".right.menu").remove($save_msg);
                });
            }
        })
    });

    $("#blog_list").click(function () {
        $(".ui.sidebar")
            .sidebar('setting', 'transition', 'overlay')
            .sidebar('toggle');
    });
});