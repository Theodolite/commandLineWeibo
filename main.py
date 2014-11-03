# -*- coding: utf-8 -*-
from terminal import Curses
from curses import wrapper
from weiboAgent import WeiboAgent


def main():
    # enable Chinese words printing
    import locale
    locale.setlocale(locale.LC_ALL, 'zh_cn')
    code = locale.getpreferredencoding()

    page = 0
    num_per_page = 5
    app = Curses()
    weibo = WeiboAgent()
    weibo.authorize()
    all_statuses = weibo.get_home_statuses(200)

    def refresh_page(page):
        app.clear()
        for i in range(page * num_per_page, (page + 1) * num_per_page):
            text = "%d >  %s\n" % (i, all_statuses['statuses'][i]['text'].encode('utf-8'))
            app.puts(i, text, 10, 1 + 4 * (i - page * num_per_page))

    refresh_page(page)

    while True:
        event = app.get_key()

        if event == ord('q'):
            app.close()
            break
        elif event == ord('j'):
            page += 1
            refresh_page(page)
        elif event == ord('k'):
            page -= 1
            refresh_page(page)
        else:
        	pass

if __name__ == "__main__":
	main()
