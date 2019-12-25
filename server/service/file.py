from markdown import markdown
from server.utils.exception.exception import APIException
from server.utils.decorators.commit import commit

@commit
def fileUpload(files):
    filesCount = len(files)
    if filesCount == 0:
        raise APIException('文件不能为空', 400)
    file = files['file']
    if file is None:
        raise APIException('file参数不能为空', 400)
    if file.content_type != 'text/markdown':
        raise APIException('文件格式不正确', 200)
    html_content = markdown(file.read().decode(encoding='utf-8'))
    return {
        'msg': '上传成功',
        'data': html_content
    }