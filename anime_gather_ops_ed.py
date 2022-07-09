from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

opt = webdriver.ChromeOptions()
# opt.add_argument('--headless')
opt.add_argument('--disable-gpu')
# opt.add_argument('--no-sandbox')
# opt.add_argument('--disable-dev-shm-usage')
resolution = "--window-size=1920,1080"
opt.add_argument(resolution)

# Initialize the service object
# service = Service(r'C:\Selenium\chromedriver_win32\chromedriver.exe')
service = Service(r'/home/extrieve/Documents/chromedriver/chromedriver')
# path = r'C:\Selenium\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(service=service, options=opt)


links = ['https://animethemes.moe/anime/bastard_ankoku_no_hakaishin_ona', 'https://animethemes.moe/anime/bucchigire', 'https://animethemes.moe/anime/cardfight_vanguard_will_dress', 'https://animethemes.moe/anime/chimimo', 'https://animethemes.moe/anime/engage_kiss', 'https://animethemes.moe/anime/extreme_hearts', 'https://animethemes.moe/anime/hoshi_no_samidare', 'https://animethemes.moe/anime/isekai_meikyuu_de_harem_wo', 'https://animethemes.moe/anime/isekai_ojisan', 'https://animethemes.moe/anime/jashin_chan_dropkick_x', 'https://animethemes.moe/anime/kami_kuzu_idol', 'https://animethemes.moe/anime/kanojo_okarishimasu_2nd_season', 'https://animethemes.moe/anime/kinsou_no_vermeil', 'https://animethemes.moe/anime/kumichou_musume_to_sewagakari', 'https://animethemes.moe/anime/luminous_witches', 'https://animethemes.moe/anime/lycoris_recoil', 'https://animethemes.moe/anime/made_in_abyss_retsujitsu_no_ougonkyou',
         'https://animethemes.moe/anime/mamahaha_no_tsurego_ga_motokano_datta', 'https://animethemes.moe/anime/prima_doll', 'https://animethemes.moe/anime/rwby_hyousetsu_teikoku', 'https://animethemes.moe/anime/shadows_house_2nd_season', 'https://animethemes.moe/anime/shin_tennis_no_ouji_sama_u_17_world_cup', 'https://animethemes.moe/anime/shoot_goal_to_the_future', 'https://animethemes.moe/anime/soredemo_ayumu_wa_yosetekuru', 'https://animethemes.moe/anime/tensei_kenja_no_isekai_life_dai_2_no_shokugyou_wo_ete_sekai_saikyou_ni_narimashita', 'https://animethemes.moe/anime/teppen', 'https://animethemes.moe/anime/tokyo_mew_mew_new', 'https://animethemes.moe/anime/utawarerumono_futari_no_hakuoro', 'https://animethemes.moe/anime/warau_arsnotoria_sun', 'https://animethemes.moe/anime/yofukashi_no_uta', 'https://animethemes.moe/anime/youkoso_jitsuryoku_shijou_shugi_no_kyoushitsu_e_2nd_season', 'https://animethemes.moe/anime/yurei_deco']

themes = []

for link in links[:1]:
    driver.get(link)
    # Wait for the page to load
    wait = WebDriverWait(driver, 4)

    for zel in driver.find_elements(By.TAG_NAME, 'a'):
        ref = str(zel.get_attribute('href'))
        print(ref)

        if 'OP' in ref or 'ED' in ref:
            themes.append(ref)


driver.close()
driver.quit()

print(themes)
