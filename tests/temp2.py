from sre_constants import SUCCESS
# import xperimental_data_conv.main as xdc
# from xperimental-data-conv.xperimental_data_conv import main as xdc
from xperimental_data_converter import main as xdc
import os

fj_user = "testaccount"
fj_pass = "12345"
sbh_user = "testaccount"
sbh_pass = "12345"
sbh_url = "https://synbiohub.colorado.edu"
# don't include :8000 in fj_url parameter
fj_url = "flapjack.rudge-lab.org"


direct = os.path.split(__file__)[0]
sbh_collec = "test" # change to desired name in sbh and fj
file_path_in = "test_files/xdc_test2.xlsx"

sbol_collec_url = xdc.xperimental_data_uploader(file_path_in, fj_url, fj_user, fj_pass,
                               sbh_url, sbh_user, sbh_pass, sbh_collec, True)
