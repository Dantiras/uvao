# Д5-Совместная охота на дикого Шурика
#
# используется флаг выхода на тру-энд alt_uvao_true
# используется флаг обеда в Д4 с Леной alt_uvao_D4_lunch_un
#
label alt_day5_capture_sh_together:
    $ routetag = "uv"
# очень хочется назвать главу "{i}Иск{/i}педиция", но боюсь, что не все оценят...
    $ alt_chapter(5, u"Юля. Поиски")
    $ persistent.sprite_time = "day"
    $ day_time()
    play ambience ambience_camp_center_day fadein 3
    play sound_loop ambience_medium_crowd_outdoors fadein 2
    scene bg ext_dining_hall_away_day with fade
    window show
# не забываем перед обедом отнести рюкзак домой
    "Выйдя из столовой, я машинально направился было к своему домику за рюкзаком, но быстро спохватился."
    th "Зачем он мне? Идём мы ненадолго, вряд ли что-то из него может понадобиться.{w} Только таскать зря."
    "Так что я развернулся и зашагал в сторону площади."
    th "Интересно, кого Ольга в отряд четвёртым припашет?{w} Что-то мне подсказывает, что кроме Слави никто добровольно на это не подписался бы…"
# площадь
    window hide
    scene bg ext_square_day with dissolve
    $ renpy.pause(1)
    window show
    "На площади никого из остальных участников спасательной экспедиции ещё не было."
    "К этому времени я успел успокоиться насчёт возможной поимки Юли и последующих неприятностей."
    th "В конце-то концов, до сих пор её не поймали - может и сейчас всё обойдётся. Тем более, я смогу вмешаться, если что."
    "Я развалился на скамеечке возле вечно поправляющего очки Генды, лениво размышляя о вынужденных добровольцах, таинственной болезни Слави…{w} И о том, что зря я не доел свой обед."
    th "И понесла же этого Шурика нелёгкая шляться где не надо!"
    th "Интересно, случайно он в старый корпус потащился именно сегодня, или всё-таки следил за мной?{w} А если следил - то зачем?"
    show un normal pioneer at center with dissolve
    un "Привет…"
    play music music_list["i_dont_blame_you"] fadein 3
    "Я вздрогнул, вырванный из потока своих размышлений незаметно подошедшей Леной."
    me "Привет…"
    un "Мне Ольга велела на площадь прийти…"
    "Надо думать, мой вгляд наглядно демонстрировал полное отсутствие мыслительных процессов, потому что она добавила:"
    un "Сказала, что я с вами пойду Шурика искать…"
    show un shy pioneer with dspr
    "Тут Лена порозовела и уставилась куда-то себе под ноги."
    me "Э-э-э… Ну да, ясно…"
    "Я наконец-то вышел из ступора и поспешно подвинулся, освобождая на скамейке место:"
    me "Садись, подождём вместе.{w} Если ты не против, конечно…"
    show un normal pioneer close at fleft with dissolve2
    "Я не удивился бы, окажись Лена очень даже против, но она неожиданно спокойно кивнула и присела на краешек скамейки."
    th "Ну конечно, кого ещё припахать в поисковую партию?{w} Правильно - того, кто не сумеет отвертеться!"
    if alt_uvao_D4_lunch_un:
        "Мне вдруг вспомнился вчерашний обед."
        th "Как бы моя любезность мне же не вышла боком.{w} Что прикажете делать, если она сейчас отморозится, как вчера, или решит довести до конца своё признание, о чём бы оно ни было?"
        th "Только этих хлопот мне сейчас не хватает! Сбежать от неё что ли, пока не поздно?"
        dreamgirl "Ты лучше подумай, что станешь делать, если решишь-таки сбежать, а она возьмёт и за тобой погонится!"
        th "Кажется, самое разумное, что можно сделать сейчас - это держать рот на замке."
    else:
        me "Э-э…"
        "На этом моё красноречие иссякло."
    "С минуту мы молчали.{w} Впрочем, Лену, кажется, это не слишком тяготило."
    show un smile pioneer close with dspr
    "Внимательно посмотрев на мою смущённую физиономию, она вдруг слегка улыбнулась, поёрзала, устраиваясь поудобнее, и мечтательно уставилась в небо, откинувшись на спинку скамейки."
    th "Кажется, мы поменялись ролями. Теперь моя очередь отмораживаться, а Лена радуется жизни…"
    "Я растерянно перевёл взгляд вверх. По выцветшему от жары послеобеденному небу лениво ползли редкие облака.{w} Где-то в кустах неподалёку перекликались птицы."
    "Мимо вальяжно прошествовали к своим домикам несколько пионеров из младших - переваривать обед."
    "Так мы и сидели молча посреди сонного лагеря - Лена с едва заметной улыбкой на губах, спокойно разглядывающая облака, и я, растерянно переводящий взгляд с девочки на небо и обратно."
    "Насмешливо взирающий на нас Генда явно понимал в происходящем больше моего, но делиться секретами не спешил."
    stop music fadeout 7
    show mt normal panama pioneer far with dissolve
    mt "Ага, вы уже здесь, это хорошо!"
    show mt angry panama pioneer
    show un normal pioneer close
    with dissolve
    extend " А где Сыроежкин? Его почему нет?!"
    "Не могу сказать, что я так уж рад был видеть Ольгу Дмитриевну, а слышать - и того меньше."
    show mt normal panama pioneer with dissolve
    "С другой стороны, наедине с Леной сидеть было ещё хуже.{w} Трудно находиться рядом с человеком, чьи действия не можешь предугадать."
    "Немного жаль только было видеть, как с появлением вожатой девочка снова спряталась, словно улитка в раковину, за свою обычную маску и теперь любовалась уже не небом, а плитами под ногами."
    th "Это не девочка, а какая-то шкатулка фокусника! Каждый раз что-то новое, и каждый раз - неожиданное."
    th "Похоже, она и вправду расслабилась в моём присутствии. С чего бы это?"
    dreamgirl "А тебе бы только клювом щёлкать!"
    dreamgirl "Девочка тебе редкое доверие оказала, позволила наблюдать себя, можно сказать, в естественной среде обитания, а ты даже поговорить с ней не мог!"
    th "Да о чём с ней говорить-то?{w} А главное - она, кажется, и без моей болтовни выглядела вполне довольной жизнью."
    if alt_uvao_D4_lunch_un:
        th "Помнится, кто-то мне впаривал вчера про «загрузит проблемами» и про «оно тебе надо?». Не ты ли?"
        dreamgirl "Да мало ли что я тебе наговорю, а ты и рад слушать, развесил уши!"
    "Начинающуюся пикировку с невидимым собеседником весьма кстати прервал вбежавший на площадь запыхавшийся Электроник."
    show el pioneer slap at fright with dissolve
    "В глаза бросалась некоторая ассиметрия его раскрасневшегося лица - одна щека была заметно румянее другой."
    dreamgirl "Вот кто у нас времени не теряет, так это Эл!"
    dreamgirl "Хотя непохоже, что ему от этого много радости - Жужелица явно перешла от слов к методам физического воздействия."
    show mt angry panama pioneer with dissolve
    el "Извините!{w=0.8} Что заставил!{w=0.8} Ждать!"
    "Выдохнул Электроник."
    "Вожатая одарила его кислым взглядом, но выговаривать ему не стала."
    play music music_list["always_ready"] fadein 3
    "Оглядев наше грозное войско (два дрища-интеллектуала и девочка-стесняша), она спросила командирским голосом:"
    show mt normal panama pioneer with dissolve
    mt "Ну что, все готовы?"
    show un normal pioneer with dissolve
    "Не знаю, как остальные, но лично я себя чувствовал готовым разве что к послеобеденному сну."
    "Впрочем, Ольга не стала дожидаться ответа, скомандовав:"
    mt "Тогда пошли!"
    "Развернувшись, она уверенно пошла в сторону дорожки мимо домиков, в конце которой пряталась калитка в заборе."
    hide mt with dissolve
    th "Минуточку! Предполагалось, что единственный, кто знает дорогу к старому корпусу - это Эл!{w} Ну и фрукт же эта вожатая!"
    "Переглянувшись, мы поплелись следом за ней."
    stop sound_loop fadeout 3
    stop ambience fadeout 3
    window hide
    scene bg ext_path_day with dissolve
    play ambience ambience_forest_day fadein 3
    $ renpy.pause(1)
    window show
