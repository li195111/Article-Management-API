# Article Management REST API - Big Data Interview

Django REST framework with JWT Authentication

## Requirements
- Docker

## Include
- Python 3.7
- Django 3.2 - `localhost:8000`
- Django-SimpleJWT
    - JWT Experid Time: default: `300 seconds ( 5 minutes )`
    - Refresh Experid Time: default: `7 days`.
    - Can setting at `article_restapi/settings.py`
- PostgreSQL 14.2 - `localhost:5432`
- pgAdmin4 - `localhost:5050`
## How To Start

1. Clone Repositry & `cd` to folder.
```
git clone https://github.com/li195111/Article-Management-API.git
cd Article-Management-API
```
2. rename `.env-sample` to `.env`

3. You have two options to start docker compose:
    1. `docker compose up` and wait a second to launch.
    2. `sh run.sh`
4. And after that will do following:
    1. If choice ( i ) in step 3, then open http://localhost:8000 and do the following APIs methods.
    2. else choice ( ii ), It will open browswe automatically. Just wait.
5. Then You can do whatever you want to test APIs.
6. To Close docker compose just run following:
    1. `docker compose stop && docker compose rm -f`
    2. `sh close.sh`

## User
Also can goto `/admin/` to edit model by default `Superuser`.
Can disable default `Superuser` by annotate line 3 in `init.sh` : `echo "from django.contrib.auth import get_user_ ...`

```
{
    "username":"admin",
    "password":"admin"
}
```

default `Normal User` create by default data in `fixtures.json`:
```
{
    "username":"hello",
    "password":"notcommonpassword"
}
```

## Set JWT

Headers : 
```
{
    "Authorization": "JWT <received JWT>"
}
```
## APIs Path, body and return

|Method|Path|Descriptions|
|-|-|-|
|POST|`/auth/users/`| Create `註冊(創建)` 使用者
|DELETE|`/auth/users/{user_id}`| Delete `刪除` 使用者
|POST|`/auth/jwt/create`| Login 登入 `取得` JWT
|POST|`/auth/jwt/refresh`| Refresh `更新` JWT
|POST|`/auth/jwt/verify`| Verify `驗證` JWT
|GET|`/api/article/authors/`| `取得所有` 作者
|GET|`/api/article/authors/{author_id}`| `取得` 作者
|POST|`/api/article/authors/`| `新增` 作者
|GET|`/api/article/articles/`| `取得所有` 文章
|GET|`/api/article/articles/{article_id}/`| `取得` 文章
|POST|`/api/article/articles/`| `新增` 文章
|PATCH|`/api/article/articles/{article_id}/`| `修改` 文章
|PUSH|`/api/article/articles/{article_id}/`| `置換` 文章
|DELETE|`/api/article/articles/{article_id}/`| `刪除` 文章

### Details

<details>
<summary><strong>POST Regeistry 註冊使用者</strong></summary>

Path: `/auth/users/`

- body:
    ```
    {
        "username":"hello",
        "email":"hello@hello.com",
        "password":"notcommonpassword"
    }
    ```

- return: 
    ```
    {
    "email": "",
    "username": "hello",
    "id": 3
    }
    ```
</details>

<details>
<summary><strong>DELETE 刪除使用者</strong></summary>

Path: `/auth/users/{user_id}`

- body:
    ```
    {
        "current_password":"notcommonpassword"
    }
    ```
- return:
    state_code 204
</details>

<details>
<summary><strong>POST Login 登入 取得 JWT</strong></summary>

Path: `/auth/jwt/create`

- body :
    ```
    {
        "username":"hello",
        "password":"notcommonpassword"
    }
    ```
- return:
    ```
    {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0NzUxMDI2OCwianRpIjoiOGI2MTYxNTU3MDBkNGEzNThjNDMxMGMyMTg2OWViMjUiLCJ1c2VyX2lkIjoyfQ.ephZg65d5yafZJfd8STjxhz7KXE5FYeBJUjfLmFLCqs",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ3NDI0MTY4LCJqdGkiOiJlZTdkZmNlODNiNjM0ODZlYmNkMTJhNjE3NjYyNDkzYyIsInVzZXJfaWQiOjJ9.jP1P0EDZsCo8u1FJXQLsgBJJnb2tfxWqXQMBinQqV7k"
    }
    ```
</details>
<details>
<summary><strong>POST Refresh 更新 JWT</strong></summary>

Path: `/auth/jwt/refresh`

