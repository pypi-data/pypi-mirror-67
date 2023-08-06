#
# Tester for Radware's configurators
#
# @author: Nofar Livkind, Radware

from api import AlteonDeviceConnection
from radware.alteon.client import AlteonClient
from radware.alteon.beans.PipNewCfgTable import *
from slb_pip import *
from l2_vlan import *
from system_time_date import *

alteon_client_params = dict(
        validate_certs=False,
        user='admin',
        password='admin1',
        https_port=443,
        server='10.175.116.185',
        timeout=15,
)

connection = AlteonDeviceConnection(**alteon_client_params)
mng_configurator = SystemTimeDateConfigurator(connection)
print("Lets start our tester!")


mng_params = SystemTimeDateParameters()
mng_params.ntp_primary_ip4 = '2.2.2.2'
mng_params.ntp_state = EnumAgNewCfgNTPService.enabled

print("Start ...")

mng_configurator.update(mng_params, True)