#
    show mt normal panama pioneer at center
    show el sad pioneer at right
    show un normal pioneer at left
    with dissolve
    "Довольно скоро я понял, что по утреннему холодку ходить по лесу намного приятнее."
    "День давно уже перевалил за середину, под деревьями было душно. Слабый ветерок, едва слышно шевеливший листья наверху, до тропинки не доставал."
    "Несмотря на жару, Ольга с самого начала задала быстрый темп, так что буквально через пару минут пот уже заливал мне глаза, а рубашка прилипла к телу."
    "Судя по взглядам, которые бросали Эл с Леной на вожатую, и по их тяжёлому дыханию, они тоже были не в восторге от выбранной скорости."
    th "И разумеется, никто из нас, включая Ольгу, не догадался захватить с собой воды. Красавцы!"
    if alt_uvao_true:
        # если тру, то очень хотим поскорее добраться до места и выручать Шурика, чтобы Юля не обидела, но устаём очень.
        th "Конечно, хорошо бы поскорее добраться до старого корпуса и найти Шурика, пока он там не начал гоняться за Юлей…"
        dreamgirl "…Или пока Юля не завялила Шурика в запасы на зиму - или на какие там угрозы для окружающих намекала Виолетта?…"
        th "…Однако, если мы не сбавим скорость, то долго я по такой жаре не протяну!"
        dreamgirl "Ну и метаболизм у вожатки! Утром ещё с похмелья зелёная была, а сейчас полюбуйтесь на неё!{w} Спортсменка, комсомолка!"
        th "Может, она потому и бодрая такая, что от вчерашнего не отошла?"
        dreamgirl "Бодрая, потому что с похмелья?! Ты вообще соображаешь, что несёшь?"
        th "Нет, не соображаю…{w} Жарко мне, отстань…"
    window hide
    scene bg ext_path2_day with dissolve
    window show
    show mt normal panama pioneer at center
    show el sad pioneer at right
    show un normal pioneer at left
    with dissolve
    "По мере того, как тропинка становилась уже, а за ноги всё чаще цеплялись корни деревьев, моя решимость кого-то спасать стремительно убывала."
