#  图片上传到piclist图床，并实现分类
> 图床上传全部基于第一个开始复制创建的，如图
>
![image-20241227222531510](https://github.xiangfeng.us.kg/tuchang/main/typora/README/image-20241227222531510.png)

## 目前实现内容

+ 功能
  - [x] 从 Typora上传并在piclist图床中创建相应目录结构并放置图片
  - [x] 根据选择的级别是多少，就在选择的图床中相应的目录结构
  - [x] 上传图片的分类，便于查找，主要还是这个
+ 缺点
  - [ ] 目前只在windows平台测试，并打包，别的平台请自行测试

前提，无论是否使用Typora都要把PicGO-server打开，不然无法使用

<img src="https://github.xiangfeng.us.kg/tuchang/main/typora/README/image-20241227215154830.png" alt="image-20241227215154830" style="zoom: 50%;" />

### 1.1 使用python
下载python3.11，然后下载脚本，运行即可
```
pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple

## 后面参数请看脚本参数解释或者 python main.py -h 或 --help查看
需要定义参数先加
python .\main.py --key 123456 "C:\Users\Administrator\Desktop\blog\xiangju_blog\source\_posts\python\can.md" "C:\Users\Administrator\Downloads\【哲风壁纸】02-粉色.png"
```
### 1.2 打包程序配合typora使用

> 在typora偏好设置——》图形——》上传服务设定——》自定义命令即可,要按照下面格式进行改

 ```bash
#这个是默认
"C:\sofeware\main.exe" "${filepath}" 

"C:\sofeware\main.exe" --key 123456 ----piclist_url http://10.4.55.10:36677 "${filepath}"
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
如果还是不明白，请运行示例.py
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

