You can see the previous work from:
- https://github.com/Curt-Park/producer-consumer-fastapi-celery
- https://github.com/Curt-Park/triton-inference-server-practice (00-quick-start)

# Benchmark FastAPI + Celery with / without Triton
<img width="844" alt="" src="https://user-images.githubusercontent.com/14961526/156115761-ed00f3ee-3bfe-4d48-aef5-77d9e8f4e28a.png">

## Preparation

#### 1. Setup packages
Install [Anaconda](https://docs.anaconda.com/anaconda/install/index.html) and execute the following commands:
```bash
$ make env        # create a conda environment (need only once)
$ source init.sh  # activate the env
$ make setup      # setup packages (need only once)
```

#### 2. Train a CNN model (Recommended on GPU)
```bash
$ source create_model.sh
```

#### 3. Check the model repository created
```bash
$ tree model_repository

model_repository
└── mnist_cnn
    ├── 1
    │   └── model.pt
    └── config.pbtxt

2 directories, 2 files
```

## How to play

#### Server (Option 1 - On your Local)
Install [Redis](https://redis.io/topics/quickstart), and run the following commands:

```bash
$ make broker     # run redis broker
$ make worker     # run celery worker
$ make api        # run fastapi server
$ make dashboard  # run dashboard that monitors celery
```

#### Server (Option 2 - Docker Compose)
Install [Docker](https://docs.docker.com/engine/install/) & [Docker Compose](https://docs.docker.com/compose/install/),
and run the following command:

```bash
$ docker-compose up
```

#### [Optional] Additional Workers
You can start up additional workers on other devices.

```bash
$ export BROKER_URL=redis://redis-broker-ip:6379
$ export BACKEND_URL=redis://redis-backend-ip:6379
$ make worker
```

#### Client

#### Option 1: In WebBrowser
http://0.0.0.0:8000/produce

#### Option 2: Test Client
Sending a number of requests simultaneously.

```bash
$ python src/client.py --n-req [N_REQUSTS]
```

#### Dashboard for Celery (Flower)
http://0.0.0.0:5555/
![image](https://user-images.githubusercontent.com/14961526/154842930-70c54154-cf94-4368-bd46-fa43bd232d35.png)


## Issue Handling

#### Redis Error 8 connecting localhost:6379. nodename nor servname provided, or not known.
`$ ulimit -n 1024`

#### Docker's `network_mode=bridge`degrades the network performance.
We recommend to use Linux server if you would like to run `docker-compose up`.

## For Developers

```bash
$ make setup-dev      # setup for developers
$ make format         # format scripts
$ make lint           # lints scripts
$ make utest          # runs unit tests
$ make cov            # opens unit test coverage information
```
