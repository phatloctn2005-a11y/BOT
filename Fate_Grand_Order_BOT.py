from ultralytics import YOLO
import pyautogui
import cv2
import pygetwindow
import time
import numpy
import pytesseract
battle_=int(input("オートしたい回数："))
bluestacks=pygetwindow.getWindowsWithTitle("BlueStacks App Player")[0]
bluestacks.restore()
bluestacks.resizeTo(1280,720)
bluestacks.activate()
time.sleep(2)

blueStacks_left=bluestacks.left
blueStacks_top=bluestacks.top
blueStacks_width=bluestacks.width
blueStacks_height=bluestacks.height

pytesseract.pytesseract.tesseract_cmd=(r"C:\Program Files\Tesseract-OCR\tesseract.exe")
model=YOLO("D:/AI/design/Project/AI/YOLO_AI/FGO-ver8_Best.pt")
battle=0
while battle<=battle_:
     time.sleep(4)
     fgo_img=pyautogui.screenshot(region=(blueStacks_left,blueStacks_top,blueStacks_width,blueStacks_height))
     fgo_img=numpy.array(fgo_img)
     fgo_img=cv2.cvtColor(fgo_img,cv2.COLOR_RGB2BGR)
     results=model.predict(fgo_img)
     theenemyhasbeenchosenlist=[]
     enemyhplist=[]
     enemylist=[]
     for enemyhp in results[0].boxes:
         enemy_x1,enemy_y1,enemy_x2,enemy_y2=enemyhp.xyxy[0]
         enemy_x=float((enemy_x1+enemy_x2)/2)
         enemy_y=float((enemy_y1+enemy_y2)/2)
         cls=int(enemyhp.cls[0])
         if cls==0:
             enemylist.append((enemy_x,enemy_y))
         elif cls==28:
             theenemyhasbeenchosenlist.append((enemy_x,enemy_y))
         elif cls==1:
             enemyhp_img=fgo_img[int( enemy_y1):int( enemy_y2),int( enemy_x1):int( enemy_x2)]
             enemyhp_hsv=cv2.cvtColor(enemyhp_img,cv2.COLOR_BGR2HSV)
             enemyhp_lower_red=numpy.array([0,90,90])
             enemyhp_upper_red=numpy.array([20,255,255])
             enemyhp_mask=cv2.inRange(enemyhp_hsv,enemyhp_lower_red,enemyhp_upper_red)
             enemyhp_pixel=cv2.countNonZero(enemyhp_mask)
             enemyhplist.append((enemy_x,enemy_y,enemyhp_pixel))
     if len(enemylist)>=1 and len(theenemyhasbeenchosenlist)>=1 and len(enemyhplist)>=1:
         current_target=theenemyhasbeenchosenlist[0][0]
         enemyhp_select=min(enemyhplist,key=lambda x:x[2])
         enemy_select=min(enemylist,key=lambda x:abs(x[0]-enemyhp_select[0]))
         if abs(enemy_select[0]-current_target)>20:
             pyautogui.click(blueStacks_left+enemy_select[0],blueStacks_top+enemy_select[1])
             time.sleep(2)

     fgo_skill_img=pyautogui.screenshot(region=(blueStacks_left,blueStacks_top,blueStacks_width,blueStacks_height))
     fgo_skill_img=numpy.array(fgo_skill_img)
     fgo_skill_img=cv2.cvtColor(fgo_skill_img,cv2.COLOR_RGB2BGR)
     skill_results=model.predict(fgo_skill_img)
     skilllist=[]
     for skillselect in skill_results[0].boxes:
         skill_x1,skill_y1,skill_x2,skill_y2=skillselect.xyxy[0]
         skill_x=float((skill_x1+skill_x2)/2)
         skill_y=float((skill_y1+skill_y2)/2)
         cls=int(skillselect.cls[0])
         if cls==6:
             skilllist.append((skill_x,skill_y))
     for skillx,skilly in skilllist:
         pyautogui.click(blueStacks_left+skillx,blueStacks_top+skilly)
         time.sleep(3)
         fgo_select_img=pyautogui.screenshot(region=(blueStacks_left,blueStacks_top,blueStacks_width,blueStacks_height))
         fgo_select_img=numpy.array(fgo_select_img)
         fgo_select_img=cv2.cvtColor(fgo_select_img,cv2.COLOR_RGB2BGR)
         select_results=model.predict(fgo_select_img)
         for select in select_results[0].boxes:
             select_x1,select_y1,select_x2,select_y2=select.xyxy[0]
             select_x=float((select_x1+select_x2)/2)
             select_y=float((select_y1+select_y2)/2)
             cls=int(select.cls[0])
             if cls==15:
                 pyautogui.click(blueStacks_left+select_x,blueStacks_top+select_y)
                 time.sleep(4)

     for attack in results[0].boxes:
         attack_x1,attack_y1,attack_x2,attack_y2=attack.xyxy[0]
         attack_x=float((attack_x1+attack_x2)/2)
         attack_y=float((attack_y1+attack_y2)/2)
         cls=int(attack.cls[0])
         if cls==7:
             pyautogui.click(blueStacks_left+attack_x,blueStacks_top+attack_y)
             time.sleep(3)

     fgo_star_img=pyautogui.screenshot(region=(blueStacks_left,blueStacks_top,blueStacks_width,blueStacks_height))
     fgo_star_img=numpy.array(fgo_star_img)
     fgo_star_img=cv2.cvtColor(fgo_star_img,cv2.COLOR_RGB2BGR)
     star_results=model.predict(fgo_star_img)
     starlist=[]
     starlocationlist=[]
     for starselect in star_results[0].boxes:
         star_x1,star_y1,star_x2,star_y2=starselect.xyxy[0]
         star_x=float((star_x1+star_x2)/2)
         star_y=float((star_y1+star_y2)/2)
         cls=int(starselect.cls[0])
         if cls==13:
             star_img=fgo_star_img[int(star_y1):int(star_y2),int(star_x1):int(star_x2)]
             star_img=cv2.cvtColor(star_img,cv2.COLOR_BGR2RGB)
             star_gray=cv2.cvtColor(star_img,cv2.COLOR_RGB2GRAY)
             star_blur=cv2.GaussianBlur(star_gray,(3,3),0)
             star_img=cv2.resize(star_blur,None,fx=6,fy=6,interpolation=cv2.INTER_CUBIC)
             star_ret,star_thresh=cv2.threshold(star_img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
             star_config="--psm 7 -c tessedit_char_whitelist=0123456789"
             star_text=pytesseract.image_to_string(star_thresh,config=star_config).strip()
             star_text="".join(filter(str.isdigit,star_text))
             star_number=(int(star_text) if star_text else 0)
             if star_number>=10:
                 starlist.append((blueStacks_left+star_x,blueStacks_top+star_y,star_number))
                 starlocationlist.append((blueStacks_left+star_x,blueStacks_top+star_y))

     fgo_card_img=pyautogui.screenshot(region=(blueStacks_left,blueStacks_top,blueStacks_width,blueStacks_height))
     fgo_card_img=numpy.array(fgo_card_img)
     fgo_card_img=cv2.cvtColor(fgo_card_img,cv2.COLOR_RGB2BGR)
     card_results=model.predict(fgo_card_img)
     redcardlist=[]
     bluecardlist=[]
     greencardlist=[]
     for prioritizecard in card_results[0].boxes:
         prioritizecard_x1,prioritizecard_y1,prioritizecard_x2,prioritizecard_y2=prioritizecard.xyxy[0]
         prioritizecard_x=float((prioritizecard_x1+prioritizecard_x2)/2)
         prioritizecard_y=float((prioritizecard_y1+prioritizecard_y2)/2)
         cls=int(prioritizecard.cls[0])
         score=0
         if cls==9:
             score+=3
             if len(starlist)>=1:
                 nearest_star=min(starlist,key=lambda x:abs(x[0]-(blueStacks_left+prioritizecard_x)))
                 score+=nearest_star[2]/10
                 redcardlist.append((prioritizecard_x,prioritizecard_y,score))
             else:
                 redcardlist.append((prioritizecard_x,prioritizecard_y,score))
         elif cls==17:
             score+=50
             redcardlist.append((prioritizecard_x,prioritizecard_y,score))
         elif cls==10:
             score+=2
             if len(starlist)>=1:
                 nearest_star=min(starlist,key=lambda x:abs(x[0]-(blueStacks_left+prioritizecard_x)))
                 score+=nearest_star[2]/10
                 bluecardlist.append((prioritizecard_x,prioritizecard_y,score))
             else:
                 bluecardlist.append((prioritizecard_x,prioritizecard_y,score))
         elif cls ==18:
             score+=40
             bluecardlist.append((prioritizecard_x,prioritizecard_y,score))
         elif cls==11:
             score+=1
             if len(starlist)>=1:
                 nearest_star=min(starlist,key=lambda x:abs(x[0]-(blueStacks_left+prioritizecard_x)))
                 score+=nearest_star[2]/10
                 greencardlist.append((prioritizecard_x,prioritizecard_y,score))
             else:
                 greencardlist.append((prioritizecard_x,prioritizecard_y,score))
         elif cls==19:
             score+=30
             greencardlist.append((prioritizecard_x,prioritizecard_y,score))
     if len(redcardlist)>=3:
         for redcard in reversed(sorted(redcardlist,key=lambda x:x[2],reverse=True)[:3]):
             pyautogui.click(blueStacks_left+redcard[0],blueStacks_top+redcard[1])
             time.sleep(2)
     elif len(bluecardlist)>=3:
         for bluecard in reversed(sorted(bluecardlist,key=lambda x:x[2],reverse=True)[:3]):
             pyautogui.click(blueStacks_left+bluecard[0],blueStacks_top+bluecard[1])
             time.sleep(2)
     elif len(greencardlist)>=3:
         for greencard in reversed(sorted(greencardlist,key=lambda x:x[2],reverse=True)[0:3]):
             pyautogui.click(blueStacks_left+greencard[0],blueStacks_top+greencard[1])
             time.sleep(2)   
     else:
         cardlist=[]     
         for cardselect in card_results[0].boxes:
             card_x1,card_y1,card_x2,card_y2=cardselect.xyxy[0]
             card_x=float((card_x1+card_x2)/2)
             card_y=float((card_y1+card_y2)/2)
             cls=int(cardselect.cls[0])
             score=0
             if cls==17:
                 score+=50
             elif cls==18:
                 score+=40
             elif cls==19:
                 score+=30
             elif cls==9:
                 score+=3
             elif cls==10:
                 score+=2
             else:
                 score+=1
             if len(starlist)>=1:
                 nearest_star=min(starlist,key=lambda s:abs(s[0]-(blueStacks_left+card_x)))
                 score+=nearest_star[2]/10
                 cardlist.append([card_x,card_y,score])
             else:
                 cardlist.append([card_x,card_y,score])
         if len(cardlist)>=3:
             servantcard=sorted(cardlist,key=lambda x:x[2],reverse=True)[:3]
             if len(servantcard)>=3:
                 for servantcard_ in reversed(servantcard):
                     pyautogui.click(blueStacks_left+servantcard_[0],blueStacks_top+servantcard_[1])
                     time.sleep(2)

     time.sleep(3)
     continue_img=pyautogui.screenshot(region=(blueStacks_left,blueStacks_top,blueStacks_width,blueStacks_height))
     continue_img=numpy.array(continue_img)
     continue_img=cv2.cvtColor(continue_img,cv2.COLOR_RGB2BGR)
     continue_results=model.predict(continue_img)
     for continue_ in continue_results[0].boxes:
         continue_x1,continue_y1,continue_x2,continue_y2=continue_.xyxy[0]
         continue_x=float((continue_x1+continue_x2)/2)
         continue_y=float((continue_y1+continue_y2)/2)
         cls=int(continue_.cls[0])
         if cls==20:
             pyautogui.click(blueStacks_left+continue_x,blueStacks_top+continue_y)
             time.sleep(2)
             pyautogui.click(blueStacks_left+continue_x,blueStacks_top+continue_y)
             time.sleep(2)

     continue_img=pyautogui.screenshot(region=(blueStacks_left,blueStacks_top,blueStacks_width,blueStacks_height))
     continue_img=numpy.array(continue_img)
     continue_img=cv2.cvtColor(continue_img,cv2.COLOR_RGB2BGR)
     continue_results=model.predict(continue_img)
     for continue_ in continue_results[0].boxes:
         continue_x1,continue_y1,continue_x2,continue_y2=continue_.xyxy[0]
         continue_x=float((continue_x1+continue_x2)/2)
         continue_y=float((continue_y1+continue_y2)/2)
         cls=int(continue_.cls[0])
         if cls==20:
             pyautogui.click(blueStacks_left+continue_x,blueStacks_top+continue_y)
             time.sleep(2)

     participateinthewar_img=pyautogui.screenshot(region=(blueStacks_left,blueStacks_top,blueStacks_width,blueStacks_height))
     participateinthewar_img=numpy.array(participateinthewar_img)
     participateinthewar_img=cv2.cvtColor(participateinthewar_img,cv2.COLOR_RGB2BGR)
     participateinthewar_results=model.predict(participateinthewar_img)
     for participateinthewar in participateinthewar_results[0].boxes:
         participateinthewar_x1,participateinthewar_y1,participateinthewar_x2,participateinthewar_y2=participateinthewar.xyxy[0]
         participateinthewar_x=float((participateinthewar_x1+participateinthewar_x2)/2)
         participateinthewar_y=float((participateinthewar_y1+participateinthewar_y2)/2)
         cls=int(participateinthewar.cls[0])
         if cls==21:
             battle+=1
             if battle>=battle_:
                 break
             pyautogui.click(blueStacks_left+participateinthewar_x,blueStacks_top+participateinthewar_y)
             time.sleep(2)
     if battle>=battle_:
                 break
     chooseenergylist=[]
     chooseenergy_img=pyautogui.screenshot(region=(blueStacks_left,blueStacks_top,blueStacks_width,blueStacks_height))
     chooseenergy_img=numpy.array(chooseenergy_img)
     chooseenergy_img=cv2.cvtColor(chooseenergy_img,cv2.COLOR_RGB2BGR)
     chooseenergy_results=model.predict(chooseenergy_img)
     for chooseenergy in chooseenergy_results[0].boxes:
         chooseenergy_x1,chooseenergy_y1,chooseenergy_x2,chooseenergy_y2=chooseenergy.xyxy[0]
         chooseenergy_x=float((chooseenergy_x1+chooseenergy_x2)/2)
         chooseenergy_y=float((chooseenergy_y1+chooseenergy_y2)/2)
         cls=int(chooseenergy.cls[0])
         if cls==26:
             chooseenergylist.append((chooseenergy_x,chooseenergy_y))
     if len(chooseenergylist)>=1:
         chooseenergy_x_,chooseenergy_y_=max(chooseenergylist,key=lambda x:x[0])
         pyautogui.click(blueStacks_left+chooseenergy_x_,blueStacks_top+chooseenergy_y_)
         time.sleep(2)

     select_img=pyautogui.screenshot(region=(blueStacks_left,blueStacks_top,blueStacks_width,blueStacks_height))
     select_img=numpy.array(select_img)
     select_img=cv2.cvtColor(select_img,cv2.COLOR_RGB2BGR)
     select_results=model.predict(select_img)
     for select in select_results[0].boxes:
         select_x1,select_y1,select_x2,select_y2=select.xyxy[0]
         select_x=float((select_x1+select_x2)/2)
         select_y=float((select_y1+select_y2)/2)
         cls=int(select.cls[0])
         if cls==15:
             pyautogui.click(blueStacks_left+select_x,blueStacks_top+select_y)
             time.sleep(4)

     borrowservantlist=[]
     borrowservant_img=pyautogui.screenshot(region=(blueStacks_left,blueStacks_top,blueStacks_width,blueStacks_height))
     borrowservant_img=numpy.array(borrowservant_img)
     borrowservant_img=cv2.cvtColor(borrowservant_img,cv2.COLOR_RGB2BGR)
     borrowservant_results=model.predict(borrowservant_img)
     for borrowservant in borrowservant_results[0].boxes:
         borrowservant_x1,borrowservant_y1,borrowservant_x2,borrowservant_y2=borrowservant.xyxy[0]
         borrowservant_x=float((borrowservant_x1+borrowservant_x2)/2)
         borrowservant_y=float((borrowservant_y1+borrowservant_y2)/2)
         cls=int(borrowservant.cls[0])
         if cls==24:
             borrowservantlist.append((borrowservant_x,borrowservant_y))
     if len(borrowservantlist)>=1:
             borrowservant_x_, borrowservant_y_=max(borrowservantlist,key=lambda x:x[0])
             pyautogui.click(blueStacks_left+borrowservant_x_,blueStacks_top+borrowservant_y_)
             time.sleep(4)
    
     thebattlebegins_img=pyautogui.screenshot(region=(blueStacks_left,blueStacks_top,blueStacks_width,blueStacks_height))
     thebattlebegins_img=numpy.array(thebattlebegins_img)
     thebattlebegins_img=cv2.cvtColor(thebattlebegins_img,cv2.COLOR_RGB2BGR)
     thebattlebegins_results=model.predict(thebattlebegins_img)
     for thebattlebegins in thebattlebegins_results[0].boxes:
         thebattlebegins_x1,thebattlebegins_y1,thebattlebegins_x2,thebattlebegins_y2=thebattlebegins.xyxy[0]
         thebattlebegins_x=float((thebattlebegins_x1+thebattlebegins_x2)/2)
         thebattlebegins_y=float((thebattlebegins_y1+thebattlebegins_y2)/2)
         cls=int(thebattlebegins.cls[0])
         if cls==25:
             pyautogui.click(blueStacks_left+thebattlebegins_x,blueStacks_top+thebattlebegins_y)
             time.sleep(4)
     print(model.names)