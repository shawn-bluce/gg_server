# 项目介绍

这是个人使用的图床，目前只有最基础的传图功能。`GG`这个听起来很诡异的名字是对`GNU -> GNU is Not Unix`这种递归命名法的一次拙劣的模仿，`GG -> GG is Graphbed`。客户端在这里[https://github.com]](https://github.com)

# 部署条件

目前服务只支持Docker部署，并且建议有域名解析到服务器上，否则后面如有迁移的需求就会非常麻烦。

1. Docker
2. docker-compose
3. Nginx

部署该服务仅需上述工具，因为引用了Docker就使得部署非常的方便

# 如何部署

1. 克隆项目`git clone https://github.com/shawn-bluce/gg_server.git`
2. `ce gg_server`
3. 本地构建镜像`make build`
4. 同步数据库`make migrate`
5. 启动服务`make run_production`
6. 创建用户`make create_user`
7. 修改项目的`gg_server_nginx_config.conf`配置，比如域名是一定要改的
8. 将项目的`nginx`配置文件复制或链接到`nginx`配置目录，检查`nginx`配置是否有问题`nginx -t`没有就进行最后一步
9. 重启载入`nginx`配置，`nginx -r`

# 如何上传图片

`POST formdata to http://xxxxx.xxx/graph/`就可以了，携带的数据是

```
username: 用户名
password: 密码
graph: 图片文件
```

接口接收`FormData`格式的数据，

# 注意

一切上传的文件都在项目目录下的`data`目录里，如需迁移服务记得将文件带走。