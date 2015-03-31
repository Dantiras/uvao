# Д5-Обед
#
# используется флаг выхода на тру-энд alt_uvao_true
#
label alt_day5_uvao_lunch:
    $ routetag = "uv"
    $ alt_chapter(5, u"Юля. Обед")
    $ persistent.sprite_time = "day"
    $ day_time()
    play ambience ambience_dining_hall_full fadein 3
    scene bg int_dining_hall_people_day with fade
    window show
    "В столовой как всегда было не протолкнуться. Я осмотрелся."
    show mi normal pioneer far at fright with dissolve
    "Мику сидела и одиноко ковыряла ложкой перловую кашу."
    show dv smile pioneer far at right
    show us laugh pioneer far at cright
    with dissolve
    "Алиса с интересом слушала хохочущую Ульяну."
    show el sad pioneer far at fleft
    show sl normal pioneer far at left
    show mt sad pioneer far at cleft
    with dissolve
    "Электроник взволнованно объяснял что-то Славе и Ольге Дмитриевне."
#Даже медсестра Виола сидела, в жеманной позе, скрестив ноги, и слушала речи пионера.
    show cs normal far at center with dissolve
    "Сидящая чуть в стороне медсестра явно прислушивалась к речам пионера."
    if alt_uvao_true:
    #тру-ветка, отчёт перед Виолой
        "Заметив, что я вошёл в столовую, она одарила меня пристальным взглядом и слегка кивнула на свободное место напротив."
