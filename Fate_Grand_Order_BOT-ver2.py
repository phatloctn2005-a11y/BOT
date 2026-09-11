from stable_baselines3 import PPO
from ultralytics import YOLO
from gymnasium import spaces
import gymnasium
import mss
import cv2
import numpy
import time
import pygetwindow
import pytesseract
import uiautomator2
pytesseract.pytesseract.tesseract_cmd=(r"C:\Program Files\Tesseract-OCR\tesseract.exe")
adb=r"d:/platform-tools-latest-windows/platform-tools/adb.exe"
fgo_windo=pygetwindow.getWindowsWithTitle("BlueStacks App Player")[0]
android=uiautomator2.connect("emulator-5554")#c6tskfnzwkayzhnf
fgo_windo.restore()
fgo_windo.resizeTo(1280,720)
fgo_windo.activate()
time.sleep(1)
fgo_left=fgo_windo.left
fgo_top=fgo_windo.top
fgo_width=fgo_windo.width
fgo_height=fgo_windo.height
print(android.window_size())
print(fgo_width, fgo_height)
class fgoevn(gymnasium.Env):
     def __init__(self):
          super().__init__()
          self.action_space=spaces.Discrete(17)
          self.observation_space=spaces.Box(low=0,high=1,shape=(66,),dtype=numpy.float32)
          self.yolo=YOLO("D:/AI/Python/Project/AI/YOLO_AI/FGO-ver8_Best.pt")
          self.mss=mss.mss()
          self.enemy_click_count=0
          self.attack_count=0
          self.list_redcard=[]
          self.list_bluecard=[]
          self.list_greencard=[]
          self.list_npredcard=[]
          self.list_npbluecard=[]
          self.list_npgreencard=[]
          self.redcard=[]
          self.bluecard=[]
          self.greencard=[]
          self.npredcard=[]
          self.npbluecard=[]
          self.npgreencard=[]
          self.redcard_click_count=0
          self.bluecard_click_count=0
          self.greencard_click_count=0
          self.npredcard_click_count=0
          self.npbluecard_click_count=0
          self.npgreencard_click_count=0
          self.list_redcard_click_count=0
          self.list_bluecard_click_count=0
          self.list_greencard_click_count=0
          self.list_npredcard_click_count=0
          self.list_npbluecard_click_count=0
          self.list_npgreencard_click_count=0
          self.redcard_click_count_step=0
          self.bluecard_click_count_step=0
          self.greencard_click_count_step=0
          self.npredcard_click_count_step=0
          self.npbluecard_click_count_step=0
          self.npgreencard_click_count_step=0
          self.batte_count=0
          self.skill_click_count=0
          self.select_click_count=0
          self.card_locked=False
          self.no_card_fram=0

     def get_state(self):
          self.redcard.clear()
          self.bluecard.clear()
          self.greencard.clear()
          self.npredcard.clear()
          self.npbluecard.clear()
          self.npgreencard.clear()
          self.redcard_click_count=0
          self.bluecard_click_count=0
          self.greencard_click_count=0
          self.npredcard_click_count=0
          self.npbluecard_click_count=0
          self.npgreencard_click_count=0
          yolo_img={"top":fgo_top,
                    "left":fgo_left,
                    "width":fgo_width,
                    "height":fgo_height}
          yolo_img=numpy.array(self.mss.grab(yolo_img))
          yolo_img=cv2.cvtColor(yolo_img,cv2.COLOR_RGB2BGR)
          yolo_results=self.yolo.predict(yolo_img,verbose=False)
          enemy_x=0#0
          enemy_y=0#1
          enemyhp_x=0#2
          enemyhp_y=0#3
          enemynp_x=0#4
          enemynp_y=0#5
          servant_x=0#6
          servant_y=0#7
          servanthp_x=0#8
          servanthp_y=0#9
          servantnp_x=0#10
          servantnp_y=0#11
          servantskill_x=0#12
          servantskill_y=0#13
          attack_x=0#14
          attack_y=0#15
          battle_x=0#16
          battle_y=0#17
          redcard_x=0#18
          redcard_y=0#19
          bluecard_x=0#20
          bluecard_y=0#21
          greencard_x=0#22
          greencard_y=0#23
          star_x=0#24
          star_y=0#25
          starcard_x=0#26
          starcard_y=0#27
          unclescommand_x=0#28
          unclescommand_y=0#29
          select_x=0#30
          select_y=0#31
          selectservant_x=0#32
          selectservant_y=0#33
          npredcard_x=0#34
          npredcard_y=0#35
          npbluecard_x=0#36
          npbluecard_y=0#37
          npgreencard_x=0#38
          npgreencard_y=0#39
          continue_x=0#40
          continue_y=0#41
          participateinthewar_x=0#42
          participateinthewar_y=0#43
          mastershirt_x=0#44
          mastershirt_y=0#45
          masterskill_x=0#46
          masterskill_y=0#47
          borrowservant_x=0#48
          borrowservant_y=0#49
          thebattlebegins_x=0#50
          thebattlebegins_y=0#51
          chooseenergy_x=0#52
          chooseenergy_y=0#53
          selectedskill_x=0#54
          selectedskill_y=0#55
          theenemyhasbeenchosen_x=0#56
          theenemyhasbeenchosen_y=0#57
          rainbowstone_x=0#58
          rainbowstone_y=0#59
          close_x=0#60
          close_y=0#61
          selectedcard_x=0#62
          selectedcard_y=0#63
          damageservant_x=0#64
          damageservant_y=0#65
          for yolo_box in yolo_results[0].boxes:
                   yolo_x1,yolo_y1,yolo_x2,yolo_y2=yolo_box.xyxy[0]
                   yolo_x=float((yolo_x1+yolo_x2)/2)
                   yolo_y=float((yolo_y1+yolo_y2)/2)
                   yolo_cls=int(yolo_box.cls[0])
                   if yolo_cls==0:
                         enemy_x=float(yolo_x/fgo_width)
                         enemy_y=float(yolo_y/fgo_height)
                   elif yolo_cls==1:
                         enemyhp_x=float(yolo_x/fgo_width)
                         enemyhp_y=float(yolo_y/fgo_height)
                   elif yolo_cls==2:
                         enemynp_x=float(yolo_x/fgo_width)
                         enemynp_y=float(yolo_y/fgo_height)
                   elif yolo_cls==3:
                         servant_x=float(yolo_x/fgo_width)
                         servant_y=float(yolo_y/fgo_height)
                   elif yolo_cls==4:
                         servanthp_x=float(yolo_x/fgo_width)
                         servanthp_y=float(yolo_y/fgo_height)
                   elif yolo_cls==5:
                         servantnp_x=float(yolo_x/fgo_width)
                         servantnp_y=float(yolo_y/fgo_height)
                   elif yolo_cls==6:
                         servantskill_x=float(yolo_x/fgo_width)
                         servantskill_y=float(yolo_y/fgo_height)
                   elif yolo_cls==7:
                         attack_x=float(yolo_x/fgo_width)
                         attack_y=float(yolo_y/fgo_height)
                   elif yolo_cls==8:
                         battle_x=float(yolo_x/fgo_width)
                         battle_y=float(yolo_y/fgo_height)
                   elif yolo_cls==9:
                         redcard_x=float(yolo_x/fgo_width)
                         redcard_y=float(yolo_y/fgo_height)
                         redcard=(int(redcard_x*fgo_width),int(redcard_y*fgo_height))
                         self.redcard.append(redcard)
                         self.redcard_click_count=len(self.redcard)
                   elif yolo_cls==10:
                         bluecard_x=float(yolo_x/fgo_width)
                         bluecard_y=float(yolo_y/fgo_height)
                         bluecard=(int(bluecard_x*fgo_width),int(bluecard_y*fgo_height))
                         self.bluecard.append(bluecard)
                         self.bluecard_click_count=len(self.bluecard)
                   elif yolo_cls==11:
                         greencard_x=float(yolo_x/fgo_width)
                         greencard_y=float(yolo_y/fgo_height)
                         greencard=(int(greencard_x*fgo_width),int(greencard_y*fgo_height))
                         self.greencard.append(greencard)
                         self.greencard_click_count=len(self.greencard)
                   elif yolo_cls==12:
                         star_x=float(yolo_x/fgo_width)
                         star_y=float(yolo_y/fgo_height)
                   elif yolo_cls==13:
                         starcard_x=float(yolo_x/fgo_width)
                         starcard_y=float(yolo_y/fgo_height)
                   elif yolo_cls==14:
                         unclescommand_x=float(yolo_x/fgo_width)
                         unclescommand_y=float(yolo_y/fgo_height)
                   elif yolo_cls==15:
                         select_x=float(yolo_x/fgo_width)
                         select_y=float(yolo_y/fgo_height)
                   elif yolo_cls==16:
                         selectservant_x=float(yolo_x/fgo_width)
                         selectservant_y=float(yolo_y/fgo_height)
                   elif yolo_cls==17:
                         npredcard_x=float(yolo_x/fgo_width)
                         npredcard_y=float(yolo_y/fgo_height)
                         npredcard=(int(npredcard_x*fgo_width),int(npredcard_y*fgo_height))
                         self.npredcard.append(npredcard)
                         self.npredcard_click_count=len(self.npredcard)
                   elif yolo_cls==18:
                         npbluecard_x=float(yolo_x/fgo_width)
                         npbluecard_y=float(yolo_y/fgo_height)
                         npbluecard=(int(npbluecard_x*fgo_width),int(npbluecard_y*fgo_height))
                         self.npbluecard.append(npbluecard)
                         self.npbluecard_click_count=len(self.npbluecard)
                   elif yolo_cls==19:
                         npgreencard_x=float(yolo_x/fgo_width)
                         npgreencard_y=float(yolo_y/fgo_height)
                         npgreencard=(int(npgreencard_x*fgo_width),int(npgreencard_y*fgo_height))
                         self.npgreencard.append(npgreencard)
                         self.npgreencard_click_count=len(self.npgreencard)
                   elif yolo_cls==20:
                         continue_x=float(yolo_x/fgo_width)
                         continue_y=float(yolo_y/fgo_height)
                   elif yolo_cls==21:
                         participateinthewar_x=float(yolo_x/fgo_width)
                         participateinthewar_y=float(yolo_y/fgo_height)
                   elif yolo_cls==22:
                         mastershirt_x=float(yolo_x/fgo_width)
                         mastershirt_y=float(yolo_y/fgo_height)
                   elif yolo_cls==23:
                         masterskill_x=float(yolo_x/fgo_width)
                         masterskill_y=float(yolo_y/fgo_height)
                   elif yolo_cls==24:
                         borrowservant_x=float(yolo_x/fgo_width)
                         borrowservant_y=float(yolo_y/fgo_height)
                   elif yolo_cls==25:
                         thebattlebegins_x=float(yolo_x/fgo_width)
                         thebattlebegins_y=float(yolo_y/fgo_height)
                   elif yolo_cls==26:
                         chooseenergy_x=float(yolo_x/fgo_width)
                         chooseenergy_y=float(yolo_y/fgo_height)
                   elif yolo_cls==27:
                         selectedskill_x=float(yolo_x/fgo_width)
                         selectedskill_y=float(yolo_y/fgo_height)
                   elif yolo_cls==28:
                         theenemyhasbeenchosen_x=float(yolo_x/fgo_width)
                         theenemyhasbeenchosen_y=float(yolo_y/fgo_height)
                   elif yolo_cls==29:
                         rainbowstone_x=float(yolo_x/fgo_width)
                         rainbowstone_y=float(yolo_y/fgo_height)
                   elif yolo_cls==30:
                         close_x=float(yolo_x/fgo_width)
                         close_y=float(yolo_y/fgo_height)
                   elif yolo_cls==31:
                         selectedcard_x=float(yolo_x/fgo_width)
                         selectedcard_y=float(yolo_y/fgo_height)
                   elif yolo_cls==32:
                         damageservant_x=float(yolo_x/fgo_width)
                         damageservant_y=float(yolo_y/fgo_height)
          return numpy.array([enemy_x,enemy_y,
                             enemyhp_x,enemyhp_y,
                             enemynp_x,enemynp_y,
                             servant_x,servant_y,
                             servanthp_x,servanthp_y,
                             servantnp_x,servantnp_y,
                             servantskill_x,servantskill_y,
                             attack_x,attack_y,
                             battle_x,battle_y,
                             redcard_x,redcard_y,
                             bluecard_x,bluecard_y,
                             greencard_x,greencard_y,
                             star_x,star_y,
                             starcard_x,starcard_y,
                             unclescommand_x,unclescommand_y,
                             select_x,select_y,
                             selectservant_x,selectservant_y,
                             npredcard_x,npredcard_y,
                             npbluecard_x,npbluecard_y,
                             npgreencard_x,npgreencard_y,
                             continue_x,continue_y,
                             participateinthewar_x,participateinthewar_y,
                             mastershirt_x,mastershirt_y,
                             masterskill_x,masterskill_y,
                             borrowservant_x,borrowservant_y,
                             thebattlebegins_x,thebattlebegins_y,
                             chooseenergy_x,chooseenergy_y,
                             selectedskill_x,selectedskill_y,
                             theenemyhasbeenchosen_x,theenemyhasbeenchosen_y,
                             rainbowstone_x,rainbowstone_y,
                             close_x,close_y,
                             selectedcard_x,selectedcard_y,
                             damageservant_x,damageservant_y],dtype=numpy.float32)
     def step(self, action):
          state=self.get_state()
          enemy=state[0]
          servantskill=state[12]
          select=state[30]
          attack=state[14]
          redcard=state[18]
          bluerard=state[20]
          greencard=state[22]
          npredcard=state[34]
          npbluecard=state[36]
          npgreencard=state[38]
          continue_=state[40]
          selectservant=state[32]
          participateinthewar=state[42]
          borrowservant=state[48]
          thebattlebegins=state[50]
          chooseenergy=state[52]
          close=state[60]
          reward=0
          continue_=state[40]
          pre_matchscreen=(chooseenergy>0 or borrowservant>0 or participateinthewar>0 or thebattlebegins>0)
          preparationscreen=(attack>0 or servantskill>0 or selectservant>0 or select>0 or selectservant>0 or close>0)
          selectedcard=(state[18]>0 or state[20]>0 or state[22]>0 or state[34]>0 or state[36]>0 or state[38]>0)
          if selectedcard:
                   self.no_card_fram+=1
                   if self.no_card_fram>=5 and not self.card_locked:
                         self.list_redcard=self.redcard.copy()
                         self.list_bluecard=self.bluecard.copy()
                         self.list_greencard=self.greencard.copy()
                         self.list_npredcard=self.npredcard.copy()
                         self.list_npbluecard=self.npbluecard.copy()
                         self.list_npgreencard=self.npgreencard.copy()
                         self.redcard.clear()
                         self.bluecard.clear()
                         self.greencard.clear()
                         self.npredcard.clear()
                         self.npbluecard.clear()
                         self.npgreencard.clear()
                         self.list_redcard_click_count=self.redcard_click_count
                         self.list_bluecard_click_count=self.bluecard_click_count
                         self.list_greencard_click_count=self.greencard_click_count
                         self.list_npredcard_click_count=self.npredcard_click_count
                         self.list_npbluecard_click_count=self.npbluecard_click_count
                         self.list_npgreencard_click_count=self.npgreencard_click_count
                         self.card_locked=True
                         self.attack_count=0
          else:
                   self.no_card_fram=0
          if not(selectedcard):
                   self.list_redcard.clear()
                   self.list_bluecard.clear()
                   self.list_greencard.clear()
                   self.list_npredcard.clear()
                   self.list_npbluecard.clear()
                   self.list_npgreencard.clear()
                   self.list_redcard_click_count=0
                   self.list_bluecard_click_count=0
                   self.list_greencard_click_count=0
                   self.list_npredcard_click_count=0
                   self.list_npbluecard_click_count=0
                   self.list_npgreencard_click_count=0
                   self.redcard_click_count_step=0
                   self.bluecard_click_count_step=0
                   self.greencard_click_count_step=0
                   self.npredcard_click_count_step=0
                   self.npbluecard_click_count_step=0
                   self.npgreencard_click_count_step=0
                   self.card_locked=False
          if action==0:#servantskill
                if state[12]>0:
                         android.click(int(state[12]*fgo_width),int(state[13]*fgo_height))
                         time.sleep(0.5)
          if action==1:#select
                if state[30]>0:
                         android.click(int(state[30]*fgo_width),int(state[31]*fgo_height))
                         self.select_click_count+=1
                         time.sleep(0.5)
                         if self.select_click_count>=2:
                               android.click(int(state[60]*fgo_width),int(state[61]*fgo_height))
                               self.select_click_count=0
                               reward-=21
                               time.sleep(0.5)
          if action==2:#enemy
                   if state[0]>0:
                         android.click(int(state[0]*fgo_width),int(state[1]*fgo_height))
                         time.sleep(0.5)
          if action==3:#attack
                if state[14]>0:
                         android.click(int(state[14]*fgo_width),int(state[15]*fgo_height))
                         time.sleep(0.5)
          if action==4:#redcard
               if state[18]>0 and len(self.list_redcard)>=1:
                         redcard_x,redcard_y=self.list_redcard.pop(0)
                         android.click(redcard_x,redcard_y)
                         time.sleep(0.5)
          if action==5:#bluecard
               if state[20]>0 and len(self.list_bluecard)>=1:
                         bluecard_x,bluecard_y=self.list_bluecard.pop(0)
                         android.click(bluecard_x,bluecard_y)
                         time.sleep(0.5)
          if action==6:#greencard
               if state[22]>0 and len(self.list_greencard)>=1:
                         greencard_x,greencard_y=self.list_greencard.pop(0)
                         android.click(greencard_x,greencard_y)
                         time.sleep(0.5)
          if action==7:#selectservant
                if state[32]>0:
                         android.click(int(state[32]*fgo_width),int(state[33]*fgo_height))
                         time.sleep(0.5)
          if action==8:#npredcard
                   if state[34]>0 and len(self.list_npredcard)>=1:
                               npredcard_x,npredcard_y=self.list_npredcard.pop(0)
                               android.click(npredcard_x,npredcard_y)
                               time.sleep(0.5)
          if action==9:#npbluecard
                   if state[36]>0 and len(self.list_npbluecard)>=1:
                               npbluecard_x,npbluecard_y=self.list_npbluecard.pop(0)
                               android.click(npbluecard_x,npbluecard_y)
                               time.sleep(0.5)
          if action==10:#npgreencard
                if state[38]>0 and len(self.list_npgreencard)>=1:
                               npgreencard_x,npgreencard_y=self.list_npgreencard.pop(0)
                               android.click(npgreencard_x,npgreencard_y)
                               time.sleep(0.5)
          if action==11:#continue
                if (not(preparationscreen or selectedcard or pre_matchscreen)or state[40]>0):
                         android.click(int(state[40]*fgo_width),int(state[41]*fgo_height))
                         time.sleep(0.5)
          if action==12:#participateinthewar
                if state[42]>0:
                         android.click(int(state[42]*fgo_width),int(state[43]*fgo_height))
                         time.sleep(0.5)
                time.sleep(0.5)
          if action==13:#borrowservant
                if state[48]>0:
                         android.click(int(state[48]*fgo_width),int(state[49]*fgo_height))
                         time.sleep(0.5)
          if action==14:#thebattlebegins
                if state[50]>0:
                         android.click(int(state[50]*fgo_width),int(state[51]*fgo_height))
                         time.sleep(0.5)
          if action==15:#chooseenergy
                if state[52]>0:
                         android.click(int(state[52]*fgo_width),int(state[53]*fgo_height))
                         time.sleep(0.5)
          if action==16:#close
                if state[60]>0 and not state[30]>0 and not state[32]>0:
                      android.click(int(state[60]*fgo_width),int(state[61]*fgo_height))
                      time.sleep(0.5)
          terminated=False
          if state[40]>0:
                 self.batte_count=0
          if state[40]>0:
                   terminated=True
          if action==0:
               if servantskill>0:
                   reward+=7
                   self.skill_click_count+=1
               else:
                   reward-=3
                   self.skill_click_count-=1
                   if self.skill_click_count<=0:
                         self.skill_click_count=0
          if action==1:
               if select>0:
                   reward+=7
               else:
                   reward-=3
          if action==2:
                if enemy>0 and self.enemy_click_count==0:
                      reward+=5
                      self.enemy_click_count+=1
                else:
                      reward-=2
          if action==3:
               if attack>0 and self.attack_count==0:
                   reward+=5
                   self.attack_count+=1
                   self.enemy_click_count=0
                   self.select_click_count=0
                   self.skill_click_count_=0
                   self.list_redcard.clear()
                   self.list_bluecard.clear()
                   self.list_greencard.clear()
               else:
                   reward-=2
          if attack>0:
             self.select_click_count=0
          if action==4:
                   if len(self.list_redcard)>0:
                         self.redcard_click_count_step+=1
                         if self.redcard_click_count_step<=self.list_redcard_click_count:
                               reward+=8+(self.skill_click_count/2)
                               self.skill_click_count=0
                         else:
                               reward-=4
                   else:
                         reward-=4
          if action==5:
                   if len(self.list_bluecard)>0:
                         self.bluecard_click_count_step+=1
                         if self.bluecard_click_count_step<=self.list_bluecard_click_count:
                               reward+=7+(self.skill_click_count/2)
                               self.skill_click_count=0
                         else:
                               reward-=3
                   else:
                         reward-=3
          if action==6:
                   if len(self.list_greencard)>0:
                         self.greencard_click_count_step+=1
                         if self.greencard_click_count_step<=self.list_greencard_click_count:
                               reward+=5+(self.skill_click_count/2)
                               self.skill_click_count=0
                         else:
                               reward-=2
                   else:
                         reward-=2
          if action==7:
                 if selectservant>0:
                        reward+=5
                 else:
                        reward-=1
          if action==8:
                   if len(self.list_npredcard)>0:
                         self.npredcard_click_count_step+=1
                         if self.npredcard_click_count_step<=self.list_npredcard_click_count:
                               reward+=30+(self.skill_click_count/2)
                               self.skill_click_count=0
                         else:
                               reward-=10
                   else:
                         reward-=10
          if action==9:
                   if len(self.list_npbluecard)>0:
                         self.npbluecard_click_count_step+=1
                         if self.npbluecard_click_count_step<=self.list_npbluecard_click_count:
                               reward+=15+(self.skill_click_count/2)
                               self.skill_click_count=0
                         else:
                               reward-=7
                   else:
                         reward-=7
          if action==10:
                   if len(self.list_npgreencard)>0:
                         self.npgreencard_click_count_step+=1
                         if self.npgreencard_click_count_step<=self.list_npgreencard_click_count:
                               reward+=10+(self.skill_click_count/2)
                               self.skill_click_count=0
                         else:
                               reward-=5
                   else:
                         reward-=5
          if action==11:
                   if continue_>0:
                         reward+=3
                   else:
                         reward-=1
          if action==12:
                   if participateinthewar>0:
                          reward+=3
                   else:
                          reward-=1
          if action==13:
                   if borrowservant>0:
                          reward+=3
                   else:
                          reward-=1
          if action==14:
                   if thebattlebegins>0:
                          reward+=3
                   else:
                          reward-=1
          if action==15:
                   if chooseenergy>0:
                          reward+=3
                   else:
                          reward-=1
          if action==16:
                   if (close==0)or(close>0 and (select>0 or selectedcard>0)):
                          reward-=1
          print("action:",action,"reward:",reward)
          return (state,reward,terminated,False,{})
     def reset(self,seed=None,options=None):
           state=self.get_state()
           self.enemy_click_count=0
           self.attack_count=0
           self.batte_count=0
           self.skill_click_count=0
           self.redcard.clear()
           self.bluecard.clear()
           self.greencard.clear()
           self.npredcard.clear()
           self.npbluecard.clear()
           self.npgreencard.clear()
           self.list_redcard.clear()
           self.list_bluecard.clear()
           self.list_greencard.clear()
           self.list_npredcard.clear()
           self.list_npbluecard.clear()
           self.list_npgreencard.clear()
           self.redcard_click_count=0
           self.bluecard_click_count=0
           self.greencard_click_count=0
           self.npredcard_click_count=0
           self.npbluecard_click_count=0
           self.npgreencard_click_count=0
           self.list_redcard_click_count=0
           self.list_bluecard_click_count=0
           self.list_greencard_click_count=0
           self.list_npredcard_click_count=0
           self.list_npbluecard_click_count=0
           self.list_npgreencard_click_count=0
           self.redcard_click_count_step=0
           self.bluecard_click_count_step=0
           self.greencard_click_count_step=0
           self.npredcard_click_count_step=0
           self.npbluecard_click_count_step=0
           self.npgreencard_click_count_step=0
           self.card_locked=False
           self.no_card_fram=0
           self.select_click_count=0
           return state,{}
env=fgoevn()
ppo_model=PPO.load( "D:/AI/Python/Project/AI/PPO_AI/fgo_ppo2_",env)
try:
      ppo_model.learn(total_timesteps=100000000,reset_num_timesteps=False)
except KeyboardInterrupt:
      print("Trainが止まりました!")
ppo_model.save("D:/AI/Python/Project/AI/PPO_AI/fgo_ppo2_")