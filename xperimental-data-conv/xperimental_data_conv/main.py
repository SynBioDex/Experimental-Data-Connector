import excel2flapjack.main as e2f
import excel2sbol.converter as conv
import sbol2
import tempfile
import requests
import os
      

def experimental_data_uploader(file_path_in, fj_user, fj_pass, sbh_user,
                               sbh_pass, sbh_collec, sbh_overwrite=False,
                               fj_overwrite=False):

     # create temporary directory to write intermediate files to
     temp_dir = tempfile.TemporaryDirectory()
     file_path_out = os.path.join(temp_dir.name, 'test.xml')
     file_path_out2 = os.path.join(temp_dir.name, 'test1.xml')

     # convert the excel file to SBOL
     # use excel2sbol - could ask for an update that just gives the doc back rather than the file
     homespace = 'http://www.examples.org/'
     conv.converter(file_path_in, file_path_out, homespace=homespace)

     # SBH Login
     response = requests.post(
          'https://synbiohub.org/login',
          headers={'Accept': 'text/plain'},
          data={
               'email': sbh_user,
               'password' : sbh_pass,
               }
     )
     x_token = response.text

     # Pull graph uri from synbiohub
     response = requests.get(
          'https://synbiohub.org/profile',
          headers={
               'Accept': 'text/plain',
               'X-authorization': x_token
               }
     )
     sbol_graph_uri = response.json()['graphUri']
     sbol_collec_url = f'{sbol_graph_uri}/{sbh_collec}/'

     # Parse sbol to create hashmap of flapjack id to sbol uri
     doc = sbol2.Document()
     doc.read(file_path_out)

     sbol_hash_map = {}
     for tl in doc:
          if 'https://flapjack.rudge-lab.org/ID' in tl.properties:
               sbol_uri = tl.properties['http://sbols.org/v2#persistentIdentity'][0]
               sbol_uri = sbol_uri.replace(homespace, sbol_collec_url)
               sbol_uri = f'{sbol_uri}/1'

               sbol_name = str(tl.properties['http://sbols.org/v2#displayId'][0])
               sbol_hash_map[sbol_name] = sbol_uri


     # upload the excel file to flapjack and get hash map back
     fj_url = "flapjack.rudge-lab.org:8000"
     # hash_map = e2f.flapjack_upload(fj_url, fj_user, fj_pass, file_path_in)
     hash_map = e2f.flapjack_upload(fj_url, fj_user, fj_pass, file_path_in,
                                    sbol_hash_map=sbol_hash_map,
                                    add_sbol_uris=True,
                                    flapjack_override=fj_overwrite,
                                    print_progress=True)
     # print(hash_map)

     # Add flapjack annotations to the SBOL
     doc = sbol2.Document()
     doc.read(file_path_out)
     for tl in doc:
          id = str(tl).split('/')[-2]
          if id in hash_map:
            setattr(tl, 'flapjack_ID',
                    sbol2.URIProperty(tl,
                    'https://flapjack.rudge-lab.org/ID',
                     '0', '*', [], initial_value=f'http://wwww.flapjack.com/{hash_map[id]}'))
     doc.write(file_path_out2)

     if sbh_overwrite:
          sbh_overwrite = '1'
     else:
          sbh_overwrite = '0'
     # SBH file upload
     response = requests.post(
          'https://synbiohub.org/submit',
          headers={
               'Accept': 'text/plain',
               'X-authorization': x_token
          },
          files={
          'files': open(file_path_out2,'rb'),
          },
          data={
               'id': sbh_collec,
               'version' : '1',
               'name' : sbh_collec,
               'description' : 'Description stuff',
               'overwrite_merge' : sbh_overwrite
          },

     )

     if response.text == "Submission id and version already in use":
          print('not submitted')
          raise AttributeError(f'The collection ({sbh_collec}) could not be submitted to synbiohub as the collection already exists and overite is not on. Note it was submitted to flapjack')
     # if response.text == "Successfully uploaded":
     #      success = True

     return(sbol_collec_url)





