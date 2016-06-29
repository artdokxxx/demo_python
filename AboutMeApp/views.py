from django.shortcuts import render
from DjangoDemo.settings import STATIC_URL
from datetime import date


def staticfiles(request):
    return {'STATIC': STATIC_URL}


def home(request):
    date_birthday = date(1991, 1, 3)
    date_diff = date.today() - date_birthday
    data = {'fio': 'леонтьев Артём пупырышкин',
            'age': (date_diff.days + date_diff.seconds / 86400) / 365.2425,
            'date_birthday': date_birthday, 'place_birthday': 'г.Сыктывкар',
            'hobbies': [{'icon': 'code', 'name': 'Программирование'},
                        {'icon': 'bicycle', 'name': 'Велоспорт'},
                        {'icon': 'car', 'name': 'Авто'}]}
    return render(request, 'index.html', data)


def work(request):
    places_work = [{'name': 'ООО "ИСС Дистрибьюшн"',
                    'desc': 'Российское представительство ESET(ООО ИСС Дистрибьюшн) открылось в январе 2005 года и входит в тройку стратегически важных представительств компании в мире. Российское представительство ESET также курирует продвижение и продажу программного обеспечения ESET в странах СНГ. На сегодняшний день региональные офисы компании открыты в Москве, Санкт-Петербурге, Самаре, Екатеринбурге, Краснодаре, Новосибирске и Алматы со штатом более 100 человек. По данным исследовательских компаний КОМКОН и «Ромир», ESET NOD32 является вторым по популярности антивирусным решением в России и защищает каждый третий компьютер. При этом 90% пользователей рекомендуют продукты ESET NOD32 своим друзьям и знакомым.',
                    'date_start': date(2011, 3, 1),
                    'date_finish': date(2013, 4, 1), 'site': 'http://eset.ru/',
                    'logo': 'eset_logo.png'},
                   {'name': 'ЗАО "Связной Логистика"',
                    'desc': '«Связной» — российская компания, федеральная розничная сеть, специализирующаяся на продаже услуг сотовых операторов и провайдеров проводного доступа в интернет, персональных средств связи, аксессуаров, портативной цифровой аудио- и фототехники.',
                    'date_start': date(2013, 4, 1),
                    'date_finish': date(2013, 11, 1),
                    'site': 'http://www.svyaznoy.ru/', 'logo': 'svz_logo.png'},
                   {'name': 'ООО "Рамблер"',
                    'desc': 'Rambler&Co — одна из крупнейших российских групп компаний, работающих в области медиа, технологий и электронной коммерции. Аудитория проектов - свыше 40 миллионов человек в месяц. Компания является лидером среди медиахолдингов по охвату в Рунете.',
                    'date_start': date(2013, 11, 1),
                    'site': 'https://rambler-co.ru',
                    'logo': 'rambler_logo.png'}, ]
    return render(request, 'work.html',
                  {'title': 'Информация об опыте работы', 'works': places_work})


def study(request):
    data = [
        {
            'name': '(МГУПП) Московский государственный университет пищевых производств Министерства образования Российской Федерации',
            'faculty': 'Институт информационных технологий, автоматизированных систем и технологического оборудования',
            'specialty': '230100: Информатика и вычислительная техника',
            'degree': 'Высшее (бакалавр), Дневная/Очная форма обучения.',
            'date_start': date(2008, 9, 1), 'date_finish': date(2012, 7, 20),
            'site': 'http://www.mgupp.ru/', 'logo': 'mgupp_logo.png'
        },
        {
            'name': '(МГУПП) Московский государственный университет пищевых производств Министерства образования Российской Федерации',
            'faculty': 'Институт информационных технологий, автоматизированных систем и технологического оборудования',
            'specialty': '230100: Информатика и вычислительная техника',
            'degree': 'Высшее (магистр), Дневная/Очная форма обучения.',
            'date_start': date(2012, 9, 1), 'date_finish': date(2014, 7, 20),
            'site': 'http://www.mgupp.ru/', 'logo': 'mgupp_logo.png'
        }
    ]
    return render(request, 'study.html', {'title': 'Информация о квалификации', 'studies': data})
