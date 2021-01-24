# Anaconda多环境多版本python配置指导

![96](https://upload.jianshu.io/users/upload_avatars/1428535/ebc223f322fb?imageMogr2/auto-orient/strip|imageView2/1/w/96/h/96)

 

[NorthPenguin](https://www.jianshu.com/u/bad199ab8628)

 

关注

2016.01.15 20:19* 字数 3526 阅读 106384评论 22喜欢 124赞赏 2

Anaconda是一个优秀的开源Python发布版本，由于中文社区对这个软件的介绍及教程比较少，还是官方文档比较详细，在此翻译如下。

原文地址：<http://conda.pydata.org/docs/test-drive.html>

------

# conda测试指南

在开始这个conda测试之前，你应该已经下载并安装好了Anaconda或者Miniconda
**注意：**在安装之后，你应该关闭并重新打开windows命令行。

# 一、Conda测试过程：

1. 使用conda。首先我们将要确认你已经安装好了conda
2. 配置环境。下一步我们将通过创建几个环境来展示conda的环境管理功能。使你更加轻松的了解关于环境的一切。我们将学习如何确认你在哪个环境中，以及如何做复制一个环境作为备份。
3. 测试python。然后我们将检查哪一个版本的python可以被安装，以及安装另一个版本的python，还有在两个版本的python之间的切换。
4. 检查包。我们将1)罗列出安装在我们电脑上的包，2)浏览可用的包，3)使用conda install命令来来安装以及移除一些包。对于一些不能使用conda安装的包，我们将4)在Anaconda.org网站上搜索。对于那些在其它位置的包，我们将5)使用pip命令来实现安装。我们还会安装一个可以免费试用30天的商业包IOPro
5. 移除包、环境以及conda.我们将以学习删除你的包、环境以及conda来结束这次测试。

# 二、完整过程

**提示：**在任何时候你可以通过在命令后边跟上--help来获得该命令的完整文档。例如，你可以通过如下的命令来学习conda的update命令。

```
conda update --help
```

## 1. 管理conda：

Conda既是一个包管理器又是一个环境管理器。你肯定知道包管理器，它可以帮你发现和查看包。但是如果当我们想要安装一个包，但是这个包只支持跟我们目前使用的python不同的版本时。你只需要几行命令，就可以搭建起一个可以运行另外python版本的环境。，这就是conda环境管理器的强大功能。
提示：无论你使用Linux、OS X或者Windows命令行工具，在你的命令行终端conda指令都是一样的，除非有特别说明。

### 检查conda已经被安装。

为了确保你已经在正确的位置安装好了conda，让我们来检查你是否已经成功安装好了Anaconda。在你的命令行终端窗口，输入如下代码：

```
conda --version
```

Conda会返回你安装Anaconda软件的版本。
**提示**：如果你看到了错误信息，检查你是否在安装过程中选择了仅为当前用户按安装，并且是否以同样的账户来操作。确保用同样的账户登录安装了之后重新打开命令行终端窗口。

### 升级当前版本的conda

接下来，让我们通过使用如下update命令来升级conda：

```
conda update conda
```

conda将会比较新旧版本并且告诉你哪一个版本的conda可以被安装。它也会通知你伴随这次升级其它包同时升级的情况。
如果新版本的conda可用，它会提示你输入y进行升级.

```
proceed ([y]/n)? y
```

conda更新到最新版后，我们将进入下一个主题。

## 2. 管理环境。

现在我们通过创建一些环境来展示conda的环境操作，然后移动它们。

### 创建并激活一个环境

使用conda create命令，后边跟上你希望用来称呼它的任何名字：

```
conda create --name snowflake biopython
```

这条命令将会给biopython包创建一个新的环境，位置在/envs/snowflakes
**小技巧：**很多跟在--后边常用的命令选项，可以被略写为一个短线加命令首字母。所以--name选项和-n的作用是一样的。通过conda -h或conda –-help来看大量的缩写。

### 激活这个新环境

