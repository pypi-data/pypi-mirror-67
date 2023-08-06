# DNS Crawling

This repository contains all the code/ documentation related to collecting information from DNS, launching scans based off of it and making it available to other projects within Shodan.


## Scheduled Tasks

The following tasks are performed periodically to keep DNSDB up to date. They are deployed to Kubernetes and are defined in **k8.yml**:

* **update-dnsdb-type-a**: ever 5 days we grab all the A/ AAAA records
* **update-dnsdb-all**: every 7 days we try to grab all common DNS records (A, AAAA, NS, MX, etc.)

## Deploying to Kubernetes

Currently, the **k8s-production** Kubernetes cluster is used to run all DNS crawling operations. To deploy the latest configuration to the cluster run the command:

```bash
kubectl apply -f k8.yml
```

> Note: Make sure any new data collection tasks are ran in the **data-collection** node pool.