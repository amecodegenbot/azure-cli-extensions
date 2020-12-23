# EXAMPLE: KustoDataConnectionValidation
def step_data_connection_event_hub_data_connection_val(test, rg, checks=None):
    test.cmd('az kusto data-connection event-hub data-connection-validation '
             '--cluster-name "{myCluster}" '
             '--database-name "KustoDatabase8" '
             '--data-connection-name "{myDataConnection}" '
             '--consumer-group "$Default" '
             '--event-hub-resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.EventHub/namespaces/{eventhub_namespace}/eventhubs/{eventhub_name}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: KustoDataConnectionsCreateOrUpdate
def step_data_connection_event_hub_create(test, rg, checks=None):
    test.cmd('az kusto data-connection event-hub create '
             '--cluster-name "{myCluster}" '
             '--data-connection-name "{myDataConnection}" '
             '--database-name "KustoDatabase8" '
             '--location "southcentralus" '
             '--consumer-group "$Default" '
             '--event-hub-resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.EventHub/namespaces/{eventhub_namespace}/eventhubs/{eventhub_name}" '
             '--resource-group "{rg}"',
             checks=[])
 
 
def step_data_connection_event_hub_update(test, rg, checks=None):
    test.cmd('az kusto data-connection event-hub update '
             '--cluster-name "{myCluster}" '
             '--data-connection-name "{myDataConnection}" '
             '--database-name "KustoDatabase8" '
             '--location "southcentralus" '
             '--consumer-group "$Default" '
             '--event-hub-resource-id "/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.EventHub/namespaces/{eventhub_namespace}/eventhubs/{eventhub_name}" '
             '--resource-group "{rg}"',
             checks=[])            