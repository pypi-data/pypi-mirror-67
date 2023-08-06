# SageUp
Interactive CLI tool for creating a SageMaker notebook instance from terminal, getting signed URL and opening it in browser.

![Screenshot](https://raw.githubusercontent.com/imankamyabi/sageup/master/images/sageup-demo.gif)


## Installation:
```shell
pip install sageup
```

## Usage

### Run
Starts an interactive session to create a SageMaker notebook instance and launch it in browser

```shell
sageup run
```

## Notes:
Default IAM role has full access to SageMaker and S3. Use a custom IAM role if need granular access, more security and protection against accidental change of resources by the notebook.

More features coming soon!

Author: Iman Kamyabi
 
Feedback: contact@imankamyabi.com