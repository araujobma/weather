## Weather Data Gathering System

System to collect Open Weather API information about cities weather when the user sends a request.

## Tools, database and frameworks used

### FastAPI Framework

#### Reason for Choice:

- Ease of Use and Performance: FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints. It is designed to be easy to use and has automatic interactive API documentation (OpenAPI).
- Asynchronous Capabilities: It allows for asynchronous request handling, making it suitable for handling multiple requests simultaneously, which is crucial for an API that deals with external data fetching.
- Developer Productivity: FastAPI increases the speed of development and reduces errors by providing detailed error messages and auto-completion in many editors.

### PostgreSQL Database

#### Reason for Choice:

- Reliability and Robustness: PostgreSQL is a powerful, open-source object-relational database system known for its robustness and reliability.
- Scalability and Performance: It can handle large volumes of data and complex queries efficiently.

### Celery

#### Reason for Choice:

- Distributed Task Queue: Celery is an asynchronous task queue/job queue based on distributed message passing. It is focused on real-time operation but supports scheduling as well.
- Concurrency: It allows the handling of multiple concurrent requests to the Open Weather API, ensuring that the service can scale and handle high loads.
- Ease of Integration: Celery integrates seamlessly with FastAPI and can be configured to use various message brokers.

### RabbitMQ

#### Reason for Choice:

- Message Broker: RabbitMQ is a robust, flexible, and easy-to-use message broker that Celery supports. It ensures reliable delivery of tasks and can handle a large number of messages efficiently.
- Performance: RabbitMQ is known for its high performance and low latency, which is crucial for real-time task processing.

### Pytest

#### Reason for Choice:

- Testing Framework: Pytest is a mature full-featured Python testing tool that helps write better programs. It is used for writing simple as well as scalable test cases.
- Ease of Use: Pytest is simple to start with and supports fixtures for managing setups and teardowns.
- Extensibility: It is highly extensible and supports plugins, which can be used to add functionalities such as parallel test execution.

### Docker and Docker Compose

#### Reason for Choice:

- Containerization: Docker allows to package the application and its dependencies into a container, ensuring that it runs consistently across different environments.
- Simplified Deployment: Docker Compose helps in defining and running multi-container Docker applications. With a single command, you can set up the entire environment, including FastAPI, PostgreSQL, Celery, and RabbitMQ.
- Isolation and Consistency: Containers provide an isolated environment, ensuring that application behaves the same way in development, testing, and production.

### Docker Installation Ubuntu 20.04+

Remove conflicts:

```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

Add apt respository:

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
 "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
 $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
 sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

Install:

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

For running docker without being superuser: https://docs.docker.com/engine/install/linux-postinstall/

Test:

```bash
docker run hello-world
```

### Test and Run Application

At this point, you should have inserted your Open Weather API KEY in the

.env file:

```bash
API_KEY=<Your api key here>
```

#### Test

To run tests type:

```bash
make run_test
# that executes these commands:
# docker compose down
# docker compose up --build test
# docker compose down
```

#### Run App

To run app type:

```bash
make run
# that executes this command:
# docker compose up -d --build web

```

To stop app type:

```bash
make stop
# that executes this command:
# docker compose down

```
