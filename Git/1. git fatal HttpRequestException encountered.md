# git fatal: HttpRequestException encountered 问题解决(Windows)

### 原因

GitHub移除了对TLSv1/TLSv1.1的支持, 参考[https://githubengineering.com/crypto-removal-notice/](https://githubengineering.com/crypto-removal-notice/)

### 解决方案

更新git凭证管理器(Credencial Manager)到最新版本.

[下载地址](https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/tag/v1.14.0)

![1546669604023](C:\Users\suyatao\AppData\Roaming\Typora\typora-user-images\1546669604023.png)