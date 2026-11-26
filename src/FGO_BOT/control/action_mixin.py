import time
class ActionMixin:
     def execute_action(self,action,state):
          red_clicked=False
          blue_clicked=False
          green_clicked=False
          npred_clicked=False
          npblue_clicked=False
          npgreen_clicked=False
          card_click=False
          reward=0
          if action==0:#servantskill
                if state[12]>0:
                         self.android.click(int(state[12]*self.screen_width),int(state[13]*self.screen_height))
                         time.sleep(0.5)
          if action==1:#select
                if state[30]>0:
                         self.android.click(int(state[30]*self.screen_width),int(state[31]*self.screen_height))
                         self.select_click_count+=1
                         time.sleep(0.5)
                         if self.select_click_count>=2:
                               if state[60]>0 and state[61]>0:
                                    self.android.click(int(state[60]*self.screen_width),int(state[61]*self.screen_height))
                                    time.sleep(0.5)
                               self.select_click_count=0
                               reward-=21
          if action==2:#enemy
                   if state[0]>0:
                         self.android.click(int(state[0]*self.screen_width),int(state[1]*self.screen_height))
                         time.sleep(0.5)
          if action==3:#attack
                if state[14]>0:
                         self.android.click(int(state[14]*self.screen_width),int(state[15]*self.screen_height))
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
                      self.android.click(int(x),int(y))
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
                         self.android.click(int(state[32]*self.screen_width),int(state[33]*self.screen_height))
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
                         clicked=self.select_np_card(name,self.android.click)
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
                              self.android.click(int(state[40]*self.screen_width),int(state[41]*self.screen_height))
                              time.sleep(0.5)
          if action==12:#participateinthewar
                if state[42]>0:
                         self.android.click(int(state[42]*self.screen_width),int(state[43]*self.screen_height))
                         time.sleep(0.5)
                time.sleep(0.5)
          if action==13:#borrowservant
                if state[48]>0:
                         self.android.click(int(state[48]*self.screen_width),int(state[49]*self.screen_height))
                         time.sleep(0.5)
          if action==14:#thebattlebegins
                if state[50]>0:
                         self.android.click(int(state[50]*self.screen_width),int(state[51]*self.screen_height))
                         time.sleep(0.5)
          if action==15:#chooseenergy
                if state[52]>0:
                         self.android.click(int(state[52]*self.screen_width),int(state[53]*self.screen_height))
                         time.sleep(0.5)
          if action==16:#close
                if state[60]>0 and not state[30]>0 and not state[32]>0:
                      self.android.click(int(state[60]*self.screen_width),int(state[61]*self.screen_height))
                      time.sleep(0.5)
          return reward, red_clicked, blue_clicked, green_clicked, npred_clicked, npblue_clicked, npgreen_clicked