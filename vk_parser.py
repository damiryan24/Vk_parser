import requests
import pandas as pd


def parser(DOMAIN, COUNT, OFFSET):
        # вызываем переменные (передалать в аргументы)
        TOKEN_USER = 'vk1.a.idgea840z2Q86Sz_08YHecrdcBNfBWgRlRE9kEJrrdckENo4D2BxyfpXC3N_q9-hDm-b_JKz9VHDnbLdbwGnAfJMyNmBqrtPsx44G0zgscxiGhP4aGL04iSr-gF3l_O1SZSV-jM7FABEBDbK3GuonXUCk5DUgwQHoYxN7sTTxHS3m13HBfp9pd7-4-cthwDCjjwLU588ngOcvLVxCe-RvQ'
        VERSION = 5.236
        #DOMAIN = '21jqofa'
        #COUNT = 5 #количество загружаемых записей, сто - максимум
        #OFFSET = 0
        COLUMNS = ['text', 'images', 'likes', 'views']

        # через api vk вызываем статистику постов
        response = requests.get('https://api.vk.com/method/wall.get',
        params={'access_token': TOKEN_USER,
                'v': VERSION,
                'domain': DOMAIN,
                'count': COUNT,
                'offset': OFFSET
                #"'filter': str('owner') #филтр, пропускает только посты от группы
                })

        data = response.json()['response']['items']



        df = pd.DataFrame(columns=COLUMNS)

        for i in range(0, len(data)):
                for column in COLUMNS:
                        path = ''
                        if column == 'text':
                                path = data[i]['text']
                        elif column == 'images':
                                for j in range(0, len(data[i]['attachments'])):
                                        try:
                                                path += (data[i]['attachments'][j]['photo']['sizes'][-1]['url'] + '\n')
                                        except:
                                                pass
                        elif column == 'likes':
                                path = data[i]['likes']['count']
                        elif column == 'views':
                                path = data[i]['views']['count']
                        df.at [i, column] = path

        df.to_excel(DOMAIN + '.xlsx')#, encoding='windows-1251')
        return str(DOMAIN + '.xlsx')