# по Автору весь путь - метров шестьсот
    "В какой-то момент я решился было плюнуть на самолюбие и запросить пощады, но тут мы вышли наконец к опушке возле старого корпуса."
    "Тут мне пришло в голову, что если мы и дальше попрёмся всей толпой, то вполне можем нарваться на Юлю, а это не нужно ни ей, ни нам."
    me "Ольга Дмитриевна, как Вы думаете, может быть нам не стоит идти сразу всем вместе? Мало ли, вдруг Шурик испугается…"
    show el surprise pioneer
    show mt surprise panama pioneer
    show un surprise pioneer
    with dspr
    mt "Семён, что ты несёшь?! Почему это он должен нас пугаться?"
    "На это возразить мне было нечего, тем более, что Электроник с Леной тоже посмотрели на меня с недоумением."
    show el sad pioneer
    show mt normal panama pioneer
    show un normal pioneer
    with dspr
    "Остановившись, Ольга несколько раз крикнула:"
    mt "Шурик!!! Шурик!!!"
    "Ей никто не ответил, и мы пошли дальше."
    th "Что же, по крайней мере, хоть шум подняли. Вряд ли Юля могла не услышать вожатую."
    th "Надеюсь, у неё хватит сообразительности куда-нибудь уйти или спрятаться."
    dreamgirl "А ты не боишься, что у Шурик тоже услышал вопли вашей предводительницы, и у него тоже хватит смекалки не попадаться вам на глаза?"
    "Преодолев последние метры между редеющими кустами, мы вышли на поляну перед знакомым уже мне зданием старого корпуса."
    window hide
    scene bg ext_old_building_day with dissolve
    window show
    show el sad pioneer at left
    show un normal pioneer at fleft
    show mt normal panama pioneer at center
    with dissolve
    "Здесь Ольга Дмитриевна остановилась."
    mt "Шурик!!!"
    "Снова никакого ответа.{w} Вожатая обернулась к нам."
    mt "Может быть, Александра здесь и нет, иначе бы он уже отозвался. Но всё равно, сначала нам надо осмотреть здание."
    mt "Думаю, если мы разделимся…"
    stop music fadeout 2
    play sound sfx_tree_branches
    show sh angry bar3 far at fright with dissolve
    show el surprise pioneer at left
    show un surprise pioneer at fleft
    show mt surprise panama pioneer at center
    with dissolve
    "Её прервал треск веток позади нас, и из кустов выбрался наш драгоценный Шурик."
    play music music_list["doomed_to_be_defeated"] fadein 3
    "Видок у него был тот ещё. Его словно таскали волоком по земле - весь в какой-то грязи, одежда местами порвана, на руках и ногах свежие ссадины, волосы растрёпаны."
    show el scared pioneer at left
    show un scared pioneer at fleft
    show mt scared3 panama pioneer at center #| Бегун, предполагалось, что указательный палец вожатой чуть-чуть закрывает рот. Видишь, он чуть-чуть снизу не дорисован? - Ленофаг
    with dissolve
    "Тут стоящая рядом Лена испуганно пискнула и спряталась мне за спину."
    hide un with easeoutleft
    "Через секунду и до меня дошло, чего она так испугалась - в руке Шурик сжимал увесистый на вид кусок арматуры.{w} В сочетании с перекошенным от гнева лицом и криво сидящими очками зрелище и в самом деле было устрашающее."
    show el scared pioneer at fleft
    show mt scared3 panama pioneer at cleft
    with ease
    "Мельком глянув на Ольгу с Элом я убедился, что они тоже не больно-то рвутся обнимать от радости вновь обретённого товарища."
    "В другой ситуации я бы и сам с удовольствием попраздновал труса, но наличие за спиной дрожащей от страха девочки странным образом в корне всё изменило."
    hide mt
    hide el
    show sh angry bar3 far at right
    with dissolve2
    "Я расправил плечи и медленно двинулся навстречу Шурику, стараясь улыбаться пошире."
    show sh angry bar at center with dissolve
    sh "Не подходи!"
    "Заверещал тот, выкатив налитые кровью глаза и выставляя перед собой арматурину, словно меч."
    me "Шурик, ты же пионер, успокойся!"
    me "Брось арматурину, это не наш метод.{w} Где гуманизм? Где человек человеку?"
    sh "Гуманизм? Да вы же вообще не люди! Вы - голоса в моей голове.{w} Хватит меня за нос водить! Вас нет.{w=.8} ВАС НЕТ!{w=.8} ВЫ - ГОЛОСА!{w=.8} УХОДИТЕ!"
    $ renpy.music.set_volume(0.5, delay=5, channel='music')
    "Мне очень не понравился нездоровый блеск в его глазах, а ещё меньше понравилось то, что в такт последним словам Шурик принялся размахивать железякой перед собой."
    th "Да что он, под кайфом?!"
    $ renpy.music.set_volume(0.3, delay=1.5, channel='music')
    me "Шурик? Может, не надо?"
