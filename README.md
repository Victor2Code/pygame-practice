# pygame-practice
https://pythonprogramming.net/pygame-python-3-part-1-intro/

# 总结
* 在crash()函数里面，blit完文字以后必须要马上调用`pygame.display.update()`，不然`time.sleep(2)`以后再update这一帧就看不见了。实验证明：如果没有这个等待两秒的动作，是可以不用在这里马上update的，而是再主循环的结尾一起update。但是即使没有等待两秒也不能保证每次都看见，还不知道原因。
* crash()函数以后将变量进行调整，同时调用了`car(x,y)`。实验证明，其实在这里是多余的，去掉不影响结果。
* 显示图形如果知道左上角坐标，就可以像`dodged()`函数那样直接定义font，render，然后blit即可；如果以别的方式定位，例如中点，就需要用`crash()`那样的方式去显示。除了center还可以用别的位置，例如midtop，去定位。
* 显示在高层的物体在代码里面靠后blit上去，例如先画障碍物，再画dodged数字。
* `pygame.PixalArray(surface)`返回一个list，长度为surface的宽，每个元素也是个list，长度是surface的高。每个pixal可以赋值一个RGB的tuple
