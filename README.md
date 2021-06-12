# Suse Cloud Foundation

* https://cloud.ibm.com/docs/blockchain-sw?topic=blockchain-sw-Removing-k8
* https://hub.docker.com/u/pixelpotato
* https://k3s.io/

````
kubectl describe pods | grep -i apparmor_parser
````

````
zypper install -t pattern apparmor
````

````
sudo curl -sfL https://get.k3s.io | K3S_KUBECONFIG_MODE="644" INSTALL_K3S_VERSION="v1.20.7+k3s1" sh -s -
````

````
kubectl port-forward po/go-helloworld-fcd468f98-qzczp 6111:6111 --address 0.0.0.0
````