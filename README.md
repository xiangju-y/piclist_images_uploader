#  Typora 图片上传到piclist图床

> 图床上传全部基于第一个开始复制创建的，如图
>
![image-20241227222531510](https://github.xiangfeng.us.kg/tuchang/main/typora/README/image-20241227222531510.png)

## 1. 目前实现内容

+ 功能

  - [x] 实现从 Typora 图片上传并在piclist图床中按指定级别创建相应目录结构并放置图片
根据选择的级别是多少，就在选择的图床中建立相对应的文件

+ 缺点
  - [ ] 目前只在windows平台测试，并打包，别的平台请自行测试
  

声明，无论是否使用Typora都要把PicGO-server打开，不然无法使用

<img src="https://github.xiangfeng.us.kg/tuchang/main/typora/README/image-20241227215154830.png" alt="image-20241227215154830" style="zoom: 50%;" />

### 1.2配合typora使用

> 在typora偏好设置——》图形——》上传服务设定——》自定义命令即可

 ```bash
 "C:\sofeware\main.exe" "${filepath}"
 ```
"C:\sofeware\main.exe" 这个是打包好的exe防止路径，请改成自己放置的路径
<img src="https://github.xiangfeng.us.kg/tuchang/main/typora/README/image-20241227214320932.png" alt="image-20241227214320932" style="zoom:50%;" />

## 3.脚本参数解释

```bash
处理文件路径和相关信息
positional arguments:
  file_path             文件路径
  image_url             图片链接 (最后给出)
options:
  -h, --help            show this help message and exit
  --dir_data DIR_DATA   piclist,data.json目录位置 (可选)
  --piclist_url PICLIST_URL
                        piclist上传更新图片api(默认是http://127.0.0.1:36677)
  --dir_level DIR_LEVEL
                        图床的目录级别,默认是2 (可选)
  --uploader UPLOADER   选择图床(默认是github)
```
### 3.1 data.json目录位置

默认设置就是图中的前三个，如果不准，请自己定义

<img src="https://github.xiangfeng.us.kg/tuchang/main/typora/README/image-20241227215834342.png" alt="image-20241227215834342" style="zoom:50%;" />

### 3.2 图床的目录级别

可看下面示例,这个是决定图片放置图床中那个位置的

>  例如：文件路径为**C:\\Users\\Administrator\\Desktop\\blog\\xiangju_blog\\source\\_posts\\python\\da.md** ，

级别为2的情况下是 **python/da/**
```
第1级 da/
第2级 python/da/
第3级 _posts/python/da/
第4级 source/_posts/python/da/
第5级 xiangju_blog/source/_posts/python/da/
第6级 blog/xiangju_blog/source/_posts/python/da/
第7级 Desktop/blog/xiangju_blog/source/_posts/python/da/
第8级 Administrator/Desktop/blog/xiangju_blog/source/_posts/python/da/
第9级 Users/Administrator/Desktop/blog/xiangju_blog/source/_posts/python/da/
第10级 C:/Users/Administrator/Desktop/blog/xiangju_blog/source/_posts/python/da/
结果: python/da/
```

