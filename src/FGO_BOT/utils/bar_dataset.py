from pathlib import Path
import time
import json
import cv2
class BarDataset:
    def __init__(self,interval=5.0,max_samples=100):
        self.output_dir=(Path(__file__).resolve().parents[1]/"FGO_bar_dataset")
        self.interval=interval
        self.max_samples=max_samples
        self.last_save_time=0
        self.sample_count=0
    def save(self,frame,detected_bars):
        if self.sample_count>=self.max_samples:
            return False
        now=time.monotonic()
        if now-self.last_save_time<self.interval:
            return False
        if not any(detected_bars.values()):
            return False
        folder=self.output_dir/str(time.time_ns())
        folder.mkdir(parents=True,exist_ok=True)
        height,width=frame.shape[:2]
        metadata={}
        for name,boxes in detected_bars.items():
            boxes=sorted(boxes,key=lambda box:box["center"][0])
            metadata[name]=[]
            for i,box in enumerate(boxes):
                x1,y1,x2,y2=map(int,box["bbox"])
                x1=max(0,min(x1,width))
                x2=max(0,min(x2,width))
                y1=max(0,min(y1,height))
                y2=max(0,min(y2,height))
                roi=frame[y1:y2,x1:x2]
                if roi.size==0:
                    continue
                filename=f"{name}_{i}.png"
                if not cv2.imwrite(str(folder/filename),roi):
                    continue
                metadata[name].append({"image":filename,
                                       "bbox":[x1,y1,x2,y2],
                                       "confidence":box["confidence"],
                                       "fill_ratio":box.get("fill_ratio")})
        cv2.imwrite(str(folder/"full_frame.png"),frame)
        with open(folder/"metadata.json","w",encoding="utf-8")as f:
            json.dump(metadata,f,indent=4)
        self.sample_count+=1
        self.last_save_time=now
        print("[BAR DATASET]",
              self.sample_count,
              "/",
              self.max_samples)
        return True