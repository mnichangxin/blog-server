from server.utils.exception.exception import APIException, ServerException
from server.utils.decorators.json_required import json_required
from server.utils.decorators.commit import commit

@commit
def fileUpload(files):
    filesCount = len(files)
    if filesCount == 0:
        raise APIException('文件不能为空')
    for i in files:
        print(dir(files[i]))
    return {
        'msg': '上传成功'
    }