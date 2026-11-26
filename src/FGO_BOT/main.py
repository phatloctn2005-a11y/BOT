import time
from stable_baselines3 import PPO
from config import PPO_PATH
from control.game_controller import connect_game
from environment.fgo_env import fgoevn
from agent.ppo_agent import predict_valid_action
from pathlib import Path
def main():
    env=fgoevn(connect_game())
    ppo_model=PPO.load(PPO_PATH,env=env)
    env.ppo_model=ppo_model
    obs,info=env.reset()
    time_start=int(time.time())
    obs, info=env.reset()
    time_stop=time.time()+300
    card_wait_count=0
    modelS_save_path=Path(__file__).resolve().resolve()
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
            available_np=[a for a in (8,9,10)
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
    ppo_model.save(modes_save_path/"models/fgo_ppo2_")"""
if __name__ == "__main__":
    main()
