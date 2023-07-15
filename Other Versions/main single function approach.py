from selenium import webdriver
from bs4 import BeautifulSoup
import time
import datetime
import pandas as pd
import numpy as np
from selenium.webdriver.common.by import By
import threading


def main(url, name):
  dff = pd.DataFrame(columns=['Job Title', 'Experience Reqd', 'City', 'Date Posted', 'Site', 'URL'])

  driver = webdriver.Chrome()
  driver.get(url)
  pages = np.arange(1, 3)

  for pages in pages:
    scroll = np.arange(1, 20)
    counter = 0
    
    for scroll in scroll:
      driver.execute_script("window.scrollTo(0,(document.body.scrollHeight))")
      time.sleep(1)

    soup1 = BeautifulSoup(driver.page_source,'html5lib')
    results = soup1.find('div', id='mainContainer')
    job_elems1 = results.find_all('div', class_=['col-lg-9 col-md-9 col-sm-8 container pdmobr5', 'col-lg-3 col-md-3 col-sm-4 pdlr0 mtb2 hidden-xs'])
    # print(job_elems1)

    for job_elem1 in job_elems1:
      finding = counter % 2
      if finding == 0:  
        try: 
          print(counter)
          counter = counter + 1
          
          # Title
          T_n_E = job_elem1.find('a', class_='mrmob5 hidden-xs')
          before_the_parts = T_n_E.get_text()
          parts = before_the_parts.split("(", 1)
          T = parts[0].strip()
          E = parts[1].strip(")")
          Title = T
          # print(Title)
          
          # Experience
          Exp = E
          # print(Exp)
          
          # Site
          S = 'iimjobs.com'
          Site = S
          # print(Site)

          # URL
          U = job_elem1.find('a',class_='mrmob5 hidden-xs').get('href')
          URL = U
        except Exception as e:
          print("EXCEPTION OCCURRED | COUNTER = " + str(counter))
          pass
      else:
        try:
          print(counter)
          counter = counter + 1
          # Date Posted
          D = job_elem1.find('span', class_='gry_txt txt12 original')
          Date=D.text 
          print(Date)

          # City
          try:
            C = job_elem1.find('span')
            City=C.text
            print(City)
          except Exception as e:
            City = None
        except Exception as e:
          print("EXCEPTION OCCURRED | COUNTER = " + str(counter))
          pass
      if finding == 1:
        dff = pd.concat([dff, pd.DataFrame([[Title, Exp, City, Date, Site, URL, ]], columns = ['Job Title', 'Experience Reqd', 'City', 'Date Posted', 'Site', 'URL'])], ignore_index=True)
        dff.to_excel("IIMJobsJobListing_" + name + '_'+ str(datetime.date.today()) + ".xlsx", index = False)
        print(dff)
      else:
        pass
    driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[9]/div[5]/div/div/div[3]/div/a').click()
    time.sleep(0.5)
    print("PAGE No. " + str(pages)+ " COMPLETE")

