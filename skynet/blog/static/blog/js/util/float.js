$(document).ready(function () {
    $(".item").popup();
    $(".page-scroll").click(function () {
        $("html, body").animate({
            scrollTop: $($(this).attr("href")).offset().top-100+"px",
        }, "slow");
    });
});
