from zipfile import Path
from gymnasium.spaces import box
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
          self.yolo=YOLO("D:/AI/design/Project/AI/YOLO_AI/FGO-ver8_Best.pt")
          self.mss=mss.mss()
          self.screen_width,self.screen_height=android.window_size()
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
          self.redcard_candidates=[]
          self.bluecard_candidates=[]
          self.greencard_candidates=[]
          self.npredcard_candidates=[]
          self.npbluecard_candidates=[]
          self.npgreencard_candidates=[]
          self.clicked_np_positions=[]
          self.batte_count=0
          self.skill_click_count=0
          self.select_click_count=0
          self.card_locked=False
          self.no_card_fram=0
          self.claer_selectedcard=0
          self.total_cards_selected=0
          self.card_stuck_frames=0
          self.current_state=None
     def get_state(self,update_cache=True):
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
          yolo_img=android.screenshot(format="opencv")
          img_height,img_width=yolo_img.shape[:2]
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
                         enemy_x=float(yolo_x/img_width)
                         enemy_y=float(yolo_y/img_height)
                   elif yolo_cls==1:
                         enemyhp_x=float(yolo_x/img_width)
                         enemyhp_y=float(yolo_y/img_height)
                   elif yolo_cls==2:
                         enemynp_x=float(yolo_x/img_width)
                         enemynp_y=float(yolo_y/img_height)
                   elif yolo_cls==3:
                         servant_x=float(yolo_x/img_width)
                         servant_y=float(yolo_y/img_height)
                   elif yolo_cls==4:
                         servanthp_x=float(yolo_x/img_width)
                         servanthp_y=float(yolo_y/img_height)
                   elif yolo_cls==5:
                         servantnp_x=float(yolo_x/img_width)
                         servantnp_y=float(yolo_y/img_height)
                   elif yolo_cls==6:
                         servantskill_x=float(yolo_x/img_width)
                         servantskill_y=float(yolo_y/img_height)
                   elif yolo_cls==7:
                         attack_x=float(yolo_x/img_width)
                         attack_y=float(yolo_y/img_height)
                   elif yolo_cls==8:
                         battle_x=float(yolo_x/img_width)
                         battle_y=float(yolo_y/img_height)
                   elif yolo_cls==9:
                         redcard_x=float(yolo_x/img_width)
                         redcard_y=float(yolo_y/img_height)
                         redcard=(int(redcard_x*img_width),int(redcard_y*img_height))
                         self.redcard.append(redcard)
                         self.redcard_click_count=len(self.redcard)
                   elif yolo_cls==10:
                         bluecard_x=float(yolo_x/img_width)
                         bluecard_y=float(yolo_y/img_height)
                         bluecard=(int(bluecard_x*img_width),int(bluecard_y*img_height))
                         self.bluecard.append(bluecard)
                         self.bluecard_click_count=len(self.bluecard)
                   elif yolo_cls==11:
                         greencard_x=float(yolo_x/img_width)
                         greencard_y=float(yolo_y/img_height)
                         greencard=(int(greencard_x*img_width),int(greencard_y*img_height))
                         self.greencard.append(greencard)
                         self.greencard_click_count=len(self.greencard)
                   elif yolo_cls==12:
                         star_x=float(yolo_x/img_width)
                         star_y=float(yolo_y/img_height)
                   elif yolo_cls==13:
                         starcard_x=float(yolo_x/img_width)
                         starcard_y=float(yolo_y/img_height)
                   elif yolo_cls==14:
                         unclescommand_x=float(yolo_x/img_width)
                         unclescommand_y=float(yolo_y/img_height)
                   elif yolo_cls==15:
                         select_x=float(yolo_x/img_width)
                         select_y=float(yolo_y/img_height)
                   elif yolo_cls==16:
                         selectservant_x=float(yolo_x/img_width)
                         selectservant_y=float(yolo_y/img_height)
                   elif yolo_cls==17:
                         npredcard_x=float(yolo_x/img_width)
                         npredcard_y=float(yolo_y/img_height)
                         npredcard=(int(npredcard_x*img_width),int(npredcard_y*img_height))
                         if not self.is_np_clicked(npredcard_x,npredcard_y):
                              self.npredcard.append(npredcard)
                              self.npredcard_click_count=len(self.npredcard)
                   elif yolo_cls==18:
                         npbluecard_x=float(yolo_x/img_width)
                         npbluecard_y=float(yolo_y/img_height)
                         npbluecard=(int(npbluecard_x*img_width),int(npbluecard_y*img_height))
                         if not self.is_np_clicked(npbluecard_x,npbluecard_y):
                              self.npbluecard.append(npbluecard)
                              self.npbluecard_click_count=len(self.npbluecard)
                   elif yolo_cls==19:
                         npgreencard_x=float(yolo_x/img_width)
                         npgreencard_y=float(yolo_y/img_height)
                         npgreencard=(int(npgreencard_x*img_width),int(npgreencard_y*img_height))
                         if not self.is_np_clicked(npgreencard_x,npgreencard_y):
                              self.npgreencard.append(npgreencard)
                              self.npgreencard_click_count=len(self.npgreencard)
                   elif yolo_cls==20:
                         continue_x=float(yolo_x/img_width)
                         continue_y=float(yolo_y/img_height)
                   elif yolo_cls==21:
                         participateinthewar_x=float(yolo_x/img_width)
                         participateinthewar_y=float(yolo_y/img_height)
                   elif yolo_cls==22:
                         mastershirt_x=float(yolo_x/img_width)
                         mastershirt_y=float(yolo_y/img_height)
                   elif yolo_cls==23:
                         masterskill_x=float(yolo_x/img_width)
                         masterskill_y=float(yolo_y/img_height)
                   elif yolo_cls==24:
                         borrowservant_x=float(yolo_x/img_width)
                         borrowservant_y=float(yolo_y/img_height)
                   elif yolo_cls==25:
                         thebattlebegins_x=float(yolo_x/img_width)
                         thebattlebegins_y=float(yolo_y/img_height)
                   elif yolo_cls==26:
                         chooseenergy_x=float(yolo_x/img_width)
                         chooseenergy_y=float(yolo_y/img_height)
                   elif yolo_cls==27:
                         selectedskill_x=float(yolo_x/img_width)
                         selectedskill_y=float(yolo_y/img_height)
                   elif yolo_cls==28:
                         theenemyhasbeenchosen_x=float(yolo_x/img_width)
                         theenemyhasbeenchosen_y=float(yolo_y/img_height)
                   elif yolo_cls==29:
                         rainbowstone_x=float(yolo_x/img_width)
                         rainbowstone_y=float(yolo_y/img_height)
                   elif yolo_cls==30:
                         close_x=float(yolo_x/img_width)
                         close_y=float(yolo_y/img_height)
                   elif yolo_cls==31:
                         selectedcard_x=float(yolo_x/img_width)
                         selectedcard_y=float(yolo_y/img_height)
                   elif yolo_cls==32:
                         damageservant_x=float(yolo_x/img_width)
                         damageservant_y=float(yolo_y/img_height)
          state=numpy.array([enemy_x,enemy_y,
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
          if update_cache:
                  self.current_state=state.copy()
          return state
     def get_valid_actions(self,state):
            valid=[]
            action_states={0:12,
                           1:30,
                           2:0,
                           3:14,
                           7:32,
                           11:40,
                           12:42,
                           13:48,
                           14:50,
                           15:52,
                           16:60}
            for action,index in action_states.items():
                  if state[index]<=0:
                        continue
                  if action==2 and self.enemy_click_count>=1:
                        continue
                  valid.append(action)
            card_actions={4:(18,self.list_redcard),
                          5:(20,self.list_bluecard),
                          6:(22,self.list_greencard),
                          }
            np_actions={8:(34,"npredcard"),
                        9:(36,"npbluecard"),
                        10:(38,"npgreencard")}
            if self.total_cards_selected<3:
                  for action,(index,cards)in card_actions.items():
                        if state[index]>0 and len(cards)>0:
                              valid.append(action)
                  if self.card_locked:
                        for action,(index,name)in np_actions.items():
                              if state[index]<=0:
                                    continue
                              if self.get_available_np_cards(name):
                                    valid.append(action)
            if self.card_locked:
                  print("========== NP VALID DEBUG ==========")
                  print("NP RED:",self.get_available_np_cards("npredcard"))
                  print("NP BLUE:",self.get_available_np_cards("npbluecard"))
                  print("NP GREEN:",self.get_available_np_cards("npgreencard"))
                  print("Clicked NP:",self.clicked_np_positions)
                  print("Selected:", self.total_cards_selected)
                  print("Valid actions:",valid)
                  print("====================================")
            return valid
     def clear_card_tracking(self):
          card_types=["redcard","bluecard","greencard",
                      "npredcard","npbluecard","npgreencard"]
          for name in card_types:
               getattr(self,f"list_{name}").clear()
               getattr(self,f"{name}_candidates").clear()
               setattr(self,f"list_{name}_click_count",0)
               setattr(self,f"{name}_click_count_step",0)
          self.card_locked=False
          self.claer_selectedcard=0
          self.no_card_fram=0
          self.total_cards_selected=0
          self.clicked_np_positions.clear()
          print("[NEW CARD TURN] Reset NP tracking")
     def remove_duplicate_np(self,distance=35):
            np_lists={"npredcard":self.list_npredcard,
                      "npbluecard":self.list_npbluecard,
                      "npgreencard":self.list_npgreencard,}
            unique_np=[]
            for name,cards in np_lists.items():
                  filterred_cards=[]
                  for x,y in cards:
                        duplicate=False
                        for saved in unique_np:
                              sx,sy=saved["position"]
                              distance_xy=((x-sx)**2+(y-sy)**2)**0.5
                              if distance_xy<distance:
                                    print("[NP DUPLICATE]",name,(x,y),saved["name"],(sx,sy))
                                    duplicate=True
                                    break
                        if not duplicate:
                              filterred_cards.append((x,y))
                              unique_np.append({"name":name,
                                                "position":(x,y)})
                  cards[:]=filterred_cards
            print("[NP UNIQUE]",
                  "red",len(self.list_npredcard),
                  "blue",len(self.list_npbluecard),
                  "green",len(self.list_npgreencard))
     def update_card_tracking(self, state):
          selectedcard=any(state[index]>0
                           for index in (18,20,22,34,36,38))
          if selectedcard:
               self.claer_selectedcard=0
               if not self.card_locked:
                    self.clicked_np_positions.clear()
                    self.total_cards_selected=0
                    card_types=["redcard","bluecard","greencard",
                                "npredcard","npbluecard","npgreencard"]
                    for name in card_types:
                         getattr(self,f"list_{name}").clear()
                         getattr(self,f"{name}_candidates").clear()
                         setattr(self,f"{name}_click_count_step",0)
                    for i in range(5):
                          if i>0:
                                self.get_state(update_cache=False)
                          for name in card_types:
                                self.add_unique_cards(getattr(self,f"{name}_candidates"),
                                                      getattr(self,name))
                          time.sleep(0.1)
                    self.remove_duplicate_np()
                    for name in card_types:
                          candidates=getattr(self,f"{name}_candidates")
                          setattr(self,f"list_{name}",candidates.copy())
                          setattr(self,f"list_{name}_click_count",len(candidates))
                    self.card_locked=True
                    self.attack_count=0
                    print("[CARD INIT]",
                          "red:",len(self.list_redcard),
                          "blue:",len(self.list_bluecard),
                          "green:",len(self.list_greencard),
                          "npred:",len(self.list_npredcard),
                          "npblue:",len(self.list_npbluecard),
                          "npgreen:",len(self.list_npgreencard))
                    print("[NP RESET]",self.clicked_np_positions)
          else:
               if self.card_locked:
                    self.claer_selectedcard+=1
                    if self.claer_selectedcard>=5:
                         self.clear_card_tracking()
          self.remove_duplicate_np()
     def add_unique_cards(self,target,detected,distance=60):
            for x,y in detected:
                if not any((x-old_x)**2+(y-old_y)**2<distance**2 for old_x,old_y in target):
                    target.append((x,y))
     def is_np_clicked(self,x,y,distance=35):
            for old_x,old_y in self.clicked_np_positions:
                  d=((x-old_x)**2+(y-old_y)**2)**0.5
                  if d<distance:
                        return True
            return False
     def mark_np_clicked(self,x,y):
            if not self.is_np_clicked(x,y):
                  self.clicked_np_positions.append((x,y))
     def get_available_np_cards(self,name):
            cards=getattr(self,f"list_{name}")
            return[(x,y)for x,y in cards
                   if not self.is_np_clicked(x,y)]
     def select_np_card(self,name,click_function):
            available=self.get_available_np_cards(name)
            if not available:
                  print("[NP SKIP] No available NP:",name)
                  return False
            x,y=available[0]
            print("========== NP TRACKING ==========")
            print("NP Red:",self.list_npredcard)
            print("NP Blue:",self.list_npbluecard)
            print("NP Green:",self.list_npgreencard)
            print("Clicked:",self.clicked_np_positions)
            print("Unique available:",self.count_unique_np())
            print("=================================")
            print("[NP CLICK BEFORE]",name,(x,y))
            click_function(int(x),int(y))
            time.sleep(1.0)
            print("[NP CLICK SENT]",name,(x,y))
            self.mark_np_clicked(x,y)
            np_names=["npredcard","npbluecard","npgreencard"]
            distance=35
            for np_name in np_names:
                  cards=getattr(self,f"list_{np_name}")
                  cards[:]=[(cx,cy)for cx,cy in cards
                                   if((cx-x)**2+(cy-y)**2)** 0.5>=distance]
            print("[NP SELECTED]",name,(x,y))
            return True
     def filter_clicked_np_candidates(self):
           for name in("npredcard","npbluecard","npgreencard"):
                 attr=f"{name}_candidates"
                 if not hasattr(self,attr):
                       continue
                 candidates=getattr(self,attr)
                 candidates[:]=[(x,y)
                                for x,y in candidates
                                if not self.is_np_clicked(x,y)]
     def count_unique_np(self,distance=35):
           positions=[]
           for name in("npredcard","npbluecard","npgreencard"):
                 cards=self.get_available_np_cards(name)
                 for x,y in cards:
                       duplicate=any(((x-px)**2+(y-py)**2)**0.5<distance
                                     for px,py in positions)
                       if not duplicate:
                             positions.append((x,y))
           return len(positions)
     def register_card_click(self,card_name):
           if self.total_cards_selected>=3:
                 print("[CARD LIMIT] Already selected 3 cards")
                 return False
           self.total_cards_selected+=1
           print("[CARD SELECTED]",card_name,self.total_cards_selected,"/ 3")
           return True
     def step(self, action):
          if self.current_state is None:
                 state=self.get_state()
          else:
                 state=self.current_state.copy()
          if(state[18]>0
             or state[34]>0
             or state[36]>0
             or state[38]>0):
            inspect_policy(ppo_model,state)
          red_clicked=False
          blue_clicked=False
          green_clicked=False
          npred_clicked=False
          npblue_clicked=False
          npgreen_clicked=False
          card_click=False
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
          selectedcard=(state[18]>0 or state[20]>0 or state[22]>0 or state[34]>0 or state[36]>0 or state[38]>0)
          if action==0:#servantskill
                if state[12]>0:
                         android.click(int(state[12]*self.screen_width),int(state[13]*self.screen_height))
                         time.sleep(0.5)
          if action==1:#select
                if state[30]>0:
                         android.click(int(state[30]*self.screen_width),int(state[31]*self.screen_height))
                         self.select_click_count+=1
                         time.sleep(0.5)
                         if self.select_click_count>=2:
                               if state[60]>0 and state[61]>0:
                                    android.click(int(state[60]*self.screen_width),int(state[61]*self.screen_height))
                                    time.sleep(0.5)
                               self.select_click_count=0
                               reward-=21
          if action==2:#enemy
                   if state[0]>0:
                         android.click(int(state[0]*self.screen_width),int(state[1]*self.screen_height))
                         time.sleep(0.5)
          if action==3:#attack
                if state[14]>0:
                         android.click(int(state[14]*self.screen_width),int(state[15]*self.screen_height))
                         time.sleep(0.5)
          if action in(4,5,6):
                if self.total_cards_selected>=3:
                      print("[CARD LIMIT] Maximun 3 cards")
                normal_cards={4:(18,"redcard",self.list_redcard),
                              5:(20,"bluerard",self.list_bluecard),
                              6:(22,"greencard",self.list_greencard)}
                index,name,cards=normal_cards[action]
                if action==5:
                      print("[BLUE DEBUG]",
                            "detected:", state[20] > 0,
                            "locked:", self.card_locked,
                            "available:", len(self.list_bluecard),
                            "candidates:", len(self.bluecard_candidates),
                            "clicked_count:", self.bluecard_click_count_step)
                if(self.card_locked
                   and self.total_cards_selected<3
                   and state[index]>0
                   and len(cards)>0):
                      x,y=cards[0]
                      print("[CARD CLICK BEFORE]",action,(x,y))
                      android.click(int(x),int(y))
                      print("[CARD CLICK SENT]",action,(x,y))
                      cards.pop(0)
                      card_click=True
                if card_click:
                      if action==4:
                            red_clicked=True
                      elif action==5:
                            blue_clicked=True
                      elif action==6:
                            green_clicked=True
                      time.sleep(0.5)
                else:
                      print("[CARD SKIP] Action:",action)
          if action==7:#selectservant
                if state[32]>0:
                         android.click(int(state[32]*self.screen_width),int(state[33]*self.screen_height))
                         time.sleep(0.5)
          if action in(8,9,10):
                if self.total_cards_selected>=3:
                      print("[CARD LIMIT] Maximun 3 cards")
                np_actions={8:(34,"npredcard"),
                            9:(36,"npbluecard"),
                            10:(38,"npgreencard")}
                index,name=np_actions[action]
                if(self.card_locked
                   and state[index]>0
                   and self.get_available_np_cards(name)):
                         clicked=self.select_np_card(name,android.click)
                         if clicked:
                              if action==8:  
                                    npred_clicked=True
                              elif action==9:
                                    npblue_clicked=True
                              elif action==10:
                                    npgreen_clicked=True
                              time.sleep(0.5)
                         else:
                              print("[CARD SKIP] Action:",action)
                else:
                      print("[NP SKIP]",name)              
          if action==11:#continue
                if (state[40]>0 and state[41]>0):
                              android.click(int(state[40]*self.screen_width),int(state[41]*self.screen_height))
                              time.sleep(0.5)
          if action==12:#participateinthewar
                if state[42]>0:
                         android.click(int(state[42]*self.screen_width),int(state[43]*self.screen_height))
                         time.sleep(0.5)
                time.sleep(0.5)
          if action==13:#borrowservant
                if state[48]>0:
                         android.click(int(state[48]*self.screen_width),int(state[49]*self.screen_height))
                         time.sleep(0.5)
          if action==14:#thebattlebegins
                if state[50]>0:
                         android.click(int(state[50]*self.screen_width),int(state[51]*self.screen_height))
                         time.sleep(0.5)
          if action==15:#chooseenergy
                if state[52]>0:
                         android.click(int(state[52]*self.screen_width),int(state[53]*self.screen_height))
                         time.sleep(0.5)
          if action==16:#close
                if state[60]>0 and not state[30]>0 and not state[32]>0:
                      android.click(int(state[60]*self.screen_width),int(state[61]*self.screen_height))
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
                   self.skill_click_count=0
               else:
                   reward-=2
          if attack>0:
             self.select_click_count=0
          if action==4:
                   if red_clicked:
                         self.redcard_click_count_step+=1
                         if self.redcard_click_count_step<=self.list_redcard_click_count:
                               reward+=8+(self.skill_click_count/2)
                               self.skill_click_count=0
                         else:
                               reward-=4
                   else:
                         reward-=4
          if action==5:
                   if blue_clicked:
                         self.bluecard_click_count_step+=1
                         if self.bluecard_click_count_step<=self.list_bluecard_click_count:
                                    reward+=7+(self.skill_click_count/2)
                                    self.skill_click_count=0
                         else:
                              reward-=3
                   else:
                         reward-=3
          if action==6:
                   if green_clicked:
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
                   if npred_clicked:
                         self.npredcard_click_count_step+=1
                         if self.npredcard_click_count_step<=self.list_npredcard_click_count:
                               reward+=30+(self.skill_click_count/2)
                               self.skill_click_count=0
                         else:
                               reward-=10
                   else:
                         reward-=10
          if action==9:
                   if npblue_clicked:
                         self.npbluecard_click_count_step+=1
                         if self.npbluecard_click_count_step<=self.list_npbluecard_click_count:
                               reward+=15+(self.skill_click_count/2)
                               self.skill_click_count=0
                         else:
                               reward-=7
                   else:
                         reward-=7
          if action==10:
                   if npgreen_clicked:
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
                         reward+=5
                   else:
                         reward-=5
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
          if any([red_clicked,blue_clicked,green_clicked,
                  npred_clicked,npblue_clicked,npgreen_clicked]):
             if self.total_cards_selected<3:
                  self.total_cards_selected+=1
                  print("[CARD SELECTED]",self.total_cards_selected," / 3")
             else:
                   print("[CARD LIMIT] Already selected 3 cards")
          time.sleep(0.3)
          next_state=self.get_state()
          print("action:",action,
                "reward:",reward,
                "next_state_nonzero:",numpy.count_nonzero(next_state))
          return next_state,reward,terminated,False,{}
     def reset(self,seed=None,options=None):
           super().reset(seed=seed)
           self.claer_selectedcard=0
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
           self.redcard_candidates.clear()
           self.bluecard_candidates.clear()
           self.greencard_candidates.clear()
           self.npredcard_candidates.clear()
           self.npbluecard_candidates.clear()
           self.npgreencard_candidates.clear()
           self.clicked_np_positions.clear()
           self.select_click_count=0
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
           self.total_cards_selected=0
           self.card_locked=False
           self.no_card_fram=0
           self.current_state=None
           state=self.get_state()
           return state,{}
env=fgoevn()
ppo_model=PPO.load( "D:/AI/design/Project/AI/PPO_AI/fgo_ppo2_",env=env)
def predict_valid_action(model,obs,valid_actions):
    if not valid_actions:
        return None
    import torch
    with torch.no_grad():
        obs_tensor=torch.as_tensor(obs,dtype=torch.float32,device=model.device).reshape(1,-1)
        distribution=model.policy.get_distribution(obs_tensor)
        probabilities=distribution.distribution.probs[0].cpu().numpy()
    action=max(valid_actions,key=lambda a:probabilities[a])
    print("[MASKED ACTION] valid:",valid_actions,"selected:",action)
    return int(action)
import torch
import numpy as np
def inspect_policy(model,obs):
    obs_tensor=torch.as_tensor(obs,dtype=torch.float32,device=model.device).unsqueeze(0)
    with torch.no_grad():
        dist=model.policy.get_distribution(obs_tensor)
        probs=dist.distribution.probs[0].cpu().numpy()
    action_names=["Servant Skill",
                  "Select",
                  "Enemy",
                  "Attack",
                  "Red Card",
                  "Blue Card",
                  "Green Card",
                  "Select Servant",
                  "NP Red",
                  "NP Blue",
                  "NP Green",
                  "Continue",
                  "Participate",
                  "Borrow Servant",
                  "Battle Begins",
                  "Choose Energy",
                  "Close"]
    print("\n========== PPO POLICY ==========")
    for action, prob in enumerate(probs):
        print(f"{action:2d}|"
              f"{action_names[action]:18s}|"
              f"{prob*100:.6f}%")
    print("================================")
    print("Best action:",int(np.argmax(probs)))
    print("YOLO RED:",obs[18]>0)
    print("YOLO NP RED:",obs[34]>0)
    print("YOLO NP BLUE:",obs[36]>0)
    print("YOLO NP GREEN:",obs[38]>0)
obs,info=env.reset()
time_start=int(time.time())
obs, info=env.reset()
time_stop=time.time()+300
card_wait_count=0
try:
    while True:
        if time.time()>time_stop:
            print("KẾT THÚC 5 PHÚT")
            break
        env.update_card_tracking(obs)
        valid_actions=env.get_valid_actions(obs)
        print("[CARD CHECK]",
              "red:",len(env.list_redcard),
              "blue:",len(env.list_bluecard),
              "green:",len(env.list_greencard),
              "npred:",len(env.list_npredcard),
              "npblue:",len(env.list_npbluecard),
              "locked:",env.card_locked,
              "selected:",env.total_cards_selected)
        if not valid_actions:
            if(env.card_locked
                and env.total_cards_selected>=3):
                card_wait_count+=1
                if card_wait_count==10:
                    print("[CARD STUCK WARNING]",
                          "Bot đã chọn 3 card nhưng",
                          "màn hình card vẫn được phát hiện")
            else:
                card_wait_count=0
            print("[WAIT] Không có action hợp lệ")
            time.sleep(0.5)
            obs=env.get_state()
            continue
        card_wait_count=0
        available_np=[a for a in (8, 9, 10)
                      if a in valid_actions]
        if available_np:
            action=available_np[0]
            print("[NP TEST] Force NP:",action)
        else:
            action=predict_valid_action(ppo_model,obs,valid_actions)
        print("[MASKED ACTION]",
              "valid:",valid_actions,
              "selected:",action)
        obs,reward,terminated,truncated,info=env.step(action)
        print("[RESULT]",
              "action:",action,
              "reward:",reward)
        if terminated or truncated:
            obs, info=env.reset()
            card_wait_count=0
except KeyboardInterrupt:
    print("Đã dừng kiểm tra PPO")
"""try:
      ppo_model.learn(total_timesteps=100000000,reset_num_timesteps=False)
except KeyboardInterrupt:
      print("Trainが止まりました!")
ppo_model.save("D:/AI/design/Project/AI/PPO_AI/fgo_ppo2_")"""