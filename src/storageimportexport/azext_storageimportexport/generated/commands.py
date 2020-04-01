# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_storageimportexport.generated._client_factory import cf_location
    storageimportexport_location = CliCommandType(
        operations_tmpl='azext_storageimportexport.vendored_sdks.storageimportexport.operations._location_operations#Lo'
        'cationOperations.{}',
        client_factory=cf_location)
    with self.command_group('storageimportexport location', storageimportexport_location,
                            client_factory=cf_location) as g:
        g.custom_command('list', 'storageimportexport_location_list')
        g.custom_show_command('show', 'storageimportexport_location_show')

    from azext_storageimportexport.generated._client_factory import cf_job
    storageimportexport_job = CliCommandType(
        operations_tmpl='azext_storageimportexport.vendored_sdks.storageimportexport.operations._job_operations#JobOper'
        'ations.{}',
        client_factory=cf_job)
    with self.command_group('storageimportexport job', storageimportexport_job, client_factory=cf_job) as g:
        g.custom_command('list', 'storageimportexport_job_list')
        g.custom_show_command('show', 'storageimportexport_job_show')
        g.custom_command('create', 'storageimportexport_job_create')
        g.custom_command('update', 'storageimportexport_job_update')
        g.custom_command('delete', 'storageimportexport_job_delete')

    from azext_storageimportexport.generated._client_factory import cf_bit_locker_key
    storageimportexport_bit_locker_key = CliCommandType(
        operations_tmpl='azext_storageimportexport.vendored_sdks.storageimportexport.operations._bit_locker_key_operati'
        'ons#BitLockerKeyOperations.{}',
        client_factory=cf_bit_locker_key)
    with self.command_group('storageimportexport bit-locker-key', storageimportexport_bit_locker_key,
                            client_factory=cf_bit_locker_key) as g:
        g.custom_command('list', 'storageimportexport_bit_locker_key_list')