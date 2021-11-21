# Typora upload script

yeah it is 20:28 now,	i have just deleted the .md file before push it as a mistake... Fuck

So i have to rewrite it



**Note that this script is just upload your picture to *Gitee*, i haven't complete a version for *Github* as the fucking examing week is coming :(**

## Usage

At first you should clone the repo to local.

And suppose that you have a py ENV

( if you dont,...👴👴

### Get Gitee Token

we need to create a repo to sotre the pictures and its name can be `images`

And then we need to generate a `token`

click you account icon and select settings

![image-20211121203349034](https://gitee.com/salt3dfish/images/raw/master/typora/21-11-21/52063302a9a2185ae88919a4e662708c.png)

and then select this ![image-20211121203412088](https://gitee.com/salt3dfish/images/raw/master/typora/21-11-21/7b1cf46d739a837172a80fe104b30e5f.png)

![image-20211121203458409](https://gitee.com/salt3dfish/images/raw/master/typora/21-11-21/4392caecc3bb0cddaadc3a7a804c36a7.png)

plz save this token if you don't want to regenerate it later 💩💩

So we now have a repo called `images` to store the pictures and a `token` to authenticate

### Configure upload.py

Since you have clone the script file to local, let's configure it for yourself

We need to change 3 essential places:

![image-20211121203950382](https://gitee.com/salt3dfish/images/raw/master/typora/21-11-21/8427c1cca57ae42b0d1cee1ffdf192b8.png)

1. owner---	it is you username like `pig` or sth other
2. repo--- where you want to store you pictures,for exp he repo `images` we just created
3. token--- we just generate it. if you have lost it ,you have to regenerate it my hommie :)💩💩

we can also change the picture's path by reset `path`,you can try it yourself

Now we just need to configure Typora to execute the script

### Configure Typora

Open settings

![image-20211121204544933](https://gitee.com/salt3dfish/images/raw/master/typora/21-11-21/2d0712cca3a0fa16baf07bb98d46357f.png)and then ![image-20211121204627388](C:\Users\JB304\AppData\Roaming\Typora\typora-user-images\image-20211121204627388.png)

we need to change 2 things:

1. select upload picture (in Chinese is `上传图片`),it makes typora upload pictures automatically and replace the picture's url
2. change command(`命令`),  the command is like this:

```bash
"python" "D:\scripts\typora-upload-sript\upload.py"
```

yeah it means execute`python D:\scripts\typora-upload-sript\upload.py pic1.jpg pic2.jpg`

typora will invoke this command whenever you copy a picture into a .md file,and the script should upload the picture to Server and return the `url` where the picture stored

And Typora will automatically replace `local url` like `c:\users\hommie\appdata\typora\...\pictures\pic1.jpg` by the url returned like `https://www.gitee.com/username/repo/blob/master/path`

All of this are completed by the script and typora

you just need to copy the script dir here ![image-20211121205708553](https://gitee.com/salt3dfish/images/raw/master/typora/21-11-21/c05401955ce9a15463284eb5ada52455.png)

the second params is where you clone the repo into,like `d:\scripts\typora-upload-script\`,and add`upload.py` to its tail, so it will look like this	`d:\scripts\typora-upload-script\upload.py`






😎😎, it seems that we have completed,we can also check if the script effects

![image-20211121210129168](https://gitee.com/salt3dfish/images/raw/master/typora/21-11-21/5bf731826715c5dbc829860d1c440a5c.png)

![image-20211121210328909](https://gitee.com/salt3dfish/images/raw/master/typora/21-11-21/52894c30f024d71cd0ca28c1bd4a2f30.png)

Success!🌞🌞🌞

What about staring it my hommie :)💋💋





## 中文教程

家人们现在是21:04我明天还要上狗都不想上的大物实验课，中文版改日再写把，fuck该死的考试周