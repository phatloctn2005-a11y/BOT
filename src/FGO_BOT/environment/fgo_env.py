import gymnasium
from gymnasium import spaces
from ultralytics import YOLO
import numpy
import mss
import time
from config import YOLO_PATH
from vision.yolo_detector import YOLODetectorMixin
from agent.action_mask.valid_action_mixin import ValidActionMixin
from control.card_mixin import CardMixin
from control.action_mixin import ActionMixin
from agent.reward_mixin import RewardMixin
from agent.ppo_agent import inspect_policy
from utils.bar_dataset import BarDataset
class fgoevn(YOLODetectorMixin,ValidActionMixin,CardMixin,ActionMixin,RewardMixin,gymnasium.Env):
     def __init__(self,android):
          super().__init__()
          self.android=android
          self.ppo_model=None
          self.action_space=spaces.Discrete(17)
          self.observation_space=spaces.Box(low=0,high=1,shape=(66,),dtype=numpy.float32)
          self.yolo=YOLO(YOLO_PATH)
          self.bar_dataset=BarDataset(interval=5.0,max_samples=100)
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
     def step(self,action):
          if self.current_state is None:
                 state=self.get_state()
          else:
                 state=self.current_state.copy()
          if(state[18]>0
             or state[34]>0
             or state[36]>0
             or state[38]>0):
            if self.ppo_model is not None:
                inspect_policy(self.ppo_model,state)
          reward,red_clicked,blue_clicked, green_clicked,npred_clicked,npblue_clicked,npgreen_clicked=self.execute_action(action,state)
          reward,terminated=self.calculate_reward(action,state,reward,red_clicked,blue_clicked,green_clicked,npred_clicked,npblue_clicked,npgreen_clicked)
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
