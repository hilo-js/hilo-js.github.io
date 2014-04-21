# 快速开始
---

## 下载安装

Hilo提供多种模块化范式的版本，您可以下载：

* [Standalone 独立版本](../../build/standalone/hilo-standalone.zip)
* [For Kissy 版本](../../build/kissy/hilo-kissy.zip)
* [For RequireJS 版本](../../build/requirejs/hilo-requirejs.zip)
* [For CommonJS 版本](../../build/cmd/hilo-cmd.zip)

此外，您也可以到GitLab上获取Hilo的所有源码：[http://gitlab.alibaba-inc.com/hilo/hilo](http://gitlab.alibaba-inc.com/hilo/hilo)

然后把Hilo类库引入到页面中：

    <script src="hilo-standalone.js"></script>

## 创建舞台

舞台Stage是一个各种图形、精灵动画等的总载体。所以可见的对象都要添加到舞台或其子容器后，才会被渲染出来。

```
var stage = new Hilo.Stage({
    canvas: canvas, 
    width: 320, 
    height: 480
});
```

Stage构造函数接收一个参数`properties`，此参数可包含创建stage的多个属性。其中常用的重要属性有：

## 创建定时器

舞台Stage上的物体的运动等变化，都是通过一个定时器Ticker不断地调用Stage.tick()方法来实现刷新的。

```
var ticker = new Hilo.Ticker(60);
ticker.addTick(stage);
ticker.start();
```

## 事件交互

要想舞台上的图形、精灵动画等对象能响应用户的点击、触碰等交互事件，就必需先为舞台开启DOM事件响应，然后就可以使用View.on()来响应事件。

```
stage.enableDOMEvent('mousedown', true);
sprite.on('mousedown', function(e){
    console.log(e.eventTarget, e.stageX, e.stageY);
});
```

## 初始化完成

至此，初始化工作基本完成。接下来，您就可以开始利用hilo提供的各种可视类来创建各种图形、精灵动画等。开始你的HTML5游戏之旅吧！