thread1 = threading.Thread(target=main("https://www.iimjobs.com/c/filter/banking-finance-jobs-in-metros_anywhere%20in%20india_ahmedabad_amritsar_andhra%20pradesh_aurangabad_bangalore_bhubaneshwar_bihar_chandigarh_chennai_chhattisgarh_cochin-kochi_coimbatore_cuttack_dehradun_delhi_delhi%20ncr_faridabad_gandhinagar_ghaziabad_goa_greater%20noida_gujarat_guntur_gurgaon-gurugram_guwahati_haridwar_haryana_hosur_hubli_hyderabad_jaipur_jalandhar_jammu_jammu%20&%20kashmir_jamshedpur_jharkhand_jodhpur_karnataka_kerala_kolkata_lucknow_ludhiana_madurai_maharashtra_mp_mumbai_mysore_nagpur_nasik_navi%20mumbai_noida_odisha_panipat_patiala_patna_pondicherry_pune_punjab_raipur_rajasthan_rajkot_ranchi_sonipat_srinagar_surat_tamil%20nadu_telangana_thane_thiruvananthapuram_udaipur_up_uttarakhand_vadodara-baroda_varanasi-banaras_vijayawada_vishakhapatnam-vizag_warangal-13-87_88_53_45_34_79_3_65_19_14_6_64_70_84_86_58_36_1_40_55_41_13_39_8_77_37_12_57_16_71_72_4_11_46_43_42_63_20_52_31_17_5_60_48_83_9_10_2_73_66_67_68_38_18_50_47_61_85_7_15_74_33_80_62_49_44_54_32_35_69_75_51_21_59_56_81_76_78_82-0-0-1.html", 'banking_finance'))
thread2 = threading.Thread(target=main('https://www.iimjobs.com/c/filter/sales-marketing-jobs-in-metros_anywhere%20in%20india_ahmedabad_amritsar_andhra%20pradesh_aurangabad_bangalore_bhubaneshwar_bihar_chandigarh_chennai_chhattisgarh_cochin-kochi_coimbatore_cuttack_dehradun_delhi_delhi%20ncr_faridabad_gandhinagar_ghaziabad_goa_greater%20noida_gujarat_guntur_gurgaon-gurugram_guwahati_haridwar_haryana_hosur_hubli_hyderabad_jaipur_jalandhar_jammu_jammu%20&%20kashmir_jamshedpur_jharkhand_jodhpur_karnataka_kerala_kolkata_lucknow_ludhiana_madurai_maharashtra_mp_mumbai_mysore_nagpur_nasik_navi%20mumbai_noida_odisha_panipat_patiala_patna_pondicherry_pune_punjab_raipur_rajasthan_rajkot_ranchi_sonipat_srinagar_surat_tamil%20nadu_telangana_thane_thiruvananthapuram_udaipur_up_uttarakhand_vadodara-baroda_varanasi-banaras_vijayawada_vishakhapatnam-vizag_warangal-14-87_88_53_45_34_79_3_65_19_14_6_64_70_84_86_58_36_1_40_55_41_13_39_8_77_37_12_57_16_71_72_4_11_46_43_42_63_20_52_31_17_5_60_48_83_9_10_2_73_66_67_68_38_18_50_47_61_85_7_15_74_33_80_62_49_44_54_32_35_69_75_51_21_59_56_81_76_78_82-0-0-1.html', 'sales_marketing'))
# thread3 = threading.Thread(target=consulting)
# thread4 = threading.Thread(target=hr_it)
# thread5 = threading.Thread(target=it_systems)
# thread6 = threading.Thread(target=scm_operations)
# thread7 = threading.Thread(target=legal)
# thread8 = threading.Thread(target=bpo)

# Start Button Here:

thread1.start()
thread2.start()

print("OPERATIONS UNDERWAY!")

thread1.join()
thread2.join()

# thread3.start()
# thread4.start()

# thread3.join()
# thread4.join()

# thread5.start()
# thread6.start()

# thread5.join()
# thread6.join()

# thread7.start()
# thread8.start()

# thread7.join()
# thread8.join()

# banking_finance = "https://www.iimjobs.com/c/filter/banking-finance-jobs-in-metros_anywhere%20in%20india_ahmedabad_amritsar_andhra%20pradesh_aurangabad_bangalore_bhubaneshwar_bihar_chandigarh_chennai_chhattisgarh_cochin-kochi_coimbatore_cuttack_dehradun_delhi_delhi%20ncr_faridabad_gandhinagar_ghaziabad_goa_greater%20noida_gujarat_guntur_gurgaon-gurugram_guwahati_haridwar_haryana_hosur_hubli_hyderabad_jaipur_jalandhar_jammu_jammu%20&%20kashmir_jamshedpur_jharkhand_jodhpur_karnataka_kerala_kolkata_lucknow_ludhiana_madurai_maharashtra_mp_mumbai_mysore_nagpur_nasik_navi%20mumbai_noida_odisha_panipat_patiala_patna_pondicherry_pune_punjab_raipur_rajasthan_rajkot_ranchi_sonipat_srinagar_surat_tamil%20nadu_telangana_thane_thiruvananthapuram_udaipur_up_uttarakhand_vadodara-baroda_varanasi-banaras_vijayawada_vishakhapatnam-vizag_warangal-13-87_88_53_45_34_79_3_65_19_14_6_64_70_84_86_58_36_1_40_55_41_13_39_8_77_37_12_57_16_71_72_4_11_46_43_42_63_20_52_31_17_5_60_48_83_9_10_2_73_66_67_68_38_18_50_47_61_85_7_15_74_33_80_62_49_44_54_32_35_69_75_51_21_59_56_81_76_78_82-0-0-1.html"

