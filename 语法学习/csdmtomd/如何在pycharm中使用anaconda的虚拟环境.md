#./weixin_43486940/如何在pycharm中使用anaconda的虚拟环境
最近项目中有许多同学咨询如何在pycharm中使用anaconda的虚拟环境（envs），这里就给大家简单介绍一下。
- 首先我们需要安装anaconda，这里就不在追述了，网上安装教程非常多。anaconda的安装路径大家需要记着因为后面会使用到。
>  
 博主这里将anaconda安装到了D盘对应目录下：D:\Work\BigData\Anaconda3 


<img src="https://img-blog.csdnimg.cn/6c950950b0e747909147e2cee923bb4e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aSn6Zu-55qE5bCP5bGL,size_20,color_FFFFFF,t_70,g_se,x_16" alt="Anaconda安装目录">
- 第二步我们打开Anaconda Powershell Prompt (Anaconda3)，创建虚拟环境。这个应用可以在安装成功Anaconda后在**开始菜单**中找到，如下：
<img src="https://img-blog.csdnimg.cn/ecee08ee8a0641caaa171a203a67b8b6.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aSn6Zu-55qE5bCP5bGL,size_20,color_FFFFFF,t_70,g_se,x_16" alt="Anaconda Powershell Prompt (Anaconda3)">
- 我们打开shell，使用如下命令创建一个虚拟环境（env）：
```
conda create -n ai_clone python=3.6

```

如下： <img src="https://img-blog.csdnimg.cn/68e122cc9c1f4704b78fdc5e5876fbec.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aSn6Zu-55qE5bCP5bGL,size_20,color_FFFFFF,t_70,g_se,x_16" alt="安装anaconda虚拟环境">
- 其中：ai_clone为本次创建的虚拟机的名称，3.6为创建的python虚拟机的版本。创建完成后，在Anaconda的安装目录的envs文件夹下，会生成刚刚创建的虚拟机名称的文件夹，如下： <img src="https://img-blog.csdnimg.cn/9b60cbe56c8e49ab85744d9774b4a7e0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aSn6Zu-55qE5bCP5bGL,size_20,color_FFFFFF,t_70,g_se,x_16" alt="Anaconda的安装目录的envs文件夹"><li>最后我们打开pycharm，选择上述截图文件夹下的编译文件，即可使用anaconda的虚拟环境，如下： 
  <ul>- 第一步、选择设置： <img src="https://img-blog.csdnimg.cn/7a208c0787d649348eb286392b8a4f03.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aSn6Zu-55qE5bCP5bGL,size_20,color_FFFFFF,t_70,g_se,x_16" alt="选择设置">- 第二步、选择新增python解释器： <img src="https://img-blog.csdnimg.cn/6bdbe11fa5e34afea643e3b583ec8145.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aSn6Zu-55qE5bCP5bGL,size_20,color_FFFFFF,t_70,g_se,x_16" alt="新增python解释器">- 第三步、选择添加： <img src="https://img-blog.csdnimg.cn/fb75234fa0944fecadf4fdaf087ed89a.png" alt="选择添加">- 第四步、手动选择解释器： <img src="https://img-blog.csdnimg.cn/53f755575c9f4f22931a9aeeb9be5351.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aSn6Zu-55qE5bCP5bGL,size_20,color_FFFFFF,t_70,g_se,x_16" alt="手动选择解释器">- 最后、找到之前安装的虚拟环境的位置，并选择对应的python.exe文件： <img src="https://img-blog.csdnimg.cn/cdcf4ba01a7440e0ba08e1b799daa902.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aSn6Zu-55qE5bCP5bGL,size_19,color_FFFFFF,t_70,g_se,x_16" alt="找到之前安装的虚拟环境的位置，并选择对应的python.exe文件">
最后博主最新上传了最近项目中涉及的代码，如果感兴趣的同学可以看看：
- 第九章：- 第八章：- 第七章：