import cv2
import numpy as np
def measure_bar_fill(image,bbox,bar_type):
    h,w=image.shape[:2]
    x1,y1,x2,y2=map(int,bbox)
    x1=max(0,min(x1,w))
    x2=max(0,min(x2,w))
    y1=max(0,min(y1,h))
    y2=max(0,min(y2,h))
    if x2-x1<8 or y2-y1<3:
        return None
    roi=image[y1:y2,x1:x2]
    rh,rw=roi.shape[:2]
    if bar_type=="enemyhp":
        top=int(rh*0.30)
        bottom=int(rh*0.65)
        ranges=[((165,150,100),
                (179,255,255)),
                ((0,150,100),
                (5,255,255))]
    elif bar_type=="servanthp":
        top=int(rh*0.30)
        bottom=int(rh*0.70)
        ranges=[((90,100,100),
                (115,255,255))]
    elif bar_type=="servantnp":
        top=int(rh*0.44)
        bottom = int(rh*0.60)
        ranges=[((10,150,120),
                (30,255,255))]
    else:
        return None
    left=int(rw*0.10)
    right=int(rw*0.90)
    roi=roi[top:bottom,left:right]
    if roi.size==0:
        return None
    hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    mask=np.zeros(hsv.shape[:2],dtype=np.uint8)
    for lower,upper in ranges:
        mask|=cv2.inRange(hsv,np.array(lower,dtype=np.uint8),
                          np.array(upper,dtype=np.uint8))
    colored_fraction=np.mean(mask>0,axis=0)
    active_columns=colored_fraction>=0.30
    if not np.any(active_columns):
        return None
    ratio=np.count_nonzero(active_columns)/len(active_columns)
    return float(np.clip(ratio,0.0,1.0))