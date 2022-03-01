# Experiment Settings

## Local
- Device: `MAC Mini M1 (2020)` (8 Core CPU + 16 GB RAM)
- Used for: FastAPI, Redis Broker

## Remote
- Device: `Intel(R) Xeon(R) Silver 4214 CPU @ 2.20GHz` x 48 + 128 GB RAM + TITAN RTX (24 GB) x 1
- Used for: Celery Worker, Triton Server

# Experimental Results

## Peak Concurrency = 1
Approximately 1,000 requests sent.

| Name | Average (ms)  | Min (ms)  |  Max (ms) | RPS (Range)  |
|:---:|:---:|:---:|:---:|:---:|
| without Triton  | 57  |  38 | 320  |  16 ~ 18 |
| with  Triton  | 34  | 28  | 66  | 29 ~ 30 |

#### without Triton Server
<img width="1268" alt="" src="https://user-images.githubusercontent.com/14961526/156196352-e568fc57-f60b-46de-a3bd-9df692ffc842.png">
<img width="1254" alt="" src="https://user-images.githubusercontent.com/14961526/156196414-8023281b-6ffc-4635-b5bd-8ad63bf7f0b1.png">

#### with Triton Server
<img width="1270" alt="" src="https://user-images.githubusercontent.com/14961526/156199306-1e041461-5ec3-43ce-942b-d217157f4dc4.png">
<img width="1256" alt="" src="https://user-images.githubusercontent.com/14961526/156199357-9ea50dd1-b416-4f24-b0f0-d765f39c73c5.png">

## Peak Concurrency = 10
Approximately 4,000 requests sent.

| Name | Average (ms)  | Min (ms)  |  Max (ms) | RPS (Range)  |
|:---:|:---:|:---:|:---:|:---:|
| without Triton  | 165  |  46 | 4863  |  59 ~ 61 |
| with  Triton  | 159  | 32  |  448 | 58 ~ 61  |

#### without Triton Server
<img width="1269" alt="" src="https://user-images.githubusercontent.com/14961526/156197902-d4d67282-07b6-456b-842d-499e15013b0f.png">

See `Run #3`.
<img width="1253" alt="" src="https://user-images.githubusercontent.com/14961526/156198107-3cd13b44-ae53-4a41-9983-fbe8c61dc816.png">

#### with Triton Server
<img width="1268" alt="" src="https://user-images.githubusercontent.com/14961526/156199847-fb09236c-5578-48b3-ac2e-022b4e0cdd95.png">

See `Run #2`.
<img width="1255" alt="" src="https://user-images.githubusercontent.com/14961526/156199902-ea65e54a-b515-4297-a840-87c12b22d255.png">


## Peak Concurrency = 30
Approximately 10,000 requests sent.

| Name | Average (ms)  | Min (ms)  |  Max (ms) | RPS (Range)  |
|:---:|:---:|:---:|:---:|:---:|
| without Triton  | 483  |  164 | 634  |  58 ~ 61 |
| with  Triton  | 495 | 180  | 806  | 58 ~ 61 |

#### without Triton Server
<img width="1272" alt="" src="https://user-images.githubusercontent.com/14961526/156198749-8754d262-8583-4cd9-bd19-c9dd4a2cf4cb.png">

See `Run #4`.
<img width="1253" alt="" src="https://user-images.githubusercontent.com/14961526/156198820-85efeba2-ad27-46a9-8d27-b14f0aefb7ae.png">

#### with Triton Server
<img width="1277" alt="" src="https://user-images.githubusercontent.com/14961526/156200667-ab82b940-b4a5-4440-8e63-9b5ddca99d3e.png">

See `Run #3`.
<img width="1244" alt="" src="https://user-images.githubusercontent.com/14961526/156200737-066ce16d-2826-4a30-bfb7-7cf4dc49c6c0.png">
