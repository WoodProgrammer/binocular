import logging
from kubernetes import client, config

class EKS(object):

    def __init__(self):
        config.load_kube_config()
        self.v1 = client.CoreV1Api()

    def findNodes(self, label_key, label_value, node_count, entire_scope=False, namespace="default", ):

        nodeList = []
        ret = self.v1.list_namespaced_pod(namespace=namespace, label_selector="{}={}".format(label_key,label_value))
        for item in ret.items:
            nodeList.append(item.spec.node_name)

        if entire_scope == False:
            data = nodeList
        else:
            data = nodeList[:-node_count]
        
        return data