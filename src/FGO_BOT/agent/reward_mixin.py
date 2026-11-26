class RewardMixin:
     def calculate_reward(self, action, state, reward, red_clicked, blue_clicked, green_clicked, npred_clicked, npblue_clicked, npgreen_clicked):
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
          continue_=state[40]
          selectedcard=(state[18]>0 or state[20]>0 or state[22]>0 or state[34]>0 or state[36]>0 or state[38]>0)
          terminated=False
          if state[40]>0:
                 self.batte_count=0
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
          return reward, terminated