# sales_marketing = "https://www.iimjobs.com/c/filter/sales-marketing-jobs-in-metros_anywhere%20in%20india_ahmedabad_amritsar_andhra%20pradesh_aurangabad_bangalore_bhubaneshwar_bihar_chandigarh_chennai_chhattisgarh_cochin-kochi_coimbatore_cuttack_dehradun_delhi_delhi%20ncr_faridabad_gandhinagar_ghaziabad_goa_greater%20noida_gujarat_guntur_gurgaon-gurugram_guwahati_haridwar_haryana_hosur_hubli_hyderabad_jaipur_jalandhar_jammu_jammu%20&%20kashmir_jamshedpur_jharkhand_jodhpur_karnataka_kerala_kolkata_lucknow_ludhiana_madurai_maharashtra_mp_mumbai_mysore_nagpur_nasik_navi%20mumbai_noida_odisha_panipat_patiala_patna_pondicherry_pune_punjab_raipur_rajasthan_rajkot_ranchi_sonipat_srinagar_surat_tamil%20nadu_telangana_thane_thiruvananthapuram_udaipur_up_uttarakhand_vadodara-baroda_varanasi-banaras_vijayawada_vishakhapatnam-vizag_warangal-14-87_88_53_45_34_79_3_65_19_14_6_64_70_84_86_58_36_1_40_55_41_13_39_8_77_37_12_57_16_71_72_4_11_46_43_42_63_20_52_31_17_5_60_48_83_9_10_2_73_66_67_68_38_18_50_47_61_85_7_15_74_33_80_62_49_44_54_32_35_69_75_51_21_59_56_81_76_78_82-0-0-1.html"

# consulting = "https://www.iimjobs.com/c/filter/sales-marketing-jobs-in-metros_anywhere%20in%20india_ahmedabad_amritsar_andhra%20pradesh_aurangabad_bangalore_bhubaneshwar_bihar_chandigarh_chennai_chhattisgarh_cochin-kochi_coimbatore_cuttack_dehradun_delhi_delhi%20ncr_faridabad_gandhinagar_ghaziabad_goa_greater%20noida_gujarat_guntur_gurgaon-gurugram_guwahati_haridwar_haryana_hosur_hubli_hyderabad_jaipur_jalandhar_jammu_jammu%20&%20kashmir_jamshedpur_jharkhand_jodhpur_karnataka_kerala_kolkata_lucknow_ludhiana_madurai_maharashtra_mp_mumbai_mysore_nagpur_nasik_navi%20mumbai_noida_odisha_panipat_patiala_patna_pondicherry_pune_punjab_raipur_rajasthan_rajkot_ranchi_sonipat_srinagar_surat_tamil%20nadu_telangana_thane_thiruvananthapuram_udaipur_up_uttarakhand_vadodara-baroda_varanasi-banaras_vijayawada_vishakhapatnam-vizag_warangal-14-87_88_53_45_34_79_3_65_19_14_6_64_70_84_86_58_36_1_40_55_41_13_39_8_77_37_12_57_16_71_72_4_11_46_43_42_63_20_52_31_17_5_60_48_83_9_10_2_73_66_67_68_38_18_50_47_61_85_7_15_74_33_80_62_49_44_54_32_35_69_75_51_21_59_56_81_76_78_82-0-0-1.html"

