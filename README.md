# pygame-practice
https://pythonprogramming.net/pygame-python-3-part-1-intro/

# 总结
* 在crash()函数里面，blit完文字以后必须要马上调用`pygame.display.update()`，不然`time.sleep(2)`以后再update这一帧就看不见了。实验证明：如果没有这个等待两秒的动作，是可以不用在这里马上update的，而是再主循环的结尾一起update。但是即使没有等待两秒也不能保证每次都看见，还不知道原因。
* crash()函数以后将变量进行调整，同时调用了`car(x,y)`。实验证明，其实在这里是多余的，去掉不影响结果。
