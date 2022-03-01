# Experiment Settings

## Local
- Device: `MAC Mini M1 (2020)` (8 Core CPU + 16 GB RAM)
- Used for: FastAPI, Redis Broker

## Remote
- Device: `Intel(R) Xeon(R) Silver 4214 CPU @ 2.20GHz` x 48 + 128 GB RAM + TITAN RTX (24 GB) x 1
- Used for: Celery Worker, Triton Server

# Experimental Results

## Peak Concurrency = 1
| Name | Average (ms)  | Min (ms)  |  Max (ms) | RPS (Range)  |
|:---:|:---:|:---:|:---:|:---:|
| without Triton  | 57  |  38 | 320  |  16 ~ 18 |
| with  Triton  |   |   |   |   |

#### without Triton Server
<img width="1268" alt="스크린샷 2022-03-02 오전 12 20 44" src="https://user-images.githubusercontent.com/14961526/156196352-e568fc57-f60b-46de-a3bd-9df692ffc842.png">
<img width="1254" alt="스크린샷 2022-03-02 오전 12 21 05" src="https://user-images.githubusercontent.com/14961526/156196414-8023281b-6ffc-4635-b5bd-8ad63bf7f0b1.png">

#### with Triton Server
TBD

## Peak Concurrency = 10

#### without Triton Server
TBD

#### with Triton Server
TBD

## Peak Concurrency = 30

#### without Triton Server
TBD

#### with Triton Server
TBD