- body:
    ```
    {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0NzUwNDczNiwiaWF0IjoxNjQ3NDE4MzM2LCJqdGkiOiI1MjBjMDA0NGRmZjU0NTk2YWFlYzYxMmM5MjcyYjRmMCIsInVzZXJfaWQiOjF9.IUOCu3glwEwSllXXaPgsjQCzIX-VVf6n402RYuXTqnE",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ3NDE4NjM2LCJpYXQiOjE2NDc0MTgzMzYsImp0aSI6ImJhMGFhNmEyZDcwZTQ5YzM5M2Y2MWQ2OTA0M2QxNjc2IiwidXNlcl9pZCI6MX0.HGqzhClKmoSKyv5A_Fj_8w09KeUqdgLAgniUq0sccSA"
    }
    ```
- return:
    ```
    {
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ3NDM3MjY5LCJqdGkiOiJhYmI4ZTVhODBiZWE0NWZlOTlmYzM1NTdiOGMxMzM2MiIsInVzZXJfaWQiOjN9.XVAW4kidj-bDst1gP6hUm504suDcskhlwmWFZitOAxA"
    }
    ```
</details>
<details>
<summary><strong>POST Verify 驗證 JWT</strong></summary>

Path: `/auth/jwt/verify`

- body:
    ```
    {
        "token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ3NDE4NjM2LCJpYXQiOjE2NDc0MTgzMzYsImp0aSI6ImJhMGFhNmEyZDcwZTQ5YzM5M2Y2MWQ2OTA0M2QxNjc2IiwidXNlcl9pZCI6MX0.HGqzhClKmoSKyv5A_Fj_8w09KeUqdgLAgniUq0sccSA"
    }
    ```
- return: 
    - success:
        ```
        {
            // Empty
        }
        ```

    - expired:
        ```
        {
        "detail": "Token is invalid or expired",
        "code": "token_not_valid"
        }
        ```
</details>

<details>
<summary><strong>GET 取得所有 作者</strong></summary>

Path: `/api/article/authors/`

- return:
    ```
    {
        "count": 0,
        "next": null,
        "previous": null,
        "results": []
    }
    ```

</details>
<details>
<summary><strong>GET 取得 作者</strong></summary>

Path: `/api/article/authors/{author_id}`

- return:
    ```
    {
        "name": "Author Name"
    }
    ```

</details>

<details>
<summary><strong>POST 新增 作者</strong></summary>

Path: `/api/article/authors/`

- body :
    ```
    {
        "name":"Author Name"
    }
    ```
- return:
    ```
    {
        "name": "Author Name"
    }
    ```

</details>

<details>
<summary><strong>GET 取得所有 文章</strong></summary>

Path: `/api/article/articles/`

- return: 
    ```
    {
        "count": 0,
        "next": null,
        "previous": null,
        "results": []
    }
    ```

</details>

<details>
<summary><strong>GET 取得 文章</strong></summary>

Path: `/api/article/articles/{article_id}`

- return:
    ```
    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "title": "YouTuber不好賺！一隻阿圓自曝月收7位數但戶頭只剩3萬",
                "tags": "一隻阿圓;月收;存錢;買房;YouTuber",
                "content": "「一隻阿圓」因為個性大方又擁有好身材，深受網友喜愛，時常位居「YouTuber聲量排行榜」上，近日許多創作者都公開自己的理財規劃，開箱買房裝潢等，但她拍片自曝，月收曾高達七位數，但由於開銷過大，現在帳戶只剩下三萬多。\nYouTuber不好賺？一隻阿圓曝：每月至少支出20萬\n阿圓透露自己雖然最高可以月收百萬，但是自己底下有兩到三位攝影師，以及兩位剪輯師，每月至少要付四個人薪水，不包含自己的生活費跟房租等，這些固定支出，每一個月至少要支出二十萬元，因此整體算下來，月收入只是比一般上班族多一些而已，而且有時候在幕後發展，職業生涯反而能走得更長久，影片中阿圓也大方公開自己付給員工的帳戶餘款，目前只剩下三萬四千元左右，YouTuber並沒有想像中那麼好賺。",
                "create_at": "2022-03-16T09:35:45.615007Z",
                "update_at": "2022-03-16T09:47:53.049018Z",
                "author": 1
            }
        ]
    }
    ```

</details>


<details>
<summary><strong>POST 新增 文章</strong></summary>

Path: `/api/article/articles/`

