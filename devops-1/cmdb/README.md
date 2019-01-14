- server:
    - /api/ => v1/v2/v3
        - /api/v1
        - /api/v2
    
- client:
    - /api/


- 服务：内网： ip: 10.0.0.100, port: 8080
- 反代：ip: 60.1.1.30/10.0.0.101,  dns: miracle.com,
    - nginx，反代，反向代理：10.0.0.101:8080 => 10.0.0.100:8080
    - 60.1.1.30:8080
    
- 内网: /api/v1/, port: 8080
- 外网: /api/ 反代 内网/api/v1/:8080

前端1请求  page=1 => 后端，page=1 => 前端2


## 作业
- 完善局部删除
- 添加在 list.html中 添加 is_online 功能
- Redis：队列，api
- agent：task，/api/，更新
- echarts：disk、net
- 进阶：
    - 跳板机
        - 主机列表中，点击任意主机，能够打开terminal：本地terminal，web terminal
        - 主机账号信息 都存在跳板机中
        - 记录操作
        - 审计
        - 日志
        - replay
    - 打标签
    - 自动部署
        - 虚拟机
        - 物理机
        - docker
    - 任务系统