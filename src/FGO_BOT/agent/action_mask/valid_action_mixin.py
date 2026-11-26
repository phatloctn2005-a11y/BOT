class ValidActionMixin:
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
