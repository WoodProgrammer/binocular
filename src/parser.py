import re

SERVICE_REGEX="Chain KUBE-SVC"

class Parser(object):

    def __init__(self):
        self.chains = []

    def get_svc_chain_names(self, iptable_chain_file):

        ## This function is responsible to fetch values from the iptable chain files
        with open(iptable_chain_file, "r") as chain_file:
            content = chain_file.readlines()
            for line in content:
                if re.search(SERVICE_REGEX, line): #"(?i)Chain" in line:
                    self.chains.append(line)