# CG Шурик атакуэ!
    window hide
    stop music fadeout 0
    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    scene cg d4_sh_stay
    with dissolve
    play music music_list["pile"] fadein 0
    window show
    "Вместо ответа он ринулся на меня с бессвязным воплем, замахиваясь куском арматуры."
    #play sound mpbt
    "От хилого на вид очкарика я никак не ожидал такой прыти…"
    dreamgirl "Не зевай!"
    with hpunch
    "В последний момент я сумел каким-то чудом увернуться от удара, но потерял равновесие и чуть не упал на спину."
    window hide
    scene bg ext_old_building_day
    show sh angry bar3 far at left
    with dissolve
    window show
    "Прежде чем я успел опомниться, Шурик уже снова пёр на меня, замахиваясь своим импровизированным мачете."
    show sh angry bar at center with dspr
    "Непроизвольно я вскинул руку, уже сознавая, что это бесполезная жертва и следующим ударом он всё равно раскроит мне череп…"
    show sh angry bar2 close at center with dspr
    "…Как вдруг увидел краем глаза какое-то движение сбоку. Шурика крутануло в сторону, и он, пролетев мимо меня, мешком рухнул на землю лицом вниз." #Показать спрайт испуганного Шурика, типа неждан?
    hide sh with easeoutleft
    "На этот раз я не терял время даром и, растянувшись в прыжке словно вратарь, пытающийся взять идущий низом мяч, со всего маху приземлился на спину Шурику."
    with vpunch
    show sh rage pioneer close at center with easeinbottom
    "Тот сдавленно крякнул, а я вцепился что было сил в его правое запястье, выкручивая руку с несостоявшимся орудием убийства."
    show el upset pioneer close at right behind sh with dissolve #| Я попробую что-нибудь сделать с этим спрайтом. Он тут не в тему. А вариант вроде  - *показать дефолтный спрайт злого Эла* - Он замахнулся и лихим ударам, словно каратист, вырубил Шурика - мне кажется явно тут не прокатит - Леноваг
    "Тут ко мне на помощь подоспел Сыроежкин."
    with hpunch
    "Вдвоём мы сумели заломать Шурику руки за спину.{w} Тот хрипел что-то неразборчиво в землю, отчаянно пытаясь освободиться."
    with vpunch
    "Что делать дальше, я не имел ни малейшего представления."
    th "Отпустить его нельзя. Связать бы, но чем?"
    dreamgirl "Свяжите его полотенцами, как того поэта!"
# нет, я не уверен, что намёк про полотенца так уж необходим - Бегун
    with vpunch
    "От неожиданности я ослабил было хватку, так что Шурик чуть не вырвался."
