from sre_constants import SUCCESS
# import xperimental_data_conv.main as xdc
# from xperimental-data-conv.xperimental_data_conv import main as xdc
import main as xdc
import os

fj_user = "dylan33smith"
fj_pass = "coco33"
sbh_user = "dylan33smith"
sbh_pass = "coco33"
sbh_url = "https://synbiohub.colorado.edu"
fj_url = "flapjack.rudge-lab.org"


direct = os.path.split(__file__)[0]
# file_path_in = os.path.join(direct, '..', 'xperimental-data-conv','tests','test_files', 'flapjack_excel_converter_v030.xlsx')
# sbh_overwrite = '1'
sbh_collec = "Flapjack"
file_path_in = "xdc_test.xlsx"

sbol_collec_url = xdc.experimental_data_uploader(file_path_in, fj_url, fj_user, fj_pass,
                               sbh_url, sbh_user, sbh_pass, sbh_collec, sbh_overwrite=True,
                               fj_overwrite=True)
