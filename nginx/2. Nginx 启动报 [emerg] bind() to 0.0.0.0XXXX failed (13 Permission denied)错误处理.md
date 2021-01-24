> 1. 端口小于1024的情况:
>
>    ```
>    [emerg] bind() to 0.0.0.0:80 failed (13: Permission denied)
>    ```
>
>    原因: 1024以下端口启动需要`root`权限, 所以`sudo nginx`即可.
>
> 2. 端口大于1024的情况:
>
>    ```
>    [emerg] bind() to 0.0.0.0:8088 failed (13: Permission denied)
>    ```
>
>    原因: selinux允许访问的端口不包括8086
>
>    处理: 
>
>    首先, 查看`http`允许访问的端口:
>
>    ```
>    # semanage port -l | grep http_port_t
>    http_port_t                    tcp      8086, 80, 81, 443, 488, 8008, 8009, 8443, 9000
>    ```
>
>    发现端口8088没有被允许访问.
>
>    其次, 将8088加入到上述端口列表中:
>
>    ```
>    # semanage port -a -t http_port_t -p tcp 8088
>    ```



