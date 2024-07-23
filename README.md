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
