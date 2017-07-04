function add_new_post(data) {
    var ul = document.getElementById('one_post')
    var li = document.createElement('li')
    var a = document.createElement('a')
    var node = document.createTextNode(data.title)
    a.appendChild(node)
    a.setAttribute('href','javascript:;')
    a.setAttribute('onclick','show_post('+data.id+')')
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

    $.ajax({
        type: 'POST',
        url: '../show_post/'+String(id)+'/',
        data:{},
        success: function (data) {
            alert(data)
            jsonObject = JSON.parse(data)
            alert(jsonObject.title)
            document.getElementById('main_title').value = jsonObject.title
            document.getElementById('main_body').innerHTML = jsonObject.body
        }
    })
}

function save_post(id) {
    title = document.getElementById('main_title')
    body = document.getElementById('main_body')
    id =
    $.ajax({
        type:'POST',
        url: '../save_post/',
        data:{
            'title':title,
            'body':body,
        }
    })
}