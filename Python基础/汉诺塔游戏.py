#递归函数的应用

#汉诺塔游戏：汉诺塔。相传在佛教圣地的寺庙里，有一个黄铜台，上面有三根宝石柱，一根柱子上有大小不同的64片金片。一个僧侣在不停的移动金片，但是必须把小片放在大片上面。当所有金片都移动到另一根柱子上时，世界就会灭了

#假如有A、B、C三个铜柱，在A上依次从小到大放着圆盘，要求每次只能移动一个到B或者C上，但是必须保证从小到大的顺序（下面的圆盘比上边的大），
#问怎么移动这些圆盘

def move(n, a, b, c):
    if n == 1:
        print(a,'--->',c)
    else:
        move(n-1,a,c,b) # a-->b将最后一个参数写成b
        move(1,a,b,c)   #a-->c将最后一个参数写为c
        move(n-1,b,a,c)  #b-->c将第一个参数写成b
move(64, 'A', 'B', 'C')   