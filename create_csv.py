import textfsm
import csv
from pprint import pprint
import os

'''
TO DO: 
- Add argparse to get rid of manual code edit for WLANstat file.
'''

template_file = os.path.abspath('./TesxFSMTemplates/netsh_wlan_show_interface.template')
data_file = os.path.abspath('./WLANstat_20192405.txt')
data_file_name = os.path.basename(data_file).split('.')[0] + '.csv'
print(f'CSV filename: {data_file_name}')

def create_csv(wlanstat_file):
    with open(template_file, 'r') as template:
        with open(wlanstat_file, 'r') as data_file:
        
            re_table = textfsm.TextFSM(template)
            data = re_table.ParseText(data_file.read())

            with open(data_file_name, 'w') as output_file:

                #print(re_table.header)
                output_file.write(','.join(re_table.header))
                output_file.write('\n')
                
                for row in data:
                    #pprint(','.join(row))
                    data_row = ','.join(row)
                    output_file.write(data_row)
                    output_file.write('\n')
                

create_csv('WLANstat_20190706.txt')