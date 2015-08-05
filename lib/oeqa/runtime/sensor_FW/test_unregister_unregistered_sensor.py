'''Verify unregistered sensor can't be unregistered'''
import os
from oeqa.utils.helper import get_files_dir
from oeqa.oetest import oeRuntimeTest

class TestUnregisterUnregisteredSensor(oeRuntimeTest):
    '''Verify sensor can't be unregistered if it's not registered'''
    def testUnregisterUnregisteredSensor(self):
        '''Verify sensor can't be unregistered if it's not registered'''
        mkdir_path = "mkdir -p /opt/sensor-test/apps/"
        (status, output) = self.target.run(mkdir_path)
        copy_to_path = os.path.join(get_files_dir(), 'test_unregister_unregistered_sensor')
        (status, output) = self.target.copy_to(copy_to_path, "/opt/sensor-test/apps/")
        client_cmd = "/opt/sensor-test/apps/test_unregister_unregistered_sensor"
        (status, output) = self.target.run(client_cmd)
        print output
        self.assertEqual(status, 1, msg="Error messages: %s" % output)
