
# 目录



# 1 混乱的Python库

你有没有遇到过这样的问题

>  
 在项目A中需要用到某个Python库`PkgA`，且项目A的其他库要求`PkgA`的版本必须为`v3.0`以上，你按要求安装了`PkgA v3.0`；过了一段时间，老板交给你一个项目B，又用到了`PkgA`，但这次其他库要求`PkgA`的版本必须为`v2.0`及以上，这时候你怎么办？  安装`PkgA v3.0`则新项目B无法运行，安装`PkgA v2.0`则旧项目A无法运行，要想同时在一个环境里使用两个项目，必须不停地重装`PkgA`来更换版本。 


上面的例子只涉及两个项目的一个依赖库冲突，如果多个项目呢？如果多个依赖冲突呢？

<img src="https://img-blog.csdnimg.cn/46bcedb130f14b69bc9e522ea7f1d53c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATXIuV2ludGVyYA==,size_19,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> 上面的例子说明了什么呢？其实就是Python语言的痛点：
-  <font color="#f00">**依赖网复杂**</font> Python的包非常丰富，轮子相当多，开发者在工作时难免会调用这样或那样的包，久而久之，一个功能依赖另一个功能，形成复杂的依赖网络 -  <font color="#f00">**包管理混乱**</font> 通过报错信息不断安装依赖包终于解决了依赖库的问题，但随之而来的就是版本问题，也就是上面例子所体现的依赖冲突，本质上是某个包开发时的不向下兼容导致的 
为了解决上面的问题，更好地管理Python库，让其扬长避短，就必须使用环境管理工具，例如本文介绍的`Anaconda`。

# 2 什么是Anaconda？

>  
 `Anaconda`是一个开源的跨平台Python发行版本，支持 
 - Windows- macOS- Linux 
 操作系统。`Anaconda`中包含了`conda`等180多个科学包及其依赖项。其中`conda`则是一个开源的软件包管理系统和环境管理系统，用于安装多个版本的软件包及其依赖关系，并在它们之间轻松切换。 


<img src="https://img-blog.csdnimg.cn/22df3957a898473888ef7030700af7d8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATXIuV2ludGVyYA==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

# 3 Anaconda的安装

进入选择相应的操作系统，本文主要介绍在Windows与Linux下的安装流程。

<img src="https://img-blog.csdnimg.cn/71f3eb00d321468b943db7c4e8f62f5d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATXIuV2ludGVyYA==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

## 3.1 Windows系统

Windows有图形化的安装向导，按下面的步骤一步步安装即可
- 运行安装向导
<img src="https://img-blog.csdnimg.cn/5516b485e8244e2ab03f4c52a36da262.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATXIuV2ludGVyYA==,size_18,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述" height="260">
- 选择`I Agree`
<img src="https://img-blog.csdnimg.cn/f83b41394e4b44b58061284f63512c74.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATXIuV2ludGVyYA==,size_18,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述" height="260">
- 选择`All Users`，其实选`Just Me`也可以，但这台主机的其他用户就无法使用`Anaconda`了
<img src="https://img-blog.csdnimg.cn/4b36004d8b6443b2a8eadaa453b445b7.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATXIuV2ludGVyYA==,size_18,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述" height="260">
- 选择安装路径
<img src="https://img-blog.csdnimg.cn/3dbc2ee138074d40801d7dabfa5ae454.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATXIuV2ludGVyYA==,size_18,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述" height="260">
- 保持默认选项
<img src="https://img-blog.csdnimg.cn/0beca8b822a945a6b0f5a3b02591f8cb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATXIuV2ludGVyYA==,size_18,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述" height="260">
- 等待安装结束
<img src="https://img-blog.csdnimg.cn/cec84410a54f4d7ba074eb8cea8bcaee.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATXIuV2ludGVyYA==,size_18,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述" height="260">
- 配置环境变量 依次点击`我的电脑`-&gt;右键`属性`-&gt;点击`高级系统设置`-&gt;点击`环境变量`，之后按下图所示配置用户变量
<img src="https://img-blog.csdnimg.cn/2a05e7d6fd714588b33d9749a566f11f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATXIuV2ludGVyYA==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

