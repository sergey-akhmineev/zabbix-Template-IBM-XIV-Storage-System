#!/usr/bin/env python3
# -*- coding: utf-8 -*

from pyxcli.client import XCLIClient
import json, sys


# Variable Arguments

ibm_user = sys.argv[1]
ibm_pass = sys.argv[2]
ibm_host_ip = sys.argv[3]

# Connect SSL to XIV - Storage
xcli_client = XCLIClient.connect_ssl(ibm_user, ibm_pass, ibm_host_ip)

result_dict = {}


# CMD commands

ups = xcli_client.cmd.ups_list().as_list

result_dict ['ups'] = ups

ats = xcli_client.cmd.ats_list().as_list

result_dict ['ats'] = ats

cna = xcli_client.cmd.cna_list().as_list

result_dict ['cna'] = cna

cpu = xcli_client.cmd.cpu_list().as_list

result_dict ['cpu'] = cpu

dimm = xcli_client.cmd.dimm_list().as_list

result_dict ['dimm'] = dimm

disk = xcli_client.cmd.disk_list().as_list

result_dict ['disk'] = disk

fan = xcli_client.cmd.fan_list().as_list

result_dict ['fan'] = fan

fc_port = xcli_client.cmd.fc_port_list().as_list

result_dict ['fc_port'] = fc_port

mm = xcli_client.cmd.mm_list().as_list

result_dict ['mm'] = mm

psu = xcli_client.cmd.psu_list().as_list

result_dict ['psu'] = psu

switch = xcli_client.cmd.switch_list().as_list

result_dict ['switch'] = switch

result_dict_json = json.dumps(result_dict)

print(result_dict_json)

