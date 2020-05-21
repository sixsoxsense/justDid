import multiprocessing
from bs4 import BeautifulSoup
from urllib import request
from urllib.request import urlopen


def scrapingPlayer(player_id):
    html = urlopen(
        "http://www.n-league.org/?act=&mid=player_search_2014&vid=&player_srl=" + str(player_id) + "&player_name=")
    bsObject = BeautifulSoup(html, "html.parser")
    try:
        img_download(bsObject, player_id)
        print(str(player_id) + "실행중")
        f = open('D://Nleaguedata/' + str(player_id) + '.txt', mode='a', encoding='utf-8')
        f.write(info_theadScraping(bsObject))
        ## tbody 수집 내용: 선수 정보
        f.write(info_tbodyScraping(bsObject))
        ## thead 수집 내용: 경력표 머리부분
        f.write(history_theadScraping(bsObject))
        ## tbody 수집 내용: 경력 내용
        f.write(history_tbodyScraping(bsObject))
        ##종료
        f.close()
    except:
        print(str(player_id) + "존재하지않음")
        pass


def info_theadScraping(bsObject):
    player_info = bsObject.find('table', class_="brd_list_player")
    thead_info = player_info.thead
    head_info = str(thead_info.get_text())
    return head_info


def info_tbodyScraping(bsObject):
    player_info = bsObject.find('table', class_="brd_list_player")
    tbody_info = player_info.tbody
    body_info = str(tbody_info.get_text())
    return body_info


def history_theadScraping(bsObject):
    player_history = bsObject.find('table', class_="brd_list brd_listfoot")
    thead_history = player_history.thead
    head_history = str(thead_history.get_text())
    return head_history


def history_tbodyScraping(bsObject):
    player_history = bsObject.find('table', class_="brd_list brd_listfoot")
    tbody_history = player_history.tbody
    body_history = str(tbody_history.get_text())
    return body_history


def img_download(bsObject, player_id):
    img_html = bsObject.find('p', class_='player_kim').find('img').get('src')
    img_file_adress = 'http://www.n-league.org' + str(img_html)
    request.urlretrieve(img_file_adress, 'D://Nleaguedata/' + str(player_id) + '.jpg')
    ##D://Nleaguedata/

if __name__ == '__main__':
    with multiprocessing.Pool(128) as ScrapingNleague:
        tasks=[ScrapingNleague.apply_async(func=scrapingPlayer,args=(i,))for i in range(0,999999)]
        ScrapingNleague.close()
        ScrapingNleague.join()
    ##131400