# websocket协议

## 1.1 背景知识

由于历史原因，在创建一个具有双向通信机制的 web 应用程序时，需要利用到 HTTP 轮询的方式。围绕轮询产生了 “短轮询” 和 “长轮询”。

### 短轮询

浏览器赋予了脚本网络通信的编程接口 `XMLHttpRequest`，以及定时器接口 `setTimeout`。因此，客户端脚本可以每隔一段时间就主动的向服务器发起请求，询问是否有新的信息产生：

1. 客户端向服务器发起一个请求，询问 “有新信息了吗”
2. 服务端接收到客户端的请求，但是此时没有新的信息产生，于是直接回复 “没有”，并关闭链接
3. 客户端知道了没有新的信息产生，那么就暂时什么都不做
4. 间隔 5 秒钟之后，再次从步骤 1 开始循环执行

### 长轮询

使用短轮询的方式有一个缺点，由于客户端并不知道服务器端何时会产生新的消息，因此它只有每隔一段时间不停的向服务器询问 “有新信息了吗”。而长轮询的工作方式可以是这样：

1. 客户端向服务器发起一个请求，询问 “有新信息了吗”
2. 服务器接收到客户端的请求，此时并没有新的信息产生，不过服务器保持这个链接，像是告诉客户端 “稍等”。于是直到有了新的信息产生，服务端将新的信息返回给客户端。
3. 客户端接收到消息之后显示出来，并再次由步骤 1 开始循环执行

可以看到 “长轮询” 相较于 “短轮询” 可以减少大量无用的请求，并且客户端接收到新消息的时机将会有可能提前。

### 继续改进

我们知道 HTTP 协议在开发的时候，并不是为了双向通信程序准备的，起初的 web 的工作方式只是 “请求-返回” 就够了。

但是由于人们需要提高 web 应用程序的用户体验，以及 web 技术本身的便捷性 - 不需要另外的安装软件，使得浏览器也需要为脚本提供一个双向通信的功能，比如在浏览器中做一个 IM（Instant Message）应用或者游戏。

通过 “长、短轮询” 模拟的双向通信，有几个显而易见的缺点：

1. 每次的请求，都有大量的重复信息，比如大量重复的 HTTP 头。
2. 即使 “长轮询” 相较 “短轮询” 而言使得新信息到达客户端的及时性可能会有所提高，但是仍有很大的延迟，因为一条长连接结束之后，服务器端积累的新信息要等到下一次客户端和其建立链接时才能传递出去。
3. 对于开发人员而言，这种模拟的方式是难于调试的

于是，需要一种可以在 “浏览器-服务器” 模型中，提供简单易用的双向通信机制的技术，而肩负这个任务的，就是 `WebSocket`

## 1.2 协议概览

协议分为两部分：“握手” 和 “数据传输”。

客户端发出的握手信息类似：

```
GET /chat HTTP/1.1
Host: server.example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
Origin: http://example.com
Sec-WebSocket-Protocol: chat, superchat
Sec-WebSocket-Version: 13
```

服务端回应的握手信息类式：

```
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
Sec-WebSocket-Protocol: chat
```

客户端的握手请求由 请求行(Request-Line) 开始。客户端的回应由 状态行(Status-Line) 开始。请求行和状态行的生产式见 [RFC2616](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc2616)。

首行之后的部分，都是没有顺序要求的 HTTP Headers。其中的一些 HTTP头 的意思稍后将会介绍，不过也可包括例子中没有提及的头信息，比如 Cookies 信息，见 [RFC6265](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc6265)。HTTP头的格式以及解析方式见 [RFC2616](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc2616)

一旦客户端和服务端都发送了它们的握手信息，握手过程就完成了，随后就开始数据传输部分。因为这是一个双向的通信，所以客户端和服务端都可以首先发出信息。

在数据传输时，客户端和服务器都使用 “消息 Message” 的概念去表示一个个数据单元，而消息又由一个个 “帧 frame” 组成。这里的帧并不是对应到具体的网络层上的帧。

一个帧有一个与之相关的类型。属于同一个消息的每个帧都有相同的数据类型。粗略的说，有文本类型（以 UTF-8 编码 [RFC3629](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc3629)）和二进制类型（可以表示图片或者其他应用程序所需的类型），控制帧（不是传递具体的应用程序数据，而是表示一个协议级别的指令或者信号）。协议中定义了 6 中帧类型，并且保留了 10 种类型为了以后的使用。

## 1.3 开始握手

握手部分的设计目的就是兼容现有的基于 HTTP 的服务端组件（web 服务器软件）或者中间件（代理服务器软件）。这样一个端口就可以同时接受普通的 HTTP 请求或则 WebSocket 请求了。为了这个目的，WebSocket 客户端的握手是一个 HTTP 升级版的请求（HTTP Upgrade request）：

```
GET /chat HTTP/1.1
Host: server.example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
Origin: http://example.com
Sec-WebSocket-Protocol: chat, superchat
Sec-WebSocket-Version: 13
```

为了遵循协议 [RFC2616](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc2616)，握手中的头字段是没有顺序要求的。

跟在 GET 方法后面的 “请求标识符 Request-URI” 是用于区别 WebSocket 链接到的不同终节点。一个 IP 可以对应服务于多个域名，这样一台机器上就可以跑多个站点，然后通过 “请求标识符”，单个站点中又可以含有多个 WebSocket 终节点。

Host 头中的服务器名称可以让客户端标识出哪个站点是其需要访问的，也使得服务器得知哪个站点是客户端需要请求的。

其余的头信息是用于配置 WebSocket 协议的选项。典型的一些选项就是，子协议选项 `Sec-WebSocket-Protocol`、列出客户端支出的扩展 `Sec-WebSocket-Extensions`、源标识 `Origin` 等。`Sec-WebSocket-Protocol` 子协议选项，是用于标识客户端想和服务端使用哪一种子协议（都是应用层的协议，比如 chat 表示采用 “聊天” 这个应用层协议）。客户端可以在 `Sec-WebSocket-Protocol` 提供几个供服务端选择的子协议，这样服务端从中选取一个（或者一个都不选），并在返回的握手信息中指明，比如：

```
Sec-WebSocket-Protocol: chat
```

