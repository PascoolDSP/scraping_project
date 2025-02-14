from bs4 import BeautifulSoup
from urllib.request import urlopen
import test_selenium


def html_online_code_grabber(url):
    html_code = test_selenium.html_grabber(url)
    with open("index.html", "w") as file:
        html_code = file.write(html_code)
    return html_code

def html_code_grabber():
    with open("index.html", "r") as file:
        html_code = file.read()
    return html_code

# grab headings
def headings_grabber():
    html_code = html_code_grabber()

    heading_list = []
    counter = 2

    soup = BeautifulSoup(html_code, 'html.parser')
    h = soup.h1
    while h != None:
        print(h.get_text())
        heading_list.append(h.get_text())
        h = soup.find(f"h{counter}")
        counter += 1

# grab title
def title_grabber():
    html_code = html_code_grabber()
    soup = BeautifulSoup(html_code, 'html.parser')
    t = soup.title.text
    print(t)
    return t

# grab by tags
def tag_grabber(tag, grab_text):
    html_code = html_code_grabber()
    soup = BeautifulSoup(html_code, 'html.parser')
    tag_list = soup.find_all(tag)
    if grab_text == 0:
        for tag in tag_list:
            print(tag)
    else:
        for tag in tag_list:
            print(tag.text)
    return tag_list


# grab anchors
def anchor_grabber(print_state):
    html_code = html_code_grabber()
    anchor_list = []

    soup = BeautifulSoup(html_code, 'html.parser')
    anchor_list = soup.find_all('a')
    if print_state == True:
        for anchor in anchor_list:
            print(anchor.get_text().strip())
    return anchor_list

# grab href of anchors
def anchor_href_grabber():
    anchor_list = anchor_grabber(False)
    href_list = []
    for anchor in anchor_list:
        href = anchor.get('href')
        href_list.append(href)
        print(href)
    return href_list

def img_grabber():
    html_code = html_code_grabber()
    soup = BeautifulSoup(html_code, 'html.parser')
    img_list = soup.find_all("img")
    for img in img_list:
        print(img)
    return img_list

def li_grabber():
    html_code = html_code_grabber()
    soup = BeautifulSoup(html_code, 'html.parser')
    li_list = soup.find_all("li")
    for li in li_list:
        print(li.text)
    return li_list

def user_input():
    try:
        while True:
            print("[99] : give url\n")
            print("[01] : headings            [21] : select")
            print("[02] : title               [22] : meta")
            print("[03] : anchor              [23] : link")
            print("[04] : paragraphs          [24] : script")
            print("[05] : anchor href         [25] : iframe")
            print("[06] : div                 [26] : strong")
            print("[07] : span                [27] : b")
            print("[08] : img                 [28] : em")
            print("[09] : ul                  [29] : i")
            print("[10] : li                  [30] : u")
            print("[11] : ol                  [31] : section")
            print("[12] : table               [32] : article")
            print("[13] : tr                  [33] : aside")
            print("[14] : td                  [34] : nav")
            print("[15] : th                  [35] : header")
            print("[16] : form                [36] : footer")
            print("[17] : input               [37] : figure")
            print("[18] : textarea            [38] : figcaption")
            print("[19] : button              [39] : video")
            print("[20] : select              [40] : audio")
            print("[41] : source")

            print("\n[00] : close\n")
            scrap_arg = input("What to scrap : ")
            print("\n")
            match scrap_arg:
                case "1" | "01":
                    headings_grabber()
                case "2" | "02":
                    title_grabber()
                case "3" | "03":
                    anchor_grabber(True)
                case "4" | "04":
                    tag_grabber("p", 1)
                case "5" | "05":
                    anchor_href_grabber()
                case "6" | "06":
                    tag_grabber("div", 0)
                case "7" | "07":
                    tag_grabber("span", 0)
                case "8" | "08":
                    img_grabber()
                case "9" | "09":
                    tag_grabber("ul", 0)
                case "10":
                    li_grabber()
                case "11":
                    tag_grabber("ol", 0)
                case "12":
                    tag_grabber("table", 0)
                case "13":
                    tag_grabber("tr", 0)
                case "14":
                    tag_grabber("td", 1)
                case "15":
                    tag_grabber("th", 1)
                case "16":
                    tag_grabber("form", 0)
                case "17":
                    tag_grabber("input", 0)
                case "18":
                    tag_grabber("textarea", 0)
                case "19":
                    tag_grabber("button", 0)
                case "20":
                    tag_grabber("select", 0)
                case "21":
                    tag_grabber("option", 0)
                case "22":
                    tag_grabber("meta", 0)
                case "23":
                    tag_grabber("link", 0)
                case "24":
                    tag_grabber("script", 0)
                case "25":
                    tag_grabber("iframe", 0)
                case "26":
                    tag_grabber("strong", 0)
                case "27":
                    tag_grabber("b", 0)
                case "28":
                    tag_grabber("em", 0)
                case "29":
                    tag_grabber("i", 0)
                case "30":
                    tag_grabber("u", 0)
                case "31":
                    tag_grabber("section", 0)
                case "32":
                    tag_grabber("article", 0)
                case "33":
                    tag_grabber("aside", 0)
                case "34":
                    tag_grabber("nav", 0)
                case "35":
                    tag_grabber("header", 0)
                case "36":
                    tag_grabber("footer", 1)
                case "37":
                    tag_grabber("figure", 0)
                case "38":
                    tag_grabber("figcaption", 1)
                case "39":
                    tag_grabber("video", 0)
                case "40":
                    tag_grabber("audio", 0)
                case "41":
                    tag_grabber("source", 0)
                case "99":
                    url = input("URL : ")
                    html_online_code_grabber(url)
                case "0" | "00":
                    break
                case default:
                    continue
            print("\n")

    except KeyboardInterrupt:
        print("\nended")
        return
    print("close")

if __name__ == "__main__":
    user_input()