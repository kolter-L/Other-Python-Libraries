### CircleCI is a service that we can connect to our repo (BitBucket). 

Circle will run tests for us whenever we push to a branch that we have told it to run tests for.

We tell circle what our environment will be. This could be linux, windows, or a docker image. 

Circle will then read from a `config.yml file` that is inside a `.circleci` folder. 

This config can do things like seeding the database, installing dependencies, and running scripts (like pytest)