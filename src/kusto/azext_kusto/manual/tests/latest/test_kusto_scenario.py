def setup_scenario(test, rg):
    test.kwargs.update({
        'eventhub_namespace': test.create_random_name(prefix='codegenlivetest', length=20),
        'eventhub_name': test.create_random_name(prefix='livetest', length=15)
    })
    test.cmd('az eventhubs namespace create --name {eventhub_namespace} -g {rg}')
    test.cmd('az eventhubs eventhub create --name {eventhub_name} --namespace-name {eventhub_namespace} -g {rg}')

def cleanup_scenario(test, rg):
    try:
        test.cmd('az eventhubs eventhub delete --name {eventhub_name} --namespace-name {eventhub_namespace} -g {rg}')
        test.cmd('az eventhubs namespace delete --name {eventhub_namespace} -g {rg}')
    except:
        pass