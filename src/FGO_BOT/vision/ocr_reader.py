import cv2
import numpy as np
import re
import pytesseract
from pathlib import Path
path=Path(__file__).resolve().parent
pytesseract.pytesseract.tesseract_cmd=(path/"tools/Tesseract-OCR/tesseract.exe")
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
def read_servant_np(frame,bbox):
    height,width=frame.shape[:2]
    x1,y1,x2,y2=map(int,bbox)
    bar_width=x2-x1
    bar_height=y2-y1
    if bar_width<=0 or bar_height<=0:
        return None
    left=x1+int(bar_width*0.45)
    right=x2
    top=y1-int(bar_height*0.65)
    bottom=y1+int(bar_height*0.40)
    left=max(0,min(left,width))
    right=max(0,min(right,width))
    top=max(0,min(top,height))
    bottom=max(0,min(bottom,height))
    roi=frame[top:bottom,left:right]
    if roi.size==0:
        return None
    gray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    gray=cv2.resize(gray,None,fx=4,fy=4,interpolation=cv2.INTER_CUBIC)
    _, binary=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    binary=cv2.bitwise_not(binary)
    config=("--psm 7 ""-c tessedit_char_whitelist=0123456789%")
    text=pytesseract.image_to_string(binary,config=config).strip()
    match=re.fullmatch(r"(\d{1,3})\s*%",text)
    if match is None:
        return None
    value=int(match.group(1))
    if not 0<=value<=300:
        return None
    return value