# раз уш Эл переехал вправо, то ОД едет влево
    show mt angry panama pioneer at fleft with dissolve
    mt "Ну-ка, переверните его!"
    "Раздался откуда-то сверху неожиданно спокойный голос вожатой."
    "Пыхтя от натуги, мы с Элом кое-как выполнили её распоряжение."
    with hpunch
    "Ольга нагнулась… И залепила Шурику звонкую оплеуху!"
    play sound sfx_face_slap
    show sh upset pioneer close with dspr
    sh "Ай!"
    play sound_loop sfx_face_slap
    "Последовала целая серия деловитых пощёчин, у бедняги только голова моталась туда-сюда."
    stop sound_loop fadeout 1
    dreamgirl "Браво! Брависсимо!"
    if alt_uvao_true:
        extend " Вот это я понимаю, настоящий специалист по адаптации! Прирождённый психолух!"
    else:
        extend " Во даёт вожатка! Так ему!{w} Слева! Справа!"
    "Наконец Шурик завопил:"
    show sh scared pioneer close with dspr
    sh "Ай! Да перестаньте же! За что?!"
    sh "Перестаньте меня бить! Отпустите!"
    stop music fadeout 9
    "Он как-то разом обмяк в наших руках, переводя испуганный взгляд с меня на Эла."
    show mt normal panama pioneer with dspr
    "Ольга вгляделась в его лицо и удовлетворённо кивнула."
    mt "Александр, как ты себя чувствуешь?"
    "Спросила она как ни в чём ни бывало."
    show sh normal pioneer close with dissolve
    sh "Н-нормально… А… А где это мы?"
    "Он ошарашенно завертел головой, оглядываясь. Увидев здание неподалёку, он явно удивился."
    show sh surprise pioneer close with dspr
    sh "Что вообще здесь происходит?"
    me "Что происходит?!"
    "Не выдержав, я перешёл на крик:"
    me "Ты только что мне голову чуть не пробил, вот что происходит!"
    show sh scared pioneer close with dspr
    sh "Я?!"
    mt "Семён, подожди!"
    "Вмешалась Ольга Дмитриевна."
    mt "Шурик, ты что последнее помнишь перед тем, как я… В общем, перед тем, как ты пришёл в себя здесь?"
    show sh upset pioneer close with dspr
    sh "Я… Я утром собирался пойти в старый корпус…"
    "Он бросил на меня вороватый взгляд и поспешно добавил:"
    sh "…За радиодеталями! Я слышал, там старое бомбоубежище внизу есть!"
    sh "Я вышел из лагеря, пошёл по тропинке сюда и потом…"
    sh "Я… Я не помню… Голова кружится…"
    "Лицо Шурика побледнело, он болезненно скривился:"
    show sh scared pioneer close with dspr
    sh "Да отпустите вы меня, ведь больно же!"
    mt "Действительно, ребята, отпустите его.{w} Думаю, он никуда теперь не убежит и вообще будет себя хорошо вести.{w} Правда, Шурик?"
    "Тот слабо кивнул.{w} Поняв, что всё ещё продолжаю выкручивать ему руки, я разжал захват."
    show sh upset pioneer close with dspr
    "Отчаянно заныло колено, пораненное утром при попытке открыть дверь в бункер.{w} Похоже, я снова здорово им приложился, когда прыгал на Шурика."
    th "Надеюсь, этому психу я тоже что-нибудь отшиб!"
    "Уложив совместными с вожатой усилиями Шурика на траву, Электроник принялся шарить вокруг в поисках очков, слетевших с того при падении."
    hide el
    hide sh
    with dissolve2
    mt "Семён, ты как?"
    "Негромко спросила Ольга Дмитриевна."
    me "Всё в порядке."
    "Кивнул я. Меня порядком трясло, но показывать этого не хотелось."
    "Подождав, пока дрожь немного утихнет, я, кое-как встав сначала на четвереньки, а потом и на ноги, огляделся по сторонам."
    window hide
    hide mt
    with dissolve
# далее спрайты un подлежат подгонке по положению на сцене и по transitions
    $ renpy.pause(1)
    show un normal pioneer far with dissolve2
    window show
    "Лена тихонько стояла в нескольких шагах от нас, не вмешиваясь в допрос."
    "Поймав мой взгляд, она явно смутилась."
    dreamgirl "Знаешь, есть у меня одна идея…"
    th "Кажется, у меня тоже."
    show un normal pioneer with dissolve2
    "Я подошёл к девочке и негромко спросил:"
    me "Лена, скажи, а ты не в курсе, как вышло, что Шурик вдруг так вовремя упал?"
    show un shy pioneer with dspr
    "Она засмущалась ещё больше и ничего не ответила."
    me "Это ведь ты ему помогла, да? Ловко у тебя вышло! Как по учебнику."
    "Я не видел, как там всё было на самом деле, но решил, что сейчас тот самый случай, когда лучше перехвалить."
    "В конце концов, нужного результата она достигла, а как именно - это уже детали."
    "Лена отчаянно покраснела и пролепетала еле слышно:"
    un "Я боялась, у меня не получится…{w} Мне папа показывал… На всякий случай, если…{w} Но я никогда раньше…"
    show un cry_smile pioneer with dissolve
    if alt_uvao_D4_lunch_un:
        "Она подняла взгляд и продолжила, гипнотизируя меня своими зелёными глазищами точь-в-точь, как вчера за обедом:"
    else:
        "Она вдруг посмотрела мне прямо в глаза."
    un "Сама не знаю, что на меня нашло, но я так за тебя испугалась, когда…"
    "Тут она окончательно смутилась и отвернулась в сторону."
    show un shy pioneer with dissolve
    "Чувствуя, что и сам краснею, я сделал несколько глубоких вдохов и выдохов."
    "Потом сказал, стараясь, чтобы голос звучал твёрдо:"
    me "Если бы не ты, я сейчас лежал бы с проломленным черепом."
    "Лена вздрогнула, но промолчала."
    me "Спасибо тебе большое. Кажется, я теперь твой должник."
    me "И да, если вдруг когда-нибудь снова захочешь спасти меня от неминуемой смерти - прошу, не отказывай себе в этом маленьком удовольствии."
    show un smile pioneer with dissolve
    "Лена в ответ смущённо хихикнула и, кажется, немного расслабилась."
    dreamgirl "А теперь самое время обменяться кольцами и поцеловать друг друга!"
    dreamgirl "Или нет, пусть лучше она объявит себя твоим рыцарем и поклянётся оберегать и защищать тебя до самой смерти!"
    mt "Лена, Семён, идите сюда!"
    show un normal pioneer with dspr
    "Голос вожатой весьма вовремя отвлёк меня от мысли подобрать ту арматурину и довести до конца затеянную Шуриком трепанацию моей черепной коробки, дабы успокоить одного навязчивого внутреннего придурка."
    show un sad pioneer far at fleft
    show el sad pioneer at right
    show sh cry pioneer at center
    show mt sad panama pioneer at left
    with dissolve
    "Мы подошли к остальным.{w} Шурик теперь уже не лежал, а сидел на траве, но выглядел всё так же неважно."
