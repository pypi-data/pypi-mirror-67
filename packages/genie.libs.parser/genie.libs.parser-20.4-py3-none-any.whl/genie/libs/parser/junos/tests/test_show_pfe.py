# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.junos.show_pfe import ShowPfeStatisticsTraffic

#=========================================================
# Unit test for show pfe statistics traffic
#=========================================================
class test_show_pfe_statistics_traffic(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    maxDiff = None

    golden_parsed_output_1 = {
        "pfe-statistics": {
            "pfe-chip-statistics": {
                "input-checksum": "0",
                "output-mtu": "0"
            },
            "pfe-hardware-discard-statistics": {
                "bad-route-discard": "962415",
                "bits-to-test-discard": "0",
                "data-error-discard": "0",
                "fabric-discard": "0",
                "info-cell-discard": "0",
                "invalid-iif-discard": "0",
                "nexthop-discard": "0",
                "stack-overflow-discard": "0",
                "stack-underflow-discard": "0",
                "tcp-header-error-discard": "0",
                "timeout-discard": "0",
                "truncated-key-discard": "0"
            },
            "pfe-local-protocol-statistics": {
                "arp-count": "56818",
                "atm-oam-count": "0",
                "bfd-count": "82347033",
                "ether-oam-count": "0",
                "fr-lmi-count": "0",
                "hdlc-keepalive-count": "0",
                "isis-iih-count": "0",
                "lacp-count": "0",
                "ldp-hello-count": "3462026",
                "ospf-hello-count": "5732336",
                "ospf3-hello-count": "4146329",
                "ppp-lcp-ncp-count": "0",
                "rsvp-hello-count": "7040269",
                "unknown-count": "0"
            },
            "pfe-local-traffic-statistics": {
                "hardware-input-drops": "0",
                "pfe-input-packets": "184259247",
                "pfe-output-packets": "370506284",
                "software-input-control-drops": "0",
                "software-input-high-drops": "0",
                "software-input-low-drops": "0",
                "software-input-medium-drops": "0",
                "software-output-low-drops": "0"
            },
            "pfe-traffic-statistics": {
                "input-pps": "14",
                "output-pps": "16",
                "pfe-fabric-input": "0",
                "pfe-fabric-input-pps": "0",
                "pfe-fabric-output": "0",
                "pfe-fabric-output-pps": "0",
                "pfe-input-packets": "763584752",
                "pfe-output-packets": "728623201"
            }
        }
    }


    golden_output_1 = {'execute.return_value': '''
                show pfe statistics traffic
        Packet Forwarding Engine traffic statistics:
            Input  packets:            763584752                   14 pps
            Output packets:            728623201                   16 pps
            Fabric Input  :                    0                    0 pps
            Fabric Output :                    0                    0 pps
        Packet Forwarding Engine local traffic statistics:
            Local packets input                 :            184259247
            Local packets output                :            370506284
            Software input control plane drops  :                    0
            Software input high drops           :                    0
            Software input medium drops         :                    0
            Software input low drops            :                    0
            Software output drops               :                    0
            Hardware input drops                :                    0
        Packet Forwarding Engine local protocol statistics:
            HDLC keepalives            :                    0
            ATM OAM                    :                    0
            Frame Relay LMI            :                    0
            PPP LCP/NCP                :                    0
            OSPF hello                 :              5732336
            OSPF3 hello                :              4146329
            RSVP hello                 :              7040269
            LDP hello                  :              3462026
            BFD                        :             82347033
            IS-IS IIH                  :                    0
            LACP                       :                    0
            ARP                        :                56818
            ETHER OAM                  :                    0
            Unknown                    :                    0
        Packet Forwarding Engine hardware discard statistics:
            Timeout                    :                    0
            Truncated key              :                    0
            Bits to test               :                    0
            Data error                 :                    0
            TCP header length error    :                    0
            Stack underflow            :                    0
            Stack overflow             :                    0
            Normal discard             :               962415
            Extended discard           :                    0
            Invalid interface          :                    0
            Info cell drops            :                    0
            Fabric drops               :                    0
        Packet Forwarding Engine Input IPv4 Header Checksum Error and Output MTU Error statistics:
            Input Checksum             :                    0
            Output MTU                 :                    0

    '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowPfeStatisticsTraffic(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowPfeStatisticsTraffic(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

if __name__ == '__main__':
    unittest.main()
