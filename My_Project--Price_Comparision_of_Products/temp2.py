

import pandas as pd
from bs4 import BeautifulSoup
import requests
import streamlit as st

search = "earbuds"
url=requests.get("https://www.amazon.in/s?k=earbuds")
#url=(url+search)
html = url.content
soup= BeautifulSoup(html,"html.parser")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

main=soup.find('body', class_='a-aui_72554-c a-aui_accordion_a11y_role_354025-c a-aui_btn_preorder_ks_359947-c a-aui_button_aria_label_markup_348458-t1 a-aui_csa_templates_buildin_ww_exp_337518-c a-aui_csa_templates_buildin_ww_launch_337517-c a-aui_csa_templates_declarative_ww_exp_337521-c a-aui_csa_templates_declarative_ww_launch_337520-c a-aui_dynamic_img_a11y_markup_345061-t1 a-aui_launch_cardui_a11y_fix_346896-c a-aui_launch_expander_ally_fix_354901-c a-aui_markup_disabled_link_btn_351411-c a-aui_pci_risk_banner_210084-c a-aui_popover_trigger_add_role_350993-c a-aui_preload_261698-c a-aui_rel_noreferrer_noopener_309527-c a-aui_template_weblab_cache_333406-c a-aui_tnr_v2_180836-c')

data=[]
for vs in main.find_all('div', class_='a-size-base a-color-price s-price a-text-bold'):
    name=vs.find('span', class_='a-size-medium a-color-base a-text-normal').text
    price=vs.find('span', class_='a-price-whole').text
    
    data.append({"name":name,
        "price":price})
print(data)
print(len(data))
pd.DataFrame(data).to_csv("Amazon_price.csv")