```
Linux，OS X: source activate snowflakes
Windows：activate snowflake`
```

**小技巧**：新的开发环境会被默认安装在你conda目录下的envs文件目录下。你可以指定一个其他的路径；去通过conda create -h了解更多信息吧。
**小技巧**：如果我们没有指定安装python的版本，donda会安装我们最初安装conda时所装的那个版本的python。

### 创建第二个环境

这次让我们来创建并命名一个新环境，然后安装另一个版本的python以及两个包 Astroid 和 Babel。

```
conda create -n bunnies python=3 Astroid Babel
```

这将创建第二个基于python3 ，包含Astroid 和 Babel 包，称为bunnies的新环境，在/envs/bunnies文件夹里。
**小技巧**：在此同时安装你想在这个环境中运行的包，
**小提示：**在你创建环境的同时安装好所有你想要的包，在后来依次安装可能会导致依赖性问题（貌似是，不太懂这个术语怎么翻）。
**小技巧**：你可以在conda create命令后边附加跟多的条件，键入conda create –h 查看更多细节。

### 列出所有的环境

现在让我们来检查一下截至目前你所安装的环境，使用conda environment info 命令来查看它:

```
conda info --envs
```

你将会看到如下的环境列表：

```
conda environments:
 snowflakes          * /home/username/miniconda/envs/snowflakes
 
 bunnies               /home/username/miniconda/envs/bunnies
 
 root                  /home/username/miniconda
