
# Lab 1: Build CI/CD Solution

## Overview

In this lab, you will learn how to implement Continuous Integration (CI) and Continuous Deployment (CD) processes using a Makefile and the Click test runner. You will perform linting, formatting, refactoring, and testing on a Python script to ensure its quality and functionality.

## Goals

By the end of this lab, you will:

1. Understand the importance of CI/CD processes in MLOps.
2. Learn how to use a Makefile for automating linting, formatting, refactoring, and testing.
3. Gain experience in writing tests for command-line tools using the Click test runner.

## Getting Started

Before you begin, watch the videos and read the resources in this module to familiarize yourself with CI/CD, Makefiles, and the Click test runner. These materials will help you navigate through the lab tasks and achieve the desired outcomes.

### Lab Tasks/Users/taoheedking/Documents/ML Ops Specialization/DevOps, DataOps, MLOps

1. Source the virtual environment:\
   `source /home/coder/venv/bin/activate`
2. Run the following steps of the Makefile:
   - `make lint`
   - `make format`
   - `make refactor`
   - `make test`

**Reflection Question**: Why does `refactor` combine `lint` and `format`? (Questions relates to Pylint)
Answer: 
- Lint is the process of analyzing code to identify potential issues, style issues, and programming error.
- Format ensures a consistent and uniform code style throughout a project.
- Refactor combines lint and format to improve code quality, consistency, automation, readability, and maintainability.

3. Run the following command-line tool and then write a test for it using the Click test runner:
   - Write a test for the `add_cli` functionality of the `main.py` function in the `test_main.py` test file.
   - Use the test for `./main.py --help` as a guide.

**Reflection Question**: How could you use this style of testing to build MLOps tools quickly? (Questions relates to 'click' library, particularly the testing portion)
Answer:
- Using a tool like click to build a command-line interface (CLI) for your MLOps (Machine Learning Operations) tools is a practical approach to streamline your workflow. It allows you to create user-friendly interfaces for managing machine learning pipelines, model deployments, data processing, and more.
- Click test runner makes it easy to create and automate tests for functions through the command line


### References

You can view this lab in GitHub here: [Coursera-MLOPs-Foundations-Lab-1-CICD](https://github.com/nogibjj/Coursera-MLOPs-Foundations-Lab-1-CICD)


### Notes

Task 2- Running Makefile: 
In order for you to be able to run the make command, make sure you are in the directory the Makefile is located in. 

Task 3: Creating Tests for Command Line Interface apps using 'click' module
In order for you to create a test for the function, you must instantiate the CliRunner() function (which is a part of the click.testing library) and assign it to a variable called runner. 

CLI apps testing resources
https://click.palletsprojects.com/en/8.1.x/testing/
https://wangonya.com/blog/testing-click-with-pytest/