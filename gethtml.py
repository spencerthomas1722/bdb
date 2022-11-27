from bs4 import BeautifulSoup
import os
import requests

letters = ['al', 'bet', 'gim', 'dal', 'he', 'waw', 'zayn', 'het', 'tet', 'yod', 'kap', 'lam', 'mem', 'num', 'sam', 'ayi', 'pe', 'sad', 'kop', 'res', 'sin', 'taw']


def scrape(url, letter):
    html_head = f"""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 //EN"><HTML><HEAD>
                    <TITLE>{letter}</TITLE><META NAME="description" CONTENT="">
                    <META NAME="keywords" CONTENT="">
                    <META NAME="author" CONTENT="Administrator">
                    <META NAME="generator" CONTENT="">
                    <LINK REL=STYLESHEET HREF="al.css">
                    <STYLE>
                    #pStyle01X0 {{text-indent: 0px; }}
                    </STYLE>
                    </HEAD>"""
    html_foot = """</BODY></HTML>"""
    page_num = 1
    all_lines = []
    hasnext = True
    while hasnext:
        indiv_url = url
        if page_num < 10:
            indiv_url += '0' + str(page_num) + '.html'
        else:
            indiv_url += str(page_num) + '.html'
        r = requests.get(indiv_url)
        soup = BeautifulSoup(r.text, 'html.parser')
        all_p = soup.find_all('p')
        all_lines.extend([str(p) for p in all_p])
        all_a = soup.find_all('a')
        hasnext = False
        for a in all_a:
            if a.text == 'Next ->':
                hasnext = True
        page_num += 1
    return html_head + '\n' + '\n'.join(all_lines) + '\n' + html_foot


def scrape_all(fpath):
    for i in range(len(letters)):
        h = scrape('http://www.ericlevy.com/revel/bdb/bdb/' + str(i+1) + '/' + letters[i], letters[i])
        with open(os.path.join(fpath, letters[i] + '.html'), 'w', encoding='utf8') as f:
            f.write(h)


if __name__ == '__main__':
    fpath = os.path.join(os.getcwd(), 'pages')
    scrape_all(fpath)
