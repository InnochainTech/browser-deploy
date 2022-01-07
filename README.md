# browser-deploy
区块链浏览器部署文件

## 前提条件

|  环境   | 版本  |
|  ----  | ----  |
| Java  | JDK8或以上版本 |
| MySQL  | MySQL-5.6或以上版本 |
| Python  | Python3.5+ |
| PyMySQL  | 使用python3时需安装 |

## 拉取安装脚本

获取部署安装包：
```shell
wget https://github.com/InnochainTech/fisco-bcos-browser/releases/download/v2.3.0/browser-deploy.zip
```
解压安装包：
```shell
unzip browser-deploy.zip
```
进入目录：
```shell
cd browser-deploy
```

## 修改配置（没有变化的可以不修改）
1. 可以使用以下命令修改，也可以直接修改文件（vi common.properties）
2. 服务端口不能小于1024
```properties
数据库IP：sed -i "s/127.0.0.1/${your_db_ip}/g" common.properties
数据库端口：sed -i "s/3306/${your_db_port}/g" common.properties
数据库用户名：sed -i "s/dbUsername/${your_db_account}/g" common.properties
数据库密码：sed -i "s/dbPassword/${your_db_password}/g" common.properties
数据库名称：sed -i "s/db_browser/${your_db_name}/g" common.properties

前端服务端口：sed -i "s/5100/${your_web_port}/g" common.properties
后端服务端口：sed -i "s/5101/${your_server_port}/g" common.properties

例子（将数据库IP由127.0.0.1改为0.0.0.0）：sed -i "s/127.0.0.1/0.0.0.0/g" application.yml
```
## 部署
部署所有服务：
```shell
python3 deploy.py installAll
```
停止所有服务：
```shell
python3 deploy.py stopAll
```
启动所有服务：
```shell
python3 deploy.py startAll
```
单独启停命令和说明可查看帮助：
```shell
python3 deploy.py help
```
更多详见[ficos-bcos  区块链浏览器部署](https://fisco-bcos-documentation.readthedocs.io/zh_CN/latest/docs/browser/deploy.html#id2)




