""" show_pfe.py

JunOs parsers for the following show commands:
    * show pfe statistics traffic
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, SchemaTypeError, Schema)

class ShowPfeStatisticsTrafficSchema(MetaParser):
    """ Schema for:
            * show pfe statistics traffic
    """

    schema = {
    "pfe-statistics": {
        "pfe-chip-statistics": {
            "input-checksum": str,
            "output-mtu": str
        },
        "pfe-hardware-discard-statistics": {
            "bad-route-discard": str,
            "bits-to-test-discard": str,
            "data-error-discard": str,
            "fabric-discard": str,
            "info-cell-discard": str,
            "invalid-iif-discard": str,
            "nexthop-discard": str,
            "stack-overflow-discard": str,
            "stack-underflow-discard": str,
            "tcp-header-error-discard": str,
            "timeout-discard": str,
            "truncated-key-discard": str
        },
        "pfe-local-protocol-statistics": {
            "arp-count": str,
            "atm-oam-count": str,
            "bfd-count": str,
            "ether-oam-count": str,
            "fr-lmi-count": str,
            "hdlc-keepalive-count": str,
            "isis-iih-count": str,
            "lacp-count": str,
            "ldp-hello-count": str,
            "ospf-hello-count": str,
            "ospf3-hello-count": str,
            "ppp-lcp-ncp-count": str,
            "rsvp-hello-count": str,
            "unknown-count": str
        },
        "pfe-local-traffic-statistics": {
            "hardware-input-drops": str,
            "pfe-input-packets": str,
            "pfe-output-packets": str,
            "software-input-control-drops": str,
            "software-input-high-drops": str,
            "software-input-low-drops": str,
            "software-input-medium-drops": str,
            "software-output-low-drops": str
        },
        "pfe-traffic-statistics": {
            "input-pps": str,
            "output-pps": str,
            "pfe-fabric-input": str,
            "pfe-fabric-input-pps": str,
            "pfe-fabric-output": str,
            "pfe-fabric-output-pps": str,
            "pfe-input-packets": str,
            "pfe-output-packets": str
        }
    }
}

class ShowPfeStatisticsTraffic(ShowPfeStatisticsTrafficSchema):
    """ Parser for:
            * show pfe statistics traffic
    """
    cli_command = 'show pfe statistics traffic'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Input  packets:            763584752                   14 pps
        p1 = re.compile(r'^Input +packets: +(?P<pfe_input_packets>\d+)'
            r' +(?P<input_pps>\d+) +pps$')

        # Output packets:            728623201                   16 pps
        p2 = re.compile(r'^Output +packets: +(?P<pfe_output_packets>\d+)'
            r' +(?P<output_pps>\d+) +pps$')

        #    Fabric Input  :                    0                    0 pps
        p3 = re.compile(r'^Fabric +Input +: +(?P<pfe_fabric_input>\d+)'
            r' +(?P<pfe_fabric_input_pps>\d+) +pps$')

        #    Fabric Output :                    0                    0 pps
        p4 = re.compile(r'^Fabric +Output +: +(?P<pfe_fabric_output>\d+)'
            r' +(?P<pfe_fabric_output_pps>\d+) +pps$')

        # Local packets input                 :            184259247
        p5 = re.compile(r'^Local +packets +input +: +(?P<pfe_input_packets>\d+)$')

        # Local packets output                :            370506284
        p6 = re.compile(r'^Local +packets +output +: +(?P<pfe_output_packets>\d+)$')

        # Software input control plane drops  :                    0
        p7 = re.compile(r'^Software +input +control +plane +drops +:'
            r' +(?P<software_input_control_drops>\d+)$')

        # Software input high drops           :                    0
        p8 = re.compile(r'^Software +input +high +drops +:'
            r' +(?P<software_input_high_drops>\d+)$')

        # Software input medium drops         :                    0
        p9 = re.compile(r'^Software +input +medium +drops +:'
            r' +(?P<software_input_medium_drops>\d+)$')

        # Software input low drops            :                    0
        p10 = re.compile(r'^Software +input +low +drops +:'
            r' +(?P<software_input_low_drops>\d+)$')

        # Software output drops               :                    0
        p11 = re.compile(r'^Software +output +drops +:'
            r' +(?P<software_output_low_drops>\d+)$')

        # Hardware input drops                :                    0
        p12 = re.compile(r'^Hardware +input +drops +:'
            r' +(?P<hardware_input_drops>\d+)$')

        # HDLC keepalives            :                    0
        p13 = re.compile(r'^HDLC +keepalives +: +(?P<hdlc_keepalive_count>\d+)$')

        # ATM OAM                    :                    0
        p14 = re.compile(r'^ATM +OAM +: +(?P<atm_oam_count>\d+)$')

        # Frame Relay LMI            :                    0
        p15 = re.compile(r'^Frame +Relay +LMI +: +(?P<fr_lmi_count>\d+)$')

        # PPP LCP/NCP                :                    0
        p16 = re.compile(r'^PPP +LCP/NCP +: +(?P<ppp_lcp_ncp_count>\d+)$')

        # OSPF hello                 :              5732336
        p17 = re.compile(r'^OSPF +hello +: +(?P<ospf_hello_count>\d+)$')

        # OSPF3 hello                :              4146329
        p18 = re.compile(r'^OSPF3 +hello +: +(?P<ospf3_hello_count>\d+)$')

        # RSVP hello                 :              7040269
        p19 = re.compile(r'^RSVP +hello +: +(?P<rsvp_hello_count>\d+)$')

        # LDP hello                  :              3462026
        p20 = re.compile(r'^LDP +hello +: +(?P<ldp_hello_count>\d+)$')

        # BFD                        :             82347033
        p21 = re.compile(r'^BFD +: +(?P<bfd_count>\d+)$')

        # IS-IS IIH                  :                    0
        p22 = re.compile(r'^IS-IS +IIH +: +(?P<isis_iih_count>\d+)$')

        # LACP                       :                    0
        p23 = re.compile(r'^LACP +: +(?P<lacp_count>\d+)$')

        # ARP                        :                56818
        p24 = re.compile(r'^ARP +: +(?P<arp_count>\d+)$')

        # ETHER OAM                  :                    0
        p25 = re.compile(r'^ETHER +OAM +: +(?P<ether_oam_count>\d+)$')

        # Unknown                    :                    0
        p26 = re.compile(r'^Unknown +: +(?P<unknown_count>\d+)$')

        # Timeout                    :                    0
        p27 = re.compile(r'^Timeout +: +(?P<timeout_discard>\d+)$')

        # Truncated key              :                    0
        p28 = re.compile(r'^Truncated +key +: +(?P<truncated_key_discard>\d+)$')

        # Bits to test               :                    0
        p29 = re.compile(r'^Bits +to +test +: +(?P<bits_to_test_discard>\d+)$')

        # Data error                 :                    0
        p30 = re.compile(r'^Data +error +: +(?P<data_error_discard>\d+)$')

        # TCP header length error    :                    0
        p31 = re.compile(r'^TCP +header +length +error +: +(?P<tcp_header_error_discard>\d+)$')

        # Stack underflow            :                    0
        p32 = re.compile(r'^Stack +underflow +: +(?P<stack_underflow_discard>\d+)$')

        # Stack overflow             :                    0
        p33 = re.compile(r'^Stack +overflow +: +(?P<stack_overflow_discard>\d+)$')

        # Normal discard             :               962415
        p34 = re.compile(r'^Normal +discard +: +(?P<bad_route_discard>\d+)$')

        # Extended discard           :                    0
        p35 = re.compile(r'^Extended +discard +: +(?P<nexthop_discard>\d+)$')

        # Invalid interface          :                    0
        p36 = re.compile(r'^Invalid +interface +: +(?P<invalid_iif_discard>\d+)$')

        # Info cell drops            :                    0
        p37 = re.compile(r'^Info +cell +drops +: +(?P<info_cell_discard>\d+)$')

        # Fabric drops               :                    0
        p38 = re.compile(r'^Fabric +drops +: +(?P<fabric_discard>\d+)$')

        # Input Checksum             :                    0
        p39 = re.compile(r'^Input +Checksum +: +(?P<input_checksum>\d+)$')

        # Output MTU                 :                    0
        p40 = re.compile(r'^Output +MTU +: +(?P<output_mtu>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Input  packets:            763584752                   14 pps
            m = p1.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-traffic-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # Output packets:            728623201                   16 pps
            m = p2.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-traffic-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            #    Fabric Input  :                    0                    0 pps
            m = p3.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-traffic-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            #    Fabric Output :                    0                    0 pps
            m = p4.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-traffic-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # Local packets input                 :            184259247
            m = p5.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-local-traffic-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # Local packets output                :            370506284
            m = p6.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-local-traffic-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # Software input control plane drops  :                    0
            m = p7.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {}).setdefault('pfe-local-traffic-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # Software input high drops           :                    0
            m = p8.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-local-traffic-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # Software input medium drops         :                    0
            m = p9.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-local-traffic-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # Software input low drops            :                    0
            m = p10.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {}).setdefault('pfe-local-traffic-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # Software output drops               :                    0
            m = p11.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-local-traffic-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # Hardware input drops                :                    0
            m = p12.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-local-traffic-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # HDLC keepalives            :                    0
            m = p13.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-local-protocol-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # ATM OAM                    :                    0
            m = p14.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-local-protocol-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # Frame Relay LMI            :                    0
            m = p15.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-local-protocol-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # PPP LCP/NCP                :                    0
            m = p16.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-local-protocol-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # OSPF hello                 :              5732336
            m = p17.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-local-protocol-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # OSPF3 hello                :              4146329
            m = p18.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-local-protocol-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # RSVP hello                 :              7040269
            m = p19.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-local-protocol-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # LDP hello                  :              3462026
            m = p20.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-local-protocol-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # BFD                        :             82347033
            m = p21.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-local-protocol-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # IS-IS IIH                  :                    0
            m = p22.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-local-protocol-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # LACP                       :                    0
            m = p23.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-local-protocol-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # ARP                        :                56818
            m = p24.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {}).setdefault('pfe-local-protocol-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # ETHER OAM                  :                    0
            m = p25.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-local-protocol-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # Unknown                    :                    0
            m = p26.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-local-protocol-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # Timeout                    :                    0
            m = p27.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-hardware-discard-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # Truncated key              :                    0
            m = p28.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-hardware-discard-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # Bits to test               :                    0
            m = p29.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-hardware-discard-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # Data error                 :                    0
            m = p30.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {}).setdefault('pfe-hardware-discard-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # TCP header length error    :                    0
            m = p31.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {}).setdefault('pfe-hardware-discard-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # Stack underflow            :                    0
            m = p32.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-hardware-discard-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # Stack overflow             :                    0
            m = p33.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-hardware-discard-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # Normal discard             :               962415
            m = p34.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-hardware-discard-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # Extended discard           :                    0
            m = p35.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-hardware-discard-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # Invalid interface          :                    0
            m = p36.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-hardware-discard-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # Info cell drops            :                    0
            m = p37.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-hardware-discard-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # Fabric drops               :                    0
            m = p38.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {}).setdefault('pfe-hardware-discard-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # Input Checksum             :                    0
            m = p39.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-chip-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

            # Output MTU                 :                    0
            m = p40.match(line)
            if m:
                entry = ret_dict.setdefault('pfe-statistics', {})\
                    .setdefault('pfe-chip-statistics', {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                continue

        return ret_dict
