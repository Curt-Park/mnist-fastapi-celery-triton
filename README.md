You can see the previous work from:
- https://github.com/Curt-Park/producer-consumer-fastapi-celery
- https://github.com/Curt-Park/triton-inference-server-practice (00-quick-start)

# Benchmark FastAPI + Celery with / without Triton

## with Triton Server
<img width="812" alt="" src="https://user-images.githubusercontent.com/14961526/156224708-9662b513-8faa-47be-b1eb-1564b1bcf4f8.png">

## without Triton Server
<img width="823" alt="" src="https://user-images.githubusercontent.com/14961526/156224736-10e8ba23-3595-42ec-869c-cecc8c2f928c.png">

## Benchmark Results
See [Benchmark Results](/benchmark)


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
Install [Redis](https://redis.io/topics/quickstart) & [Docker](https://docs.docker.com/engine/install/),
and run the following commands:

```bash
$ make triton     # run triton server
$ make broker     # run redis broker
$ make worker     # run celery worker
$ make api        # run fastapi server
$ make dashboard  # run dashboard that monitors celery
```

#### Server (Option 2 - Docker Compose available on GPU devices)
Install [Docker](https://docs.docker.com/engine/install/) & [Docker Compose](https://docs.docker.com/compose/install/),
and run the following command:

```bash
$ docker-compose up
```

#### [Optional] Additional Triton Servers
You can start up additional Triton servers on other devices.

```bash
$ make triton
```

#### [Optional] Additional Workers
You can start up additional workers on other devices.

```bash
$ export BROKER_URL=redis://redis-broker-ip:6379    # default is localhost
$ export BACKEND_URL=redis://redis-backend-ip:6379  # default is localhost
$ export TRITON_SERVER_URL=http://triton-server-ip:9000   # default is localhost
$ make worker
```

* NOTE: Worker needs to run on the machine which Triton runs on due to shared memory settings.

#### Dashboard for Celery (Flower)
http://0.0.0.0:5555/
![image](https://user-images.githubusercontent.com/14961526/154842930-70c54154-cf94-4368-bd46-fa43bd232d35.png)

## Load Test (w/ Locust)

#### Execute Locust
```bash
$ make load  # for load test without Triton
or
$ make load-triton  # for  load test with Triton
```

#### Open http://0.0.0.0:8089
Type url for the API server.

<img width="1272" alt="" src="https://user-images.githubusercontent.com/14961526/156191413-be5a4366-c90b-4ceb-99ce-3f4c978f709c.png">


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
