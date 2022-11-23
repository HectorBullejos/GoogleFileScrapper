import keyring
from bs4 import BeautifulSoup
import requests, lxml, urllib.request
from serpapi import GoogleSearch
import os, urllib.request

service_id = "serpapi"
username = "bulle"
credentials = keyring.get_credential(service_id, None)
if credentials is not None:
    username = credentials.username  # example_username
    password = credentials.password  # example_password


params = {
    "q": "filetype:PDF aws engineer resume .pdf"
}
cwd = os.getcwd()
file_path = os.path.join(cwd, "Files")

def get_pdfs():
    params = {
      "api_key": password,
      "engine": "google",
      "q": "filetype:PDF aws engineer resume .pdf",
      "hl": "en",
      "num": "200"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    print(results)

    for index, result in enumerate(results['organic_results']):
      if '.pdf' in result['link']:
        try:
            pdf_file = result['link']
            print(pdf_file)

            opener=urllib.request.build_opener()
            opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582')]
            urllib.request.install_opener(opener)

            # save PDF
            file_name = r"\zzpdf_file_" + str(index) + ".pdf"
            storage_file_path = file_path + file_name
            urllib.request.urlretrieve(pdf_file, storage_file_path)

            print(f'Saving PDF №{index}..')
        except Exception as urlibexcep:
            print(urlibexcep)
      else: pass

get_pdfs()
