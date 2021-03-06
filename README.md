# lambda-docker-prototype

Prototype of a project that uses AWS Lambda, Docker, SAM, Python.
Inside of it you can found two functions.
One of the functions is a simple "Hello World".
The other one is a function that have a custom third-part image, that execute an random binary.

I don't know why this repo exists, I'm just playing with AWS Lambda to see its power.

## Getting started

### First time

Install AWS CLI
```bash
sudo apt install awscli
```

Install SAM following (this steps)[https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html].

Configure AWS. Put your AWS User credentials.
```bash
aws configure
```

Configure your project and deploy it:
```bash
sam deploy --guided
```
### Modify

You can open `functions/your_function/app.py` file and change the behavior of the functions.
Each folder inside `functions` folder is like a sub project, with its own Dockerfile that describe its image.

### Build

Just run:
```bash
sam build
```
This build your images base on the Dockerfile define in each function.

### Test locally

If you want to test your HelloWorldFunction function:
```bash
sam build
sam local invoke HelloWorldFunction --event events/event.json
```

The SAM CLI can also emulate your application's API. Use the `sam local start-api` to run the API locally on port 3000.

```bash
sam local start-api
curl http://localhost:3000/hello
```

### Deploy

Just run:
```bash
sam deploy --guided
```

Or, if you already have an `samconfig.toml` file, run:
```bash
sam deploy
```

### Add a new function

In the `functions` directory, select `hello_world` and copy it next to it.
Then open `template.yaml` file and copy the `HelloWorldFunction` bundle.
Make your custom changes, modify the `events` section.
Modify `DockerContext`, change `./functions/hello_world` to the new location.
You can also put some custom `DockerTag`. It'll be the name of the image of that function.
You also have to add a repositoy to your `samconfig.toml` file. So, at your new deploy, run:
```bash
sam deploy --guided
```

### Unit tests

Tests are defined in the `tests` folder in this project. Use PIP to install the [pytest](https://docs.pytest.org/en/latest/) and run unit tests from your local machine.

```bash
pip install pytest pytest-mock --user
python -m pytest tests/ -v
```

### Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
aws cloudformation delete-stack --stack-name lambda-docker-prototype
```

## Miscellaneous

### Files and folders

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- functions - Code for the application's Lambda functions and Dockerfiles.
- events - Invocation events that you can use to invoke the function.
- tests - Unit tests for the application code. 
- template.yaml - Configuration of SAM, where you can define your resources. You must declare and configure all your Lambda functions here. The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.
- samconfig.toml - Another configuration file about the project.

### Fetch, tail, and filter Lambda function logs

To simplify troubleshooting, SAM CLI has a command called `sam logs`. `sam logs` lets you fetch logs generated by your deployed Lambda function from the command line. In addition to printing the logs on the terminal, this command has several nifty features to help you quickly find the bug.

`NOTE`: This command works for all AWS Lambda functions; not just the ones you deploy using SAM.

```bash
sam logs -n HelloWorldFunction --stack-name lambda-docker-prototype --tail
```

You can find more information and examples about filtering Lambda function logs in the [SAM CLI Documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-logging.html).
