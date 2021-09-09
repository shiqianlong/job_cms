# 企业面试管理系统

## 1. 介绍

基于django框架自带的admin后台管理系统进行深度改造，快速开发出一个成熟的企业面试管理系统，具有一下功能：

**管理员**：

- 职位发布，修改，查看，删除
- 简历查看，修改，删除
- 将简历导入面试流程
- 指定面试官（一面，二面）面试
- 根据面试流程（一面，二面）每位面试官仅拥有该面试环节填写权限
- 应聘者 导入/导出csv 文件
- 进入面试流程时集成钉钉群机器人通知面试者，面试官
- 简历附件，照片等选择存储到阿里云OSS

**用户（应聘者）**：

- 职位查看
- 注册/ 登录
- 在线投递简历
- 查看自己简历

## 2. 使用

- `pip install -r requirements.txt`
- 本地使用默认`sqlite` 数据库，可以在`setting.py`中自行修改
- 如需使用阿里云OSS存储，请在`setting.py`中进行配置相关key

## 3. 效果图

![image-20210909174216526](https://sqlimage.oss-cn-beijing.aliyuncs.com/img/image-20210909174216526.png)

![image-20210909174233808](https://sqlimage.oss-cn-beijing.aliyuncs.com/img/image-20210909174233808.png)

![image-20210909174252086](https://sqlimage.oss-cn-beijing.aliyuncs.com/img/image-20210909174252086.png)

![image-20210909174309129](https://sqlimage.oss-cn-beijing.aliyuncs.com/img/image-20210909174309129.png)

![image-20210909174326704](https://sqlimage.oss-cn-beijing.aliyuncs.com/img/image-20210909174326704.png)

![image-20210909174349825](https://sqlimage.oss-cn-beijing.aliyuncs.com/img/image-20210909174349825.png)

![image-20210909174410529](https://sqlimage.oss-cn-beijing.aliyuncs.com/img/image-20210909174410529.png)

![image-20210909174423305](https://sqlimage.oss-cn-beijing.aliyuncs.com/img/image-20210909174423305.png)