## 3.2 Linux系统

对于Linux系统，没有图形化的安装界面，按下面输入终端命令即可
<li>进入Anaconda安装目录并运行官方安装程序<pre><code class="prism language-shell">bash ./Anaconda3-2021.11-Linux-x86_64.sh
</code></pre> </li><li>添加环境变量，其中`~/Project/anaconda3/bin`替换成自己的安装目录<pre><code class="prism language-shell">echo 'export PATH="~/Project/anaconda3/bin:$PATH"' &gt;&gt; ~/.bashrc
source ~/.bashrc
</code></pre> </li>
## 3.3 测试

打开`cmd`(Windows)或`Terminal`(Linux)，输入

```
conda --version

```

如果输出版本号则说明安装成功，如下所示。

<img src="https://img-blog.csdnimg.cn/01160b84f99f4a86b2accad978ba4766.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATXIuV2ludGVyYA==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> 注意，若运行python脚本时仍然是原环境而非`Anaconda`环境，则需要注意配置编辑器的python解释器路径。VSCode中，在`tasks.json`中的`args`参数中配置

```
{<!-- -->
    "version": "2.0.0",
    "tasks": [
        {<!-- -->
            "label": "catkin_make:debug",
            "type": "shell",
            "command": "catkin_make",
            "args": ["-DPYTHON_EXECUTABLE=/home/winter/Project/anaconda3/envs/server/bin/python "],
            "group": {<!-- -->"kind":"build","isDefault":true},
            "presentation": {<!-- -->
                "reveal": "always"
            },
            "problemMatcher": "$msCompile"
        }
    ]
}

```

# 4 虚拟环境管理(速查字典)

用`Anaconda`可以创建虚拟环境，虚拟环境间彼此隔离，可以解决依赖混乱的情况。虚拟环境管理主要涉及以下的命令，可以作为速查字典以备不时之需
<li> <font color="#4a86e8">**创建虚拟环境**</font> <pre><code class="prism language-shell">conda create -n test python=3.8
</code></pre> 创建了一个名为`test`的采用3.8版本Python解释器的虚拟环境 </li><li> <font color="#4a86e8">**切换虚拟环境**</font> <pre><code class="prism language-shell">conda activate test
</code></pre> 切换到名为`test`的虚拟环境。默认地，用户会进入`Anaconda`自带的`base`环境，注意`base`环境已经与安装`Anaconda`前的环境不同，因此第一次使用`Anaconda`可能会产生依赖冲突和缺失。 </li><li> <font color="#4a86e8">**查看虚拟环境**</font> <pre><code class="prism language-shell">conda env list
</code></pre> </li><li> <font color="#4a86e8">**依赖安装与卸载**</font> <pre><code class="prism language-shell"># 安装
conda install pkg
pip install pkg
# 卸载
conda remove pkg
pip uninstall pkg
</code></pre> 这里推荐使用清华源加快安装速度，使用方法是 <pre><code class="prism language-shell">pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pkg==version 
</code></pre> 即安装了名为`pkg`，版本为`version`的包 如果依赖很多，建议使用`requirements.txt`批量配置，命令为 <pre><code class="prism language-shell">pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
</code></pre> </li><li> <font color="#4a86e8">**查看环境依赖**</font> <pre><code class="prism language-shell">conda list
</code></pre> </li><li> <font color="#4a86e8">**复制虚拟环境**</font> <pre><code class="prism language-shell">conda env export &gt; test_env.yaml
conda env create -f test_env.yaml
</code></pre> 常用于导出当前虚拟环境的信息或复制虚拟环境 </li><li> <font color="#4a86e8">**删除虚拟环境**</font> <pre><code class="prism language-shell">conda remove -n test --all
</code></pre> 删除名为`test`的虚拟环境 </li>
