function add_new_post(data) {
    var ul = $('#one_post')
    var li = document.createElement('li')
    var a = document.createElement('a')
    var node = document.createTextNode(data.title)
    a.appendChild(node)
    a.setAttribute('href', 'javascript:;')
    a.setAttribute('onclick', 'show_post(' + data.id + ')')
    li.appendChild(a)
    ul.prepend(li)
}
function clicks() {
    $.ajax({
        type: 'POST',
        url: '../add_new_post/',
        data: {},
        scriptCharset: 'utf-8',
        success: function (data) {
            jsonObject = JSON.parse(data)
            add_new_post(jsonObject)
        }
    })
}

function show_post(id) {
    $("#one_post li").click(function () {
        $(this).siblings('li').attr('data-s', "1")
        $(this).siblings('li').css('background-color','#fff')
        $(this).attr("data-s", "2")
        $(this).css('background-color','#f60')
    });
    $.ajax({
        type: 'POST',
        url: '../show_post/' + String(id) + '/',
        data: {},
        success: function (data) {
            jsonObject = JSON.parse(data)
            $('#main_title').val(jsonObject.title)
            $('#main_body').val(jsonObject.body)
        }
    })
}
function get_id() {
    $('#one_post li').each(function () {
        var s = ($(this)).attr('data-s')
        if (s == 2){
            id = $(this).attr('data-id')
            return false
        }
    })
    return id
}

function set_title(id , title) {
    $('#one_post li').each(function () {
        var s = ($(this)).attr('data-id')
        if (s == id){
            $(this).find('a').html(title)
            return false
        }
    })
}

function save_post() {
    title = $('#main_title').val()
    body = $('#main_body').val()
    id = get_id()
    $.ajax({
        type: 'POST',
        url: '../save_post/' +String(id)+'/',
        data: {
            'title': title,
            'body': body,
            'id':id
        },
        success:function(data) {
            set_title(id, title)
        },
    })
}