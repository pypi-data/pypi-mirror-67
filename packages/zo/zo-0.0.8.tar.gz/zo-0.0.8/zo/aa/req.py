# ! /usr/bin/python
# coding=utf-8
import re
from urllib.parse import unquote


def g_headers():
    aa = '''
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: en,en-US;q=0.9,zh-CN;q=0.8,zh;q=0.7
cache-control: max-age=0
cookie: ezCMPCCS=true; __cfduid=d2fd28047e63e913bac15f4f99425c5b11587948090; ezds=ffid%3D1%2Cw%3D1920%2Ch%3D1080; ezoadgid_164851=-1; ezoref_164851=; ezoab_164851=mod54; lp_164851=https://fccid.io/; ezovid_164851=407748798; ezovuuid_164851=1762afef-fb8b-4174-7ff0-050822e292a3; ezohw=w%3D1417%2Ch%3D946; pageViewCount=5; ezux_lpl_164851=1587971377025|f09cf1e2-cb1c-42aa-6e72-e4a95def8d6e|true; active_template::164851=pub_site.1587971454; ezopvc_164851=9; ezepvv=4108; ezovuuidtime_164851=1587971455
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: none
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36
'''
    aa = re.findall('(\w.*?):(.+)', aa)
    x = dict()
    for i in aa:
        x[i[0]] = re.sub('^ {1,}', '', i[1])
    for i in x:
        print('[%-20s] : %s' % (i, x[i]))
    print('- ' * 30)
    print(x)


def form_data_to_dict(v: str) -> dict:
    """
    Args:
        v: grantee_code=&product_code=...

    Returns:
        rst: dict
    """
    v = v.split('&')
    rst = {}
    for i in v:
        aa = i.split('=')
        rst[aa[0]] = unquote(aa[1])
    return rst


v2 = 'grantee_code=&product_code=&applicant_name=&grant_date_from=01%2F01%2F2020&grant_date_to=01%2F02%2F2020&comments=&application_purpose=&application_purpose_description=&grant_code_1=&grant_code_2=&grant_code_3=&test_firm=&application_status=&application_status_description=&equipment_class=&equipment_class_description=&lower_frequency=&upper_frequency=&freq_exact_match=on&bandwidth_from=&emission_designator=&tolerance_from=&tolerance_to=&tolerance_exact_match=on&power_output_from=&power_output_to=&power_exact_match=on&rule_part_1=&rule_part_2=&rule_part_3=&rule_part_exact_match=on&product_description=&modular_type_description=&tcb_code=&tcb_code_description=&tcb_scope=&tcb_scope_description=&outputformat=HTML&show_records=10&fetchfrom=0&calledFromFrame=N'
import pprint
pprint.pprint(form_data_to_dict(v2))
