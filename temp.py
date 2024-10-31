from sre_constants import SUCCESS
import xperimental_data_conv.main as xdc
import os

fj_user = ""
fj_pass = ""
sbh_pass = ''
sbh_user = ''


direct = os.path.split(__file__)[0]
file_path_in = os.path.join(direct, 'xperimental-data-conv','tests','test_files', 'flapjack_excel_converter_v030.xlsx')
sbh_overwrite = '1'
sbh_collec = 'Flapjack'

sbol_collec_url = xdc.experimental_data_uploader(file_path_in, fj_user, fj_pass,
                               sbh_user, sbh_pass, sbh_collec, sbh_overwrite=True,
                               fj_overwrite=True)
