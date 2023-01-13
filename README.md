# python-backend-tasks

Tasks for candidates on the Python Backend Developer role

## Getting started

This repository contains tasks to perform by candidates on the Python Backend Developer role.

Please find below the [Tasks](#Task) and [Submitting process and requirements](#Submit your task-response). All required input data are located in the main branch.

Ask any questions related to Task or Submittion by creating an [**Issue**](https://gitlab.com/p-a-system-team/data-engineer-june-2022/-/issues)


## Submit your tasks-response

1. Clone this repository
2. Create new branch named as __your-surname-name__. Please, do not use nickname, accounts, etc. as the brach name will be used to match with your CV.
3. In this brach locate your response, including code and other artifacts. Please, locate any text answer/comments for a task in `README.md` of corresponding task-folder. Also `README.md` _must not be empty_, please put there meaningful description of commited artifacts, required configuration and running procedure.
4. Request access for a developer role to this project according to [gitlab documentation](https://docs.gitlab.com/ee/user/project/members/#request-access-to-a-project)
5. Push your brach to this repository

## Tasks

### Task 1

You are given with a container hosting Image Classification model. The contenerized application (further _modelCLS App_) supports RabbitMQ interface to recieve image file and its metadata and to send back results of image classification.

The sources of this app is [here][1.1]:

Please, implement the second application (platform App) with the following requirements:

1. The application should:
    1. read image files from configured filesystem directory
    2. send each images via RabbitMQ queue to running _modelCLS App_
    3. read via RabbitMQ queue _modelCLS App_ responces
    4. write responces into _SQLite_ db
2. The application should initialize RabbitMQ queues required in described workflow
3. The application should follow the message structure which is supported by given _modelCLS App_ See implentation in the `pripabox-modelcls\modelcls\queues.py`. Particularly, images should be base64-encoded.
3. The application should be containerized and be able to run via _docker-composer_
4. The application should log each step of the decsribed workflow into file.


**Expected artifacts in your submittion**:
1. Source code of implemented application.
2. `docker-composer.yaml` which with the `docker-compose up` command makes both _platform_ and _modelCLS application_ up and starts processing of all images in the configured directory
3. Log file of test run
4. SQLlite db file with a image classification results
	
[1.1]:../pripabox-modelcls.zip


## Contributing
This repository is suppoused to be contributed by candidates on the team role with responses on suggested tasks.
Making contribution to this repository each candidates acknowledge that his contributions are subject of parent repository license stated in License section below.

## License
MIT License

Copyright (c) 2022 P-A-Systems

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