# взгляд расфокусировавшийся
    dreamgirl "Лицо бледное, взгляд мутный. Похоже, наш Рэмбо порядком подустал.{w} Перенапрягся, пока по кустам бегал да железяками размахивал, вот головка и бо-бо."
    th "Ты-то веселишься. А я вот уже догадываюсь, кто его сейчас потащит на себе."
    "К сожалению, вожатая подтвердила мои опасения."
    play music music_list["always_ready"] fadein 5
    mt "Надо бы поскорее доставить Александра в медпункт."
    mt "Давайте попробуем его поднять - может быть, он сможет идти, если вы будете его поддерживать с двух сторон."
    "Ухватив Шурика под руки, мы с Элом кое-как подняли его и даже сумели сделать несколько шагов, после чего ноги у болящего подогнулись и вся наша троица полетела на землю."
    play sound sfx_bodyfall_1
    with vpunch
    "И разумеется, меня в третий раз угораздило приложиться больной ногой!{w} С трудом сдерживая рвущиеся с языка ругательства я поднялся."
    mt "Кажется, придётся кому-то бежать в лагерь за помощью. Без носилок не обойтись."
    show sh upset pioneer with dissolve
    "Тут я сообразил, что за всей этой вознёй я совсем забыл про Юлю."
    th "Оставаться здесь сейчас совсем не с руки."
    if alt_uvao_true:
# dreamgirl "может, Юля шибанула."
        dreamgirl "И вообще, не ушастая ли ему помогла крышу потерять? Может, Виола на что-то такое и намекала?"
    me "Эл, ты на «замке» когда-нибудь человека носил?"
    show el surprise pioneer with dspr
    "До Сыроежкина довольно быстро дошло, что я имею в виду."
    show el sad pioneer with dspr
    el "Нет, нам рассказывали в школе, но применить на практике как-то никогда не приходилось."
    me "Ну вот и попрактикуемся сейчас.{w} Как думаешь, осилишь?"
    "Эл вздохнул:"
    show el normal pioneer with dspr
    el "Во всяком случае, мы должны попробовать. Не можем же мы бросить друга в беде!"
    "Сдержавшись, я не стал развивать тему своих дружеских чувств к Шурику, вместо этого просто кивнув."
    "С третьей попытки мы с Элом сообразили, как правильно сложить руки в замок."
    "Ольга Дмитриевна с Леной помогли Шурику усеться на получившееся сиденье, он ухватился за наши плечи, и мы с Элом потащили его в лагерь."
    window hide
    scene bg ext_path2_day with dissolve
    window show
    "Обратная дорога запомнилась преимущественно как множество веток, норовящих ударить по лицу, и корней, упорно цепляющих за ноги."
    "Идти по узкой тропинке вдвоём, да ещё и с увесистым грузом, было дьявольски неудобно."
    "Прохлады в лесу ничуть не прибавилось, так что очень скоро мою одежду можно было выжимать."
    window hide
    scene bg ext_path_day with dissolve
    window show
    "Постепенно тропинка расширилась и идти стало немного легче, но к этому времени мы с Электроником успели изрядно вымотаться."
    play sound_loop breath fadein 5
    "Потные ладони упорно пытались соскользнуть с запястий, уставшие пальцы норовили разжаться, спину ломило."
    "Рука Шурика давила мне на шею. Оттягивающее наши руки седалище Шурика тоже не пробуждало бурной радости."
    dreamgirl "Лучше бы вы девочку какую несли! Славю, скажем. Или ту же Лену - её, кстати, есть за что - она вам, балбесам, жизнь спасла…{w} Да хоть вожатую - всё приятнее было бы!"
    th "Вожатую мы бы далеко не унесли…{w} Хотя и Шурик мог бы быть немного полегче. Раскормили, блин! Все руки мне оттянул!"
    "Впереди уже показалась ограда лагеря, когда Электроник пропыхтел:"
    show el sad pioneer close at right
    show sh upset pioneer close at center
    with dissolve2
    el "Может…{w=0.8} Устроим…{w=0.8} Привал?"
    me "Если мы сейчас остановимся{w=0.8}, то ещё раз его уже не поднимем.{w} Давай уже просто донесём поскорее{w=0.8}, немного осталось!"
    sh "Ребята, мне так неловко…"
    "Слабым голосом пробормотал Шурик."
    me "А ты лучше молчи.{w} Лично я предпочёл бы тебя не нести{w=0.8}, а по земле перекатывать{w=0.8} всю дорогу. Так что{w=0.8} просто{w=0.8} молчи!"
