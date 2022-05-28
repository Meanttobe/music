require.config({
    paths: {
        "jquery": "plugins/jquery.min",
        "com": "plugins/common.min"
    }
});

require(['jquery', 'com'], function ($, com) {
    //登录注册切换
    $('#unauth_main').on('click', '.switch', function () {
        var _this = this;
        setTimeout(function () {
            $(_this).closest('.switch_box').hide().siblings().show();
        }, 400);
        setTimeout(function () {
            $('#unauth_main').removeClass('switching');
        }, 600);

        $('#unauth_main').addClass('switching');
    });

});
