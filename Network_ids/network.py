from nfstream import NFStreamer
import pandas as pd
import joblib
import numpy as np
import time

pipeline = joblib.load('models/Net-basedIDS3.pkl')

model = pipeline['model']
scaler = pipeline['scaler']
selected_features = pipeline['features']
from email_alert import send_email_alert

print("Starting live capture...")

#feature mapping function 

def features_mapping(flow):
    try:
        duration_sec = flow.bidirectional_duration_ms / 1000.0 
        if duration_sec <= 0 : 
           duration_sec = 0.000001
        total_packets = flow.src2dst_packets + flow.dst2src_packets
        total_bytes = flow.src2dst_bytes + flow.dst2src_bytes
        data = {
           'Header_Length':flow.bidirectional_bytes,
           'Rate' : total_packets / duration_sec,
           'Srate' : flow.src2dst_packets / duration_sec,
           'syn_flag_number' : 0,
           'rst_flag_number' : 0,
           'psh_flag_number' : 0,
           'ack_flag_number' : 0,
           'rst_count' : 0,
           'HTTPS': 1 if flow.dst_port == 443 else 0,
           'TCP': 1 if flow.protocol == 6 else 0,
           'UDP': 1 if flow.protocol == 17 else 0,
           'ICMP': 1 if flow.protocol == 1 else 0,
           'Tot sum': total_packets,
           'Max': total_packets,
           'AVG': total_bytes / max(total_packets, 1),
           'Std': 0,
           'Tot size': total_bytes,
           'Magnitue': total_bytes,
           'Radius': 0,
           'Variance': total_packets,
        }
        
        return data
        
    except Exception as e:
        print("error:", e)
        return None
        
streamer = NFStreamer(source= "wlan0", statistical_analysis=True, active_timeout=10, idle_timeout=5)

email_sent = False
for flow in streamer:
       src_ip = flow.src_ip
       dst_ip = flow.dst_ip
       mapped = features_mapping(flow)
       if mapped is None:
           continue
       df = pd.DataFrame([mapped])
       for col in selected_features:
           if col not in df.columns:
               df[col] = 0
      
       df = df[selected_features]
       x_scaled = scaler.transform(df.values)
      
       start = time.time()
       prob = model.predict_proba(x_scaled)[0][1]
       end = time.time()
       latency = end - start
       print(f"Latency:{latency:.5f}
       threshold = 0.2
       
       if prob > threshold:
          if not email_sent :
              send_email_alert(
                  " MedIDS Network Alert",
                  f" 🚨 MedIDS Network Alert : Attack Detected !! 🚨"
                  f"Source:{src_ip} "
                  f" -> " 
                  f"Destination: {dst_ip}\n"
              )
          print(
                 f" 🚨 Attack detected !!! 🚨  "
                 f"Source:{src_ip} "
                 f" -> " 
                 f"Destination: {dst_ip}\n"
             )
       else:
          print(
                 f"Benign  "   
                 f"Source:{src_ip}" 
                 f" -> " 
                 f"Destination: {dst_ip}\n"
             )
          
          

       
