$(document).ready(function () {
    $('.ui.login.form').form({
        inline: true,
        on: 'blur',
        fields: {
            name: {
                identifier: 'name',
                rules: [
                    {
                        type: 'empty',
                        prompt: '邮箱不能为空'
                    }
                ]
            },
            pwd: {
                identifier: 'pwd',
                rules: [
                    {
                        type: 'empty',
                        prompt: '密码不能为空'
                    },
                    {
                        type: 'length[6]',
                        prompt: '您的密码至少6位'
                    }
                ]
            }
        },
    }).api({
        url: '../login/',
        serializeForm: true,
        method: 'post',
        onSuccess: function (response) {
            if (response.error != '') {
                $('.ui.form').form('add prompt', 'email', response.error)
            } else {
                window.location.href = '../'
            }
        },
    });
    $(document).ready(function () {
        $('.ui.register.form').form({
            inline: true,
            on: 'blur',
            fields: {
                name: {
                    identifier: 'name',
                    rules: [
                        {
                            type: 'empty',
                            prompt: '昵称不能为空'
                        },
                    ]
                },
                email: {
                    identifier: 'email',
                    rules: [
                        {
                            type: 'empty',
                            prompt: '邮箱不能为空'
                        },
                        {
                            type: 'email',
                            prompt: '请输入有效的邮箱'
                        }
                    ]
                },
                pwd: {
                    identifier: 'pwd',
                    rules: [
                        {
                            type: 'empty',
                            prompt: '密码不能为空'
                        },
                        {
                            type: 'length[6]',
                            prompt: '您的密码至少6位'
                        }
                    ]
                },
                pwd2: {
                    identifier: 'pwd2',
                    rules: [
                        {
                            type: 'empty',
                            prompt: '密码不能为空'
                        },
                        {
                            type: 'length[6]',
                            prompt: '您的密码至少6位'
                        }
                    ]
                }
            },
        }).api({
            url: '../register/',
            serializeForm: true,
            method: 'POST',
            onSuccess: function (response) {
                if (response.error != '') {
                    $('.ui.form').form('add prompt', response.field, response.error);
                } else {
                    window.location.href = '../';
                }
            },
        });
    });
});
