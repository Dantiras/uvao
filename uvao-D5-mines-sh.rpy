label alt_day5_uvao_mines_sh:
# Д5 - Охота на Шурика в шахтах.
#
# <---строки ниже удалить при сборке!>
    $ night_time()
    $ persistent.sprite_time = "night"
    scene bg black with fade2    
# <---строки выше удалить при сборке!>
    #"Она шла быстрее, чем обычно, словно предчувствуя какую-то беду."
    play music music_list["doomed_to_be_defeated"] fadein 3
#    "Она ускорила шаг и сжала мою ладонь чуть сильнее, словно предчувствуя беду."
    "Она ускорила шаг, сжав мою ладонь чуть сильнее."
    "Вдруг Юля остановилась так резко, что я чуть не врезался в неё."
    uv "Стой. Не ходи дальше."
    me "Почему?"
    uv "Тихо."
    "Я не очень понял, что происходит, но решил подчиниться."
    "Юля некоторое время стояла, почти не шевелясь. Потом она прошептала:"
    uv "Он там, дальше."
    "Первым делом я решил осмотреться, куда же это Шурик нас притащил."
    window hide
    play sound match_lights
    scene bg int_mine_halt
    show match_lights   
    show uv dontlike at center
    with dissolve
    window show
    "Брошенные инструменты, какие-то разбитые ящики. Рельсы заворачивали вправо, и на повороте у стены лежала опрокинутая вагонетка."
    th "Наверно, слетела с рельсов на вираже. Катались они на ней, что ли?"
    "Я бросил спичку, чтобы не обжечь пальцы, и все погрузилось во тьму…"
    window hide
    scene int_mines_halt_spotlight with fade2 # тот же поворот, только темный и с подсвеченой стеной за углом
    show uv black silhouette at cleft
    with dissolve
    window show
    "…но не полностью! Я заметил какой-то тусклый свет из-за поворота."
    window hide
    hide uv
    scene int_mines_halt_spotlight:
        zoom 1.0 xalign 0.5 yalign 0.4
        linear 2.5 zoom 1.7 xalign 0.8 yalign 0.4
    #show uv normal at cleft # плохо смотрится зум фона и неподвижный спрайт Юли поверх
    with dissolve
    window show
    th "Это Шурик там? Больше некому, вроде. Но какого черта ему здесь надо?"
    dreamgirl "Может, плутоний добывает?"
    th "Ка…какой плутоний?"
    dreamgirl "Оружейный, балда! Кирку взял и копает! Подкрадись и посмотри, чем он там занят, вместо того, чтобы гадать!"
    "Я последовал совету и осторожно двинулся вперёд, изо всех сил стараясь не споткнуться и не налететь на что-нибудь в темноте. Судя по тихому, но азартному посапыванию где-то в районе моего плеча, Юля держалась рядом."
    "Вскоре мы подобрались достаточно близко, чтобы выглянуть из-за угла."
    window hide
    scene cg d4_sh_sit
    window show
    "Шурик действительно был там. С фонариком, с какой-то сумкой через плечо - он явно подготовился к походу в катакомбы."
    "Впрочем, выглядел он совершенно не как храбрый исследователь подземелий."
    "Скорчившись в какой-то нише в стене, он раскачивался и монотонно бормотал:"
    sh "…Пришёл… {w=1}А тут пусто… {w}Они говорили - налево… направо…{w=1} Куда вели?…{w=1} Я правильно шёл…{w=1} И никого…{w=1} Надо искать…{w=1} Она где-то здесь…{w=1} Тогда поверят…"
    "Его поведение меня довольно сильно испугало."
    th "Да у него совсем крыша съехала… Чёрт, и что с ним теперь делать? Нельзя же его тут оставить!"
    dreamgirl "А я думаю - можно. Лучше сначала самому выбраться, а за ним вернуться потом, с санитарами и успокоительным."
    th "Да хрен его потом тут найдёшь, в шахтах-то. Надо как-то увести его отсюда. Но как?"
    dreamgirl"Может, оглушить его? А потом как мешок картошки вынести."
    dreamgirl "Хлороформ бы для этого идеально подошёл. Подкрался бы сейчас к нему со спины, спросил бы, как пройти в библиотеку…"
    th "Ну ты-то хоть с ума не сходи.{w} Да и вообще, даже если удастся его оглушить, как я его понесу потом? Он же явно потяжелее мешка картошки будет."
    dreamgirl "Моё дело предложить. Попробую с ним поговорить тогда, вдруг он не совсем псих?"
    window hide
    scene bg int_mine_coalface
    with dissolve
    window show
    "Я выпрямился и, изобразив дружелюбную улыбку, медленно вступил в круг света."
    me "Шурик! Привет! А ты что здесь делаешь?"
    show sh scared pioneer far
    "Шурик вздрогнул и вскочил, вжимаясь в стену."
    sh "Семён?… Это ты?…"
    me "Я, я. Не видишь что ли?"
    sh "А где… она?"
    me "Она? Кто - она?{w} Шурик, ты себя нормально чувствуешь?"
    sh "Не притворяйся! Я всё про тебя знаю! Ты - ненастоящий!"
    me "Шурик, подожди… Давай успокоимся…"
    sh "Не подходи! Говори, где она?!"
    me "Да кто она-то?"
    th "Он что, Юлю сюда пришёл искать?!"
    sh "Ты знаешь!…{w} Ты должен мне сказать…{w} Говори, где она!"
    show sh angry bar3 with dspr #Палка опущена
    "Он угрожающе шагнул ко мне, сжимая в руках неведомо откуда взявшуюся железяку."
    me "Эй, эй! Ты что творишь, псих?! Это же я, Семён!"
    "Я попятился, а он продолжал приближаться, поднимая свое орудие."
    show sh angry bar with dspr #Палка посередине
    sh "Ты…{w} мне…" 
    show sh angry bar2 close with dspr #Палка в замахе
    extend " всё…{w} расскажешь…"
    dreamgirl "Берегись!"
    window hide
    show cg d4_sh_stay
    window show
    "Он ринулся вперёд, целя дубиной мне в голову."
    "Я рефлекторно отпрыгнул назад,{w} но оступился на камнях и рухнул на спину."
    with vpunch
    window hide
    scene bg int_mine_coalface
    show sh angry bar3 far at cright #Палка опущена
    show uv rage at cleft
    with dissolve
    window show
    "Внезапно с каким-то странным яростным мявом из-за камней выпрыгнула Юля и встала между нами, как бы защищая меня."
    show sh scared pioneer far at cright with dspr
    sh "А… а…{w=1.0} Она здесь?…{w=1.0} Я не…{w=1.0} нет…"
    "Он забормотал что-то неразборчивое, отступая в темноту."
    hide sh with easeoutright
    "Потом внезапно развернулся и со всех ног бросился прочь - туда, откуда мы пришли."
    show uv guilty close with dissolve
    "Юля наклонилась ко мне."
    uv "Вставай. Ты не ушибся?"
    me "Вроде бы нет."
    "Я поднялся и отряхнулся."
    show uv normal with dissolve
    th "И что теперь с этим полудурком очкастым делать? Искать его по всей шахте?"
    dreamgirl "Тебе железяки в голову показалось мало? Охота ещё лопатой по шее получить?"
    th "Ну блин, явно же не в себе человек! Если его бросить - навернётся, сломает себе что-нибудь, да так и сгинет.{w} А потом сюда пригонят спасателей, они тут все перероют… И Юлю уже точно найдут!"
    me "Юля, ты не знаешь, куда он побежал?"
    uv "Обратно. Туда, откуда мы пришли."
    me "Проведёшь? Надо его отсюда выгнать, вернуть заблудшую душу в коллектив, так сказать."
    show uv smile with dspr
    uv "Хорошо, пошли. Я его буду выгонять."
    th "Как это она его будет выгонять?"
    dreamgirl "А ты заметил, то как только она выпрыгнула - Шурик сразу весь боевой пыл растерял и драпанул? Не так уж она проста, наша кошечка…"
    "Я подобрал фонарик Шурика - трофей, взятый в бою! Теперь не придётся спотыкаться в темноте и жечь спички."
    th "Он, получается, без света убежал? Тогда мы его быстро нагоним."
    dreamgirl "У него в сумке мог быть запасной. Он, похоже, изначально собирался лезть в подземелья, вот и подготовился."
    me "Хорошо, тогда идём скорее!"
    "Не медля, Юля взяла меня за руку и решительно потянула за собой."
    window hide
    play sound_loop sfx_slavya_run fadein 2
    scene bg int_mine_crossroad with fade2:
        linear 0.1 pos (5,3)
        linear 0.1 pos (5,0)
        linear 0.1 pos (-5,5)
        linear 0.1 pos (-5,0)
        repeat
    window show
    "Идти с фонарём было гораздо быстрее, чем плестись в полной темноте, спотыкаясь на каждом шагу. Почти бегом мы пересекли несколько перекрёстков - каждый раз Юля без тени сомнения выбирала направление."
    window hide
    scene bg int_mine_crossroad with fade2:
        linear 0.1 pos (5,3)
        linear 0.1 pos (5,0)
        linear 0.1 pos (-5,5)
        linear 0.1 pos (-5,0)
        repeat
    window show
    th "Интересно, это она на слух определяет, куда идти, или следы замечает?"
    stop sound_loop fadeout 2
    window hide
    scene bg int_mine with fade2:
        linear 0.1 pos (5,3)
        linear 0.1 pos (5,0)
        linear 0.1 pos (-5,5)
        linear 0.1 pos (-5,0)
        repeat        
    show uv normal at cright
    with dissolve
    window show
    "Кажется, мы его нагоняли - мне иногда чудился какой-то свет впереди. Все-таки у него нашёлся запасной фонарь."
    "За очередным поворотом распахнулся длинный прямой штрек, в потолке которого зияла осыпавшаяся дыра."
    me "Это мы здесь спускались?"
    "Спросил я, пытаясь не сбиться с дыхания."
    uv "Нет, это другой вход. Тот там."
    "Она махнула рукой куда-то вправо. Там - значит там, сейчас это без разницы."
    uv "Он наверх вылез."
    me "Значит и мы за ним!"
    "Нас обоих разбирал азарт погони. Я с трудом представлял, что я буду делать, когда догоню его, но это все казалось неважным - впереди добыча! И она уходит!"
    window hide
    scene bg int_catacombs_entrance
    show uv upset close
    with dissolve
    window show
    "Юля с лёгкостью забралась наверх. Впрочем, тут же выяснилось, что самостоятельно последовать за ней я не могу, так что ей пришлось помогать мне забраться наверх. Не похоже, что её это очень уж обрарадовало, но деваться ей было некуда."
    "Наверху оказался тоннель - может быть, тот самый, который вёл из старого корпуса, а может и нет - мне они все казались слишком похожими."
    # show uv dontlike close at cright with dissolve
    me "Это тот, первый тоннель, в который мы через люк спустились?"
    uv "Да. Лестница там, а он побежал туда. Там тоже выход есть."
    "Она махнула вперёд, где брезжил какой-то свет."
    hide uv
    "Мы продолжили преследование, и через пару минут увидели тот самый выход - обвалившийся потолок тоннеля, выводящий на поверхность где-то в лесу, судя по виднеющимся наверху веткам деревьев. Я прикинул высоту - до поверхности где-то метра три."
    window hide
    scene int_catacombs_entrance_light
    show uv dontlike at cright
    with dissolve
    window show
    uv "Он наверх вылез."
    "Констатировала Юля и, похоже, приготовилась взбираться по торчащим из стены крюкам, по которым протягивались кабели."
    me "Эй, погоди! Я тут не влезу! Как тут Шурик вообще вскарабкался?"
    th "Вроде бы навыков ниндзя я за ним не замечал…"
    dreamgirl "Когда за тобой гонится крупный хищник из рода кошачьих, навыки ниндзя проявляются у всех."
    uv "Не знаю. Но он точно здесь вылез. И спускался тоже здесь."
    th "Может быть, он по верёвке спустился, а потом поднялся сам, и верёвку поднял?"
    me "Пошли по лесенке тогда поднимемся, как спускались."
    "Мы развернулись и побежали обратно."
    window hide
    scene bg int_catacombs_entrance
    show uv normal at cright
    with dissolve
    window show
    "Я первым заметил лестницу, вскарабкался по ней и откинул люк. Свет, бьющий через щели в забитом досками окне, ослепил меня и заставил зажмуриться."
    window hide
    stop ambience
    $ meet('mt', 'Голос')
    $ day_time()
    $ persistent.sprite_time = "day"
    scene int_old_building_day_uvao with flash
    window show
    show uv shocked with dissolve
    "Судя по всему, свет ослепил не меня одного. Хоть тут с ней никаких сюрпризов."
    "Мы понемногу привыкали к солнечному свету, как вдруг снаружи раздался чей-то крик."
    show uv surprise with dspr
    mt "ШУ-У-У-УРИ-И-И-ИК!"
    th "Голос знакомый. Ольга Дмитриевна?"
    dreamgirl "Не мы одни тут на психованных изобретателей охотимся."
    "Мы с Юлей подобрались к окну и одновременно выглянули в щель между досками."
    window hide
    $ meet('mt','Ольга Дмитриевна')
    scene bg ext_old_building_day
    show mt pioneer normal veryfar:
        xalign 0.001 yalign 0.9
    show sl pioneer serious veryfar:
        xalign 0.1 yalign 0.9
    show un pioneer serious veryfar:
        xalign 0.2 yalign 0.9
    show el pioneer normal veryfar:
        xalign 0.3 yalign 0.9
    with dissolve
    window show
    "Спасательная команда в составе Ольги Дмитриевны, Слави, Лены и Электроника стояла посреди заросшего бурьяном двора и озиралась." # Состав спасательной команды вроде бы такой?
    th "И как они теперь будут его искать? Ещё нас заметят, чего доброго. Наверное, придётся нам снова прятаться в тоннелях, или в убежище…"
    if alt_uvao_D5_hentai:
        dreamgirl "Ага-ага, спрятаться, и ещё разок объездить кошечку. Ну, чтоб время скоротать."
        "Я отмахнулся и от лезущей в голову похабщины, и от моего назойливого альтер эго."
    "Пионеры тем временем продолжали звать потерянного товарища на все лады."
    mt "Шу-у-у-у-ури-и-и-ик! Шу-у-у-ури-и-и-ик!"
    sl "Ау-у-у-у, Шу-у-ури-и-и-ик!"
    el "Эге-ге-е-ей, Шу-у-ури-и-ик!"
    th "Что-то я сомневаюсь, что он сам добровольно выйдет…"
    show sh angry bar3 veryfar behind mt with dissolve:
        xalign 0.9 yalign 0.85
    # TODO: Испуганных маленьких пионеров сюда.
    "И в этот момент из зарослей появился сам виновник торжества. Чумазый, ободранный, и все с той же приснопамятной железякой в руке."
    "Не тратя времени на разговоры, он размахнулся своим рубилом и бросился на замерших в испуге спасателей."
    th "Он сейчас точно кому-нибудь голову проломит!"
    "Я уже собрался было выскочить на подмогу, но… Непонятно как спасатели повалили нашего Рэмбо и старательно закрутили ему руки."
    show sh pioneer angry veryfar behind mt:
        xalign 0.9 yalign 0.85
    show un pioneer serious veryfar behind mt:
        xalign 0.8 yalign 0.85
    with dspr
    "Лена в это время вырвала арматурину из его рук и выкинула куда подальше."
    show mt pioneer angry veryfar:
        xalign 0.8 yalign 0.85
    show un pioneer serious veryfar:
        xalign 0.7 yalign 0.85
    with dspr
    mt "Ну-ка, переверните его!"
    show mt pioneer angry veryfar:
        xalign 0.5 yalign 0.85
    show un pioneer normal veryfar:
        xalign 0.65 yalign 0.85
    show sl pioneer normal veryfar behind sh:
        xalign 0.8 yalign 0.85
    show el pioneer normal veryfar behind sh:
        xalign 0.999 yalign 0.85
    with dspr
    "Вожатая наклонилась над ним{w} и отвесила несколько смачных оплеух!"
    play sound sfx_face_slap
    $ renpy.pause(0.8)
    play sound sfx_face_slap
    $ renpy.pause(0.8)
    play sound sfx_face_slap
    "Внезапно, это подействовало - Шурик перестал вырываться из рук Слави и Электроника, и в целом вроде как подуспокоился."
    dreamgirl "Вот что значит советская педагогика! А если б ногами - вообще был бы как шёлковый!"
    "Вожатая о чем-то спрашивала у Шурика, но тот явно не мог ничего объяснить, только растерянно озирался по сторонам."
    "Вскоре вся поисковая партия двинулась по направлению к лагерю. Шурика шатало туда-сюда, и шёл он только благодаря поддержке Эла и Слави."
    hide un
    hide sl
    hide sh
    hide el
    show mt pioneer normal veryfar:
        yalign 0.85
    with dspr
    "Ольга Дмитриевна зачем-то обернулась и озабоченно обвела взглядом поляну. По-видимому, не найдя ничего подозрительного, она повернулась и скрылась за деревьями вслед за остальными."
    hide mt with dspr
    jump alt_day5_parking_back
