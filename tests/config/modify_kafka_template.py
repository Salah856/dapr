#!/usr/bin/python3
import sys

# This is a quick and dirty hack (with no additional dependacies) to work around that fact that the kafka
# helm chart doesn't support affinity for config jobs.
# We can remove it once https://github.com/helm/charts/pull/23544 is merged upstream
stdin_contents = sys.stdin.read()

for template in stdin_contents.split("---")[1:]:
    if "dapr-kafka-test-topic" in template:
        continue
    print("---", )
    print(template)
    if "dapr-kafka-config" in template:
        print("""      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
              - matchExpressions:
                - key: kubernetes.io/os
                  operator: In
                  values:
                  - linux
""")