# дорожка
    window hide
    scene bg ext_houses_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    window show
    "Вскоре мы протиснулись в калитку и затопали по мощёной плитами дорожке лагеря."
    "Встречные пионеры смотрели на нас, разинув рот, но помогать никто не рвался."
# площадь
    window hide
    scene bg ext_square_day with fade
    window show
    "Всё ускоряясь, мы миновали площадь…"
# перед медпунктом (всё ещё день)
    window hide
    scene bg ext_aidpost_day with fade
    window show
    "По дорожке к медпункту мы с Элом уже практически бежали.{w} Бросившаяся вперёд Лена распахнула перед нами дверь…"
# скрип двери
    play sound sfx_open_door_clubs fadein 0
    "И мы ввалились внутрь."
    window hide
    stop music fadeout 5
    scene bg int_aidpost_day with fade
    play ambience ambience_camp_center_day fadein 3
#
    show un sad pioneer far at fleft
    show mt sad panama pioneer far at left
    show el sad pioneer at fright
    show sh upset pioneer at cright
    show cs normal far at cleft
    with dissolve
    window show
    "Не обращая внимания на изумлённую Виолетту, я скомандовал:"
    me "На кушетку!"
    "Последние несколько шагов, и мы с Электроником свалили свою ношу на кровать и без сил опустились на пол рядом."
    hide sh with dissolve
    "Кажется, Ольга Дмитриевна что-то объясняла медсестре, та тоже что-то говорила, но мне было всё равно."
# все спрайты исчезают
    stop sound_loop fadeout 5
    hide un
    hide mt
    hide el
    hide sh
    hide cs
    scene bg black
    with dissolve2
    "Весь мир сейчас для меня сжался до надёжного прочного пола, на котором можно было сидеть, и края кушетки, на которую можно было опереться спиной."
    "Единственное неудобство доставляли только руки, вытянувшиеся, судя по ощущениям, до пятиметровой длины как минимум."
    th "Странно, что они вообще помещаются в медпункте, а не высовываются на крыльцо."
    dreamgirl "А ты расскажи о своих ощущениях Виоле. Пусть сразу и тебе что-нибудь от галлюцинаций вколет заодно с Шуриком, зачем ей два раза возиться?"
    "Наконец, в голове перестали грохотать кузнечными молотами, а пальцы рук начали ощущаться как часть тела, а не как отдельно лежащая на полу субстанция."
