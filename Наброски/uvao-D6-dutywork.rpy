#Хозработы (Со Славей). Палевная Ветка
#
# Используется флаг alt_uvao_D5_sh_mines
#
label alt_day6_uvao_duty_sl:
    window hide
    $ alt_chapter(6, u"Юля. Хозработы")
    scene bg ext_square_day with dissolve
    play ambience ambience_camp_center_day fadein 4
    play music music_list["get_to_know_me_better"] fadein 4
    #REMOVE THIS!
    $ persistent.sprite_time = "day"
    $ day_time()
    #REMOVE THIS!
    window show
    "Славя уже была на месте и подметала площадку возле Генды. Вот ведь деятельная девочка! Не зря её вожатая своим заместителем назначила."
    dreamgirl "Само-собой. Кто-то ведь в лагере должен работать. А Ольге Ленивовне недосуг. Она занята - ленится."
    "Я бы тоже не отказался сейчас сесть на скамеечку, в тенёчек и предаться блаженной праздности. Но обещал ведь помочь, значит надо выполнять обещание."
    show sl normal pioneer far at center with dissolve
    "Я невольно залюбовался Славей, чуть не танцующей с метёлкой в руках. Как у неё ловко всё выходит. А подойдя поближе, ещё и услышал как она напевает какую-то мелодию."
    sl "…ах, какое блаженство, знать, что ты совершенство, знать, что ты идеал…"
    me "Привет ещё раз, Славя. Что это ты такое поёшь?"
    show sl smile pioneer at center with dissolve
    "Славя заметила меня и заулыбалась."
    sl "А, это из фильма одного. Про Леди Совершенство."
    me "Про тебя значит?"
    show sl shy pioneer with dspr
    "Не смог сдержать улыбки и я."
    sl "Ну что ты!"
    "Отмахнулась она, хотя я видел, что ей явно было приятно."
    sl "Какое я совершенство? Я обычная пионерка."
    "Решив оставить на потом размышления о совершенствах и пионерках, я спросил."
    show sl smile pioneer with dspr
    me "Слушай, Славь."
    sl "Да, Сёма?"
    me "Всё-таки, почему ты решила обратиться именно ко мне? Я ведь мог и отказаться."
    show sl laugh pioneer with dspr
    sl "На самом деле нет, не мог."
    "Рассмеялась девочка."
    "А я удивлённо поднял бровь. Как это понимать – \"не мог отказаться\"? Лагерь всё-таки не исправительный, а пионерский. Или она имеет ввиду что-то другое?"
    show sl smile pioneer with dspr
    sl "На самом деле, меня Ольга Дмитриевна к тебе направила."
    "Решила не томить меня неведением Славя."
    sl "Сказала, что ты на весь день поступаешь в моё личное распоряжение по хозяйственной части."
    "Ах вот оно что..  Видимо Славя заметила тень разочарования, мелькнувшую на моём лице, поэтому решила подсластить пилюлю."
    sl "Но я обратилась бы к тебе в любом случае. Мне хотелось бы, чтобы мне помогал именно ты. И я не хотела без лишней необходимости применять эту крайнюю меру принуждения."
    show sl shy pioneer with dspr
    sl "Я знала, что ты не откажешь мне, Сёма."
    "И она снова улыбнулась."
    show sl smile pioneer with dspr
    sl "А теперь, когда мы всё выяснили, давай начнём работать."
    hide sl with dissolve
    "Она скрылась  за постаментом  памятника и вышла оттуда со второй метлой в руках."
    show sl normal pioneer with dissolve
    sl "Вот, бери метлу, давай уберём площадь. Это не займёт много времени."
    "Я оглядел площадь. Ну да, конечно."
    "И внезапно вспомнил, что кого-то здесь явно не хватает."
    me "Так, а Электроник где? Помнится, у тебя ещё один помощник должен быть."
    sl "А он на сцене - проверяет электропроводку. Для подключения аппаратуры."
    me "Аппаратуры?"
    sl "Ну да, из музыкального клуба. Концерт же будет, забыл что-ли?"
    sl "Мы тут сейчас быстренько подметём и сразу туда. Он к этому времени тоже как раз должен закончить."
    window hide
    hide sl with dissolve
    window show
    "Ну быстро - не быстро, а примерно полчаса времени пришлось потратить на подметание. Мусора на площади было хоть отбавляй - нерадивые пионеры постарались. Вот их бы сейчас и заставить убираться."
    me "Что теперь? Садимся на мётлы -  и вперёд, на сцену?"
    show sl laugh pioneer at center with dissolve
    "Славя снова рассмеялась моей шутке."
    dreamgirl "Да ты сегодня в ударе, гусар."
    sl "Мётлы  можно пока здесь оставить, я их вечером отнесу в подсобку. А мы с тобой сразу в клуб пойдём. Электроник нас уже наверное заждался."
    sl "Я ему сказала, чтобы через полчаса был как штык возле музыкального клуба. А он очень ответственный, будет волноваться ещё."
    hide sl with dissolve
    "И оставив мётлы около памятника Генды, мы отправились к музыкальному клубу."
    window hide
    scene bg ext_musclub_day
    show sl normal pioneer
    with dissolve
    window show
    "Но возле клуба Электроника не было."
    th "Где же наш невероятно пунктуальный кибернетик?"
    el "Ребята! Вот вы где!"
    "Раздался сзади запыхавшийся голос Сыроежкина."
    show sl normal pioneer at right
    show el normal pioneer at left
    with dissolve
    el "Слушайте, где вы ходите? Я вас по всему лагерю ищу бегаю… Работа же стоит."
    "Сам того не подозревая, Электроник процитировал фразу из очень известного фильма."
    me "Работа стоит, а срок идёт. Не забывай: у тебя зарплата в рублях, а у меня в сутках."
    "В тон ему ответил я."
    show sl laugh pioneer at right
    show el laugh pioneer at left
    with dissolve
    "Все рассмеялись."
    show sl normal pioneer at right
    show el normal pioneer at left
    with dissolve
    sl "Ладно, заходим, а то и правда не успеем ничего."
    window hide
    play ambience ambience_music_club_day fadein 4
    scene bg int_musclub_day with dissolve
    window show
    "В этот раз Мику не сидела под роялем, а вполне себе репетировала какую-то песню. Наверное репертуар на вечер подбирает."
    show mi normal pioneer at right behind sl
    show sl normal pioneer
    show el normal pioneer at left
    with dissolve
    mi "Привет, ребята! Как хорошо, что вы зашли."
    "Защебетала болтушка и махнула головой, отчего длиннющие ультрамариновые хвосты её волос прыгнули вверх-вниз. Я невольно залюбовался."
    show mi happy pioneer at right with dspr
    mi "А мне Ольга Дмитриевна уже всё рассказала. Вечером будет концерт. Художественная самодеятельность."
    "И Мику от удовольствия зажмурилась."
    mi "Я буду играть и петь. Я много на чем умею играть, честно-честно. На гитаре, на барабанах и на флейте ещё."
    mi "И другие ребята будут играть. А ты, Сёмочка, играешь на чём-нибудь? А ты, Сыроежкин?"
    sl "Подожди, Мику."
    show mi normal pioneer at right with dspr
    "Остановила девочку-оркестр Славя."
    sl "Нам нужны инструменты и аппаратура."
    mi "Конечно-конечно, берите. Вот гитары, вот барабанная установка, вот усилитель, а вот здесь колонки."
    "Говорила она, показывая на озвученные предметы."
    mi "А вот шнуры ещё. И стойки для микрофонов."
    "Я почесал затылок, оглядывая всё это музыкальное добро. Много. За один раз-то и не унести. Но уж взялся за гуж…"
    "И вот уже второй раз мы с Электроником стали товарищами по несчастью в переноске всяких тяжёлых и бесполезных грузов."
    window hide
    play ambience ambience_camp_center_day fadein 4
    scene bg ext_stage_normal_day
    with dissolve
    window show
    "Проклятый усилитель оттянул мне все руки, а несчастные две сотни метров от клуба до сцены показались марафонской дистанцией. Почему здесь так распространён ручной труд? Надо в следующий раз какую-нибудь тачку приспособить."
    "Мы занесли деревянного монстра по ступенькам и с усилием поставили на дощатый пол сцены. Так, самое сложное позади. Правда своей очереди на переноску ожидают четыре колонки, но они явно весят меньше, чем усилок."
    "Провозившись пару часов, мы наконец перенесли всё. Хорошо, что девочки помогали. Да, Мику тоже не смогла усидеть в клубе, и под предлогом «мне тут одной всё равно скучно», вместе со Славей носила то, что полегче."
    play music eat_horn fadein 3
    "Тем не менее, всё устали и с облегчением вздохнули, когда раздался сигнал горна, призывающий пионеров на обед."
    stop music fadeout 5
    #jump на обед
    return 

