import json
import subprocess

def lambda_handler(event, context):
    proc = subprocess.Popen(
        ['./bin/VideoStitcher', '-h'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    returncode = proc.wait()

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                'returncode': returncode,
            }
        ),
    }
