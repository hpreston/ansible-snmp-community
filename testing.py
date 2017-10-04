from pysnmp.hlapi import *
import unittest


class SnmpTest(unittest.TestCase):
    def test_read_only(self):
        print "Executing test {}".format(self)
        #self.assertIsInstance(test, int)


        iterator = getCmd(SnmpEngine(),
                          CommunityData('r3@d0nly'),
                          UdpTransportTarget(('127.0.0.1', 1161)),
                          ContextData(),
                          ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysName', 0)))

        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

        if errorIndication:  # SNMP engine errors
            print(errorIndication)
        else:
            if errorStatus:  # SNMP agent errors
                print('%s at %s' % (errorStatus.prettyPrint(), varBinds[int(errorIndex)-1] if errorIndex else '?'))
            else:
                for varBind in varBinds:  # SNMP response contents
                    print(' = '.join([x.prettyPrint() for x in varBind]))
        self.assertIsInstance(varBinds, list)

unittest.main()
