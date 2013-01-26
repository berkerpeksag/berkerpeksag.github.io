(function () {
    'use strict';
    var titleElm = document.querySelector('article > header');
    var bodyElm = document.querySelector('article > .body');
    if (!titleElm || !bodyElm)
        return;
    var limit = titleElm.offsetTop;
    var titleCls = titleElm.classList;
    var bodyCls = bodyElm.classList;
    window.onscroll = function (evt) {
        var scrollTop = Math.max(document.body.scrollTop,
                                 document.documentElement.scrollTop);
        if (limit < scrollTop) {
            titleCls.add('float');
            bodyCls.add('body-padding');
        }
        else {
            titleCls.remove('float');
            bodyCls.remove('body-padding');
        }
    };
 })();
