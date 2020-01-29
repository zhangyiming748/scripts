# Scripts
# 方法来源https://github.com/yeziyezi/scripts
对我来说相当于启蒙教育,我也不太懂GitHub上怎么新建分支申请融合,我就按照了代码提供的方法和思想自己制作了一个
- [x] 一开始我自己fork一份之后按照过滤图片的方式延伸了各种过滤器的方法,并且按照模块分开
- [x] 封装成类,init负责提供个人信息
- [x] 终端打印日志记录请求时间保存到log.md
- [x] 过滤掉相同🆔的文件,不过效果存疑,目前根据个人判断id的数据类型是无符号短整型,只能表示65536个id号,超出范围重新计算
- [x] 由于在不同平台切换的过程中经常要修改IDE自动生成的venv文件夹,而"聪明"的IDE会自动把依赖库安装到工程的第三方包文件夹,导致有时候一不小心就删掉了千方百计下载的依赖,所以一怒之下干脆把依赖直接放在代码里
- [x] 尽量合并代码冗余代码
- [x] 突然意识到我直接fork后在新生成的文件里填写了自己的telegram机器人信息可以被任何人访问,紧急下架
- [x] 本地基于Windows分支修改,单独文件负责传递个人信息
- [x] 同步更改UbuntuVersion和MacOSVersion
- [x] 重新fork原作者代码库,删去个人信息后重新上传代码
- [ ] 继续精简代码,合并获取时间的代码等

原文如下
>分别制作了
一些实用小脚本的集合，不定期更新～
>### 下载telegram频道中的图片
>- 链接：[download-telegram-channel-pictures.py](./download-telegram-channel-pictures.py)
>- 环境: python3
>- 依赖: Telethon,PySocks(如果需要通过代理连接到telegram的话)
>- 使用方法: 
>1. 在[my.telegram.org/apps](https://my.telegram.org/apps)拿到你的api-id以及api-hash
>2. 将一些变量替换成你需要的值
>3. 运行
>- 注意事项：首次运行脚本需要输入tg所绑定的手机号和验证码，然后telethon才能以你的身份登录去下载图片
>- 其他说明：[关于Telethon的文档在这里](https://telethon.readthedocs.io/en/latest/index.html)
>### 删除指定文件夹下的重复文件
>- 链接：[delete-duplicate-files.rb](./delete-duplicate-files.rb)
>- 环境：ruby2.6.2
>- 使用方法：将文件中“指定文件夹”替换为需要的值，然后```ruby delete-duplicate-files.rb```运行。