# спрайты Виолы, Эла (normal) и ОД (far)
    window hide
    scene bg int_aidpost_day
    show mt normal panama pioneer far at left
    show el sad pioneer at right
    show cs normal glasses at center
    with dissolve2
    window show
    "Сидевший рядом Эл тоже завозился, пытаясь подняться."
    cs "Я смотрю, пионеры, вы уже пришли в себя."
    "Покопавшись в холодильнике, Виолетта извлекла оттуда бутылку «Боржоми».{w} Достав из шкафа пару стаканов, она нацедила в них минералки и всучила один Электронику, а другой мне:"
    cs "Пейте маленькими глотками."
    "Я честно старался делать, как велено, но весь стакан почему-то уместился в три глотка."
    cs "Всё с вами ясно."
    "Вздохнула Виола, отбирая стакан."
    cs "А теперь поднимайтесь и оба марш отсюда.{w} Мне ещё этому пионеру ссадины обработать надо и ввести противостолбнячную сыворотку."
    "Она кивнула на Шурика который уже вовсю спал, вытянувшись на кушетке.{w} Похоже, что-то она ему уже успела вколоть для расслабления духа."
    show cs smile glasses with dspr
    cs "Конечно, если вы тоже хотите стать моими {i}пациентами{/i}, то можете задержаться."
    cs "В конце концов, надо бы провести тщательный {i}осмотр{/i}, мало ли какие травмы вы могли получить…"
    show el scared pioneer with dspr
    "Голос медсестры, ставший медовым, произвёл на Электроника прямо-таки волшебное действие - вскочив, словно и не сидел только что на полу без сил, он залепетал что-то и устремился к двери."
    hide el with easeoutright
    show mt laugh panama pioneer far with dspr
    "Ольга Дмитриевна тихонько хихикнула по-девчоночьи, но ничего не сказала."
    "Кое-как подобрав свои руки-ноги, я поднялся и тоже направился на выход."
    if alt_uvao_true:
        show cs normal glasses
        show mt normal panama pioneer far
        with dspr
        cs "Семён, на ужине мне не забудь рассказать, как твоя неврастения себя ведёт."
        "Кивнув Виолетте, я вышел на крыльцо вслед за Сыроежкиным."
    window hide
    play ambience ambience_camp_center_evening fadein 3
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    scene bg ext_aidpost_sunset with dissolve
    play sound sfx_close_door_1
    show un normal pioneer at left
    show el sad pioneer at right
    with dissolve
    window show
    "Лена ждала нас снаружи. Похоже, её успели вытурить раньше, пока мы с Элом расслаблялись."
    "Судя по её усталому лицу, сегодняшняя прогулка тоже далась ей не просто так, хотя она и не участвовала в переноске тяжелораненных с поля боя."
    play sound sfx_close_door_1
    show mt smile panama pioneer at center with dissolve
    "Вышедшая через минуту Ольга Дмитриевна, напротив, была до неприличия бодра."
    dreamgirl "После сегодняшнего рассказа Юли сдаётся мне, что неприличная бодрость нашей вожатой имеет вполне себе неприличные же причины!"
    dreamgirl "Зарядилась ночью от Саныча, вот и…"
    th "Да по мне - хоть от Шурика! Уймись!{w} Вон, кажется, она сказать что-то хочет."
    mt "Виолетта говорит, что Шурик отлежится немного и всё с ним будет нормально.{w} Наверняка будет ясно завтра, когда он проснётся - она ввела ему снотворное."
    "Тут Ольга приосанилась и произнесла торжественным тоном:"
    show mt normal panama pioneer with dspr
    mt "Я рада, что все вы показали себя сегодня надёжными товарищами и не посрамили высокое звание пионера!"
    mt "Вы, ребята, продемонстрировали настоящее мужество и достойную подражания выдержку, оказывая помощь пострадавшему."
    show el normal pioneer with dissolve
    "Она посмотрела на на нас с Электроником с гордостью, словно лично занималась нашим воспитанием на протяжении последних лет, и продолжила:"
    mt "Особенно я хочу отметить участие Лены."
    mt "Мало того, что она сегодня не растерялась в критической ситуации и э-э… пришла на помощь оказавшемуся в опасности Семёну."
    show un shy pioneer with dspr
    mt "Лена ещё и {i}добровольно{/i} приняла участие в поисках пропавшего товарища, по своей инициативе вызвавшись пойти с отрядом!{w} Вот пример, на который все должны равняться!"
    "Лицо Лены к этому моменту сделалось пунцовым. Кажется, она с трудом сдерживалась, чтобы не броситься бежать куда глаза глядят."
    "Ольга же, раздав всем сёстрам по серьге, продолжила уже вполне будничным тоном:"
    mt "Сейчас всем отдыхать, только далеко не разбредайтесь - ужин уже скоро."
    "Она критически оглядела нас с Элом."
    show mt angry panama pioneer with dspr
    mt "И приведите себя в порядок! Подвиги подвигами, но в таком виде в столовую я вас не пущу."
    dreamgirl "Полагаю, этого человека не спасти. Занудство уже поработило его мозг."
    "Ольга сошла с крыльца и неспешно направилась в сторону площади."
    hide mt with dissolve
    "Куда исчезла Лена я не мог с уверенностью сказать, но через секунду в пределах видимости её уже не было."
    hide un with easeoutleft
    "Мы с Электроником переглянулись и поплелись к умывальникам."
    hide el with dissolve
    play music music_list["my_daily_life"] fadein 5
    dreamgirl "А ведь ты, похоже, так ничего и не заметил?"
    th "А что именно я должен был заметить? Что Ольга умеет толкнуть речь к месту и не к месту?"
    dreamgirl "Что стесняша потащилась в эту вашу нелепую вылазку добровольно, идиот!"
    dreamgirl "Причём напомню на случай, если ты ещё и склерозом страдаешь - пару часов назад она тебе сказала, что её Ольга припахала."
    dreamgirl "А теперь внимание, правильный вопрос!{w} То, что она пошла добровольно, это ещё полбеды, но зачем она тебе соврала?"
    th "Слушай, кто из нас интуицией заведует? Ты! Вот и подскажи мне."
    dreamgirl "Интуиция здесь не при чём, здесь аналитику надо задействовать. Так что постарайся сам подумать."
    "Ни стараться, ни думать мне сейчас отчаянно не хотелось."
    window hide
    scene bg ext_washstand2_day
    with dissolve
    window show
    play sound sfx_open_water_sink
    $ renpy.pause(1)
    play sound_loop sfx_water_sink_stream
    "Поэтому я ограничился тем, что дойдя до умывальников, кое-как умылся привычно уже ледяной водой и почистил вымазанную землёй и травой одежду, как смог."
    "Закончив прихорашиваться, я прикинул, что ходить туда-сюда по лагерю мне не с руки и побрёл сразу в сторону столовой."
    window hide
    stop sound_loop
    play sound sfx_close_water_sink
    pause(1)
    stop music fadeout 5
    play sound_loop ambience_medium_crowd_outdoors fadein 2
    scene bg ext_dining_hall_away_sunset with dissolve2
    window show
    "Плюхнувшись на скамейку недалеко от входа, я откинулся на спинку и наконец-то расслабился."
    play sound eat_horn fadein 2
    "Впрочем, долго отдыхать мне было не суждено - через несколько минут с небес прогремели трубы, зовущие пионеров вкусить вечернюю трапезу."
    stop sound fadeout 2
    "Вздохнув, я поднялся и повёл свой организм питаться."
    stop ambience fadeout 3
    stop sound_loop fadeout 3
    window hide