#Хозработы. Беспалевная Ветка
#
# Используется флаг alt_uvao_D5_sh_mines
#
label alt_day6_uvao_duty:
    window hide
    $ alt_chapter(6, u"Юля. Хозработы")
    scene bg ext_dining_hall_near_day with dissolve
    play ambience ambience_camp_center_day fadein 4
    play music music_list["went_fishing_caught_a_girl"] fadein 4
    #REMOVE THIS!
    $ persistent.sprite_time = "day"
    $ day_time()
    #REMOVE THIS!
    window show
    "Надо наверное Юлю навестить. Или лучше всё-таки сходить после обеда? И сделать это надо как можно незаметнее. А то мне как будто сегодняшней взбучки мало. Кроме того, в обед булочки будут. А я как раз Юле обещал. Не идти же с пустыми руками."
    "Решено: возьму какое-нибудь поручение от вожатой и свалю по-тихому. Осталось придумать это самое поручение. И желательно подальше от центра лагеря. Что бы такое придумать?"
    "Но придумывать мне ничего не пришлось. У выхода из столовая меня уже ждала Ольга Дмитриевна собственной персоной."
    show mt normal panama pioneer at cleft with dissolve
    mt "Вот и ты, Семён. Прекрасно. Пойдём, прогуляемся."
    "Я мысленно застонал. Ну что же это такое…?"
    dreamgirl "Это карма, чувак. Смирись. А ещё лучше посмотри на это с другой стороны. Ведь ты искал повод уйти из лагеря. А теперь у тебя есть официальная причина – ты выполняешь поручение вожатой."
    "Чего-чего, а логического мышления у Шизы не отнять."
    dreamgirl "А то!"
    dreamgirl "Учись пока я здесь."
    th "И самодовольства тоже."
    dreamgirl "Эй. А вот это уже было обидно!"
    "Надеюсь я не кажусь со стороны полным тормозом, когда проходят вот такие внутренние беседы…"
    "А мы между тем прогулочным шагом шли по дорожке. Нас обогнали кибернетики, спеша по каким-то своим кибернетическим делам."
    window hide
    scene bg ext_dining_hall_away_day
    show mt normal panama pioneer at cleft
    with dissolve
    window show
    mt "Семён, я не стала говорить этого при всех. Ты вчера хоть и провинился отчасти, но есть некто, кто провинился ещё больше. Пусть и неумышленно, возможно."
    dreamgirl "Ну наконец-то. Справедливость восторжествовала! Аве, Ольга Дмитриевна!"
    "Я не обратил внимания на кривлянье Шизы. Не до того сейчас."
    me "И этот некто – Шурик, если я верно понимаю ситуацию."
    show mt smile panama pioneer at cleft with dspr
    mt "Совершенно верно."
    "Кивнула она головой."
    window hide
    scene bg ext_square_day
    show mt normal panama pioneer at cleft
    with dissolve
    window show
    "Тем временем мы уже подошли к площади."
    mt "Если честно, он меня вчера напугал довольно сильно. Такая неожиданная вспышка агрессии со стороны всегда спокойного человека."
    mt "Он ведь мог кого-нибудь серьёзно покалечить."
    me "Запросто. Он вообще страшный человек."
    show mt angry panama pioneer at cleft with dspr
    "Вожатая нахмурилась."
    mt "Семён, прекрати паясничать пожалуйста. В этом лагере хоть у кого-нибудь есть капля рассудительности?"
    show mt smile panama pioneer at cleft with dspr
    mt "Так вот, друг ты мой ситный. Я ведь не сказала, что проступок Шурика аннулирует твой."
    show mt normal panama pioneer at cleft with dspr
    mt "Расскажи-ка мне, где ты всё-таки вчера был первую половину дня? Почему ты вернулся такой грязный?"
    me "Я же говорю: ходил по грибы, по ягоды. Поскользнулся, упал…"
    dreamgirl "Очнулся – гипс."
    "Ожидаемо хохотнула Шиза."
    mt "Не думай, что я поверила в твои сказки на линейке."
    "Спокойно сказала вожатая."
    me "Мне больше нечего вам сказать."
    "Я пожал плечами."
    "Тогда Ольга Дмитриевна, видимо решив зайти с другого конца, спросила:"
    mt "Семён, а ты вчера не видел ничего необычного, подозрительного?"
    mt "Сам понимаешь, у нас тут всё-таки внештатная ситуация. Шурик пострадал, мы сами чуть не пострадали…"
    mt "Как вожатая, я обязана провести расследование."
    mt "А там, где ты вчера собирал грибы, ягоды… Кстати, напомни, где это было?"
    "И она выжидающе посмотрела на меня."
    "Ну Ольга Дмитриевна, ну тонкий психолог! Ага, щас. Так я всё и рассказал."
    me "Нет, ничего необычного не было."
    "Я снова пожал плечами."
    "Видимо вожатая поняла, что больше от меня ничего не добьётся."
    mt "Значит говорить ты не хочешь. Прекрасно."
    mt "Покидание пределов оздоровительного учреждения пионерами без сопровождения взрослых категорически запрещено."
    mt "Поэтому ты должен понести заслуженное наказание…"
    me "А как же…"
    "Начал я, вспомнив вчерашние мытарства с Шуриком."
    "Но Ольга Дмитриевна жестом остановила меня."
    mt "Но поскольку ты вчера принял активное участие в поисково-спасательных работах и показал себя надёжным товарищем, на которого можно положиться, то наказание частично аннулируется."
    me "Спасибо Ольга Дмитриевна! Я…"
    "Она снова остановила меня."
    mt "Я сказала – частично."
    mt "Поэтому, чтобы загладить свою вину полностью, ты сегодня ты весь день будешь работать на благо общества. И если будешь продолжать в том же духе, тогда, возможно, когда-нибудь ты станешь образцовым пионером."
    "И она замолчала, наконец оставив меня в покое. Надолго ли?"
    window hide
    play ambience ambience_camp_center_day fadein 4
    play music music_list["get_to_know_me_better"] fadein 4
    scene bg ext_stage_normal_day
    show mt normal panama pioneer at cleft
    show el sad pioneer far at right
    with dissolve
    window show
    "Тем временем мы подошли к сцене, где суетился Электроник. Он что-то подкручивал отвёрткой в неудобной позе и пыхтел от натуги. На лавках сидели ребята разных возрастов. Они весело болтали и смеялись."
    show sl smile pioneer with dissolve
    "Мимо прошла жизнерадостная и активная, как всегда, Славя. Эх, мне бы хоть капельку её энергии и оптимизма!"
    hide sl with dissolve
    show mt smile panama pioneer at cleft with dspr
    mt "Сыроежкин, принимай помощника!"
    show el normal pioneer far at right
    "Крикнула вожатая."
    "Тот распрямился и явно обрадовался."
    mt "Семён тебе поможет принести и расставить аппаратуру."
    mt "И чтобы сегодня к вечеру всё было готово!"
    show el laugh pioneer far at right with dspr
    el "Конечно, конечно, Ольга Дмитриевна."
    "Затараторил кибернетик."
    el "К вечеру всё будет готово, не беспокойтесь."
    el "Мы с Семёном всё сделаем."
    "Я с тоской посмотрел в сторону сцены. Да, многолюдно здесь. Сбежать явно не получится."
    "Но ничего, ещё не вечер…"
    me "Кажется меня об этом как-то забыли спросить…"
    "Пробурчал я про себя."
    show mt normal panama pioneer at cleft with dspr
    mt "Что ты говоришь, Семён?"
    "Притворилась, что не расслышала вожатая."
    me "Я говорю, что здесь же других ребят полно. И Славя вот например. Кроме того, у Электроника Шурик есть. Они в паре лучше работают."
    show mt angry panama pioneer at cleft with dspr
    mt "Семён."
    "Строго сказал вожатая."
    "Как же она обожает эти нравоучения."
    mt "Во первых, ты наказан, не забывай об этом. Во вторых, Шурик плохо себя чувствует, ты прекрасно знаешь об этом. В третьих, Славяна девочка. Неужели ты позволишь девочке выполнять мужскую работу, где требуется физическая сила?"
    mt "Так что за работу. А я потом приду и проверю."
    hide mt with dissolve
    "И, выполнив свою назидательную миссию, она удалилась."
    th "Я бы лично позволил. Мне совсем не улыбалось таскать здоровенные колонки и усилители по всему лагерю."
    dreamgirl "Эх ты, джентльмен…"
    th "А ещё лучше я бы нагрузил все эти тяжести на Шурика."
    dreamgirl "А вот это уже хорошая идея"
    "Хихикнула Шиза."
    th "Но не осуществимая"
    show el normal pioneer at center with dissolve
    "Тем временем ко мне подошёл отвратительно жизнерадостный Электроник."
    show el smile pioneer with dspr
    el "Ну что, Семён, поработаем?"
    "Весело спросил он."
    me "Сработаемся."
    "Мрачно ответил я."
    "Этот разговор вдруг почему-то напомнил мне сцену из какого-то фильма."
    me "Эл, скажи, а у вас в лагере несчастные случаи были?"
    show el surprise pioneer with dspr
    el "Нет, никогда. А почему ты спрашиваешь?"
    "Удивился кибернетик."
    show sl serious pioneer at left with dissolve
    sl "Семён, что ты такое говоришь?"
    "Строго спросила подошедшая Славя."
    sl "Какие ещё несчастные случаи?"
    show sl normal pioneer at left
    show el normal pioneer
    with dspr
    sl "Пойдёмте мальчики, у нас работы полно. Из клуба много чего перенести надо."
    "И мы втроём отправились в музыкальный клуб."
    window hide
    play ambience ambience_music_club_day fadein 4
    scene bg int_musclub_day with dissolve
    window show
    "В этот раз Мику не сидела под роялем, а вполне себе репетировала какую-то песню. Наверное репертуар на вечер подбирает."
    show mi normal pioneer at right behind sl
    show sl normal pioneer
    show el normal pioneer at left
    with dissolve
    mi "Привет, ребята! Как хорошо, что вы зашли."
    "Защебетала болтушка и махнула головой, отчего длиннющие ультрамариновые хвосты её волос прыгнули вверх-вниз. Я невольно залюбовался."
    show mi happy pioneer at right with dspr
    mi "А мне Ольга Дмитриевна уже всё рассказала. Вечером будет концерт. Художественная самодеятельность."
    "И Мику от удовольствия зажмурилась."
    mi "Я буду играть и петь. Я много на чем умею играть, честно-честно. На гитаре, на барабанах и на флейте ещё."
    mi "И другие ребята будут играть. А ты, Сёмочка, играешь на чём-нибудь? А ты, Сыроежкин?"
    sl "Подожди, Мику."
    show mi normal pioneer at right with dspr
    "Остановила девочку-оркестр Славя."
    sl "Нам нужны инструменты и аппаратура."
    mi "Конечно-конечно, берите. Вот гитары, вот барабанная установка, вот усилитель, а вот здесь колонки."
    "Говорила она, показывая на озвученные предметы."
    mi "А вот шнуры ещё. И стойки для микрофонов."
    "Я почесал затылок, оглядывая всё это музыкальное добро. Много. За один раз-то и не унести. Но уж взялся за гуж…"
    "И вот уже второй раз мы с Электроником стали товарищами по несчастью в переноске всяких тяжёлых и бесполезных грузов."
    window hide
    play ambience ambience_camp_center_day fadein 4
    scene bg ext_stage_normal_day
    with dissolve
    window show
    "Проклятый усилитель оттянул мне все руки, а несчастные две сотни метров от клуба до сцены показались марафонской дистанцией. Почему здесь так распространён ручной труд? Мы занесли деревянного монстра по ступенькам и с усилием поставили на дощатый пол сцены."
    show el normal pioneer at cright with dissolve
    "Я присел на край сцены, тяжело дыша. Болели руки. Электроник пристроился рядом. С меня градом лил пот. По лицу кибернетика было видно, что он чувствует себя не лучше. А ведь ещё четыре колонки, каждая из которых весит как половина усилителя ждали своего часа…"
    me "Передохнём пару минут."
    "Предложил я."
    el "Ага."
    sl "Семён, помоги пожалуйста."
    "Позвала Славя. Она расставляла по сцене микрофонные стойки."
    th "Блин! Ну почему я-то сразу?"
    "Пришлось встать и подойти."
    hide el
    show sl normal pioneer
    with dissolve
    me "Что такое, Славя?"
    "Спросил я, по возможности изображая дружелюбие."
    sl "Семён, ты устал?"
    show sl shy pioneer with dspr
    "Заботливо спросила активистка."
    me "Есть немного."
    "Небрежно кивнул головой я."
    me "Ничего страшного."
    me "Не надо обо мне беспокоиться. Беспокойся вон, о нём."
    "И показал на Электроника."
    show sl laugh pioneer with dspr
    sl "Да с ним всё будет в порядке."
    "Отмахнулась Славя."
    show sl shy pioneer with dspr
    sl "Другое дело ты…"
    "Как-то она это по особому сказала. Я внимательно посмотрел на девочку."
    "И выглядит она сейчас как-то иначе."
    me "А что я?"
    sl "Ну ты же вчера ещё днем где-то упал. Грязный ведь пришёл какой."
    sl "А потом ещё Шурик тебя стукнул. Тебе больно наверное было? Бедный…"
    "Почти промурлыкала Славя. Да она, что, флиртует со мной?"
    dreamgirl "Вот оно! Не упускай своего шанса. Девки на тебя штабелями вешаются, гусар."
    dreamgirl "Как говорится – дамы легли и просят."
    th "Нет, так нельзя. Что же, меня пальчиком помани и я пойду? Пусть знает, что меня голыми руками не возьмёшь. Голыми ногами, разве что. А ножки у Слави ничего, кстати."
    dreamgirl "Ах да, у тебя же вариантов дохрена. Понравился ты девочке, не видишь что-ли?"
    "Я внимательно посмотрел на Славю. Она также внимательно смотрела мне прямо в глаза."
    me "Ну допустим не стукнул."
    "Спокойно отпарировал я."
    me "Я просто поскользнулся. Вот и всё."
    me "Что делать-то надо?"
    sl "Да нет, нет, ничего…"
    show sl normal pioneer far with dissolve
    "Как-то рассеяно ответила она и отошла."
    hide sl with dissolve
    "Я пожал плечами. Не хотите – как хотите. Эх, сбежать бы к Юле сейчас!"
    "Но боюсь не получится, пока всю аппаратуру не перетаскаем. Но вот потом, когда концерт начнётся, за мной уже не будут так пристально следить…"
    show us normal pioneer with dissolve
    "Но как всегда планы мои были нарушены. В этот раз подбежавшей Ульянкой."
    us "Семён, там тебя ОльДмитревна искала. Сказала, чтобы ты домой шёл немедленно."
    hide us with dissolve
    "И она также быстро растворилась в кустах. Какой-то ниндзя просто."
    "Так, а если я уйду, кто же у нас будет выступать в роли вьючной лошадки? Впрочем это уже не моя забота. У меня официальный повод – вызов к вожатой. Интересно, что ей от меня понадобилось?"
    show sl normal pioneer far at fleft with dissolve
    "С такими мыслями я удалился. Славя проводила меня задумчивым взглядом. Да, с ней явно что-то не то."
    if not alt_uvao_D5_sh_mines:
        menu:
            "Забить на всё и пойти к Юле":
                #TODO: Jump
                "Идём в шахты к нашей кошочке"
            "Поверить Ульяне":
                jump alt_day6_uvao_isolator_house
    else:
        jump alt_day6_uvao_isolator_house
