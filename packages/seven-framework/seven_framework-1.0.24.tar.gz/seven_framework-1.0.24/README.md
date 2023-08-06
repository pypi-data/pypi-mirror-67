

<!--
 * @Author: ChenXiaolei
 * @Date: 2020-04-22 17:57:36
 * @LastEditTime: 2020-04-30 11:24:08
 * @LastEditors: ChenXiaolei
 * @Description: 
 -->
# seven_framework

## 天志互联Python开发库

### 1.0.24 更新内容
* base_handler增加request_body_to_entity方法

### 1.0.23 更新内容
* 优化base_handler get_param 空值也返回默认值

### 1.0.22 更新内容
* 优化base_handler filter_check_params 装饰器,允许不检查必填参数

### 1.0.20 更新内容
* 优化MysqlHelper

### 1.0.19 更新内容
* 将MysqlHelper 的condition参数 拆开为 where/group_by/order_by/limit 参数
* 将MysqlHelper及base_model 增加事务执行函数transaction_execute

### 1.0.18 更新内容
* 解决base_api_handler的初始化bug

### 1.0.17 更新内容
* 优化框架结构
* 修改CryptoHelper 的 AES加解密方法