- body:
    ```
    {
        "title":"YouTuber不好賺！一隻阿圓自曝月收7位數但戶頭只剩3萬",
        "tags":"一隻阿圓;月收;存錢;買房;YouTuber",
        "content":"「一隻阿圓」因為個性大方又擁有好身材，深受網友喜愛，時常位居「YouTuber聲量排行榜」上，近日許多創作者都公開自己的理財規劃，開箱買房裝潢等，但她拍片自曝，月收曾高達七位數，但由於開銷過大，現在帳戶只剩下三萬多。\nYouTuber不好賺？一隻阿圓曝：每月至少支出20萬\n阿圓透露自己雖然最高可以月收百萬，但是自己底下有兩到三位攝影師，以及兩位剪輯師，每月至少要付四個人薪水，不包含自己的生活費跟房租等，這些固定支出，每一個月至少要支出二十萬元，因此整體算下來，月收入只是比一般上班族多一些而已，而且有時候在幕後發展，職業生涯反而能走得更長久，影片中阿圓也大方公開自己付給員工的帳戶餘款，目前只剩下三萬四千元左右，YouTuber並沒有想像中那麼好賺。",
        "author":1
    }
    ```

- return:
    ```

    ```

</details>


<details>
<summary><strong>PATCH 修改 文章 </strong></summary>

Path: `/api/article/articles/{article_id}/`

- body: 
    ```
    {
        "content":"「一隻阿圓」因為個性大方又擁有好身材，深受網友喜愛，時常位居「YouTuber聲量排行榜」上，近日許多創作者都公開自己的理財規劃，開箱買房裝潢等，但她拍片自曝，月收曾高達七位數，但由於開銷過大，現在帳戶只剩下三萬多。\nYouTuber不好賺？一隻阿圓曝：每月至少支出20萬\n阿圓透露自己雖然最高可以月收百萬，但是自己底下有兩到三位攝影師，以及兩位剪輯師，每月至少要付四個人薪水，不包含自己的生活費跟房租等，這些固定支出，每一個月至少要支出二十萬元，因此整體算下來，月收入只是比一般上班族多一些而已，而且有時候在幕後發展，職業生涯反而能走得更長久，影片中阿圓也大方公開自己付給員工的帳戶餘款，目前只剩下三萬四千元左右，YouTuber並沒有想像中那麼好賺。"
    }
    ```

- return: 
    ```
    {
        "id": 1,
        "title": "YouTuber不好賺！一隻阿圓自曝月收7位數但戶頭只剩3萬",
        "tags": "一隻阿圓;月收;存錢;買房;YouTuber",
        "content": "「一隻阿圓」因為個性大方又擁有好身材，深受網友喜愛，時常位居「YouTuber聲量排行榜」上，近日許多創作者都公開自己的理財規劃，開箱買房裝潢等，但她拍片自曝，月收曾高達七位數，但由於開銷過大，現在帳戶只剩下三萬多。\nYouTuber不好賺？一隻阿圓曝：每月至少支出20萬\n阿圓透露自己雖然最高可以月收百萬，但是自己底下有兩到三位攝影師，以及兩位剪輯師，每月至少要付四個人薪水，不包含自己的生活費跟房租等，這些固定支出，每一個月至少要支出二十萬元，因此整體算下來，月收入只是比一般上班族多一些而已，而且有時候在幕後發展，職業生涯反而能走得更長久，影片中阿圓也大方公開自己付給員工的帳戶餘款，目前只剩下三萬四千元左右，YouTuber並沒有想像中那麼好賺。",
        "create_at": "2022-03-16T09:35:45.615007Z",
        "update_at": "2022-03-16T09:47:53.049018Z",
        "author": 1
    }
    ```

</details>


<details>
<summary><strong>PUSH 置換 文章 </strong></summary>

Path: `/api/article/articles/{article_id}/`

- body : 
    ```
    {
        "title": "YouTuber不好賺！一隻阿圓自曝月收7位數但戶頭只剩3萬",
        "tags": "一隻阿圓;月收;存錢;買房;YouTuber",
        "content":"「一隻阿圓」因為個性大方又擁有好身材，深受網友喜愛，時常位居「YouTuber聲量排行榜」上，近日許多創作者都公開自己的理財規劃，開箱買房裝潢等，但她拍片自曝，月收曾高達七位數，但由於開銷過大，現在帳戶只剩下三萬多。\nYouTuber不好賺？一隻阿圓曝：每月至少支出20萬\n阿圓透露自己雖然最高可以月收百萬，但是自己底下有兩到三位攝影師，以及兩位剪輯師，每月至少要付四個人薪水，不包含自己的生活費跟房租等，這些固定支出，每一個月至少要支出二十萬元，因此整體算下來，月收入只是比一般上班族多一些而已，而且有時候在幕後發展，職業生涯反而能走得更長久，影片中阿圓也大方公開自己付給員工的帳戶餘款，目前只剩下三萬四千元左右，YouTuber並沒有想像中那麼好賺。",
        "author": 1
    }
    ```

- return:
    ```
    ```

</details>


<details>
<summary><strong>DELETE 刪除 文章</strong></summary>

Path: `/api/article/articles/{article_id}/`

</details>