# hr_it = "https://www.iimjobs.com/c/filter/hr-ir-jobs-in-metros_anywhere%20in%20india_ahmedabad_amritsar_andhra%20pradesh_aurangabad_bangalore_bhubaneshwar_bihar_chandigarh_chennai_chhattisgarh_cochin-kochi_coimbatore_cuttack_dehradun_delhi_delhi%20ncr_faridabad_gandhinagar_ghaziabad_goa_greater%20noida_gujarat_guntur_gurgaon-gurugram_guwahati_haridwar_haryana_hosur_hubli_hyderabad_jaipur_jalandhar_jammu_jammu%20&%20kashmir_jamshedpur_jharkhand_jodhpur_karnataka_kerala_kolkata_lucknow_ludhiana_madurai_maharashtra_mp_mumbai_mysore_nagpur_nasik_navi%20mumbai_noida_odisha_panipat_patiala_patna_pondicherry_pune_punjab_raipur_rajasthan_rajkot_ranchi_sonipat_srinagar_surat_tamil%20nadu_telangana_thane_thiruvananthapuram_udaipur_up_uttarakhand_vadodara-baroda_varanasi-banaras_vijayawada_vishakhapatnam-vizag_warangal-17-87_88_53_45_34_79_3_65_19_14_6_64_70_84_86_58_36_1_40_55_41_13_39_8_77_37_12_57_16_71_72_4_11_46_43_42_63_20_52_31_17_5_60_48_83_9_10_2_73_66_67_68_38_18_50_47_61_85_7_15_74_33_80_62_49_44_54_32_35_69_75_51_21_59_56_81_76_78_82-0-0-1.html"

# it_systems = "https://www.iimjobs.com/c/filter/it-systems-jobs-in-metros_anywhere%20in%20india_ahmedabad_amritsar_andhra%20pradesh_aurangabad_bangalore_bhubaneshwar_bihar_chandigarh_chennai_chhattisgarh_cochin-kochi_coimbatore_cuttack_dehradun_delhi_delhi%20ncr_faridabad_gandhinagar_ghaziabad_goa_greater%20noida_gujarat_guntur_gurgaon-gurugram_guwahati_haridwar_haryana_hosur_hubli_hyderabad_jaipur_jalandhar_jammu_jammu%20&%20kashmir_jamshedpur_jharkhand_jodhpur_karnataka_kerala_kolkata_lucknow_ludhiana_madurai_maharashtra_mp_mumbai_mysore_nagpur_nasik_navi%20mumbai_noida_odisha_panipat_patiala_patna_pondicherry_pune_punjab_raipur_rajasthan_rajkot_ranchi_sonipat_srinagar_surat_tamil%20nadu_telangana_thane_thiruvananthapuram_udaipur_up_uttarakhand_vadodara-baroda_varanasi-banaras_vijayawada_vishakhapatnam-vizag_warangal-15-87_88_53_45_34_79_3_65_19_14_6_64_70_84_86_58_36_1_40_55_41_13_39_8_77_37_12_57_16_71_72_4_11_46_43_42_63_20_52_31_17_5_60_48_83_9_10_2_73_66_67_68_38_18_50_47_61_85_7_15_74_33_80_62_49_44_54_32_35_69_75_51_21_59_56_81_76_78_82-0-0-1.html"

# scm_operations = "https://www.iimjobs.com/c/filter/scm-operations-jobs-in-metros_anywhere%20in%20india_ahmedabad_amritsar_andhra%20pradesh_aurangabad_bangalore_bhubaneshwar_bihar_chandigarh_chennai_chhattisgarh_cochin-kochi_coimbatore_cuttack_dehradun_delhi_delhi%20ncr_faridabad_gandhinagar_ghaziabad_goa_greater%20noida_gujarat_guntur_gurgaon-gurugram_guwahati_haridwar_haryana_hosur_hubli_hyderabad_jaipur_jalandhar_jammu_jammu%20&%20kashmir_jamshedpur_jharkhand_jodhpur_karnataka_kerala_kolkata_lucknow_ludhiana_madurai_maharashtra_mp_mumbai_mysore_nagpur_nasik_navi%20mumbai_noida_odisha_panipat_patiala_patna_pondicherry_pune_punjab_raipur_rajasthan_rajkot_ranchi_sonipat_srinagar_surat_tamil%20nadu_telangana_thane_thiruvananthapuram_udaipur_up_uttarakhand_vadodara-baroda_varanasi-banaras_vijayawada_vishakhapatnam-vizag_warangal-19-87_88_53_45_34_79_3_65_19_14_6_64_70_84_86_58_36_1_40_55_41_13_39_8_77_37_12_57_16_71_72_4_11_46_43_42_63_20_52_31_17_5_60_48_83_9_10_2_73_66_67_68_38_18_50_47_61_85_7_15_74_33_80_62_49_44_54_32_35_69_75_51_21_59_56_81_76_78_82-0-0-1.html"

