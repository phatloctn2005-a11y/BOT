import torch
import numpy as np
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