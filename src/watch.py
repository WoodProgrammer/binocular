from kubernetes import client, config, watch
import asyncio

async def services():
    config.load_kube_config()

    v1 = client.CoreV1Api()
    w = watch.Watch()
    for event in w.stream(v1.list_service_for_all_namespaces):
        print("Event: %s %s %s" % (event['type'], event['object'].kind, event['object'].metadata.name))
        await asyncio.sleep(0) 

ioloop = asyncio.get_event_loop()

ioloop.create_task(services())
ioloop.run_forever()
