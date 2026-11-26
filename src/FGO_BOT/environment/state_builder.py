import numpy
from vision.yolo_detector import get_state
from vision.ocr_reader import measure_bar_fill
class statebuilderMixin:
    def state_builder(self,update_cache=True):
          yolo_cls,yolo_x,yolo_y,img_width,img_height,yolo_img=get_state()
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