# legal = "https://www.iimjobs.com/c/filter/legal-jobs-in-metros_anywhere%20in%20india_ahmedabad_amritsar_andhra%20pradesh_aurangabad_bangalore_bhubaneshwar_bihar_chandigarh_chennai_chhattisgarh_cochin-kochi_coimbatore_cuttack_dehradun_delhi_delhi%20ncr_faridabad_gandhinagar_ghaziabad_goa_greater%20noida_gujarat_guntur_gurgaon-gurugram_guwahati_haridwar_haryana_hosur_hubli_hyderabad_jaipur_jalandhar_jammu_jammu%20&%20kashmir_jamshedpur_jharkhand_jodhpur_karnataka_kerala_kolkata_lucknow_ludhiana_madurai_maharashtra_mp_mumbai_mysore_nagpur_nasik_navi%20mumbai_noida_odisha_panipat_patiala_patna_pondicherry_pune_punjab_raipur_rajasthan_rajkot_ranchi_sonipat_srinagar_surat_tamil%20nadu_telangana_thane_thiruvananthapuram_udaipur_up_uttarakhand_vadodara-baroda_varanasi-banaras_vijayawada_vishakhapatnam-vizag_warangal-21-87_88_53_45_34_79_3_65_19_14_6_64_70_84_86_58_36_1_40_55_41_13_39_8_77_37_12_57_16_71_72_4_11_46_43_42_63_20_52_31_17_5_60_48_83_9_10_2_73_66_67_68_38_18_50_47_61_85_7_15_74_33_80_62_49_44_54_32_35_69_75_51_21_59_56_81_76_78_82-0-0-1.html"

# bpo = "https://www.iimjobs.com/c/filter/bpo-jobs-in-metros_anywhere%20in%20india_ahmedabad_amritsar_andhra%20pradesh_aurangabad_bangalore_bhubaneshwar_bihar_chandigarh_chennai_chhattisgarh_cochin-kochi_coimbatore_cuttack_dehradun_delhi_delhi%20ncr_faridabad_gandhinagar_ghaziabad_goa_greater%20noida_gujarat_guntur_gurgaon-gurugram_guwahati_haridwar_haryana_hosur_hubli_hyderabad_jaipur_jalandhar_jammu_jammu%20&%20kashmir_jamshedpur_jharkhand_jodhpur_karnataka_kerala_kolkata_lucknow_ludhiana_madurai_maharashtra_mp_mumbai_mysore_nagpur_nasik_navi%20mumbai_noida_odisha_panipat_patiala_patna_pondicherry_pune_punjab_raipur_rajasthan_rajkot_ranchi_sonipat_srinagar_surat_tamil%20nadu_telangana_thane_thiruvananthapuram_udaipur_up_uttarakhand_vadodara-baroda_varanasi-banaras_vijayawada_vishakhapatnam-vizag_warangal-22-87_88_53_45_34_79_3_65_19_14_6_64_70_84_86_58_36_1_40_55_41_13_39_8_77_37_12_57_16_71_72_4_11_46_43_42_63_20_52_31_17_5_60_48_83_9_10_2_73_66_67_68_38_18_50_47_61_85_7_15_74_33_80_62_49_44_54_32_35_69_75_51_21_59_56_81_76_78_82-0-0-1.html"

# time.sleep(3)


# driver2 = webdriver.Chrome()
# driver2.get(sales_marketing)
# soup2 = BeautifulSoup(driver2.page_source,'html5lib')

# driver3 = webdriver.Chrome()
# driver3.get(consulting)
# soup3 = BeautifulSoup(driver3.page_source,'html5lib')

# driver4 = webdriver.Chrome()
# driver4.get(hr_it)
# soup4 = BeautifulSoup(driver4.page_source,'html5lib')

# driver5 = webdriver.Chrome()
# driver5.get(it_systems)
# soup5 = BeautifulSoup(driver5.page_source,'html5lib')

# driver6 = webdriver.Chrome()
# driver6.get(scm_operations)
# soup6 = BeautifulSoup(driver6.page_source,'html5lib')

# driver7 = webdriver.Chrome()
# driver7.get(legal)
# soup7 = BeautifulSoup(driver7.page_source,'html5lib')

# driver8 = webdriver.Chrome()
# driver8.get(bpo)
# soup8 = BeautifulSoup(driver8.page_source,'html5lib')

# print (soup1.prettify(), soup2.prettify())