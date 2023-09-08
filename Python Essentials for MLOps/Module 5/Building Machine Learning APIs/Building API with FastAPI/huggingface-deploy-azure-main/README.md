# MLOps deployment to Azure Container Apps

_Take advantage of insta-scaling for live inferencing_

This repository and its examples are part of the [MLOps Coursera specialization offered by Duke University](https://www.coursera.org/specializations/mlops-machine-learning-duke)

Learn how to deploy an ML container with FastAPI and deploy it to [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/overview?WT.mc_id=academic-0000-alfredodeza) with GitHub Actions. This repository gives you a good starting point with a Dockerfile, GitHub Actions workflow, and Python code.

## Generate a PAT

The access token will need to be added as an Action secret. [Create one](https://github.com/settings/tokens/new?description=Azure+Container+Apps+access&scopes=write:packages) with enough permissions to write to packages.

## Create an Azure Service Principal

You'll need the following:

1. An Azure subscription ID [find it here](https://portal.azure.com/#view/Microsoft_Azure_Billing/SubscriptionsBlade) or [follow this guide](https://docs.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id)
1. A Service Principal with the following details the AppID, password, and tenant information. Create one with: `az ad sp create-for-rbac -n "REST API Service Principal"` and assign the IAM role for the subscription. Alternatively set the proper role access using the following command (use a real subscription id and replace it):

```
az ad sp create-for-rbac --name "CICD" --role contributor --scopes /subscriptions/$AZURE_SUBSCRIPTION_ID --sdk-auth
``` 


## Azure Container Apps

Make sure you have one instance already created, and then capture the name and resource group. These will be used in the workflow file.

## Change defaults 

Make sure you use 2 CPU cores and 4GB of memory per container. Otherwise you may get an error because loading HuggingFace with FastAPI requires significant memory upfront.

## Gotchas

There are a few things that might get you into a failed state when deploying:

* Not having enough RAM per container
* Not using authentication for accessing the remote registry (ghcr.io in this case). Authentication is always required
* Not using a PAT (Personal Access Token) or using a PAT that doesn't have write permissions for "packages".
* Different port than 80 in the container. By default Azure Container Apps use 80. Update to match the container.

If running into trouble, check logs in the portal or use the following with the Azure CLI:

```
az containerapp logs  show  --name $CONTAINER_APP_NAME --resource-group $RESOURCE_GROUP_NAME --follow
```

Update both variables to match your environment

## API Best Practices

Although there are a few best practices for using the FastAPI framework, there are many different other suggestions to build solid HTTP APIs that can be applicable anywhere. 

### Use HTTP Error codes
The HTTP specification has several error codes available. Make use of the appropriate error code to match the condition that caused it. For example the `401` HTTP code can be used when access is unauthorized. You shouldn't use a single error code as a catch-all error.

Here are some common scenarios associated with HTTP error codes:

- `400 Bad request`: Use this to indicate a schema problem. For example if the server expected a string but got an integer
- `401 Unauthorized`: When authentication is required and it wasn't present or satisfied
- `404 Not found`: When the resource doesn't exist

Note that it is a good practice to use `404 Not Found` to protect from requests that try to find if a resource exists without being authenticated. A good example of this is a service that doesn't want to expose usernames unless you are authenticated.


### Accept request types sparingly

| GET | POST | PUT | HEAD|
|---|---|---|---|
| Read Only | Write Only | Update existing | Does it exist? |



### Chapter Quiz

1. Question 1
When it is a good opportunity to write a single file Python script?

When automating a task that doesn't need many inputs and it can work without dependencies (answer)

2. Question 2
What is a module from the Python standard library you can use to look at arguments passed into a script?

sys.argv

3. Question 3
When is it a good time to use a command-line tool framework like ArgParse?

When wanting to handle different options, values, and flags

4. Question 4
What is a good way to use external dependencies in a command-line tool?

Declaring them in a setup.py file that can optionally read them from requirements.txt 

5. Question 5
When packaging a Python command-line tool, does the code need to be in a directory? Or can it be a single file?

It can be both. There is no hard requirement when packaging a tool.

6. Question 6
What are some of the key differences between the Click framework and the Argparse framework for building command-line tools?

The Click Python framework is designed to be more user-friendly than the argparse framework. It also offers more features, and it is easier to extend.

7. Question 7
What are some benefits of using GitHub Actions?

Ability to automate tasks

Easily create and share workflows

Integrate with other services 

Access to a community of users

8. Question 8
What are two benefits of using the Flask framework?

It is an easy framework to use for building HTTP APIs

It is well supported by the community as one of the most popular frameworks for Python

9. Question 9
What is one good reason to use the FastAPI framework?

It uses type hints that allow to detect common errors in HTTP APIs when handling requests

10. Question 10
What are common usages of POST GET and PUT HTTP requests?

POST is for creating a resource

GET is for read-only requests, usually to retrieve data

PUT is to update an existing resource



