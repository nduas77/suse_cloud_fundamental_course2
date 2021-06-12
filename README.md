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

````
kubectl expose deploy go-helloworld --port=6112 --target-port=6112
kubectl get svc
kubectl run test-$RANDOM --namespace=default --rm -it --image=alpine -- sh
wget -qO- 10.43.30.56:6112
````

````
kubectl get cm
kubectl create cm test-cm --from-literal=color=blue
kubectl describe cm test-cm
kubectl get secrets
kubectl create secret generic  test-sec --from-literal=color=red
kubectl get secrets
kubectl describe secrets test-sec
kubectl get secrets test-sec -o yaml
echo "cmVk" | base64 -d
````

````
kubectl get ns
kubectl create ns test-udacity
kubectl get po
kubectl get po -n test-udacity
kubectl create deploy [PARAMS] -n test-udacity
````