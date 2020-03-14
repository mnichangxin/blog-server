### API（B端）

1. 登录：/api/v1/internal/user/login

* 入参：

```json
    {
        "username": "", // 用户名
        "password": "" // 密码
    }
```

* 返回：

```json
    {
        "status": 0,
        "msg": "登录成功",
        "data": null
    }
```

2. 登出：/api/v1/internal/user/logout

* 入参：无

* 返回：

```json
    {
        "status": 0,
        "msg": "登出成功",
        "data": null
    }
```

3. 获取用户登录状态：/api/v1/internal/user/checkLogin

* 入参：无

* 返回：

```json
    {
        "status": 0,
        "msg": "用户未登录",
        "loginStatus": false,
        "data": null
    }
```

4. 文章发布：/api/v1/internal/post/publish

* 入参：

```json
    {
        "title": "", // 文章标题
        "content": "", // 文章内容
        "category_name", // 分类名称
        "tag_names": [] // 标签名称
    }
```

* 返回：

```json
    {
        "status": 0,
        "msg": "发布成功",
        "data": null
    }
```

5. 文章删除：/api/v1/internal/post/delete

* 入参：

```json
    {
        "post_id": "", // 文章 id 
    }
```

* 返回：

```json
    {
        "status": 0,
        "msg": "删除成功",
        "data": null
    }
```

6. 文章更新：/api/v1/internal/post/update

* 入参：

```json
    {
        "post_id": "", // 文章 id 
        "title": "", // 文章标题
        "content": "", // 文章内容
        "category_name", // 分类名称
        "tag_names": [], // 标签名称
    }
```

* 返回：

```json
    {
        "status": 0,
        "msg": "更新成功",
        "data": null
    }
```

7. 文章列表查询：/api/v1/internal/post/query

* 入参：

```json
    {
        "page_num": "", // 第 m 页
        "page_size": "", // 每页 n 条
    }
```

* 返回：

```json
    {
        "status": 0,
        "msg": "查询成功",
        "data": {
            "page_num": 1,
            "page_count": 10,
            "total": 50,
            "data": [{
                "id": 4,
                "title": "文章1",
                "category": null,
                "content": "only test",
                "tags": [{
                    "id": 1,
                    "tag_name": "Flask"
                }, {
                    "id": 2,
                    "tag_name": "Python"
                }],
                "created_date": "Sun, 12 Jan 2020 16:37:06 GMT",
                "updated_date": null
            }]
        }
    }
```

8. Markdown 文件上传解析：/api/v1/internal/post/fileUpload

* 入参：

```json
    {
        "file": "", // 文件 
    }
```

* 返回：

```json
    {
        "status": 0,
        "msg": "上传成功",
        "data": "<h1>文章1<h1><p>内容</p>"
    }
```