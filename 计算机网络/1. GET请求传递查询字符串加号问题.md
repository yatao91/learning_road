# URL中的+号变成空格的处理办法

### 1. 修改客户端, 将客户端带"+"的参数中的"+"全部替换成"2B%"

### 2. 修改服务器端, 将接口请求方式由GET转成POST, 从body体中传参

### 3. 附一段转义URL特殊字符的JS代码

```javascript
function URLencode(sStr)
{
    return escape(sStr).replace(/\+/g, '+').replace(/\"/g,'"').replace(/\'/g, ''').replace(/\//g,'/');
}
```

