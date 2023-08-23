# direct-vpc-egress-for-cloud-run

This repository contains a sample app to test the direct vpc egress for cloud run setup.

The sample app contains the below endpoints.

- `/` - Dummy endpoint to check the container health
- `/external` - Calls the external endpoint `https://ipecho.net/plain` and returns the IP address of IGW
- `/internal` - Calls the internal service endpoint, and the internal endpoint value is passed in the environment variable

Build and push the container image to the GCP artifact registry and deploy the image to the cloud-run service.