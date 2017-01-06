KindEditor.ready(function (K) {
    window.editor = K.create('textarea[name="content"]', {
        width: '800',
        height: '200',
        //图片上存路径
        uploadJson: '/admin/upload/kindeditor',
    });
});