positions = {'x':[],'y':[],'shu_now':[]}
#positions = []
#shu = []

def setup():
    size(600, 600, P2D)
    global cat, a, a_now, img, ks_time, b, shuzi, kaishihua, you, bild1
    cat = load_image('cat.png')
    #a = 0
    b = 0#白色图层增加的透明度
    ks_time = 0#第一次左键按下后开始的时间
    a_now = 0
    img = create_image(20, 20, ARGB)
    shuzi = -1
    kaishihua = False
    you = True
    bild1 = load_image('1.jpg')

    
def draw():
    global cat, a, a_now, img, ks_time, b, shuzi, you, bild1
    #background('#FFFFFF')
    tint(253,253,253)
    image(cat,0,0,600,600)
    #tint(255, 255, 255, a_now)

    b = (millis() - ks_time)/1000
    if you:
        a_now = min(255, int(b))
        #print(a_now)
        
    if ks_time == 0:#画之前
        image(bild1, 0, 0, 600, 600)
        stroke_weight(3)
        text_size(20)
        fill('#000000')
        text('Linksklick zum Zeichnen', 20, 560)
        
    if you:#结束之前
        fill('#000000')
        text('Rechtsklick zum Beenden der Zeichnung', 20, 582)
        

    img.load_pixels()#调用白色图层每个像素
    if ks_time != 0:
        for i in range(400):
            img.pixels[i] = color(255, 255,255, a_now)
    img.update_pixels()#关闭
    
    image(img, 0,0, 600, 600)
    
    for i in range(len(positions['x'])):
        dianwei_x = positions['x'][i]
        dianwei_y = positions['y'][i]

        stroke('#000000')
        stroke_weight(5)
        point(dianwei_x, dianwei_y)
            
        dianshu = positions['shu_now'][i]
        fill('#000000')
        #stroke_weight(3)
        text_size(15)
        text(dianshu, dianwei_x, dianwei_y-5)
        
    
    if not you:
        for i in range(15):
            stroke('#347537')
            stroke_weight(5)
            daodan_x1 = random(30)+random(570)
            daodan_y1 = random(30)+random(570)
            point(int(daodan_x1), int(daodan_y1))
        for i in range(15):
            stroke('#FA6B2A')
            stroke_weight(5)
            daodan_x2 = random(30)+random(570)
            daodan_y2 = random(30)+random(570)
            point(int(daodan_x2), int(daodan_y2))
        for i in range(10):
            stroke('#1398DF')
            stroke_weight(5)
            daodan_x3 = random(30)+random(570)
            daodan_y3 = random(30)+random(570)
            point(int(daodan_x3), int(daodan_y3))
        no_loop()
    

    
def mouse_pressed():
    global ks_time, shuzi, kaishihua, you, a_now
    if mouse_button == LEFT:
        shuzi+=1
        if kaishihua:
            positions['x'].append(mouse_x)
            positions['y'].append(mouse_y)
            positions['shu_now'].append(shuzi)
        print(positions)
            #shu.append(shuzi)
            
        if ks_time == 0:
            kaishihua = True
            ks_time = millis()


        #shuzi += 1
        print(shuzi)
        
    elif mouse_button == RIGHT:
        you = False
        a_now = 255
        #no_loop()


    
#def key_pressed():
    #global a
    #if key == 'z':   # 如果按下 z 键
        #print('z')
        
        
        
run_sketch()