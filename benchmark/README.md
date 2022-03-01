# Experiment Settings

## Local
- Device: `MAC Mini M1 (2020)` (8 Core CPU + 16 GB RAM)
- Used for: FastAPI, Redis Broker

## Remote
- Device: `Intel(R) Xeon(R) Silver 4214 CPU @ 2.20GHz` x 48 + 128 GB RAM + TITAN RTX (24 GB) x 1
- Used for: Celery Worker, Triton Server

# Experimental Results

- **Average, Min, Max**: Lower is better
- RPS (Request Per Second) reached to around 60
- Triton consumes around 1.3GB gpu memory
- Non-Triton consumes around 1.2GB x 10 gpu memory (10 processes)

## Peak Concurrency = 1
Approximately 1,000 requests sent.

| Name | Average (ms)  | Min (ms)  |  Max (ms) |
|:---:|:---:|:---:|:---:|
| without Triton  | 57  |  38 | 320  |
| with  Triton  | 34  | 28  | 66  |
| with  Triton (+ shared memory)  | 31  | 24  | 67  |

#### without Triton Server
<img width="1268" alt="" src="https://user-images.githubusercontent.com/14961526/156196352-e568fc57-f60b-46de-a3bd-9df692ffc842.png">
<img width="1254" alt="" src="https://user-images.githubusercontent.com/14961526/156196414-8023281b-6ffc-4635-b5bd-8ad63bf7f0b1.png">

#### with Triton Server
<img width="1270" alt="" src="https://user-images.githubusercontent.com/14961526/156199306-1e041461-5ec3-43ce-942b-d217157f4dc4.png">
<img width="1256" alt="" src="https://user-images.githubusercontent.com/14961526/156199357-9ea50dd1-b416-4f24-b0f0-d765f39c73c5.png">

#### with Triton Server (+ shared memory)
<img width="1272" alt="" src="https://user-images.githubusercontent.com/14961526/156217741-f3244aa6-a9d9-4a7b-bd3e-b981919e73e5.png">
<img width="1246" alt="" src="https://user-images.githubusercontent.com/14961526/156217775-bd27b71d-e18e-4656-9981-10a8ed6cbafc.png">

## Peak Concurrency = 10
Approximately 4,000 requests sent.

| Name | Average (ms)  | Min (ms)  |  Max (ms) |
|:---:|:---:|:---:|:---:|
| without Triton  | 165  |  46 | 4863  |
| with  Triton  | 159  | 32  |  448 |
| with  Triton (+ shared memory)  | 160  | 37  | 339  |

#### without Triton Server
<img width="1269" alt="" src="https://user-images.githubusercontent.com/14961526/156197902-d4d67282-07b6-456b-842d-499e15013b0f.png">

See `Run #3`.
<img width="1253" alt="" src="https://user-images.githubusercontent.com/14961526/156198107-3cd13b44-ae53-4a41-9983-fbe8c61dc816.png">

#### with Triton Server
<img width="1268" alt="" src="https://user-images.githubusercontent.com/14961526/156199847-fb09236c-5578-48b3-ac2e-022b4e0cdd95.png">

See `Run #2`.
<img width="1255" alt="" src="https://user-images.githubusercontent.com/14961526/156199902-ea65e54a-b515-4297-a840-87c12b22d255.png">

#### with Triton Server (+ shared memory)
<img width="1271" alt="" src="https://user-images.githubusercontent.com/14961526/156218147-704fadd7-df35-414d-a7d7-f16eb96dd520.png">

See `Run #2`.
<img width="1252" alt="" src="https://user-images.githubusercontent.com/14961526/156218180-c6477754-0d3d-42d3-b7fe-811dbd8da5d3.png">

## Peak Concurrency = 30
Approximately 10,000 requests sent.

| Name | Average (ms)  | Min (ms)  |  Max (ms) |
|:---:|:---:|:---:|:---:
| without Triton  | 483  |  164 | 634  |
| with  Triton  | 495 | 180  | 806  |
| with  Triton (+ shared memory)  | 489  | 182  | 779  |

#### without Triton Server
<img width="1272" alt="" src="https://user-images.githubusercontent.com/14961526/156198749-8754d262-8583-4cd9-bd19-c9dd4a2cf4cb.png">

See `Run #4`.
<img width="1253" alt="" src="https://user-images.githubusercontent.com/14961526/156198820-85efeba2-ad27-46a9-8d27-b14f0aefb7ae.png">

#### with Triton Server
<img width="1277" alt="" src="https://user-images.githubusercontent.com/14961526/156200667-ab82b940-b4a5-4440-8e63-9b5ddca99d3e.png">

See `Run #3`.
<img width="1244" alt="" src="https://user-images.githubusercontent.com/14961526/156200737-066ce16d-2826-4a30-bfb7-7cf4dc49c6c0.png">

#### with Triton Server (+ shared memory)
<img width="1276" alt="" src="https://user-images.githubusercontent.com/14961526/156218725-f3c4ea00-67f9-4ac5-95f1-b49b45d9828a.png">

See `Run #3`.
<img width="1258" alt="" src="https://user-images.githubusercontent.com/14961526/156218808-91c37651-6166-43c4-8fd7-45cab64e166f.png">
