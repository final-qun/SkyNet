$(document).ready(function () {
    $('#delete_blog').click(function () {
        index = $('#delete_blog').attr('data-index');
        $('#confirm').attr('href','/blog/delete/'+index);
        $('.ui.modal').modal({
            closable: false,
        }).modal('show');
    })
});