#        hide el
#        hide sl
#        hide mt
        hide dv
        hide us
        hide mi
        with dissolve
        "Так же сдержанно кивнув в ответ, я направился за подносом."
        dreamgirl "Прямо-таки конспиративная встреча Тульева и Исаева!{w} Надеюсь, ты уже выбрал пути отхода на случай провала? Капсула с ядом наготове?"
        "Ольга косо глянула на меня, но ничего не сказала, продолжив вполголоса что-то обсуждать со Славей и Элом."
        hide sl with easeoutleft
        "Впрочем, Славя почти сразу поднялась со своего места и куда-то убежала."
        show cs normal close at center
        hide el
        hide mt
        with dissolve
        "Стоило мне сесть напротив Виолы, как она тут же громко поинтересовалась у меня:"
        show cs smile close at center with dspr
        cs "Ну что, пионер, как самочувствие? Давай рассказывай! Предписания все выполнял?"
        dreamgirl "Знаем мы, какие предписания она имеет в виду! Ничего, ты можешь собой гордиться, непокобелимый ты наш!"
        "Почувствовав, что краснею, я замямлил:"
        me "Да я… Спасибо, лучше стало…"
        show cs normal close at center with dspr
        "Впрочем, следовало признать, что прикрытие Виолетта придумала довольно удобное."
        "Пристроив на лице выражение «мне неловко обсуждать такое при всех» и говоря вполголоса, я кратко отчитался об утренней экспедиции."
        "Услышав про Шурика, Виола нахмурилась:"
        cs "Что?! Он там наедине с аномалией остался?"
        me "Что такого-то? Юля ему всё равно на глаза не покажется."
        cs "Ей и необязательно показываться. Если твоя Юля решит, что он ей как-то угрожает…"
        "Она бросила взгляд на Ольгу и продолжила:"
        cs "Семён, необходимо как можно скорее его найти и увести оттуда."
        cs "Одного тебя отправлять глупо, да это и не понадобится.{w} Его ещё за завтраком хватились, так что сейчас начнут искать уже всерьёз."
        cs "Присоединишься к поисковой партии и проследишь, чтобы там всё прошло гладко, без ненужных контактов… пионер."
        me "Но…"
        "Не дожидаясь моего ответа, Виола обратилась к вожатой:"
        "Оль, тут вот пионер говорит, что видел сегодня Александра за пределами лагеря."
        th "Нет, ты подумай, какая наглость! Снова без меня меня женили!"
        show el sad pioneer at fleft
        show mt sad pioneer at cright
        show cs normal at fright
        with dissolve
    else:
    #не-тру-ветка
        hide dv
        hide us
        with dissolve
        "Я решил сесть рядом с Мику."
        th "Лучше уж потерять душевное равновесие, чем физическое здоровье, сев с рыжими."
        "Однако только я двинулся было в ту сторону, как меня окликнули:"
        mt "Семен! Подойди сюда."
        hide sl with easeoutleft
        "Ничего не оставалось кроме как подчиниться, тем более Славя уже ушла.{w} Я сел на освободившееся место."
        hide dv
        hide us
        hide mi
        show el sad pioneer at fleft
        show mt sad pioneer at cright
        show cs normal at fright
        with dissolve
        mt "Семен, ты не… Почему не в форме?"
        show mt angry pioneer at cright with dspr
        "Она кивнула на незавязанный галстук."
        me "Ну, я…"
        cs "Господи, Оль, сейчас не это важно!"
        me "Что-то случилось?"
        show mt sad pioneer at cright with dspr
        "Не успела Ольга Дмитриевна открыть рот, как Электроник воскликнул:"
        el "Шурик пропал!"
        me "Как пропал? Куда?"
        mt "Вот мы и решили поинтересоваться у тебя. Видел ли ты его сегодня?"
        me "Кстати, видел."
        show el surprise pioneer at fleft
        show mt surprise pioneer at cright
        with dspr
        "Электроник и Ольга Дмитриевна выпучили глаза. Даже тонкая бровь Виолы поползла вверх."
    mt "И где же?"
    me "В лесу. Он выглядел как-то потрепанно…"
    show el normal pioneer at fleft
    show mt normal pioneer at cright
    with dspr
    mt "Что он там делал?"
    if alt_uvao_true:
        "Она покосилась на Эла и добавила:"
        mt "…И кстати, что ты, Семён, там делал?"
    else:
        extend " Что ты там делал?"
    me "Ну, я гулял… Думал о своем…"
    if alt_uvao_true:
        cs "У Семёна лёгкая э-э… гипостеническая неврастения, так что я прописала ему прогулки на свежем воздухе в одиночестве."
        "Вмешалась Виолетта, обращаясь больше к Электронику, чем к Ольге Дмитриевне."
    me "Да не важно ведь! Важно, что {i}он{/i} там делал?"
    el "В лесу же ничего интересного! Хотя…"
    "Теперь все смотрели на Электроника."
    el "Может он ушел в старый лагерь?"
    dreamgirl "Не спались! Лицо проще!"
    me "А что он там мог забыть?"
    el "Я не знаю… Говорят, там были какие-то подвалы, или бункер со старым оборудованием."
    "Я покрылся холодным потом."
    if not alt_uvao_true:
        cs "С тобой все в порядке, пионер? Какой-то ты бледный."
        "Я не сразу понял, что обращаются ко мне."
        me "Да, я просто… Проголодался."
        "Я с остервенением начал проталкивать в себя пресную перловку, как бы подтверждая свои слова.{w} Было противно, но я ощущал три пары наблюдающих за мной глаз."
    "Обстановку разрядила прибежавшая Славя."
    show sl sad pioneer at cleft with dissolve
    sl "Девочки из младшего отряда видели, как он выходил со склада. Они говорят, что он шел в лес."
    mt "Что-нибудь еще?"
    sl "Да, они сказали, что он выскочил, ничего с собой не взяв. Женя так же сказала, что он спрашивал у нее батарейки для фонарика. И что она-то и отправила его на склад."
    show el surprise pioneer at fleft with dspr
    el "И она ничего не заподозрила?"
    me "А чего здесь подозревать? Руководитель технического кружка и батарейки - всё логично."
    show el normal pioneer at fleft with dspr
    "Ольга Дмитриевна отмахнулась от меня:"
    mt "Это дело десятое. Спасибо, Славя. Теперь мы знаем, что Шурик ушел в лес с фонариком."
    el "Это как раз подтверждает теорию о том, что он направился в старый корпус."
    el "Сами посудите, если бы он решил прогуляться в лесу, то он бы взял спальник или еще что-то. В конце концов, у него же аналитический ум, он привык все продумывать…"
    mt "Что ж, теперь на повестке дня вопрос: что делать дальше?"
    el "Как что? Искать его надо!"
    "Электроник демонстративно ударил по столу кулаком."
    mt "А кто искать пойдет?"
    cs "От меня помощи не ждите, у меня полный изолятор пациентов."
    show sl normal pioneer at cleft with dspr
    sl "Борис Александрович сказал, что у него инвентаризация. Говорит, приказ директора лагеря."
    "Я подивился осведомленностью Слави. Впрочем, от нее другого ожидать не приходилось."
    "Ольга Дмитриевна не отрываясь смотрела на меня."
    mt "Отлично, сформируем поисковый отряд. Выступаем после обеда. Нас четверо, думаю хватит."
    sl "Простите, но я не могу. Я же предупреждала…"
    cs "Да-да, прости Ольга, но сегодня она моя пациентка."
    show sl shy pioneer at cleft with dspr
    "Славя покраснела."
    "На лице Электроника, впрочем как и на моем, красовалось недоумение."
    "Виола и Славя покинули столик и направились к выходу."
    hide sl
    hide cs
    with dissolve
    if alt_uvao_true:
        th "Если уж я собираюсь идти на поиски, как просила Виола, то сейчас самое время прояснить этот вопрос."
        me "Э-э… Судя по всему, мне тоже придётся идти?"
        mt "Ты должен, Семен! Это твой пионерский долг. Где это видано, чтобы пионер бросал товарища в беде?"
        "Я возможно небрежнее пожал плечами:"
        me "Да нет, в принципе-то я не против…"
        mt "Вот и отлично!"
        "Отрезала Ольга Дмитриевна."
    else:
        "И тут меня осенило, к чему клонит вожатая."
        me "Э-э, нет!"
        mt "Ты должен, Семен! Это твой пионерский долг. Где это видано, чтобы пионер бросал товарища в беде?"
        me "Но…"
        show mt angry pioneer at cright with dspr
    mt "Тем более ты последний, кто его видел. Сыроежкин тоже пойдет с нами, ты ведь знаешь дорогу туда?"
    "Она уже обращалась к Электронику."
    el "Ну… В теории…"
    show mt normal pioneer at cright with dspr
    mt "Еще одного человека в группу я так и быть найду. И пойду с вами, в качестве контроля. Встретимся на площади, там все обсудим."
    "Она встала из-за стола и направилась к выходу."
    hide mt with dissolve
    el "Я пойду, подготовлюсь."
    "Электроник тут же засуетился и чуть ли не бегом покинул столовую."
    hide el with dissolve
    dreamgirl "С Жужелицей попрощаться пошел, не иначе…"
    "Я мысленно кивнул Шизе."
    if alt_uvao_true:
        "Аппетита больше не было. Да и какой сейчас аппетит?{w} Если Юлю обнаружат…"
    else:
        "От перловки было противно, и я залпом выпил компот, стараясь перебить вкус."
        "Аппетита больше не было. Да и какой сейчас аппетит?{w} Юлю обнаружат, потом разбор полетов, а затем…"
    "Я встал, убрал посуду с так и не начатой рыбной котлетой и направился к выходу."
    stop ambience fadeout 2
