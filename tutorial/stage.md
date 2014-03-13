## Stage（舞台）

stage是可视对象的根，是顶级容器。使用Hilo创建和显示的元素都属于`可视对象`，他们都是stage的子级。

创建一个hilo应用一般都是从创建一个stage开始的。例如：

```
var stage = new Hilo.Stage({
    canvas: canvas, 
    width: 320, 
    height: 480
});
```

Stage构造函数接收一个参数`properties`，此参数可包含创建stage的多个属性。其中常用的重要属性有：

* **`canvas`** - 舞台所对应的画布（渲染区域）。如果canvas是一个`HTMLCanvasElement`，则会使用canvas渲染模式；如果是一个普通的`HTMLElement`，比如div，则会使用dom+css3渲染模式。
* **`width`** - 舞台的宽度。
* **`height`** - 舞台的高度。
* **`paused`** - 舞台是否暂停渲染。默认为false。

## 属性
	
* **`renderer`** - 舞台渲染器。只读。
* **`viewport`** - 舞台内容在页面中的渲染区域。包含的属性有：left、top、width、height。只读。## 方法

* **`enableDOMEvent(type, enable)`** - 开启/关闭舞台DOM事件。
* **`updateViewport()`** - 更新舞台在页面中的渲染区域。当舞台canvas的样式border、margin、padding等属性更改后，需要调用此方法更新舞台渲染区域。

## 舞台更新和渲染

舞台默认是不会更新和渲染的，需要一个计时器来调用stage的`tick`方法来触发更新和渲染。Hilo提供了一个计时器类`Ticker`。

使用示例：

```
var ticker = new Hilo.Ticker(60);
ticker.addTick(stage);
ticker.start();
```