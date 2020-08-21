# Useful resources

  * [Locust](https://locust.io/)
  * [Distributed Load Testing with Kubernetes (and Locust)](https://github.com/GoogleCloudPlatform/distributed-load-testing-using-kubernetes)

## Running the tests

You must follow these logical steps to ensure that you deploy Locust correctly, specifically for distributed mode, which this assumes.

`kustomize build dist/overlays/<env> | kubectl [-n <env>] apply -f -`

This will deploy the kustomization of the Kubernetes resource definitions for Locust in the environment specified by `<env>`.

Once deployed you should navigate to the webview on the master for Locust and check that there are either no workers connected. You should also find there are 0 worker pods. If you do see that there are workers connected to the master (which means they probably don't exist anymore now) you can delete the master pod and restart to ensure 0 worker pods are connected.

It is important that you do the above as it ensures that the master is flushed of older or unavailable workers when you start. Unfortunately Locust doesn't handle dieing workers very well or ephemeral workers and does not attempt to manage this process for you, so it's quite manual at present and why you must do this if you wish for Locust to run as you anticipate.

Once you have deployed this into the Kubernetes cluster and ensured no workers are connected to the master and no worker pods exists, then you can bump up the number of worker pods to the amount of replicas you wish to simulate your load with. To do this you should run the following:

`kubectl [-n <env>] scale deployment locust-worker --replicas <num>`

This will scale the number of replicas of the locust worker to the value specified by `<num>`. Once you have done this check on the web UI to ensure that the master now has `<num>` number of workers connected.

Once you have confirmed the correct number of workers exist and are connected to master you can start the test.