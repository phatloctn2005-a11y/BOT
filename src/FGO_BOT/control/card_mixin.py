import time
class CardMixin:
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