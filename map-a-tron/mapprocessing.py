import cv2
import numpy as np  
loop = 320
h = 40
s = 0
v = 0
thres = 0 
blur = 1
ken = 1
loopdonev = False
loopdones = False
loopdoneh = False
bestdiff = 1
besth = 0
bests = 0
bestv = 0
vals = [1, 63.75, 127.5, 191.25, 255]

uph = 55
ups = 115
upv = 163

kernel1 = np.array([[0, 0, 0],
                        [0, 1, 0],
                        [0, 0, 0]], np.uint8)
kernel2 = np.array([[1, 1, 1],
                        [1, 0, 1],
                        [1, 1, 1]], np.uint8)

img = cv2.imread('output2.jpg', cv2.IMREAD_UNCHANGED)
testimg = cv2.imread('testimg2.png', cv2.IMREAD_GRAYSCALE) 
_, testimg = cv2.threshold(testimg, 180, 255, cv2.THRESH_BINARY_INV)  

# # img = cv2.resize(img, (455, 228))
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def difcalc(img1, img2):
    global h
    global s
    global v
    global bestdiff
    global besth
    global bests
    global bestv

    img1 = cv2.resize(img1, (911, 457))
    img2 = cv2.resize(img2, (911, 457))
    if img1.shape == img2.shape:
        diff = cv2.absdiff(img1, img2)
        diffsum = np.sum(diff > 0)/(911*457)
        print("diffsum:", diffsum)
        print("Best diff:", bestdiff)
        if diffsum < bestdiff:
            besth = h
            bests = s
            bestv = v
            bestdiff = diffsum
        print(diffsum)
        return diffsum
    else: 
        print("imgase not same")
        print(img1.shape)
        print(img2.shape)
        pass


    
def on_changeh(val):
    pass

def on_changes(val):
    pass

def on_changev(val):
    pass

def on_changethesh(val):
    pass

def on_changeblur(val):
    pass

def on_changeken(val):
    pass

