**playwright 测试**
## 安装依赖
```
pip install -r requirment.txt
```

## 运行测试
```
pytest testPlaywright.py
```



## 目录解读
- test_src/test/testPlaywright.py 测试用例 （调用服务层执行测试）
- test_src/page/HomePage.py 页面元素 （封装对应的页面操作）
- test_src/service/NavigateService.py 页面操作 （复杂交互，多个页面对象完成业务流程）
- test_src/requirment.txt 依赖
- test_src/README.md 说明
