### API（C端）

1. 文章列表查询：/api/v1/internal/view/post/query

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

2. 文章列表查询（根据分类）：/api/v1/internal/view/post/queryByCategory

* 入参：

```json
    {
        "category_id": "", // 分类 id
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

3. 文章列表查询（根据标签）：/api/v1/internal/view/post/queryByTag

* 入参：

```json
    {
        "tag_id": "", // 标签 id
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

4. 文章详细内容查询：/api/v1/internal/view/post/queryDetail

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
        "msg": "查询成功",
        "data": {
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
        }
    }
```