def rivers(thresimg, img):
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([123, 55, 55])
    upper_blue = np.array([179, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    result = cv2.bitwise_and(thresimg, thresimg, mask=mask)
    return result


def calcs():
    global h
    global bestdiff
    global besth
    global bests
    global bestv

    if h < 180:
        for i in vals:
            for t in vals:
                
                lower_blue = np.array([h, i, t], dtype=np.uint8)
                upper_blue = np.array([180, 255, 255], dtype=np.uint8)
                mask = cv2.inRange(hsv, lower_blue, upper_blue)
                result = cv2.bitwise_and(img, img, mask=mask)
                
                print("h is", h)
                print("s is", i)
                print("v is", t)
                diff = difcalc(testimg, mask)
                if (diff < bestdiff):
                    besth = h
                    bests = i
                    bestv = t
                    bestdiff = diff
                    print("new best")
                    print(bestdiff)
    else:
        print("loop done")
        print(bestdiff, besth, bests, bestv)
    h += 1

def noDots(inputimg):
    input_image = cv2.threshold(inputimg, 254, 255, cv2.THRESH_BINARY)[1]
    input_image_comp = cv2.bitwise_not(inputimg)  # could just use 255-img

    kernel1 = np.array([[0, 0, 0],
                        [0, 1, 0],
                        [0, 0, 0]], np.uint8)
    kernel2 = np.array([[1, 1, 1],
                        [1, 0, 1],
                        [1, 1, 1]], np.uint8)

    hitormiss1 = cv2.morphologyEx(input_image, cv2.MORPH_ERODE, kernel1)
    hitormiss2 = cv2.morphologyEx(input_image_comp, cv2.MORPH_ERODE, kernel2)
    hitormiss = cv2.bitwise_and(hitormiss1, hitormiss2)
    hitormiss_comp = cv2.bitwise_not(hitormiss)
    

    del_isolated = cv2.bitwise_and(inputimg, inputimg, mask=hitormiss_comp)
    return (del_isolated, input_image_comp)



windowName = 'output'
cv2.namedWindow(windowName, cv2.WINDOW_GUI_NORMAL)
cv2.namedWindow('Blue Mask')
cv2.namedWindow('Blue Filtered Result')

cv2.createTrackbar('uph', windowName, 0, 179, on_changeh)
cv2.createTrackbar('ups', windowName, 0, 255, on_changes)
cv2.createTrackbar('upv', windowName, 0, 255, on_changev)
cv2.createTrackbar('thres', windowName, 0, 255, on_changethesh)
cv2.createTrackbar('lowh', windowName, 0, 179, on_changeblur)
cv2.createTrackbar('lows', windowName, 0, 255, on_changeken)
cv2.createTrackbar('lowv', windowName, 0, 255, on_changeken)

while True: 
    
    img = cv2.imread('output2.jpg', cv2.IMREAD_UNCHANGED)
    
    
    # img = cv2.resize(img, (455, 228))

# for i in range(179):
#     h += 1
#     print(h)
#     for t in range(255):
#         s += 1
#         if s > 255:
#             s = 0 
#         print(s)
#         for g in range(255):
#             v += 1
#             if v > 255:
#                 v = 0
#             lower_blue = np.array([h, s, v])
#             upper_blue = np.array([180, 255, 255])
#             mask = cv2.inRange(hsv, lower_blue, upper_blue)
#             result = cv2.bitwise_and(img, img, mask=mask)
#             print(h)
#             print(s)
#             print(v)


    print(img.shape)

# show each channel individually
    B, G, R = cv2.split(img)
    
    uph = cv2.getTrackbarPos('uph', windowName)
    ups = cv2.getTrackbarPos('ups', windowName)
    upv = cv2.getTrackbarPos('upv', windowName)
    thres = cv2.getTrackbarPos('thres', windowName)
    lowh = cv2.getTrackbarPos('lowh', windowName)
    lows = cv2.getTrackbarPos('lows', windowName)
    lowv = cv2.getTrackbarPos('lowv', windowName)
    # if blur % 2 == 0:
    #     blur += 1
    # if blur == 0:
    #     blur = 1
    
    # if ken % 2 == 0:
    #     ken += 1
    # if ken == 0:
    #     ken = 1
    kernal = np.array(([[1,1,1],
    [1, 0, 1],
    [1, 1, 1]]), np.uint8)

    gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresimg = cv2.threshold(gimg, thres, 255, cv2.THRESH_BINARY_INV)
    z = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
    RBmerge = cv2.merge([B, z ,R])
    RGmerge = cv2.merge([z, G, R])
    BGmerge = cv2.merge([B, G, z])


    
    # B = cv2.merge([B, z, z])
    # G = cv2.merge([z, G, z])
    # R = cv2.merge([z, z, R])
    
    
    gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    

    
    _, thresimg = cv2.threshold(gimg, thres, 255, cv2.THRESH_BINARY_INV)
# code>
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lower_blue = np.array([lowh, lows, lowv])
    upper_blue = np.array([uph, ups, upv])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    result = cv2.bitwise_and(img, img, mask=mask)
    erroedres = cv2.erode(result, (kernal), iterations = 1)
    resultgray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    _, binresult = cv2.threshold(resultgray, thres, 255, cv2.THRESH_BINARY)

    

    # input_image = cv2.threshold(binresult, 254, 255, cv2.THRESH_BINARY)[1]
    # input_image_comp = cv2.bitwise_not(binresult)  # could just use 255-img

    # kernel1 = np.array([[0, 0, 0],
    #                     [0, 1, 0],
    #                     [0, 0, 0]], np.uint8)
    # kernel2 = np.array([[1, 1, 1],
    #                     [1, 0, 1],
    #                     [1, 1, 1]], np.uint8)

    # hitormiss1 = cv2.morphologyEx(input_image, cv2.MORPH_ERODE, kernel1)
    # hitormiss2 = cv2.morphologyEx(input_image_comp, cv2.MORPH_ERODE, kernel2)
    # hitormiss = cv2.bitwise_and(hitormiss1, hitormiss2)
    # hitormiss_comp = cv2.bitwise_not(hitormiss)
    # del_isolated = cv2.bitwise_and(binresult, binresult, mask=hitormiss_comp)

#code^
    ditatedmask = cv2.dilate(result, (kernal), iterations = 1)
    errode_dilate = cv2.dilate(erroedres, (kernal), iterations = 1)
    dilate_erroed = cv2.erode(ditatedmask, (kernal), iterations = 1)
    opening = cv2.morphologyEx(thresimg, cv2.MORPH_OPEN, kernal)

    bgr_result = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)
    gray_result = cv2.cvtColor(bgr_result, cv2.COLOR_BGR2GRAY)
    # thresimg, resout = noDots(thresimg)
    results, resout = noDots(mask)
    processed_resultblur = cv2.medianBlur(gray_result, (5))
    
    _, processed_resultblurthres = cv2.threshold(processed_resultblur, thres, 255, cv2.THRESH_BINARY_INV)
    _, processed_resultthres = cv2.threshold(result, thres, 255, cv2.THRESH_BINARY_INV)
    diff = difcalc(testimg, processed_resultblurthres)
    print(mask.shape)
    print(processed_resultblurthres.shape)
    
    _, threshmask = cv2.threshold(mask, thres, 255, cv2.THRESH_BINARY_INV)
    final = cv2.bitwise_and(threshmask, processed_resultblurthres, dst=None)
    # result = rivers(thresimg, img)


    
    

    # rivercontours, hierarchy = cv2.findContours(result, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # contoursimg = np.zeros((result.shape[0], result.shape[1]), dtype = np.uint8)
    # cv2.drawContours(contoursimg, rivercontours, -1, (0,255,0), 1)
    # for c in range(len(rivercontours)):
    #     M = cv2.moments(rivercontours[c])
    #     if M["m00"] != 0:
    #       cX = int(M["m10"]/ M["m00"])
    #       cY = int(M["m01"]/ M["m00"])
    #       cv2.putText(contoursimg, str(c) , (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
      
        

    # calcs()

    
    cv2.moveWindow('output', 1, 1)
    # cv2.moveWindow('Blue Mask', 0, 225)
    cv2.moveWindow('Blue Filtered Result', 0, 500)
    

    
    
    cv2.imshow('Blue Mask', mask)
    cv2.imshow('result out ', resout)
    cv2.imshow('Blue Filtered Result', results)
    cv2.imshow("output", img)
    # cv2.imshow("hit or miss", hitormiss)
    cv2.imshow("final", final)
    cv2.imshow("threshmask", threshmask)
    # cv2.imshow("Green", G)
    # cv2.imshow("Blue", B)
    # cv2.imshow("red", R)
    cv2.imshow("thresimg", thresimg)
    cv2.imshow("blur", processed_resultblur)
    cv2.imshow("blur thres", processed_resultblurthres)
    cv2.imshow("result thres", processed_resultthres)
    cv2.imshow("dilated", ditatedmask)
    cv2.imshow("erroded", erroedres)
    cv2.imshow("erroed then dillated", errode_dilate)
    cv2.imshow("dilated then erroded", dilate_erroed)
    
    # cv2.imshow("diff", diff)
    cv2.imshow("test", testimg)
    cv2.imshow("opening", opening)
    # cv2.imshow("contours", contoursimg)
    # cv2.imshow("RB", RBmerge)
    # cv2.imshow("RG", RGmerge)
    # cv2.imshow("BG", BGmerge)

    
    

    # if loopdonev == True:
    #     v = 0
    #     s += 1
    #     loopdonev = False
    # elif v == 255:
    #     loopdonev = True
    # else:
    #     v += 1


    # if loopdones == True:
    #     s = 0
    #     loopdones = False
    #     h += 1
    # elif s == 255:
    #     loopdones = True
    

    # if h > 180:
    #     loopdoneh = True

    # if loopdoneh == False:
    #     lower_blue = np.array([h, s, v])
    #     upper_blue = np.array([180, 255, 255])
    #     mask = cv2.inRange(hsv, lower_blue, upper_blue)
    #     result = cv2.bitwise_and(img, img, mask=mask)
    #     print(h)
    #     print(s)
    #     print(v)
    #     diff = difcalc(testimg, mask)
    #     if (diff < bestdiff).any:
    #         besth = h
    #         bests = s
    #         bestv = v
    #         bestdiff = diff

    # else:
    #     print("loop done")
    #     print(bestdiff, besth, bests, bestv)



    


        

        

    
    key = cv2.waitKey(1)
    if key == 27:
        print("Best vals:", bestdiff, besth, bests, bestv)
        break
cv2.destroyAllWindows()

