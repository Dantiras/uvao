label alt_day6_lunch_dv_sl_1:
    #Поставил label для теста. Потом интегрировать нужно будет в alt_day6_lunch_dv_sl.
       "Постаравшись сделать вид, что не заметил Алису, я подрулил со своим подносом к столику, за которым устроилась Славя."
       "Пусть Славя и ведёт себя как-то странно, но садиться с рыжей - верное самоубийство."
       if alt_day2_sl_bf:
           th "В конце концов, ничем плохим обед с нашей активисточкой пока не заканчивался."
       me "Можно к тебе?"
       #if not alt_uvao_D5_evening_sl and alt_uvao_D4_lunch_sl: #Ничего кошерного с музыкой не придумалось. Хотя была задумка сначала: дать более эротичную мелодию под тру-ветку и более романтичную - под амурный выход. - ED
           #play music music_list["two_glasses_of_melancholy"] fadein 1
       show sl shy pioneer at center with dissolve
       "Славя расплылась в улыбке и, лукаво потупив взгляд, ответила:"
       sl "Садись конечно же{w=.4}, {i}Сёмушка{/i}!"
       "Я невольно проглотил слюну и, внимательно посмотрев на неё, медленно уселся за стол. "
       show sl smile2 pioneer at center with dissolve
       th "Не помню, чтобы она раньше меня так называла…"
       th "И что с ней вообще такое?"
       "Чувствуя, что лучше не задавать глупых вопросов, я уткнулся в тарелку."
       window hide
       scene cg d1_food_normal with dissolve #Может, всё-таки нарисует кто солянку? - ED
       "Всё-таки обед сегодня был необычным. И не только из-за продолжения любезностей от Слави. "
       "На первое сегодня повара приготовили солянку{w=.3} - {i}настоящую{/i} ароматную солянку, огненно-красную, с янтарными блёстками жира на поверхности, сквозь которые просвечивали уварившиеся кусочки копчёного мяса. "
       if alt_uvao_D5_hentai or alt_uvao_D5_sh_mines:
           "Чувство голода преследовало ещё со вчерашнего дня, и я решил не отказывать себе в резонном желании наконец наесться."
       else:
           "От такого аппетитного блюда грех было отказываться, и, выбросив из головы Славю, я поспешил приступить к обеду."
       "Бережно размешав сметану и отогнав в сторону подвернувшуюся некстати дольку лимона, я с вожделением зачерпнул первую, самую вкусную ложку..."
       "Славя, за всё это время даже не притронувшаяся к еде, негромко сказала:"
       #show sl smile pioneer at center with dspr
       sl "Приятного аппетита."
       "Не отрываясь от супа, я промычал невнятно:"
       me "Спасибо. И тебе."
       "Аппетита у меня и правда было вдоволь. Так что уже через какие-то три минуты с супом было покончено."
       "Я почувствовал, как желудок приятно тяжелеет. Такой вкусной солянки мне не доводилось пробовать, наверное, уже лет восемь."
       th "Ведь могут же когда хотят."
       "А ведь на второе ещё была целая тарелка золотистого плова."
       show blink
       "Я откинулся на спинку стула и закрыл глаза. Всё-таки стоило немного перевести дух."
       "Вдруг я почувствовал, что мою ладонь накрыли нежные пальчики."
       sl "{i}Сёмушка{/i}..." with vpunch
       $ renpy.pause(.6)
       hide blink
       show unblink
       scene bg int_dining_hall_people_day  
       show sl shy pioneer 
       "Суматошно открыв глаза, я уставился на Славю.{w} Она всё также сидела напротив меня, приветливо улыбаясь и неспешно теребя свою косу."
       sl "Какие у тебя планы на вечер?"
       "Голос её был таким бархатистым, а взгляд таким игривым, что я с трудом нашёлся что ответить:"
       me "А какие у меня должны быть планы?"
       show sl smile pioneer with dissolve
       sl "Ну как же! Ведь сегодня прощальная дискотека."
       me "И… и что с того?"
       show sl shy pioneer at center with dissolve
       sl "Это ведь последний шанс потанцевать {i}вместе{/i}."
       if alt_uvao_D4_lunch_un or alt_uvao_D5_evening_dv_un:
           show un shy pioneer far at right with dspr
           $ renpy.pause(.4)
           show un scared pioneer far with dissolve
           "Сидевшая за соседним столом Лена, искоса наблюдавшая за нами, вдруг побледнела и неожиданно выбежала из столовой, так и не закончив обед."
           hide un with easeoutright
           th "Кругом что, все с ума посходили?"
       show sl smile2 pioneer with dspr
       if alt_day3_dancing == 2:
           me "Что? Прошлый танец понравился?"
           sl "Очень. А уж какие слова ты мне говорил…"
           show sl shy pioneer with dissolve
           "Славя в очередной раз окатила меня таким взглядом, что щёки предательски заалели от смущения."
           th "Да как она это делает! Ведьма натуральная!"
           if not alt_uvao_D5_evening_sl and alt_uvao_D4_lunch_sl:
               dreamgirl "Цыц. Не мешай девочке, раз уж сам такой тормоз."
           else:
               dreamgirl "Ведьма-неведьма, но что-то задумала. Будь осторожен."
           me "Может… обойдёмся без этого? Да мало ли парней вокруг – вон тот же Электроник!"
       else:
           me "Может… э… не стоит? Всё-таки танцор из меня не очень."
           me "Давай об этом потом поговорим? А то сытый голодного не разумеет. Ты чего не ешь, кстати?"
           show sl shy pioneer with dissolve
           "Славя посмотрела мне прямо в глаза и глубоко вздохнула."
           sl "Может, наглядеться на тебя не могу{w=.4}, {i}Сёмушка{/i}?"
           if not alt_uvao_D5_evening_sl and alt_uvao_D4_lunch_sl:
               dreamgirl "Ух! Какая настойчивая. Не профукай свой шанс, балбес!"
           else:
               dreamgirl "Что-то хитрит наша Валькирия. Будь осторожен."
           show sl smile2 pioneer with dissolve
           sl "Может, хватит уже уходить от темы?{w=.6} Я ведь не кусаюсь."
           show sl shy pioneer with dissolve
           sl "Разве только чуть-чуть..."
       show sl smile2 pioneer with dissolve
       sl "Я хочу танцевать только с тобой."
       "Она проговаривала каждое слово с лёгким придыханием и продолжала сверлить меня своими голубыми глазищами."
       dreamgirl "Хорошая у Виолетты ученица. А как с косами играет…"
       if not alt_uvao_D5_evening_sl and alt_uvao_D4_lunch_sl:
           dreamgirl "Не забыл про третью сигнальную систему? Женщины тянутся к волосам, мужики к воротникам, прихорашиваясь."
       else:
           dreamgirl "Вся извертелась аж - нервничает. Но ни слова правды пока не сказала."
       th "Ты хочешь сказать, что…"
       "И тут меня как молнией ударило."
       th "Да нет... Это же бред какой-то!"
       if alt_uvao_true:
           dreamgirl "Тебе пляжа мало было, чтобы её намёки понять?"
       dreamgirl "Ну что ты как маленький, Сём Сёмыч!"
       hide sl with dissolve
       stop music fadeout 3
       show mt normal pioneer at left with dissolve
       mt "Минуточку внимания, пожалуйста!"
       $ renpy.music.set_volume(0.3, delay=2, channel='ambience')
       "Сильный голос вожатой легко перекрыл обычный шум столовой, заставив Славю повернуться к ней."
       show mt smile pioneer at left with dspr
       mt "Ребята, напоминаю вам ещё раз, что полдник сегодня будет на сорок минут раньше, а сразу после него начнётся итоговый концерт! Обещаю, будет интересно, так что не опаздывайте!"
       $ renpy.music.set_volume(1.0, delay=3, channel='ambience')
       mt "Явка на концерт, кстати, обязательна для всех."
       hide mt with dissolve
       "Пользуясь минуткой я быстро доел остатки плова и быстро продумывал план побега, но…"
       show sl smile2 pioneer at center with dissolve
       #play music music_list["two_glasses_of_melancholy"] fadeout 5
       sl "Ты уже всё?{w} {i}Сёмушка{/i}?"
       th "Да блин! Не могла Олька подольше потрындеть, что ли?!"
       "Я нервно улыбнулся Славе."
       me "Ну… да."
       sl "Тогда пойдём."
       "Она поднялась и встала рядом со мной, всем своим видом давая понять, что разговор не закончен."
       "Проклиная всё на свете, я встал и отправился за ней."
       "Убедившись, что вожатая чем-то занята, Славя обхватила мою руку и прижалась ко мне всем телом." 
       me "Прекрати. Не сбегу я, не сбегу."
       show sl shy pioneer with dissolve
       sl "Глупенький. А, может, мне так нравится?" 
       "Щеки горели как раскалённая сталь, а рука млела от прикосновений её мягкой и упругой кожи."
       stop ambience
       scene bg ext_dining_hall_near_day with dissolve
       $ renpy.pause(1.1)
       scene bg ext_dining_hall_away_day with dissolve
       show sl smile pioneer at center with dissolve
       play ambience ambience_camp_center_day fadein 3
       "Наконец мы отошли от столовой и Славя решилась продолжить наш разговор."
       sl "Так что ты решил?"
       me "Может… Как-нибудь без этого, а?"
       show sl smile2 pioneer at center with dissolve
       sl "Приходи обязательно. А после дискотеки мы могли бы немного прогуляться."
       show sl shy pioneer with dissolve
       "Сказав это, Славя еле заметно покраснела."
       if not alt_uvao_D5_evening_sl and alt_uvao_D4_lunch_sl:
           dreamgirl "Это до ближайших кустов-то? Всегда пожалуйста!"
       else:
           dreamgirl "{i}Проглуляться{/i}? В ближайший лесок. А там она надругается над тобой и убьёт в порыве страсти."
       if alt_uvao_D5_hentai:
           dreamgirl "Чувааак. Да ты прям секс-бомба! Каждый день с новой!"
       else:
           dreamgirl "Хоть напоследок что-то интересное будет!"
       "Пока внутренний голос выл от радости, я быстро терял последние остатки самообладания."
       me "А… а… о чём ты?"
       th "Выдохнуть. Всё в порядке. Этот маньяк в моей голове просто шутит. Просто шутит…"
       show sl smile2 pioneer at center with dissolve
       sl "Ты же не откажешь девушке?"
       me "Э… Да… То есть, н-нет… Я… я подумаю, ладно?"
       show sl smile2 pioneer close at center with dissolve
       "Славя подошла ближе и тихо шепнула на ухо:"
       sl "У нас есть {i}очень{/i} важное дело."
       show sl shy pioneer close at center with dissolve
       "Она была так близко и смотрела на меня нежно-нежно из-под своих пушистых ресниц."
       if not alt_uvao_D5_evening_sl and alt_uvao_D4_lunch_sl:
           th "Какая же она красивая…"
       else:
           th "Нужно хоть что-то сказать: иначе не отвяжется."
       "Я расплылся в глупой улыбке и тихо промямлил."
       me "Да… Конечно…"
       show sl happy pioneer close with dissolve
       $ renpy.pause(.6)
       show sl happy pioneer at center with dissolve
       sl "Вот и славно. Увидимся на концерте."
       show sl happy pioneer far with dspr
       $ renpy.pause(.6)
       show sl normal pioneer far at cright with dissolve
       "Славя аккуратно отпустила мою руку"
       show sl serious pioneer far at cright with dissolve
       extend " и, бросив на меня странный оценивающий взгляд, быстро отправилась в сторону эстрады."
       show sl normal pioneer far at cright with dissolve
       $ renpy.pause(.6)
       hide sl with dissolve
       stop music fadeout 6
       "А я…{w=.4} Я простоял столбняком ещё пару минут, а потом, взяв как-то себя в руки, поспешил к умывальникам."
       scene bg ext_washstand_day with dissolve
       play ambience ambience_forest_day fadein 3
       $ renpy.pause(1.6)
       play sound sfx_open_water_sink
       play sound_loop sfx_water_sink_stream fadein 1
       scene bg ext_washstand2_day with dissolve
       th "Раз. Два. Три.."
       show blink
       "Несколько горстей обжигающе ледяной воды одна за другой полетели мне в лицо."
       $ renpy.pause(.6)
       me "Фу-у-ух."
       play sound sfx_open_water_sink
       stop sound_loop
       hide blink
       show unblink
       scene bg ext_washstand_day with dissolve
       "Набрав больше воздуха в грудь, я от души рявкнул:"
       me "ДА ЧТО ЭТО БЫЛО ВООБЩЕ?!"
       dreamgirl "Не ори, придурок. Ну флиртовала с тобой девушка: что тут такого?"
       if alt_uvao_D5_hentai:
           dreamgirl "Вчера на хвостатую без раздумий согласился."
       dreamgirl "Сама паладинша до тебя снизошла, радуйся!"
       if alt_uvao_D5_evening_sl and alt_uvao_D4_lunch_sl:
           dreamgirl "Хотя после вчерашнего вечера стоило бы и усомниться в её дееспособности."
           th "А почему только её? Сначала Шурик с арматуриной, теперь эта то плачет на пляже, то на шею чуть не вешается. Влюбилась что ли?"
           dreamgirl "Не раскатывай губу: искренности в её поступках нет. От слова «совсем»."
           dreamgirl "Таким как она, Семён, ты и даром не нужен. А это значит…"
           th "Ты хочешь сказать…"
           dreamgirl "Бинго."
           th "Но зачем ей меня использовать? Я же здесь никто и звать меня никак. Разве что…"
           if not alt_uvao_D6_CS_vetrov:
                dreamgirl "Прознала, что ты засланец из далёкой галактики."
           else: 
                dreamgirl "Решила попрактиковать свои знания о попаданцах в обход всех Виол."####Чесс треба дописать в тру-толк подробности.
           "Уверенно констатировал голос в моей голове."
           if not alt_uvao_D6_CS_vetrov:
                th "Но как?"
           else:
                th "Но зачем?"
           dreamgirl "Да какая разница. Но совершенно неизвестно, что этой активистке взбредёт в голову: может, твой скальп снять собралась. Или сдать гэбистам на опыты."
           menu:
               "Поверить Шизе.":
                   th "Нужно как-то избегать её. Или сбежать?"
                   dreamgirl "Найдёт, не сомневайся. А далеко ты не сбежишь с подводной лодки."
                   th "Что же делать?.."
                   dreamgirl "Пока ты не ушёл в очередной мыслительный астрал, предлагаю сдать эту горе-куртизанку вожатке. За аморальное поведение."
                   dreamgirl "И чем скорее, тем лучше."
                   "Не став спорить с внутренним пошляком, я уверенно зашагал к своему домику."
                   scene bg black with fade
                   stop ambience
                   stop music
                   stop sound
                   stop sound_loop
                   jump scenario_uvao_debug
                   jump alt_day6_uvao_mt_day_talk
               "Поверить Славе.":
                   th "Бред какой-то. Ну не может Славя пойти на какой-то обман. Она на это просто не способна."
                   "Мне совершенно не хотелось очернять её образ бессмысленными подозрениями."
                   dreamgirl "Как знаешь. Моё мнение ты услышал. Что делать-то собрался?"
                   th "Есть в ней что-то манящее, загадочное… А вдруг она не шутила!"
                   dreamgirl "Лихо она тебя приворожила. Из штанов только от счастья не выпрыгни."
                   dreamgirl "Ну так чего стоишь? Приводи себя в порядок и дуй на концерт к своей пассии."
                   $ alt_uvao_D6_sl_pickup = True #Флаг амурного пути
                   "Не став спорить с внутренним пошляком, я уверенно зашагал к своему домику."
                   scene bg black with fade
                   stop ambience
                   stop music
                   stop sound
                   stop sound_loop
                   jump scenario_uvao_debug
                   jump alt_day6_uvao_mt_day_talk
       else:
           dreamgirl "Только она к тебе интерес и проявляла все эти дни."
           th "Думаешь, это что-то серьёзное?.."
           dreamgirl "А почему нет? Вилась вокруг тебя вьюном от самого автобуса, а потом ты опять ушёл в свой мир Вечного Одиночества."
           dreamgirl "Похоже, у неё одной хватило мозгов не спустить это всё на тормозах. Хотя…"
           th "Думаешь, это что-то серьёзное?.."
           dreamgirl "Сам вспоминай свои похождения, казанова пионерского масштаба."
           if alt_day2_sl_guilty == 2:
               th "Я ведь даже как смог прикрыл её тогда с ключами. Жаль, что потом игнорировал её…"
           elif alt_day3_dancing == 2:
               th "Странно я вёл себя на прошлых танцах: комплименты вдруг начал раздавать ни с того ни с сего. Может, решила, что небезразлична мне?"
           else:
               th "Она с первого дня не оттолкнула меня, накормила. Да и времени мы провели немало вместе. Может, это любовь с первого взгляда?"
           dreamgirl "Такие девочки на дороге не валяются, Сём Сёмыч. А ты её куда отдаёшь? Электроникам?"
           if alt_uvao_D5_evening_sl or alt_uvao_D4_lunch_sl:
               th "Вела она, конечно, себя странно в последние дни. Но какая разница?"
           th "Она ведь активистка… Откуда мне знать, как у них там всё происходит? Вечно бегает где-то, вечно занята."
           th "Может, только в предпоследний день поняла, что счастье её вот-вот уедет и быть может навсегда?"
           #play music music_list["two_glasses_of_melancholy"] fadein 1
           th "А ведь Славя мне и правда понравилась…"
           if alt_uvao_true:
              extend " А уж после зрелища на пляже…"
           dreamgirl "Ну так чего стоишь? Приводи себя в порядок и дуй на концерт к своей пассии."
           "Не став спорить с внутренним пошляком, я уверенно зашагал к своему домику."
           $ alt_uvao_D6_sl_pickup = True #Флаг амурного пути
           window hide
           scene bg black with fade
           stop ambience
           stop music
           stop sound
           stop sound_loop
           jump scenario_uvao_debug
           #Обрезать здесь
           jump alt_day6_uvao_mt_day_talk
        
       #Далее в амурной ветке Семён быстро наводит марафет, ничего не говорит ОД и направляется на эстраду (кстати, ещё вставлю разговор краткий с Алисой). На концерте будут небольшие правки поведения ГГ в сторону большей нерешительности Семёна и самонакручивания. Добавлю танец-обжиманец на вечер для пущего эффекта.
       #Во врезке ГГ сдаёт Славю, но ОД не воспринимает это всерьёз. Поэтому он начинает собственное расследование.