```

### 确认当前环境

你现在处于哪个环境中呢？snowflakes还是bunnies？想要确定它，输入下面的代码：

```
conda info -envis
```

conda将会显示所有环境的列表，当前环境会显示在一个括号内。

```
(snowflakes)  
```

注意：conda有时也会在目前活动的环境前边加上*号。

### 切换到另一个环境(activate/deactivate)

为了切换到另一个环境，键入下列命令以及所需环境的名字。

```
Linux，OS X: source activate snowflakes
Windows：activate snowflakes
```

如果要从你当前工作环境的路径切换到系统根目录时，键入：

```
Linux，OS X: source deactivate
Windows: deactivate
```

当该环境不再活动时，将不再被提前显示。

### 复制一个环境

通过克隆来复制一个环境。这儿将通过克隆snowfllakes来创建一个称为flowers的副本。

```
conda create -n flowers --clone snowflakes
```

通过conda info –-envs来检查环境
你现在应该可以看到一个环境列表：flowers, bunnies, and snowflakes.

### 删除一个环境

如果你不想要这个名为flowers的环境，就按照如下方法移除该环境：

```
conda remove -n flowers --all
```

为了确定这个名为flowers的环境已经被移除，输入以下命令：

```
conda info -e
```

flowers 已经不再在你的环境列表里了，所以我们知道它被删除了。

### 学习更多关于环境的知识

如果你想学习更多关于conda的命令，就在该命令后边跟上 `-h`

```
conda remove -h
```

## 3. 管理Python

conda对Python的管理跟其他包的管理类似，所以可以很轻松地管理和升级多个安装。

### 检查python版本

首先让我们检查那个版本的python可以被安装：

```
conda search --full --name python
```

你可以使用conda search python来看到所有名字中含有“python”的包或者加上`--full --name`命令选项来列出完全与“python”匹配的包。

### 安装一个不同版本的python

现在我们假设你需要python3来编译程序，但是你不想覆盖掉你的python2.7来升级，你可以创建并激活一个名为snakes的环境，并通过下面的命令来安装最新版本的python3：

```
conda create -n snakes python=３
·Linux，OS X：source activate snakes
·Windows： activate snakes
```

**小提示：**给环境取一个很形象的名字，例如“Python3”是很明智的，但是并不有趣。

### 确定环境添加成功

为了确保snakes环境已经被安装了，键入如下命令：

```
conda info -e
```

conda会显示环境列表，当前活动的环境会被括号括起来`（snakes）`

### 检查新的环境中的python版本

确保snakes环境中运行的是python3：

```
python --version
```

### 使用不同版本的python

为了使用不同版本的python，你可以切换环境，通过简单的激活它就可以，让我们看看如何返回默认2.7

```
·Linux，OS X: source activate snowflakes
·Windows：activate snowflakes
```

### 检查python版本：

确保snowflakes环境中仍然在运行你安装conda时安装的那个版本的python。

```
python --version
```

### 注销该环境

当你完成了在snowflakes环境中的工作室，注销掉该环境并转换你的路径到先前的状态：

```
·Linux，OS X：source deactivate
·Windows：deactivate
```

## 4. 管理包

现在让我们来演示包。我们已经安装了一些包（Astroid，Babel和一些特定版本的python），当我们创建一个新环境时。我们检查我们已经安装了那些包，检查哪些是可用的，寻找特定的包并安装它。接下来我们在Anconda.org仓库中查找并安装一些指定的包，用conda来完成更多pip可以实现的安装，并安装一个商业包。

### 查看该环境中包和其版本的列表：

使用这条命令来查看哪个版本的python或其他程序安装在了该环境中，或者确保某些包已经被安装了或被删除了。在你的终端窗口中输入：

```
conda list
```

### 使用conda命令查看可用包的列表

一个可用conda安装的包的列表，按照Python版本分类，可以从这个地址获得：
<http://docs.continuum.io/anaconda/pkg-docs.html>

### 查找一个包

首先让我们来检查我们需要的这个包是否可以通过conda来安装：

```
conda search beautifulsoup4
```

它展示了这个包，所以我们知道它是可用的。

### 安装一个新包

我们将在当前环境中安装这个Beautiful Soup包，使用conda命令如下；
conda install --name bunnies beautifulsoup4
**提示：**你必须告诉conda你要安装环境的名字（`-n bunies`）否则它将会被安装到当前环境中。
现在激活bunnies环境，并且用conda list来显示哪些程序被安装了。

```
·Linux，OS X：source activate bunnies
·Windows：activate bunnies
所有的平台：
conda list
```

### 从Anaconda.org安装一个包

如果一个包不能使用conda安装，我们接下来将在Anaconda.org网站查找。Anaconda.org向公开和私有包仓库提供包管理服务。Anaconda.org是一个连续分析产品。
**提示：**你在Anaconda.org下载东西的时候不强制要求注册。
为了从Anaconda.org下载到当前的环境中，我们需要通过指定Anaconda.org为一个特定通道，通过输入这个包的完整路径来实现。
在浏览器中，去 [http://anaconda.org](http://anaconda.org/) 网站。我们查找一个叫“bottleneck”的包，所以在左上角的叫“Search Anaconda Cloud”搜索框中输入“bottleneck”并点击search按钮。
Anaconda.org上会有超过一打的bottleneck包的版本可用，但是我们想要那个被下载最频繁的版本。所以你可以通过下载量来排序，通过点击Download栏。
点击包的名字来选择最常被下载的包。它会链接到Anaconda.org详情页显示下载的具体命令：

```
conda install --channel https：//conda .anaconda.ort/pandas bottleneck
```

### 检查被下载的包

```
conda list
```

### 通过pip命令来安装包

对于那些无法通过conda安装或者从Anaconda.org获得的包，我们通常可以用pip（“pip install packages”的简称）来安装包。
**提示：** pip只是一个包管理器，所以它不能为你管理环境。pip甚至不能升级python，因为它不像conda一样把python当做包来处理。但是它可以安装一些conda安装不了的包，和vice versa（此处不会翻译）。pip和conda都集成在Anaconda或miniconda里边。

我们激活我们想放置程序的环境，然后通过pip安装一个叫“See”的程序。

```
·Linux，OS X： source activate bunnies
·Windows：activate bunnies
所有平台：
pip install see
```

### 检查pip安装

检查See是否被安装：

```
conda list
```

### 安装商业包

安装商业包与你安装其他的包的过程异常。举个例子，让我们安装并删除一个更新的商业包的免费试用 IOPro，可以加速你的python处理速度：

```
conda install iopro
```

**提示：**除了学术使用，该版本在30天后试用期满

你现在可以安装以及检查你想用conda安装的任何包，无论使用conda命令、从Anaconda.org下载或者使用pip安装，无论开源软件还是商业包。

## 5. 移除包、环境、或者conda

如果你愿意的话。让我们通过移除一个或多个试验包、环境以及conda来结束这次测试指导。

### 移除包

假设你决定不再使用商业包IOPro。你可以在bunnies环境中移除它。

```
conda remove -n bunnies iopro
```

### 确认包已经被移除

使用conda list命令来确认IOPro已经被移除了

```
conda list
```

### 移除环境

我们不再需要snakes环境了，所以输入以下命令：
conda remove -n snakes --all

### 确认环境被移除

为了确认snakes环境已经被移除了，输入以下命令：

```
 conda info --envis
```

snakes不再显示在环境列表里了，所以我们知道它已经被删除了

### 删除conda

- Linux，OS X：
  移除Anaconda 或 Miniconda 安装文件夹

```
rm -rf ~/miniconda OR  rm -rf ~/anaconda
```

- Windows：
  去控制面板，点击“添加或删除程序”，选择“Python2.7（Anaconda）”或“Python2.7（Miniconda）”并点击删除程序。