`Origin`可以预防在浏览器中运行的脚本，在未经 WebSocket 服务器允许的情况下，对其发送跨域的请求。浏览器脚本在使用浏览器提供的 WebSocket 接口对一个 WebSocket 服务发起连接请求时，浏览器会在请求的 `Origin` 中标识出发出请求的脚本所属的[源](https://www.jianshu.com/p/09d4cc6e1b45)，然后 WebSocket 在接受到浏览器的连接请求之后，就可以根据其中的源去选择是否接受当前的请求。

比如我们有一个 WebSocket 服务运行在 `http://websocket.example.com`，然后你打开一个网页 `http://another.example.com`，在个 another 的页面中，有一段脚本试图向我们的 WebSocket 服务发起链接，那么浏览器在其请求的头中，就会标注请求的源为 `http://another.example.com`，这样我们就可以在自己的服务中选择接收或者拒绝该请求。

服务端为了告知客户端它已经接收到了客户端的握手请求，服务端需要返回一个握手响应。在服务端的握手响应中，需要包含两部分的信息。第一部分的信息来自于客户端的握手请求中的 `Sec-WebSocket-Key` 头字段：

```
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
```

客户端握手请求中的 `Sec-WebSocket-Key` 头字段中的内容是采用的 base64 编码 [RFC4648](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc4648) 的。服务端并不需要将这个值进行反编码，只需要将客户端传来的这个值首先去除首尾的空白，然后和一段固定的 GUID [RFC4122](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc4122) 字符串进行连接，固定的 GUID 字符串为 `258EAFA5-E914-47DA-95CA-C5AB0DC85B11`。连接后的结果使用 SHA-1（160数位）[FIPS.180-3](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc6455#ref-FIPS.180-3) 进行一个哈希操作，对哈希操作的结果，采用 base64 进行编码，然后作为服务端响应握手的一部分返回给浏览器。

比如一个具体的例子：

1. 客户端握手请求中的 `Sec-WebSocket-Key` 头字段的值为 `dGhlIHNhbXBsZSBub25jZQ==` 
2. 服务端在解析了握手请求的头字段之后，得到 `Sec-WebSocket-Key` 字段的内容为 `dGhlIHNhbXBsZSBub25jZQ==`，注意前后没有空白
3. 将 `dGhlIHNhbXBsZSBub25jZQ==` 和一段固定的 GUID 字符串进行连接，新的字符串为 `dGhlIHNhbXBsZSBub25jZQ==258EAFA5-E914-47DA-95CA-C5AB0DC85B11`。
4. 使用 SHA-1 哈希算法对上一步中新的字符串进行哈希。得到哈希后的内容为（使用 16 进制的数表示每一个字节中内容）：`0xb3 0x7a 0x4f 0x2c 0xc0 0x62 0x4f 0x16 0x90 0xf6 0x46 0x06 0xcf 0x38 0x59 0x45 0xb2 0xbe 0xc4 0xea` 
5. 对上一步得到的哈希后的字节，使用 base64 编码，得到最后的字符串`s3pPLMBiTxaQ9kYGzzhZRbK+xOo=` 
6. 最后得到的字符串，需要放到服务端响应客户端握手的头字段 `Sec-WebSocket-Accept` 中。

服务端的握手响应和客户端的握手请求非常的类似。第一行是 HTTP状态行，状态码是 `101`：

```
HTTP/1.1 101 Switching Protocols
```

任何其他的非 `101` 表示 WebSocket 握手还没有结束，客户端需要使用原有的 HTTP 的方式去响应那些状态码。状态行之后，就是头字段。

`Connection` 和 `Upgrade` 头字段完成了对 HTTP 的升级。`Sec-WebSocket-Accept` 中的值表示了服务端是否接受了客户端的请求。如果它不为空，那么它的值包含了客户端在其握手请求中 `Sec-WebSocket-Key` 头字段所带的值、以及一段预定义的 GUID 字符串（上面已经介绍过怎么由二者合成新字符串的）。任何其他的值都被认为服务器拒绝了请求。服务端的握手响应类似：

```
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
```

这些字符需要被 WebSocket 的客户端（一般就是浏览器）检查核对之后，才能决定是否继续执行相应的客户端脚本，或者其他接下来的动作。

可选的头字段也可以被包含在服务端的握手响应中。在这个版本的协议中，主要的可选头字段就是 `Sec-WebSocket-Protocol`，它可以指出服务端选择哪一个子协议。客户端需要验证服务端选择的子协议，是否是其当初的握手请求中的 `Sec-WebSocket-Protocol` 中的一个。作为服务端，必须确保选的是客户端握手请求中的几个子协议中的一个:

```
Sec-WebSocket-Protocol: chat
```

服务端也可以设置 cookie 见[RFC6265](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc6265)，但是这不是必须的。

## 1.4 关闭握手

关闭握手的操作也很简单。

任意一端都可以选择关闭握手过程。需要关闭握手的一方通过发送一个特定的控制序列（第 5 节会描述）去开始一个关闭握手的过程。一端一旦接受到了来自另一端的请求关闭控制帧后，接收到关闭请求的一端如果还没有返回一个作为响应的关闭帧的话，那么它需要先发送一个关闭帧。在接受到了对方响应的关闭帧之后，发起关闭请求的那一端就可以关闭连接了。

在发送了请求关闭控制序列之后，发送请求的一端将不可以再发送其他的数据内容；同样的，一但接收到了一端的请求关闭控制序列之后，来自那一端的其他数据内容将被忽略。注意这里的说的是数据内容，控制帧还是可以响应的。否则就下面一句就没有意义了。

两边同时发起关闭请求也是可以的。

之所以需要这样做，是因为客户端和服务器之间可能还存在其他的中间件。一段关闭之后，也需要通知另一端也和中间件断开连接。

## 1.5 设计理念

WebSocket 协议的设计理念就是提供极小的帧结构（帧结构存在的目的就是使得协议是基于帧的，而不是基于流的，同时帧可以区分 Unicode 文本和二进制的数据）。它期望可以在应用层中使得元数据可以被放置到 WebSocket 层上，也就是说，给应用层提供一个将数据直接放在 TCP 层上的机会，再简单的说就可以给浏览器脚本提供一个使用受限的 Raw TCP 的机会。

从概念上来说，WebSocket 只是一个建立于 TCP 之上的层，它提供了下面的功能：

- 给浏览器提供了一个基于源的安全模型（origin-based security model）
- 给协议提供了一个选址的机制，使得在同一个端口上可以创立多个服务，并且将多个域名关联到同一个 IP
- 在 TCP 层之上提供了一个类似 TCP 中的帧的机制，但是没有长度的限制
- 提供了关闭握手的方式，以适应存在中间件的情况

从概念上将，就只有上述的几个用处。不过 WebSocket 可以很好的和 HTTP 协议一同协作，并且可以充分的利用现有的 web 基础设施，比如代理。WebSocket 的目的就是让简单的事情变得更加的简单。

协议被设计成可扩展的，将来的版本中将很可能会添加关于多路复用的概念。

## 1.6 安全模型

WebSocket 协议使用源模型（origin model），这样浏览器中的一个页面中的脚本需要访问其他源的资源时将会有所限制。如果是在一个 WebSocket 客户端中直接使用了 WebSocet（而不是在浏览器中），源模型就没有什么作用，因为客户端可以设置其为任意的值。

并且协议的设计目的也是不希望干扰到其他协议的工作，因为只有通过特定的握手步骤才能建立 WebSocket 连接。另外由于握手的步骤，其他已经存在的协议也不会干扰到 WebSocket 协议的工作。比如在一个 HTTP 表单中，如果表单的地址是一个 WebSocket 服务的话，将不会建立连接，因为到目前本文成文为止，在浏览器中是不可以通过 HTML 和 Javascript APIs 去设置 `Sec-` 头的。

## 1.7 和 TCP 以及 HTTP 之间的关系

WebSocket 是一个独立的基于 TCP 的协议，它与 HTTP 之间的唯一关系就是它的握手请求可以作为一个升级请求（Upgrade request）经由 HTTP 服务器解释（也就是可以使用 Nginx 反向代理一个 WebSocket）。

默认情况下，WebSocket 协议使用 80 端口作为一般请求的端口，端口 443 作为基于传输加密层连（TLS）[RFC2818](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc2818) 接的端口

## 1.8 建立一个连接

因为 WebSocket 服务通常使用 80 和 443 端口，而 HTTP 服务通常也是这两个端口，那么为了将 WebSocket 服务和 HTTP 服务部署到同一个 IP 上，可以限定流量从同一个入口处进入，然后在入口处对流量进行管理，概况的说就是使用反向代理或者是负载均衡。

## 1.9 WebSocket 协议的子协议

在使用 WebSocket 协议连接到一个 WebSocket 服务器时，客户端可以指定其 `Sec-WebSocket-Protocol` 为其所期望采用的子协议集合，而服务端则可以在此集合中选取一个并返回给客户端。

这个子协议的名称应该遵循第 11 节中的内容。为了防止潜在的冲突问题，应该在域名的基础上加上服务组织者的名称（或者服务名称）以及协议的版本。比如 `v2.bookings.example.net` 对应的就是 `版本号-服务组织（或服务名）-域名`

## 2 一致性的要求

见原文 [section-2](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc6455#section-2)

## 3 WebSocket URIs

在这份技术说明中，定义了两种 URI 方案，使用 ABNF 语法 [RFC 5234](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc5234)，以及 URI 技术说明 [RFC3986](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc3986) 中的生产式。

```
ws-URI = "ws:" "//" host [ ":" port ] path [ "?" query ]
wss-URI = "wss:" "//" host [ ":" port ] path [ "?" query ]

host = <host, defined in [RFC3986], Section 3.2.2>
port = <port, defined in [RFC3986], Section 3.2.3>
path = <path-abempty, defined in [RFC3986], Section 3.3>
query = <query, defined in [RFC3986], Section 3.4>
```

端口部分是可选的；“ws” 默认使用的端口是 80，“wss” 默认使用的端口是 443。

如果资源标识符（URI）的方案（scheme）部分使用的是大小写不敏感的 “wss” 的话，那么就说这个 URI 是 “可靠的 secure”，并且说明 “可靠标记（secure flag）已经被设置”。

“资源名称 resource-name” 也就是 4.1 节中的 `/resource name/`，可以按下面的部分（顺序）连接：

- 如果不用路径不为空，加上 “/”
- 紧接着就是路径部分
- 如果查询组件不为空 ，加上 “?“
- 紧接着就是查询部分

片段标识符（fragment identifier） “#” 在 WebSocket URIs 的上下文是没有意义的，不能出现在 URIs 中。在 WebSocket 的 URI 中，如果出现了字符 “#” 需要使用 %23 进行转义。

## 4.1 客户端要求

为了建立一个 WebSocket 连接，由客户端打开一个连接然后发送这一节中定义的握手信息。连接初始的初始状态被定义为 “连接中 `CONNECTING`”。客户端需要提供 /host/，/port/，/resource name/ 和 /secure/ 标记，这些都是上一节中的 WebSocket URI 中的组件，如果有的话，还需要加上使用的 /protocols/ 和 /extensions/。另外，如果客户端是浏览器，它还需要提供 /origin/。

连接开始前需要的设定信息为（/host/, /port/, /resource name/ 和 /secure/）以及需要使用的 /protocols/ 和 /extensions/，如果在浏览器下还有 /origin/。这些设定信息选定好了之后，就必须打开一个网络连接，发送握手信息，然后读取服务端返回的握手信息。具体的网络连接应该如何被打开，如何发送握手信息，如何解释服务端的握手响应，这些将在接下来的部分讨论。我们接下来的文字中，将使用第 3 节中定义的项目名称，比如 “/host/” 和 “/secure/”。

1. 在解析 WebSocket URI 的时候，需要使用第 3 节中提到的技术说明去验证其中的组件。如果包含了任何无效的 URI 组件，客户端必须将连接操作标记为失败，并停止接下来的步骤
2. 可以通过 /host/ 和 /port/ 这一对 URI 组件去标识一个 WebSocket 连接。这一部分的意思就是，如果可以确定服务端的 IP，那么就使用 “服务端 IP + port” 去标识一个连接。这样的话，如果已经存在一个连接是 “连接中 `CONNECTING`” 的状态，那么其他具有相同标识的连接必须等待那个正在连接中的连接完成握手后，或是握手失败后关闭了连接后，才可以尝试和服务器建立连接。任何时候只能有一个具有相同的标识的连接是 “正在连接中” 的状态。

但是如果客户端无法知道服务器的IP（比如，所有的连接都是通过代理服务器完成的，而 DNS 解析部分是交由代理服务器去完成），那么客户端就必须假设每一个主机名称对应到了一个独立服务器，并且客户端必须对同时等待连接的的连接数进行控制（比如，在无法获知服务器 IP 的情况下，可以认为 `a.example.com` 和 `b.example.com` 是两台不同的服务器，但是如果每台服务器都有三十个需要同时发生的连接的话，可能就应该不被允许）

注意：这就使得脚本想要执行 “拒绝服务攻击 denial-of-service attack” 变得困难，不然的话脚本只需要简单的对一个 WebSocket 服务器打开很多的连接就可以了。服务端也可以进一步的有一个队列的概念，这样将暂时无法处理的连接放到队列中暂停，而不是将它们立刻关闭，这样就可以减少客户端重连的比率。

注意：对于客户端和服务器之间的连接数是没有限制的。在一个客户端请数目（根据 IP）达到了服务端的限定值或者服务端资源紧缺的时候，服务端可以拒绝或者关闭客户端连接。

1. 使用代理：如果客户端希望在使用 WebSocket 的时候使用代理的话，客户端需要连接到代理服务器并要求代理服务器根据其指定的 /host/，/port/ 对远程服务器打开一个 TCP 连接，有兴趣的可以看 [Tunneling TCP based protocols through Web proxy servers](https://link.jianshu.com?t=http://www.ietf.org/archive/id/draft-luotonen-web-proxy-tunneling-01.txt)。

如果可能的话，客户端可以首选适用于 HTTPS 的代理设置。

如果希望使用 [PAC](https://link.jianshu.com?t=https://en.wikipedia.org/wiki/Proxy_auto-config) 脚本的话，WebSocket URIs 必须根据第 3 节说的规则。

注意：在使用 PAC 的时候，WebSocket 协议是可以特别标注出来的，使用 “ws” 和 “wss”。

1. 如果网络连接无法打开，无论是因为代理的原因还是直连的网络问题，客户端必须将连接动作标记为失败，并终止接下来的行为。
2. 如果设置了 /secure/，那么客户端在和服务端建立了连接之后，必须要先进行 TLS 握手，TLS 握手成功后，才可以进行 WebSocket 握手。如果 TLS 握手失败（比如服务端证书不能通过验证），那么客户端必须关闭连接，终止其后的 WebSocket 握手。在 TLS 握手成功后，所有和服务的数据交换（包括 WebSocket 握手），都必须建立在 TLS 的加密隧道上。

客户端在使用 TLS 时必须使用 “服务器名称标记扩展 Server Name Indication extension” [RFC6066](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc6066)

一旦客户端和服务端的连接建立好（包括经由代理或者通过 TLS 加密隧道），客户端必须向服务端发送 WebSocket 握手信息。握手内容包括了 HTTP 升级请求和一些必选以及可选的头字段。握手的细节如下：

1. 握手必须是一个有效的 HTTP 请求，有效的 HTTP 请求的定义见 [RFC2616](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc2616)

2. 请求的方法必须是 `GET`，并且 HTTP 的版本必须至少是 1.1

   比如，如果 WebSocket 的 URI 是 `ws://example.com/chat`，那么请求的第一行必须是 `GET /chat HTTP/1.1`。

3. 请求的 `Request-URI` 部分必须遵循第 3 节中定义的 /resource name/ 的定义。可以使相对路径或者绝对路径，比如：

相对路径：`GET /chat HTTP/1.1` 中间的 `/chat` 就是请求的 `Request-URI`，也是 /resource name/
 绝对路径：`GET http://www.w3.org/pub/WWW/TheProject.html HTTP/1.1`，其中的 /resource name/ 就是 `/pub/WWW/TheProject.html` 感谢 @forl 的指正

绝对路径解析之后会有 /resource name/，/host/ 或者可能会有 /port/。/resource name/ 可能会有查询参数的，只不过例子中没有。

1. 请求必须有一个 |Host| 头字段，它的值是 /host/ 主机名称加上 /port/ 端口名称（当不是使用的默认端口时必须显式的指明）
2. 请求必须有一个 |Upgrade| 头字段，它的值必须是 `websocket` 这个关键字（keyword）
3. 请求必须有一个 |Connection| 头字段，它的值必须是 `Upgrade` 这个标记（token）
4. 请求必须有一个 |Sec-WebSocket-Key| 头字段，它的值必须是一个噪音值，由 16 个字节的随机数经过 base64 编码而成。每个连接的噪音必须是不同且随机的。

注意：作为一个例子，如果选择的随机 16 个字节的值是 `0x01 0x02 0x03 0x04 0x05 0x06 0x07 0x08 0x09 0x0a 0x0b 0x0c 0x0d 0x0e 0x0f 0x10`，那么头字段中的值将是 `AQIDBAUGBwgJCgsMDQ4PEC==`

1. 如果连接来自浏览器客户端，那么 |Origin| [RFC6454](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc6454) 就是必须的。如果连接不是来自于一个浏览器客户端，那么这个值就是可选的。这个值表示的是发起连接的代码在运行时所属的源。关于源是由哪些部分组成的，见 [RFC6454](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc6454)。

作为一个例子，如果代码是从 `http://cdn.jquery.com` 下载的，但是运行时所属的源是 `http://example.com`，如果代码向 `ww2.example.com` 发起连接，那么请求中 |Origin| 的值将是 `http://example.com`。

1. 请求必须有一个 |Sec-WebSocket-Version| 头字段，它的值必须是 13
2. 请求可以有一个可选的头字段 |Sec-WebSocket-Protocol|。如果包含了这个头字段，它的值表示的是客户端希望使用的子协议，按子协议的名称使用逗号分隔。组成这个值的元素必须是非空的字符串，并且取值范围在 U+0021 到 U+007E 之间，不可以包含定义在 [RFC2616](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc2616#section-2.2) 的分隔字符（separator character），并且每个以逗号分隔的元素之间必须相互不重复。
3. 请求可以有一个可选的头字段 |Sec-WebSocket-Extensions|。如果包含了这个字段，它的值表示的是客户端希望使用的协议级别的扩展，具体的介绍以及它的格式在第 9 节
4. 请求可以包含其他可选的头字段，比如 cookies [RFC6265](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc6265)，或者认证相关的头字段，比如 |Authorization| 定义在 [RFC2616](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc2616)，它们的处理方式就参照定义它们的技术说明中的描述。

一旦客户端的握手请求发送完成后，客户端必须等待服务端的握手响应，在此期间不可以向服务器传输任何数据。客户端必须按照下面的描述去验证服务端的握手响应：

1. 如果服务端传来的状态码不是 101，那么客户端可以按照一般的 HTTP 请求处理状态码的方式去处理。比如服务端传来 401 状态码，客户端可以执行一个授权验证；或者服务端回传的是 3xx 的状态码，那么客户端可以进行重定向（但是客户端不是非得这么做）。如果是 101 的话，就接着下面的步骤。
2. 如果服务端回传的握手中没有 |Upgrade| 头字段或者 |Upgrade| 都字段的值不是 ASCII 大小写不敏感的 `websocket` 的话，客户端必须标记 WebSocket 连接为失败。
3. 如果服务端回传的握手中没有 |Connection| 头字段或者 |Connection| 的头字段内容不是大小写敏感的 `Upgrade` 的话，客户端必须表示 WebSocket 连接为失败。
4. 如果服务端的回传握手中没有 |Sec-WebSocket-Accept| 头字段或者 |Sec-WebSocket-Accept| 头字段的内容不是 |Sec-WebSocket-Key| 的内容（字符串，不是 base64 解码后的）联结上字符串 `258EAFA5-E914-47DA-95CA-C5AB0DC85B11` 的字符串进行 SHA-1 得出的字节再 base64 编码得到的字符串的话，客户端必须标记 WebSocket 连接为失败。

简单的说就是客户端也必须按照服务端生成 |Sec-WebSocket-Accept| 头字段值的方式也生成一个字符串，与服务端回传的进行对比，如果不同就标记连接为失败的。

1. 如果服务端回传的 |Sec-WebSocket-Extensions| 头字段的内容不是客户端握手请求中的扩展集合中的元素或者 `null` 的话，客户端必须标记连接为失败。这个头字段的解析规则在第 9 节中进行了描述。

比如客户端的握手请求中的期望使用的扩展集合为：

```
Sec-WebSocket-Extensions: bar; baz=2
```

那么服务端可以选择使用其中的某个（些）扩展，通过在回传的 |Sec-WebSocket-Extensions| 头字段中表明：

```
Sec-WebSocket-Extensions: bar; baz=2
```

上面的服务端返回表示都使用。也可以使用其中的一个：

```
Sec-WebSocket-Extensions: bar
```

如果服务端希望表示一个都不使用，即表示 `null`，那么服务端回传的信息中将不可以包含 |Sec-WebSocket-Extensions|。

失败的界定就是，如果客户端握手请求中有 |Sec-WebSocket-Extensions|，但是服务端返回的 |Sec-WebSocket-Extensions| 中包含了客户端请求中没有包含的值，那么必须标记连接为失败。服务端的返回中不包含 |Sec-WebSocket-Extensions| 是可以的，表示客户端和服务端之间将不使用任何扩展。

1. 如果客户端在握手请求中包含了子协议头字段 |Sec-WebSocket-Protocol|，其中的值表示客户端希望使用的子协议的集合。如果服务端回传信息的 |Sec-WebSocket-Protocol| 值不属于客户端握手请求中的子协议集合的话，那么客户端必须标记连接为失败。

如果服务端的握手响应不符合 4.2.2 小节中的服务端握手定义的话，客户端必须标记连接为失败。

请注意，根据 [RFC2616](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc2616) 技术说明，请求和响应的中所有头字段的名称都是大小写不敏感的（不区分大小写）。

如果服务端的响应符合上述的描述的话，那么就说明 WebSocket 的连接已经建立了，并且连接的状态变为 “OPEN 状态”。另外，服务端的握手响应中也可以包含 cookie 信息，cookie 信息被称为是 “服务端开始握手的 cookie 设置”。

## 4.2 服务端要求

WebSocket 服务器可能会卸下一些对连接的管理操作，而将这些管理操作交由网络中的其他代理，比如负载均衡服务器或者反向代理服务器。对于这种情况，在这个技术说明中，将组成服务端的基础设施的所有部分合起来视为一个整体。

比如，在一个数据中心，会有一个服务器专门用户响应客户端的握手请求，在握手成功之后将连接转交给实际处理任务的服务器。在这份技术说明中，服务端指代的就是这里的两台机器的组成的整体。

## 4.2.1 读取客户端的握手请求

当客户端发起一个 WebSocket 请求时，它会发送握手过程种属于它那一部分的内容。服务端必须解析客户端提交的握手请求，以从中获得生成服务端响应内容的必要的信息。

客户端的握手请求有接下来的几部分构成。服务端在读取客户端请求时，发现握手的内容和下面的描述不相符（注意 [RFC2616](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc2616)，头字段的顺序是不重要的），包括但不限于那些不符合相关 ABNF 语法描述的内容时，必须停止对请求的解析并返回一个具有适当的状态码 HTTP 响应（比如 400 Bad Request）。

1. 必须是 HTTP/1.1 或者以上的 GET 请求，包含一个 “请求资源标识符 Request-URI”，请求资源标识符遵循第 3 节中定义的 /resource name/。
2. 一个 |Host| 头字段，向服务器指明需要访问的服务名称（域名）
3. 一个 |Upgrade| 头字段，值为大小写不敏感的 `websocket` 字符串
4. 一个 |Connection| 头字段，它的值是大小写不敏感的字符串 `Upgrade`
5. 一个 |Sec-WebSocket-Key| 头字段，它的值是一段使用 base64 编码[Section 4 of [RFC4648\]](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc4648#section-4) 后的字符串，解码之后是 16 个字节的长度。
6. 一个 |Sec-WebSocket-Version| 头字段，它的值是 13.
7. 可选的，一个 |Origin| 头字段。这个是所有浏览器客户度必须发送的。如果服务端限定只能由浏览器作为其客户端的话，在缺少这个字段的情况下，可以认定这个握手请求不是由浏览器发起的，反之则不行。
8. 可选的，一个 |Sec-WebSocket-Protocol| 头字段。由一些值组成的列表，这些值是客户端希望使用的子协议，按照优先级从左往右排序。
9. 可选的，一个 |Sec-WebSocket-Extensions| 头字段。有一些值组成的列表，这些值是客户端希望使用的扩展。具体的表示在第 9 节。
10. 可选的，其他头字段，比如那些用于向服务端发送 cookie 或则认证信息。未知的头字段将被忽略 [RFC2616](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc2616)

## 4.2.2 发送服务端的握手响应

当客户端对服务端建立了一个 WebSocket 连接之后，服务端必须完成接下来的步骤，以此去接受客户端的连接，并回应客户端的握手。

1. 如果连接发生在 HTTPS（基于 TLS 的 HTTP）端口上，那么要执行一个 TLS 握手。如果 TLS 握手失败，就必须关闭连接；否则的话之后的所有通信都必须建立在加密隧道上。
2. 服务端可以对客户端执行另外的授权认证，比如通过返回 401 状态码和 对应的 |WWW-Authenticate|，相关描述在 [RFC2616](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc2616)
3. 服务端也可以对客户端进行重定向，使用 3xx 状态码 [RFC2616](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc2616)。注意这一步也可以发生在上一步之前。
4. 确认下面的信息：

- /origin/

  客户端握手请求中的 |origin| 头字段表明了脚本在发起请求时所处的源。源被序列化成 ASCII 并且被转换成了小写。服务端可以选择性地使用这个信息去决定是否接受这个连接请求。如果服务端不验证源的话，那么它将接收来自任何地方的请求。如果服务端不想接收这个连接的话，它必须返回适当的 HTTP 错误状态码（比如 403 Forbidden）并且终止接下来的 WebSocket 握手过程。更详细的内容，见第 10 节

- /key/

  客户端握手请求中的 |Sec-WebSocket-Key| 头字段包含了一个使用 base64 编码后的值，如果解码的话，这个值是 16 字节长的。这个编码后的值用于服务端生成表示其接收客户端请求的内容。服务端没有必要去将这个值进行解码。

- /version/

  客户端握手请求中的 |Sec-WebSocket-Version| 头字段包含了客户端希望进行通信的 WebSocket 协议的版本号。如果服务端不能理解这个版本号的话，那么它必须终止接下来的握手过程，并给客户端返回一个适当的 HTTP 错误状态码（比如 426 Upgrade Required），同时在返回的信息中包含一个 |Sec-WebSocket-Version| 头字段，通过其值指明服务端能够理解的协议版本号。

- /subprotocol/

  服务端可以选择接受其中一个子协议，或者 `null`。子协议的选取必须来自客户端的握手信息中的 |Sec-WebSocket-Protocol| 头字段的元素集合。如果客户端没有发送 |Sec-WebSocket-Protocol| 头字段，或者客户端发送的 |Sec-WebSocket-Protocol| 头字段中没有一个可以被当前服务端接受的话，服务端唯一可以返回值就是 `null`。不发送这个头字段就表示其值是 `null`。注意，空字符串并不表示这里的 `null` 并且根据 [RFC2616](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc2616) 中的 ABNF 定义，空字符串也是不合法的。根据协议中的描述，客户端握手请求中的 |Sec-WebSocket-Protocol| 是一个可选的头字段，所以如果服务端必须使用这个头字段的话，可以选择性的拒绝客户端的连接请求。

- /extensions/

  一个可以为空的列表，表示客户端希望使用的协议级别的扩展。如果服务端支持多个扩展，那么必须从客户端握手请求中的 |Sec-WebSocket-Extensions| 按需选择多个其支持的扩展。如果客户端没有发送次头字段，则表示这个字段的值是 `null`，空字符并不表示 `null`。返回的 |Sec-WebSocket-Extensions| 值中不可以包含客户端不支持的扩展。这个字段值的选择和解释将在第 9 节中讨论

1. 如果服务端选择接受来自客户端的连接，它必须回答一个有效的 HTTP 响应：
2. 一个状态行，包含了响应码 101。比如 `HTTP/1.1 101 Switching Protocols`
3. 一个 |Upgrade| 头字段，值为 `websocket`
4. 一个 |Connection| 头字段，值为 `Upgrade`
5. 一个 |Sec-WebSocket-Accept| 头字段。这个值通过连接定义在 4.2.2 节中的第 4 步的 /key/ 和字符串 `258EAFA5-E914-47DA-95CA-C5AB0DC85B11`，连接后的字符串运用 SHA-1 得到一个 20 字节的值，最后使用 base64 将这 20 个字节的内容编码，得到最后的用于返回的字符串。

```
相应的 ABNF 定义如下：

​```
Sec-WebSocket-Accept     = base64-value-non-empty
base64-value-non-empty = (1*base64-data [ base64-padding ]) |
                        base64-padding
base64-data      = 4base64-character
base64-padding   = (2base64-character "==") |
                  (3base64-character "=")
base64-character = ALPHA | DIGIT | "+" | "/"
​```

    注意：作为一个例子，如果来自客户端握手请求中的 |Sec-WebSocket-Key| 的值是 `dGhlIHNhbXBsZSBub25jZQ==` 的话，那么服务端需要将 `258EAFA5-E914-47DA-95CA-C5AB0DC85B11` 字符串追加到其后，变成 `dGhlIHNhbXBsZSBub25jZQ==258EAFA5-E914-47DA-95CA-C5AB0DC85B11`，再对这个连接后的字符串运用 SHA-1 哈希得到这些内容 `0xb3 0x7a 0x4f 0x2c 0xc0 0x62 0x4f 0x16 0x90 0xf6 0x46 0x06 0xcf 0x38 0x59 0x45 0xb2 0xbe 0xc4 0xea`，对于哈希后的内容进行 base64 编码，最后得到 `s3pPLMBiTxaQ9kYGzzhZRbK+xOo=`，然后将这个值作为服务端返回的头字段 |Sec-WebSocket-Accept| 的字段值。
```

1. 可选的，一个 |Sec-WebSocket-Protocol| 头字段，它的值已经在第 4.2.2 节中的第 4 步定义了
2. 可选的，一个 |Sec-WebSocket-Extensions| 头字段，它的值已经在第4.2.2 节中的第 4 步定义了。如果有服务端选择了多个扩展，可以将它们分别放在 |Sec-WebSocket-Extensions| 头字段中，或者合并到一起放到一个 |Sec-WebSocket-Extensions| 头字段中。

这样就完成了服务端的握手。如果服务端没有发生终止的完成了所有的握手步骤，那么服务端就可以认为连接已经建立了，并且 WebSocket 连接的状态变为 OPEN。在这时，客户端和服务端就可以开始发送（或者接收）数据了。

## 4.3 握手中使用的新的头字段的 ABNF

这一节中将使用定义在 [Section 2.1 of [RFC2616\]](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc2616#section-2.1) ABNF 语法/规则，包括隐含的 LWS 规则（implied *LWS rule）。为了便于阅读，这里给出 LWS 的简单定义：任意数量的空格，水平 tab 或者换行（换行指的是 CR（carriage return） 后面跟着 LF（linefeed），使用转义字符表示就是 `\r\n`）。

注意，接下来的一些 ABNF 约定将运用于这一节。一些规则的名称与与之对应的头字段相关。这些规则表示相应的头字段的值的语法，比如 Sec-WebSocket-Key ABNF 规则，它描述了 |Sec-WebSocket-Key| 头字段的值的语法。名字中具有 `-Client` 后缀的 ABNF 规则，表示的是客户端向服务端发送请求时的字段值语法；名字中具有 `-Server` 后缀的 ABNF 规则，表示的是服务端向客户端发送请求时的字段值语法。比如 ABNF 规则 Sec-WebSocket-Protocol-Client 描述了 |Sec-WebSocket-Protocol| 存在与由客户端发送到服务端的请求中的语法。

接下来新头字段可以在握手期间由客户端发往服务端：

```
Sec-WebSocket-Key = base64-value-non-empty
Sec-WebSocket-Extensions = extension-list
Sec-WebSocket-Protocol-Client = 1#token
Sec-WebSocket-Version-Client = version

base64-value-non-empty = (1*base64-data [ base64-padding ]) |
                        base64-padding
base64-data      = 4base64-character
base64-padding   = (2base64-character "==") |
                 (3base64-character "=")
base64-character = ALPHA | DIGIT | "+" | "/"
extension-list = 1#extension
extension = extension-token *( ";" extension-param )
extension-token = registered-token
registered-token = token

extension-param = token [ "=" (token | quoted-string) ]
       ; When using the quoted-string syntax variant, the value
       ; after quoted-string unescaping MUST conform to the
       ; 'token' ABNF.
  NZDIGIT       =  "1" | "2" | "3" | "4" | "5" | "6" |
                   "7" | "8" | "9"
  version = DIGIT | (NZDIGIT DIGIT) |
            ("1" DIGIT DIGIT) | ("2" DIGIT DIGIT)
            ; Limited to 0-255 range, with no leading zeros
```

下面的新字段可以在握手期间由服务端发往客户端：

```
Sec-WebSocket-Extensions = extension-list
Sec-WebSocket-Accept     = base64-value-non-empty
Sec-WebSocket-Protocol-Server = token
Sec-WebSocket-Version-Server = 1#version
```

## 4.4 支持多个版本的 WebSocket 协议

这一节对在客户端和服务端之间提供多个版本的 WebSocket 协议提供了一些指导意见。

使用 WebSocket 的版本公告能力（|Sec-WebSocket-Version| 头字段），客户端可以指明它期望的采用的协议版本（不一定就是客户端已经支持的最新版本）。如果服务端支持相应的请求版本号的话，则握手可以继续，如果服务端不支持请求的版本号，它必须回应一个（或多个） |Sec-WebSocket-Version| 头字段，包含所有它支持的版本。这时，如果客户端也支持服务端的其中一个协议的话，它就可以使用新的版本号去重复客户端握手的步骤。

下面的例子可以作为上文提到的版本协商的演示：

客户端发送：

```
GET /chat HTTP/1.1
Host: server.example.com
Upgrade: websocket
Connection: Upgrade
...
Sec-WebSocket-Version: 25
```

服务端的返回看起来类似：

```
HTTP/1.1 400 Bad Request
...
Sec-WebSocket-Version: 13, 8, 7
```

注意，服务器也可以返回下面的内容：

```
HTTP/1.1 400 Bad Request
...
Sec-WebSocket-Version: 13
Sec-WebSocket-Version: 8, 7
```

客户端现在就可以重新采用版本 13 （如果客户端也支持的话）进行握手请求了：

```
GET /chat HTTP/1.1
Host: server.example.com
Upgrade: websocket
Connection: Upgrade
...
Sec-WebSocket-Version: 13
```

## 5. 使用帧去组织数据

## 5.1 概览

在 WebSocket 协议中，数据的传输使用一连串的帧。为了使得中间件不至于混淆（比如代理服务器）以及为了第 10.3 节将讨论安全原因，客户端必须将要发送到服务端的帧进行掩码，掩码将在第 5.3 节详细讨论。（注意，不管 WebSocket 有没有运行在 TLS 之上，都必须有掩码操作）服务端一旦接收到没有进行掩码的帧的话，必须关闭连接。这种情况下，服务端可以发送一个关闭帧，包含一个状态码 1002（协议错误 protocol error），相关定义在 [Section 7.4.1](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc6455#section-7.4.1)。服务端不必对发送到客户端的任何帧进行掩码。如果客户端接收到了服务端的掩码后的帧，客户端必须关闭连接。在这个情况下，客户端可以向服务器发送关闭帧，包含状态码 1002（协议错误 protocol error），相关定义在 [Section 7.4.1](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc6455#section-7.4.1)。（这些规则可能在将来技术说明中没有严格要求）

基础帧协议通过操作码（opcode）定义了一个帧类型，一个有效负荷长度，以及特定的位置存放 “扩展数据 Extension data” 和 “应用数据 Application data”，扩展数据和应用数据合起来定义了 “有效负荷数据 Payload data”。某些数位和操作码是保留的，为了将来的使用。

在客户端和服务端完成了握手之后，以及任意一端发送的关闭帧（在第 5.5.1 节介绍）之前，客户端可以和服务端都可以在任何时间发送数据帧。

## 基础帧协议

这一节中将使用 ABNF 详细定义数据传输的格式。（注意，和这文档中的其他 ABNF 不同，这一节中 ABNF 操作的是一组数位。每一组数位的长度将以注释的形式存在。当数据在网络中传输时，最高有效位是在 ABNF 的最左边（大端序））。下面的文本图像可以给出关于帧的一个高层概览。如果下面的文本插图和后的 ABNF 描述发送冲突时，以插图为准。

```
  0                   1                   2                   3
  0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
 +-+-+-+-+-------+-+-------------+-------------------------------+
 |F|R|R|R| opcode|M| Payload len |    Extended payload length    |
 |I|S|S|S|  (4)  |A|     (7)     |             (16/64)           |
 |N|V|V|V|       |S|             |   (if payload len==126/127)   |
 | |1|2|3|       |K|             |                               |
 +-+-+-+-+-------+-+-------------+ - - - - - - - - - - - - - - - +
 |     Extended payload length continued, if payload len == 127  |
 + - - - - - - - - - - - - - - - +-------------------------------+
 |                               |Masking-key, if MASK set to 1  |
 +-------------------------------+-------------------------------+
 | Masking-key (continued)       |          Payload Data         |
 +-------------------------------- - - - - - - - - - - - - - - - +
 :                     Payload Data continued ...                :
 + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
 |                     Payload Data continued ...                |
 +---------------------------------------------------------------+
```

- FIN: 1 个数位（bit）

  标记这个帧是不是消息中的最后一帧。第一个帧也可以是最后一帧。

- RSV1，RSV2，RSV3： 各 1 个数位

  必须是 0，除非有扩展赋予了这些数位非 0 值的意义。如果接收到了一个非 0 的值并且没有扩展赋予这些非 0 值的意义，那么接收端需要标记连接为失败。

- 操作码：4 个数位
   定义了如何解释 “有效负荷数据 Payload data”。如果接收到一个未知的操作码，接收端必须标记 WebSocket 为失败。定义了如下的操作码：

  -  `%x0` 表示这是一个继续帧（continuation frame）
  -  `%x1` 表示这是一个文本帧 （text frame）
  -  `%x2` 表示这是一个二进制帧 （binary frame）
  -  `%x3-7` 为将来的非控制帧（non-control frame）而保留的
  -  `%x8` 表示这是一个连接关闭帧 （connection close）
  -  `%x9` 表示这是一个 ping 帧
  -  `%xA` 表示这是一个 pong 帧
  -  `xB-F` 为将来的控制帧（control frame）而保留的

- 掩码标识 Mask：1 个数位

  定义了 “有效负荷数据” 是否是被掩码的。如果被设置为 1，那么在 `masking-key` 部分将有一个掩码钥匙（masking key），并且使用这个掩码钥匙去将 “有效负荷数据” 进行反掩码操作（第 5.3 节描述）。所有的由客户端发往服务端的帧此数位都被设置成 1。

- 有效负荷长度（Payload length）: 7、7+16 或者 7+64 数位

  表示了 “有效负荷数据 Payload data” 的长度，以字节为单位：如果是 0-125，那么就直接表示了负荷长度。如果是 126，那么接下来的两个字节表示的 16 位无符号整型数则是负荷长度。如果是 127，则接下来的 8 个字节表示的 64 位无符号整型数则是负荷长度。表示长度的数值的字节是按网络字节序（network byte order 即大端序）表示的。注意在所有情况下，必须使用最小的负荷长度，比如，对于一个 124 字节长度的字符串，长度不可以编码成 126，0，124。负荷长度是 “扩展数据 Extension data” 长度 + “应用数据Application data” 长度 。“扩展数据” 的长度可以是 0，那么此时 “应用数据” 的长度就是负荷长度。

- 掩码钥匙 Masking key：0 或者 4 个数位

  所有由客户端发往服务端的帧中的内容都必须使用一个 32 位的值进行掩码。这个字段有值的时候（占 4 个数位）仅当掩码标识位设置成了 1，如果掩码标识位设置为 0，则此字段没有值（占 0 个数位）。对于进一步掩码操作，见第 5.3 节。

- 有效负荷数据 Payload data：(x+y) 字节 byte

  “有效负荷数据” 的定义是 “扩展数据” 联合 “应用数据”。

- 扩展数据 Extension data: x 字节

  “扩展数据是” 0 个字节的，除非协商了一个扩展。任何的扩展都必须提供 “扩展数据” 的长度或者该长度应该如何计算，以及在握手阶段如何使用 “扩展数据” 进行扩展协商。如果 “扩展数据” 存在，那么它的长度被包含在了负荷长度中。

- 应用数据 Application data: y字节

  可以是任意的 “应用数据”，它在一个帧的范围内紧接着 “扩展数据”。“应用数据” 的长度等于负荷长度减去 “扩展数据” 的长度

基础帧协议通过接下来的 ABNF [RFC5234](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc5234) 来定义其形式。一个重要的注意点就是下面的 ABNF 表示的是二进制数据，而不是其表面上的字符串。比如， %x0 和 %x1 各表示一个数位，数位上的值为 0 和 1，而不是表示的字符 “0” 和 “1” 的 ASCII 编码。[RFC5234](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc5234) 没有定义 ABNF 的字符编码。在这里，ABNF 被特定了使用的是二进制编码，这里二进制编码的意思就是每一个值都被编码成具有特定数量的数位，具体的数量因不同的字段而异。

```
ws-frame                = frame-fin           ; 1 bit in length
                          frame-rsv1          ; 1 bit in length
                          frame-rsv2          ; 1 bit in length
                          frame-rsv3          ; 1 bit in length
                          frame-opcode        ; 4 bits in length
                          frame-masked        ; 1 bit in length
                          frame-payload-length   ; either 7, 7+16,
                                                 ; or 7+64 bits in
                                                 ; length
                          [ frame-masking-key ]  ; 32 bits in length
                          frame-payload-data     ; n*8 bits in
                                                 ; length, where
                                                 ; n >= 0

frame-fin               = %x0 ; more frames of this message follow
                        / %x1 ; final frame of this message
                              ; 1 bit in length

frame-rsv1              = %x0 / %x1
                          ; 1 bit in length, MUST be 0 unless
                          ; negotiated otherwise

frame-rsv2              = %x0 / %x1
                          ; 1 bit in length, MUST be 0 unless
                          ; negotiated otherwise

frame-rsv3              = %x0 / %x1
                          ; 1 bit in length, MUST be 0 unless
                          ; negotiated otherwise

frame-opcode            = frame-opcode-non-control /
                          frame-opcode-control /
                          frame-opcode-cont

frame-opcode-cont       = %x0 ; frame continuation

frame-opcode-non-control= %x1 ; text frame
                        / %x2 ; binary frame
                        / %x3-7
                        ; 4 bits in length,
                        ; reserved for further non-control frames

frame-opcode-control    = %x8 ; connection close
                        / %x9 ; ping
                        / %xA ; pong
                        / %xB-F ; reserved for further control
                                ; frames
                                ; 4 bits in length


frame-masked            = %x0
                            ; frame is not masked, no frame-masking-key
                            / %x1
                            ; frame is masked, frame-masking-key present
                            ; 1 bit in length

frame-payload-length    = ( %x00-7D )
                        / ( %x7E frame-payload-length-16 )
                        / ( %x7F frame-payload-length-63 )
                        ; 7, 7+16, or 7+64 bits in length,
                        ; respectively

frame-payload-length-16 = %x0000-FFFF ; 16 bits in length

frame-payload-length-63 = %x0000000000000000-7FFFFFFFFFFFFFFF
                        ; 64 bits in length

frame-masking-key       = 4( %x00-FF )
                          ; present only if frame-masked is 1
                          ; 32 bits in length

frame-payload-data      = (frame-masked-extension-data
                           frame-masked-application-data)
                        ; when frame-masked is 1
                          / (frame-unmasked-extension-data
                            frame-unmasked-application-data)
                        ; when frame-masked is 0

frame-masked-extension-data     = *( %x00-FF )
                        ; reserved for future extensibility
                        ; n*8 bits in length, where n >= 0

frame-masked-application-data   = *( %x00-FF )
                        ; n*8 bits in length, where n >= 0

frame-unmasked-extension-data   = *( %x00-FF )
                        ; reserved for future extensibility
                        ; n*8 bits in length, where n >= 0

frame-unmasked-application-data = *( %x00-FF )
                        ; n*8 bits in length, where n >= 0
```

## 5.3 客户端到服务端掩码

一个被掩码的帧需要将掩码标识位（第 5.2 节定义）设置为 1。

掩码钥匙 masking key 整个都在帧中，就像第 5.2 节定义的。它用于对 “有效负荷数据” 进行掩码操作，包括 “扩展数据” 和 “应用数据”。

掩码钥匙由客户端随机选取一个 32 位的值。在每次准备对帧进行掩码操作时，客户端必须选择在可选的 32 位数值集合中选取一个新的掩码钥匙。掩码钥匙的值需要是不可被预测的；因此，掩码钥匙必须来源于一个具有很强保密性质的生成器，并且 服务器/代理 不能够轻易的预测到一连串的帧中使用的掩码钥匙。不可预测的掩码钥匙可以防止恶意程序在帧的传输过程中探测到掩码钥匙的内容。[RFC4086](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc4086) 具体讨论了为什么对于一个安全性比较敏感的应用程序需要使用一个很强保密性质的生成器。

掩码不会影响 “有效负载数据” 的长度。为了将掩码后的数据进行反掩码，或者倒过来，可以使用下面的算法。同样的算法适用于不同方向发来的帧，比如，对于掩码和反掩码使用相同的步骤。

传输数据中的每 8 个数位的字节 i （transformed-octet-i），生成方式是通过原数据中的每 8 个数位的字节 i （original-octet-i）与以 i 与 4 取模后的数位为索引的掩码钥匙中的 8 为字节 j（masking-key-octet-j） 进行异或（XOR）操作：

```
j = i MOD 4
transformed-octet-i = original-octet-i XOR masking-key-octet-j
```

负载的长度不包括掩码钥匙的长度，它是 “有效负载数据 Payload data” 的长度，比如，位于掩码钥匙后的字节的长度。

## 5.4 消息碎片化

消息碎片化的目的就是允许发送那些在发送时不知道其缓冲的长度的消息。如果消息不能被碎片化，那么一端就必须将消息整个地载入内存缓冲，这样在发送消息前才可以计算出消息的字节长度。有了碎片化的机制，服务端或者中间件就可以选取其适用的内存缓冲长度，然后当缓冲满了之后就发送一个消息碎片。

碎片机制带来的另一个好处就是可以方便实现多路复用。没有多路复用的话，就需要将一整个大的消息放在一个逻辑通道中发送，这样会占用整个输出通道。多路复用需要可以将消息分割成小的碎片，使这些小的碎片可以共享输出通道。（注意多路复用的扩展在这片文档中并没有进行描述）

除非运用了特定的扩展，否则帧是没有特定的语义的。在客户端和服务端协商了某个扩展，或者客户端和服务端没有协商扩展的情况下，中间件都有可能将帧进行 合并/分隔。也就是说，在客户端和服务端没有协商某个扩展时，双方都不应该猜测帧与帧之间的边界。注：这里的某个扩展的意思就是赋予了帧特定的语义的扩展，比如多路复用扩展。

下面的规则解释了如何进行碎片化：

- 一个没有被碎片化的消息只包含一个帧，并且帧的 FIN 数位被设置为 1，且操作码 opcode 不为 0。

- 一个碎片化的消息包含了一个 FIN 未被置为 0 的帧，且这个帧的 opcode 不为 0，在这个帧之后，将有 0 个或者多个 FIN 为 0 且 opcode 为 0 的帧，最后以一个 FIN 为 1 和 opcode 为 0 的帧结束。对于一个碎片化后的消息，它的有效负荷就等于将碎片化后的帧的有效负荷按顺序连接起来；不过当存在扩展时，这一点就不一定正确了，因为扩展可能会设置帧的 “扩展数据”。在没有 “扩展数据” 的情况下，下面的例子演示了碎片化是如何工作的。

  例子：对于一个以三个帧发送的文本消息，其第一个帧的 opcode 是 0x1 并且 FIN 位是 0，第二个帧的 opcode 是 0x0 且 FIN 位是 0，第三个帧的 opcode 是 0x0 且 FIN 位是 1。

- 控制帧（见第 5.5 节），可能会夹杂在消息帧之间。控制帧是不能被碎片化的。

- 消息帧必须以其被发送时的顺序传递到接收端。

- 不同消息的消息帧之间不可以相互夹杂，除非协商了一个定义了如何解释这种夹杂行为的扩展。

- 发送端可以创建任意大小的非控制帧。

- 客户端和服务端必须支持发送和接受碎片化或者非碎片化的消息。

- 一个控制帧是不可以被碎片化的，中间件必须不可以试图将控制帧进行碎片化。

- 如果帧中使用了 RSV 数位，但是中间件不理解其中的任意的 RSV 数位 的值时，它必须不可以改变消息的原有的碎片化帧。

- 在中间件不能确定客户端和服务端进行了哪些扩展协商的情况下，中间件必须不可以修改原有的碎片化帧。

- 最后，组成消息的所有帧都是相同的数据类型，在第一个帧中的 opcode 中指明。因为控制帧不能被碎片化，组成消息的碎片类型必须是文本、二进制、或者其他的保留类型。

注意：如果控制帧不能夹杂在消息帧的话，那么将导致 ping 的结果产生延迟，比如在处理了一个非常长的消息后才响应 ping 控制帧时。因此，要求在处理消息帧的期间可以响应控制帧。

重点注意：在没有扩展的情况下，接收端为了处理消息不是非得缓冲所有的帧。比如如果使用了 流API （streaming API），数据帧可以直接传递给应用层。不过这样假设并不一定在所有的扩展中都适用。

## 5.5 控制帧

控制帧是通过它的 opcode 的最高有效位是 1 去确定的。当前已经定义了的控制帧包括 `0x8 (close)`，`0x9 (Ping)`，`0xA (Pong)`。操作码 `0xB-0xF` 是为将来的控制帧保留的，目前尚未定义。

控制帧是为了在 WebSocket 中通信连接状态。控制帧可以夹杂在消息帧之间发送。

所有的控制帧的负载长度都必须是 125 字节，并且不能被碎片化。

## 关闭帧

关闭帧的操作码 opcode 是 `0x8`。

关闭帧可以包含消息体（通过帧的 “应用数据” 部分）去表示关闭的原因，比如一端正在关闭服务，一端接收到的帧过大，或者一端接收到了不遵循格式的帧。如果有消息体的话，消息体的前两个字节必须是无符号的整型数（采用网络字节序），以此整型数去表示状态码 /code/ 定义在第 7.4 节。在两个字节的无符号整型数之后，可以跟上以 UTF-8 编码的数据表示 /reason/，/reason/ 数据的具体解释方式此文档并没有定义。并且 /reason/ 的内容不一定是人类可读的数据，只要是有利于发起连接的脚本进行调试就可以。因为 /reason/ 并不一定就是人类可读的，所以客户端必须不将此内容展示给最终用户。

客户端发送的每一个帧都必须按照第 5.3 节中的内容进行掩码。

应用程序在发送了关闭帧之后就不可以再发送其他数据帧了。

如果接收到关闭帧的一端之前没有发送过关闭帧的话，那么它必须发送一个关闭帧作为响应。（当发送一个关闭帧作为响应的时候，发送端通常在作为响应的关闭帧中采用和其接收到的关闭帧相同的状态码）。并且响应必须尽快的发送。一端可以延迟关闭帧的发送，比如一个重要的消息已经发送了一半，那么可以在消息的剩余部分发送完之后再发送关闭帧。但是作为首先发送了关闭帧，并在等待另一端进行关闭响应的那一端来说，并不一定保证其会继续处理数据内容。

在发送和接收到了关闭帧之后，一端就可以认为 WebSocket 连接已经关闭，并且必须关闭底层相关的 TCP 连接。如果是服务端首先发送了关闭帧，那么在接收到客户端返回的关闭帧之后，服务端必须立即关闭底层相关的 TCP 连接；但是如果是客户端首先发送了关闭帧，并接收到了服务端返回的关闭帧之后，可以选择其认为合适的时间关闭连接，比如，在一段时间内没有接收到服务端的 TCP 关闭握手。

如果客户端和服务端同时发送了关闭消息，那么它们两端都将会接收到来自对方的关闭消息，那么它们就可以认为 WebSocket 连接已经关闭，并且关闭底层相关的 TCP 连接。

## 5.5.2 Ping

Ping 帧的操作码是 `0x9`

Ping 帧也可以有 “应用数据”

一旦接收到了 Ping 帧，接收到的一端必须发送一个 Pong 帧作为响应，除非它已经接收到了关闭帧。响应的一端必须尽快的做出响应。Pong 帧定义在第 5.5.3 节。

一端可以在连接建立之后，到连接关闭之前的任意时间点发送 Ping 帧。

注意：Ping 帧的目的可以是保持连接（keepalive）或者是验证服务端是否还是有响应的。

## 5.5.3 Pong

Pong 帧的操作码是 `0xA`

第 5.5.2 节的要求同时适用于 Ping 帧和 Pong 帧。

Pong 帧的 “应用数据” 中的内容必须和其响应的 Ping 帧中的 “应用数据” 的内容相同。

如果一端接收到了 Ping 帧并且在没有来得及响应的时候又接收到了新的 Ping 帧，那么响应端可以选择最近的 Ping 帧作为响应的对象。

Pong 帧可以在未被主动请求的情况下发送给对方。这被认为是单向的心跳包。单向心跳包是得不到响应的。

## 5.6 数据帧

数据帧（比如，非控制帧）是通过操作码的最高有效位是 0 来确定的。当前已经定义的数据帧包括 `0x1 (文本)`，`0x2 (二进制)`。操作码 `0x3-0x7` 是为了将来的非控制帧的使用而保留的。

数据帧承载了 “应用层 application-layer” 或者 “扩展层 extension-layer” 的数据。操作码决定了数据的表现形式。

- 文本 Text

  “有效负载数据 Payload data” 是以 UTF-8 编码的文本。注意，作为整个文本消息的一部分的部分文本帧可能包含了部分的 UTF-8 序列；但是整个的消息的内容必须是一个有效的 UTF-8 序列。对于无效的 UTF-8 消息的处理在第 8.1 节中描述。

- 二进制 Binary

  “有效负荷数据 Payload data” 是仅由应用层来决定的任意二进制内容。

## 5.7 例子

- 一个单个帧的没有进行掩码的文本消息
  - 0x81 0x05 0x48 0x65 0x6c 0x6c 0x6f（消息内容为 “Hello”）
- 一个单个帧的掩码后的消息
  - 0x81 0x85 0x37 0xfa 0x21 0x3d 0x7f 0x9f 0x4d 0x51 0x58（消息内容为 “ Hello”）
- 一个碎片化的没有掩码的文本消息
  - 0x01 0x03 0x48 0x65 0x6c（消息内容为 “Hel”）
  - 0x80 0x02 0x6c 0x6f（消息内容为 “lo”）
- 没有掩码的 Ping 请求和其掩码后的响应
  - 0x89 0x05 0x48 0x65 0x6c 0x6c 0x6f（消息体部分为 “Hello”，只不过是例子，可以为任意内容）
  - x8a 0x85 0x37 0xfa 0x21 0x3d 0x7f 0x9f 0x4d 0x51 0x58（消息体部分也是 “Hello”，和其响应的 Ping 相同）
- 256 个字节的二进制消息，使用单个未掩码的帧
  - 0x82 0x7E 0x0100 [256 个字节的二进制数据]
- 64 Kb 的二进制消息，使用单个未掩码的帧
  - 0x82 0x7F 0x0000000000010000 [65536 个字节的二进制数据]

## 5.8 扩展性

协议被设计为允许扩展，扩展可以在基础协议的功能上添加更多的功能。通信双方必须在握手期间完成扩展的协商。在这份技术说明中，为扩展提供使用的部分为：操作码 0x3 到 0x7、以及 0xB 到 0xF，“扩展数据 Extension data” 字段，frame-rsv1、frame-rsv2、frame-rsv3 这三个位于帧头部的数位。关于扩展协商的详细在第 9.1 节中讨论。下面的列表是关于扩展的预期使用形式，不过它既不完整也不规范：

- “扩展数据” 可以放在 “应用数据” 之间，它们共同组成 “有效负荷数据”
- 保留的数位可以为每一帧按需分配
- 保留的操作码可以被定义
- 如果需要更多的操作码的话，可以占用保留数位以为操作码提供更多的数位空间
- 占用保留数位，或者在 “有效负荷数据” 之外定义 “扩展” 的操作码，以此获得更大的操作码表示空间，或者更多的区别每一帧的数位

## 6 发送和接收数据

## 6.1 发送数据

为了在 WebSocket 连接上发送由 /data/ 组成的 WebSocket 消息，发送端必须按下的步骤去执行：

1. 发送端必须确定当前的 WebSocket 连接的状态是 OPEN（见 第 4.1 和 4.2 节）。在任何时间点，如果连接的状态改变了，那么发送端必须终止下面的步骤。
2. 发送端必须使用 WebSocket 帧将 /data/ 按第 5.2 节中描述的形式包裹起来。如果数据太大，或者在发送时不能整个地获取需发送数据，那么发送端可以按照第 5.4 节中描述的，将数据分割成一连串的帧进行发送。
3. 包含数据的第一个帧的操作码必须设置为适当的数据类型，以便接收端可以确定用文本还是二进制来解释其接收到的数据，数据类型定义在第 5.2 节。
4. 在消息的最后一个包含数据的帧中必须将其 FIN 设置为 1，相关定义在第 5.2 节。
5. 如果数据是由客户端发送的，那么数据在发送前必须按照第 5.2 中定义的方式进行掩码。
6. 如果连接中进行了扩展协商，那么额外的扩展相关的处理将会应用到帧上。
7. 帧必须经由 WebSocket 底层相关的网络连接发送。

## 6.2 接收数据

为了接收  WebSocket 数据，接收端必须监听底层相关的网络连接。接收到的数据必须按照第 5.2 节中定义的格式进行解析。如果接收到的是一个控制帧，那么必须按照第 5.5 节中的定义去处理。一旦接收到第 5.6 节中定义的数据帧，接收端必须注意数据帧的类型 /type/，这点根据帧的 opcode，定义在第 5.2 节。“应用数据 Application data” 被定义为消息的数据 /data/。如果帧是一个没有被碎片化的帧，定义在第 5.4 节，那么就说明一个消息已经被完全接收了，即知道了其类型 /type/ 和数据 /data/。如果帧是碎片化消息的一部分，那么其随后的帧的 “应用数据” 连接在一起组成消息的数据 /data/。当最后一个碎片化的帧被接收时，也就是帧的 FIN 位为 1 时，表明一个 WebSocket 消息已经被完全接收了，其数据 /data/ 就是所有相关碎片化的帧的 “应用数据” 连接到一起的值，而 /type/ 就是第一个或者其他组成消息的碎片化帧的操作码。之后的帧必须被解释为属于一个新的消息。

扩展（第 9 节）可能会更改数据被读取的方式，特别是如何界定消息之间的边界。扩展在有效负荷中的 “应用数据” 之前添加的 “扩展数据” 也可能会修改 “应用数据” 的内容（比如进行了压缩）。

服务端必须将来自客户端的帧进行反掩码，操作定义在第 5.3 节。

## 7 关闭连接

## 7.1 定义

## 7.1.1 关闭 WebSocket 连接

为了关闭 WebSocket 连接，一端可以关闭底层的 TCP 连接。一端在关闭连接的时候必须干净的关闭，比如 TLS 会话，尽可能的丢弃所有已经接收但是尚未处理的字节。一端可以在需要的时候以任意的理由去关闭连接，比如在收到攻击时。

底层的 TCP 连接，在一般情况下应该由服务端先进行关闭，而客户端则需要在一段时间内等待服务端的 TCP 关闭，如果超过了客户端的等待时间，客户端则可以关闭 TCP 连接。

一个以使用 Berkeley sockets 的 C 语言的例子演示如何干净的关闭连接：首先一端需要调用对 socket 调用 shutdown() 函数，并以 SHUT_WR 为函数的参数，然后调用 recv() 函数直到其返回值为 0，最后调用 close() 函数关闭 socket。

## 7.1.2 开始 WebSocket 关闭握手

为了关闭开始 WebSocket 关闭握手，需要关闭的一端必须选择一个状态码（第 7.4 节）/code/ 和可选的关闭原因 （第 7.1.6 节）/reason/，然后按照第 5.5.1 节中的描述发送一个关闭帧，帧的状态码以及原因就是之前选取的 /code/ 和 /reason/。一旦一端发送并接收到了关闭帧，就可以按照第 7.1.1 节中定义的内容关闭 WebSocket 连接。

## 7.1.3 WebSocket 关闭握手已经开始

一旦任何一端发送或者接收到关闭帧，就表明 WebSocket 关闭握手已经开始，并且 WebSocket 连接的状态变为 CLOSING。

## 7.1.4 WebSocket 连接已经关闭

当底层的 TCP 连接已经关闭时，就表明 WebSocket 连接已经关闭，并且 WebSocket 连接的状态变为 CLOSED。如果 TCP 连接在 WebSocket 关闭握手完成之后才进行关闭，就说明关闭是干净（cleanly）的。否则的话就说明 WebSocket 连接已经关闭，但不是干净地（cleanly）。

## 7.1.5 WebSocket 连接关闭代码

与第 5.5.1 节和第 7.4 节中定义的一样，一个关闭帧可以包含一个关闭状态码，以此表明关闭的原因。WebSocket 的关闭可以由任意一端发起，或者同时发起。返回的关闭帧的状态码与接收到的关闭帧的状态码相同。如果关闭帧没有包含状态码，那么就认为其状态码是 1005。如果一端发现 WebSocket 连接已经关闭但是没有收到关闭帧，那么就认为此时的状态码是 1006。

注意：两端的关闭帧的状态码不必相同。比如，如果远程的一端发送了一个关闭帧，但是本地的应用程序还没有读取位于接收缓存中的关闭帧，并且应用程序也发送了一个关闭帧，那么两端都将会达到 “发送了” 和 “接收到” 关闭帧的状态。每一端都会看到来自另一端的具有不同状态码的关闭帧。因此，两端可以不必要求发送和接收到的关闭帧的状态码是相同的，这样两端就可以大概同时进行 WebSocket 连接的关闭了。

## 7.1.6 WebSocket 连接关闭原因

与第 5.5.1 节和第 7.4 节中定义的相同，关闭帧可以包含一个状态码，并且在状态码之后可以跟随以 UTF-8 编码的数据，具体这些数据应该如何被解释依赖于对端的实现，本协议并没有明确的定义。每一端都可以发起 WebSocket 关闭，或者同时发起。WebSocket 连接关闭原因的定义就是跟随在关闭状态码之后的以 UTF-8 编码的数据，响应的关闭帧中的 /reason/ 内容来自请求的关闭帧中 /reason/，并与之相同。如果没有定义这些 UTF-8 数据，那么关闭的原因就是空字符串。

注意：遵循第 7.1.5 节中描述的逻辑，两端不必要求发送和接收的关闭帧的 /reason/ 是相同的。

## 7.1.7 将 WebSocket 连接标记为失败

因为某种算法或者特定的需求使得一端需要将 WebSocket 连接表示位失败。为了达到这个目的，客户端必须关闭 WebSocket 连接，并且可以将问题以适当的方式反馈给用户（对于开发者来说可能非常重要）。同样的，服务端为了达到这个目的也必须关闭 WebSocket 连接，并且使用日志记录下发生的问题。

如果在希望将 WebSocket 连接标记为失败之前，WebSocket 连接已经建立的话，那么一端在关闭 WebSocket 连接之前应该发送关闭帧，并带上适当的状态码（第 7.4 节）。如果一端认为另一端不可能有能力去接受和处理关闭帧时，比如 WebSocket 连接尚未建立，那么可以省略发送关闭帧的过程。如果一端标记了 WebSocket 连接为失败的，那么它不可以再接受和处理来自远程的数据（包括响应一个关闭帧）。

除了上面的情况或者应用层需要（比如，使用了 WebSocket API 的脚本），客户端不应该关闭连接。

## 7.2 异常关闭

## 7.2.1 客户端发起的关闭

因为某种算法或者在开始握手的实际运作过程中，需要标记 WebSocket 连接为失败。为了达到这个目的，客户端必须按照第 7.1.7 节中描述的内容将 WebSocket 连接标记为失败。

如果在任意时间点，底层的传输层连接发送了丢失，那么客户端必须将 WebSocket 连接标记为失败。

除了上面的情况或者特定的应用层需要（比如，使用了 WebSocket API 的脚本），客户端不可以关闭连接。

## 7.2.2 服务端发起的关闭

因为某种算法或者在握手期间终止 WebSocket 连接，服务端必须按照第 7.1.1 节的描述去关闭 WebSocket 连接。

## 7.2.3 从异常中恢复

异常关闭可能有很多的原因引起。比如一个短暂的错误导致的异常关闭，在这种情况下，通过重连可以使用一个没有问题的连接，然后继续正常的操作。然而异常也可能是一个由非短暂的问题引起的，如果所有发布的客户端在经历了一个异常关闭之后，立刻不断的试图向服务器发起重连，如果有大量的客户端在试图重连的话，那么服务器将有可能面对拒绝服务攻击（denial-of-service attack）。这样造成的结果就是服务将无法在短期内恢复。

为了防止这个问题出现，客户端应该在发生了异常关闭之后进行重连时使用一些补偿机制。

第一个重连应该延迟，在一个随机时间后进行。产生用于延迟的随机时间的参数由客户端去决定，初始的重连延迟可以在 0 到 5 秒之间随机选取。客户端可以根据实际应用的情况去决定具体的随机值。

如果第一次的重连失败，那么接下来的重连应该使用一个更长的延迟，可以使用一些已有的方法，比如 [truncated binary exponential backoff](https://link.jianshu.com?t=https://en.wikipedia.org/wiki/Exponential_backoff)

## 7.3 连接的一般关闭

服务端可以在其需求的时候对 WebSocket 连接进行关闭。客户端不应该随意的关闭 WebSocket 连接。当需要进行关闭的时候，需要遵循第 7.1.2 节中定义的过程。

## 状态码

当关闭已经建立的连接时（比如在握手完成后发送关闭帧），请求关闭的一端必须表明关闭的原因。如何解释原因，以及对于原因应该采取什么动作，都是这份技术说明中没有定义的。这份技术说明中定义了一组预定义的状态码，以及扩展、框架、最终应用程序使用的状态码范围。状态码相关的原因 /reason/ 在关闭帧中是可选的。

## 7.4.1 已定义的状态码

当发送关闭帧的时候，一端可以采用下面的预定义的状态码：

- 1000
  - 1000 表明这是一个正常的关闭，表示连接已经圆满完成了其工作。
- 1001
  - 1001 表明一端是即将关闭的，比如服务端将关闭或者浏览器跳转到了其他页面。
- 1002
  - 1002 表明一端正在因为协议错误而关闭连接。
- 1003
  - 1003 表明一端因为接收到了无法受理的数据而关闭连接（比如只能处理文本的一端接收到了一个二进制的消息）
- 1004
  - 保留的。特定的含义会在以后定义。
- 1005
  - 1005 是一个保留值，并且必须不可以作为关闭帧的状态码。它的存在意义就是应用程序可以使用其表示帧中没有包含状态码。
- 1006
  - 1006 这是一个保留值，并且必须不可以作为关闭帧的状态码。它的存在意义就是如果连接非正常关闭而应用程序需要一个状态码时，可以使用这个值。
- 1007
  - 1007 表明一端接收到的消息内容与之标记的类型不符而需要关闭连接（比如文本消息中出现了非 UTF-8 的内容）
- 1008
  - 1008 表明了一端接收到的消息内容违反了其接收消息的策略而需要关闭连接。这是一个通用的状态码，可以在找不到其他合适的状态码时使用此状态码，或者希望隐藏具体与接收端的哪些策略不符时（比如 1003 和 1009）。
- 1009
  - 1009 表明一端接收了非常大的数据而其无法处理时需要关闭连接。
- 1010
  - 1010 表明了客户端希望服务端协商一个或多个扩展，但是服务端在返回的握手信息中包含协商信息。扩展的列表必须出现在其发送给服务端的关闭帧的 /reason/ 中。注意这个状态码并不被服务端使用。
- 1011
  - 1011 表明了一端遇到了异常情况使得其无法完成请求而需要关闭连接。
- 1015
  - 1015 是一个保留值，并且它必须不可以作为状态码在关闭帧中使用，在应用程序需要一个状态码去表明执行 TLS 握手失败时，可以使用它（比如服务端的证书没有通过验证）。

## 7.4.2 保留的状态码区间

- 0-999

  在 0-999 之间的状态码是不被使用的

- 1000-2999

  在 1000-2999 之间的状态码是本协议保留的，并且扩展可以在其公开的技术说明中使用。

- 3000-3999

  在 3000-3999 之间的状态码是为库、框架、应用程序保留的。这些状态码可以直接通过 IANA 进行注册。状态码的具体表示意义为在本协议中定义。

- 4000-4999

  在 4000-4999 之间的状态码是为了私有使用而保留的，因此不可以被注册。相应状态码的使用及其意义可以在 WebSocket 应用程序之间事先商议好。这些状态码的意义在本协议中未定义。

## 错误处理

## 8.1 处理编码错误的 UTF-8 数据

当一端在以 UTF-8 编码解释接收到的数据，但是发现其实不是有效的 UTF-8 编码时，一端必须标记 WebSocket 连接为失败。这个规则适用于握手以及随后的数据传输阶段。

## 9. 扩展

在这份技术说明中，客户端是可以请求使用扩展的，并且服务端可以受理客户端请求的扩展中的一个或者所有扩展。服务端响应的扩展必须属于客户端请求的扩展列表。如果扩展协商中包含了相应的扩展参数，那么参数的选择和应用必须按照具体的扩展的技术说明中描述的方式。

## 9.1 扩展协商

客户端通过包含 |Sec-WebSocket-Extensions| 去请求扩展，此字段名遵循普通的 HTTP 头字段的规则 [RFC2616], Section 4.2]([https://tools.ietf.org/html/rfc2616#section-4.2](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc2616#section-4.2))，其内容的形式经由下面的 ABNF [RFC2616](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc2616) 表达式给出定义。注意，着一节中的 ABNF 语法规则遵循 [RFC2616](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc2616)，包括了 “隐含的 *LWS 规则”。如果一端接收到的值不符合下面的 ABNF，那么接收端必须立刻标记 WebSocket 连接为失败。

```
Sec-WebSocket-Extensions = extension-list
extension-list = 1#extension
extension = extension-token *( ";" extension-param )
extension-token = registered-token
registered-token = token
extension-param = token [ "=" (token | quoted-string) ]
    ;When using the quoted-string syntax variant, the value
    after quoted-string unescaping MUST conform to the
    ;'token' ABNF.
```

注意，和其他的 HTTP 头字段一样，这些头字段也可以分隔成多行，或者由多行合并。因此下面的两个是等价的：

```
Sec-WebSocket-Extensions: foo
Sec-WebSocket-Extensions: bar; baz=2
```

等价于

```
Sec-WebSocket-Extensions: foo, bar; baz=2
```

任何的 extension-token 比如使用已注册的 token（见第 11.4 节）。为扩展提供的参数比如遵循相应扩展的定义。注意，客户端只是提供它希望使用的扩展，除非服务端从中选择了一个或多个表明其也希望使用，否则客户端不可以私自的使用。

注意，扩展的在列表中顺序是重要的。多个扩展之间的交互方式，可能在具体定义了扩展的文档中进行了描述。如果没有定义描述了多个扩展之间应该如何交互，那么排在靠前位置的扩展应该最先被考虑使用。在服务端响应中列出的扩展将是连接实际将会使用的扩展。扩展之间修改数据或者帧的操作顺序，应该假设和扩展在服务端握手响应中的扩展列表中出现的顺序相同。

比如，如果有两个扩展 “foo” 和 “bar”，并且在服务端发送的 |Sec-WebSocket-Extensions| 的值为 “foo, bar”，那么对数据的操作整体来看就是 `bar(foo(data))`，对于数据或者帧的修改过程看起来像是 “栈 stack”。

一个关于受理扩展头字段的非规范化的例子：

```
Sec-WebSocket-Extensions: deflate-stream
Sec-WebSocket-Extensions: mux; max-channels=4; flow-control, deflate-stream
Sec-WebSocket-Extensions: private-extension
```

服务端受理一个或者多个扩展，通过 |Sec-WebSocket-Extensions| 头字段包含一个或者多个来自客户端请求中的扩展。扩展参数的解释，以及服务端如何正确响应客户端的参数，都在各自扩展的定义中描述。

## 9.2 已知的扩展

扩展提供了一个插件的机制，以提供额外的协议功能。这份文档没有定义任何的扩展，但是实现时可以使用独立定义在其他文档的扩展。

## 10. 安全考虑

这一节描述了一些 WebSocket 协议在使用中需要注意的问题。问题被分成了不同的小节。

## 10.1 非浏览器客户端

WebSocket 可以抵御运行在被信任的应用程序（比如浏览器）中的恶意 Javascript 脚本，比如，通过检查 |Origin| 头字段。不过当面对具有更多功能的客户端时就不能采用此方法了（检查 |Origin| 头字段）。

这份协议可以适用于运行在 web 页面中的脚本，也可以直接被主机所使用。那些主机可以因为自身的目的发送一个伪造的 |Origin| 头字段，以此迷惑服务器。服务端因此服务器不应该信息任何的客户端输入。

例子：如果服务端使用了客户端的 SQL 查询语句，所有的输入文本在提交到 SQL 服务器之前必须进行跳脱操作（escape），减少服务端被 SQL 注入的风险。

## 10.2 Origin 的考虑

服务端不必接收来自互联网的所有请求，可以仅仅受理包含特定源的请求。如果请求的源不符合服务端的接收范围，那么服务端应该在对客户端的握手响应中包含状态码 “403 Forbidden”。

|Origin| 的作用是可以预防来自运行在可信任的客户端中的 Javascript 的恶意攻击。客户端本身可以连接到服务器，通过 |Origin| 的机制决定是否将通信的权限交给 Javascript 应用。这么做的目的不是针对非浏览器的连接，而是杜绝运行在被信任的浏览器可能的潜在威胁 -  Javascript 脚本伪造 WebSocket 连接。

## 10.3 针对基础设施的攻击

除了一端的终节点会收到攻击之外，基础设施中的其他部分，比如代理，也可能会收到攻击。

针对代理的攻击实际上是针对那些在实现上有缺陷的代理服务器，有缺陷的代理服务器的工作方式类似：

1. 首先你通过 Socket 的方式和 IP 为 2.2.2.2 的服务器建立连接，连接是经由代理的。
2. 在连接建立完成后，你发送了类似下面的文本：

```
GET /script.js HTTP/1.1
Host: target.com
```

（更多更深入的描述见 [Talking](https://link.jianshu.com?t=http://w2spconf.com/2011/papers/websocket.pdf)）

这段文本首先是传到代理服务器的，代理服务器正确的工作方式是应该将此文本直接转发给 IP 为 2.2.2.2 的服务器。可是，有缺陷的代理会认为这是一个 HTTP 请求，需要采用 HTTP 代理的机制，进而访问了 target.com 并获取了 /script.js。

这种错误的工作方式并不是你所期望的。但是不可能一一检查网络中所有可能存在此问题的代理，所以最好的方式就是将客户端发送的内容都进行掩码操作，这样就不会出现那种让有缺陷的代理服务器产生迷惑的内容了。

## 10.4 特定实现的限制

在协议实现中，可能会有一些客观的限制，比如特定平台的限制，这些限制与帧的大小或者所有帧合并后的消息的大小相关（比如，恶意的终节点可以通过发送单个很大的帧（2**60），或者发送很多很小的帧但是这些帧组成的消息非常大，以此来耗尽另一方的资源）。因此在实现中，一端应该强制使用一些限制，限制帧的大小，以及许多帧最后组成的消息的大小。

## 10.5 WebSocket 客户端认证

这份协议没有规定任何方式可被用于服务端在握手期间对客户端进行认证。WebSocket 服务端可以使用任何在普通 HTTP 服务端中使用的对客户端的认证方式，比如 cookie，HTTP 认证，或者 TLS 认证。

## 10.6 连接的保密性和完整性

WebSocket 协议的保密性和完整性是通过将其运行在 TLS 上达到的。WebSocket 实现必须支持 TLS 并在需要的时候使用它。

对于使用 TLS 的连接，TLS 提供的大部分好处都是基于 TLS 握手阶段协商的算法的强度。比如，一些 TLS 加密算法没有保证信息的保密性。为了使安全达到合适的程度，客户端应该只使用高强度的 TLS 算法。[W3C.REC-wsc-ui-20100812](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc6455#ref-W3C.REC-wsc-ui-20100812) 具体讨论了什么是高强度的 TLS 算法，[RFC5246](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc5246) 的附录 A.5 和 附录 D.3 提供了一些指导意见。

## 10.7 处理错误数据

客户端和服务端接收的数据都必须经过验证。如果在任意时间点上，一端接收到了无法理解的或者违反标准的数据，或者发现了不安全的数据，或者在握手期间接收到了非期望的值（比如错误的路径或者源），则可以关闭 TCP 连接。如果接收到无效数据时 WebSocket 连接已经建立，那么一端在关闭 WebSocket 连接之前，应该向另一端发送一个带有适当的状态码的关闭帧。通过使用具有适当状态码的关闭帧，可以帮助定位问题。如果在握手期间接收到了无效的数据，那么服务端应该返回适当的 HTTP 状态码 [RFC2616](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc2616)。

一个典型的安全问题就是当发送的数据采用了错误的编码时。这份协议中规定了，文本数据包含的必须是 UTF-8 编码的数据。应用程序需要通过一个长度去确定帧序列的传输何时结束，但是这个长度往往在事先不好确定（碎片化的消息）。这就给检查文本消息是否采用了正确的编码带来了困难，因为必须等到消息的所有碎片帧都接受完成了，才可以检查它们组成的消息的编码是否正确。不过如果不检查编码的话，就不能确保接收的数据可以被正确的解释，并会带来潜在的安全问题。

## 10.8 在 WebSocket 握手中采用 SHA-1

这份文档中描述的 WebSocket 握手并不依赖于 SHA-1 算法的安全属性，比如抗碰撞性或者在 [RFC4270](https://link.jianshu.com?t=https://tools.ietf.org/html/rfc4270) 中描述的 second pre-image attack。

作者：mconintet

链接：https://www.jianshu.com/p/fc09b0899141

來源：简书

简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。