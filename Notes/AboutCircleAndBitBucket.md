
| **Test Type**   | **What It Tests**                                 | **Speed**  | **Complexity** | **Common Tools**                    | **When to Run**                            |
| --------------- | ------------------------------------------------- | ---------- | -------------- | ----------------------------------- | ------------------------------------------ |
| **Unit**        | Single function/module in isolation               | ⚡ Fast     | 🟢 Low         | `pytest`, `unittest`, `Jest`        | Local, CI on every push                    |
| **Integration** | Interaction between components (e.g. API + DB)    | ⚡⚡ Medium  | 🟡 Medium      | `pytest + requests`, `Supertest`    | Local, CI, staging                         |
| **End-to-End**  | Full system flow through UI or API                | 🐢 Slow    | 🔴 High        | `Playwright`, `Cypress`, `Selenium` | CI (light), staging (full), post-deploy QA |
| **Smoke**       | Basic functionality: "Does it start and respond?" | ⚡ Fast     | 🟢 Low         | `curl`, shell scripts, `Pingdom`    | Staging, prod (health check)               |
| **Performance** | Speed, scalability, and resource usage under load | 🐘 Slowest | 🔴 High        | `Locust`, `k6`, `JMeter`            | Staging, pre-prod stress testing           |


### CircleCI is a service that we can connect to our repo (BitBucket). 

Circle will run tests for us whenever we push to a branch that we have told it to run tests for.

We tell circle what our environment will be. This could be linux, windows, or a docker image. 

Circle will then read from a `config.yml file` that is inside a `.circleci` folder. 

This config can do things like seeding the database, installing dependencies, and running scripts (like pytest)

jinja
https://jinja.palletsprojects.com/en/stable/


Evelyn Klein
11:06 AM
https://support.testrail.com/hc/en-us/articles/7077083596436-Introduction-to-the-TestRail-API

https://jvns.ca/blog/brag-documents/

