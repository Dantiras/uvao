# Д5-Дорога в старый лагерь
#
# используется флаг выхода на тру-энд alt_uvao_true
#
#    $ routetag = "uv"
#    $ alt_chapter(5, u"Юля. Дорога в старый лагерь")
label alt_day5_uvao_road_to_old_camp:
    window hide
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    scene bg ext_path_sunset with fade
    play ambience ambience_forest_day fadein 3
    window show
    "Выйдя наружу и хозяйственно прикрыв за собой калитку, я решительно двинулся в сторону деревьев, подступавших здесь к самому забору."
    "Лес становился все гуще. Торчащие из земли корни норовили попасть прямо под ноги - несколько раз я чудом избегал падения."
    "Несмотря на то, что с каждым шагом я отходил от лагеря, тропинка все не кончалась."
    th "Кстати, о тропинке. К ней что, весь лагерь ходит? Понапротаптывали…"
    dreamgirl "Не ты первый, не ты последний, мой дружок."
    th "Не думаю, что все так прозаично, иначе зачем она меня позвала?"
    dreamgirl "Ну как ты думаешь, зачем девушка может позвать юношу в уединенное место?"
    th "Да ну тебя!"
    if alt_uvao_true:
        th "Ещё и Виола эта со своими страшилками. Сама же говорит, что Юля для меня безопасна, а потом - что 'близкие контакты закончатся печально'."
        th "И вот как это понимать? Что, съест она меня?"
        "Я вспомнил остренькие зубки… Всё-таки до волка или даже до собаки ей далеко, да и я не мышь какая-нибудь.{w} Не съест."
        dreamgirl "Разве что понадкусывает немного!"
    "Очередной корешок подвернулся под ногу, но я устоял, практически сев на шпагат."
    th "Главное рюкзак донести. А то буду ползать по лесу и собирать просыпанные конфеты."
    if alt_uvao_true:
        dreamgirl "А ещё при {i}слишком близких{/i} контактах ты можешь заразиться, и у тебя тоже вырастут уши и хвост. А ещё…"
    "Я вздохнул.{w} Тропинка и не думала заканчиваться. Мне даже казалось, что я иду по кругу."
    window hide
    scene bg ext_path2_day with dissolve2
    window show
    "Немного подумав, я решил оставить зарубку на дереве."
    th "Если хожу кругами, то хотя бы пойму это."
    # согласно Автору там всего-то 600 метров, так что продолжительность путешествия сокращаем
    "Однако отметину в следующие несколько минут пути я больше не увидел, а там и лес начал редеть."
    "Вскоре показалась небольшая опушка, на которой стояло…"
    window hide
    scene bg ext_old_building_day with dissolve
    window show
    dreamgirl "Избушка, избушка, повернись к лесу передом, а к Ивану задом!"
    "«Избушкой» оказалось здание, судя по всему, когда-то бывшее собственностью либо пионерского лагеря, либо какого-то детсада."
    "Ржавая ограда, скрипящая детская площадка, прохудившаяся местами крыша. Ночью здесь наверняка страшно."
    th "И она здесь живет?"
    dreamgirl "Хочешь проверить?"
    "Была  - не была."
    "Я открыл скрипящую калитку и вступил на вымощенную плиткой тропинку к входу."
    "Зияющая чернота входа, с валявшейся рядом дверью, словно приглашали меня прогуляться по внутренностям ужасного чудовища."
    dreamgirl "Штанишки не намочил?"
    th "Что, я трус какой? Нас такой ерундой не запугаешь!"
    window hide
    scene int_old_building_day_uvao with fade
    window show
    "Внутри оказалось не так темно, как я ожидал. Солнечные лучи нет-нет, да и пробирались через дыры в потолке и разбитые окна."
    "Здание выглядело необитаемым, но осмотреть его на предмет признаков жизни стоило."
    "Вокруг царило запустение."
    "Всюду валялся мусор. Толстый слой пыли покрывал старые деревянные столики, подоконники, гардеробные вешалки…"
    "Я задумался и не заметил, как под ногу подвернулось что-то мягкое. Я взглянул вниз."
    "Старый пыльный плюшевый медведь, без правой задней лапы, печально взирал на меня своим единственным глазом-пуговицей."
    "Возникало ощущение, будто я очутился то ли в каком-то городе-призраке, то ли в низкобюджетном фильме ужасов."
    dreamgirl "Ага. Теперь иди проверь вооон ту тёмную комнату. Главное, не забудь перед этим громко поинтересоваться, есть ли там кто-нибудь."
    th "Очень смешно."
    "Осмотр первого этажа результатов не дал, я лишь наглотался пыли и начихался вдоволь, поэтому решил подняться на второй."
    "На втором этаже было ничуть не лучше, чем внизу.{w} Те же разбросанные пыльные игрушки вперемешку с книгами, поваленные шкафы и тумбочки."
    "Пару раз под ноги попадались старые куклы, а один раз я чуть не упал, наступив на маленькую матрешку."
    "Создавалось впечатление, что это было излюбленное место для вандализма."
#СТРАШНЫЙ скрип
    play sound sfx_carousel_squeak
    "Внизу что-то громко и протяжно заскрипело. По моей спине прошел холодок."
    "Перочинный ножик моментально перекочевал из кармана в руку, однако двинуться с места я не решался."
    "Минуты медленно тянулись одна за другой, но ничто больше не нарушало вновь воцарившуюся тишину."
    "Наконец я набрался храбрости и решился спуститься вниз.{w} Аккуратно, шаг за шагом двинулся по лестнице…{w} Вот уже преодолел один лестничный поворот…"
    show uv normal far at left with dissolve
    "В дверях я заметил чей-то силуэт и облегченно выдохнул: на пороге, спиной ко мне, стояла Юля и смотрела куда-то вдаль."
    "Я, убрав нож от греха подальше, собрался было окликнуть ее…"
    "Внезапно ступени под моей ногой скрипнули."
    show uv rage far with dspr
    "Ушки Юли тут же дёрнулись в мою сторону, а хвост распушился и стал напоминать ершик для чистки бутылок. С кошачьей проворностью она развернулась и уже готова была атаковать…"
    me "Стой! Это я, Семён!"
    show uv shocked far with dspr
    uv "Семён? Ты меня напугал. Незаметно пришел."
    "Она заметно успокоилась, хотя её распушенный хвост все так же ходил из стороны в сторону."
    show uv normal at center with dissolve
    me "Ты тут живешь?"
    uv "Не тут, рядом. Тут часто бродят ваши… Я живу там."
    "Она махнула рукой куда-то вниз, как мне показалось, и снова развернулась к выходу."
    me "А что ты высматриваешь? Там кто-то есть?"
    uv "Показалось. Никого нету."
    "Она повернулась ко мне и потянула носом."
    show uv smile at center with dissolve
    uv "Булочки! Вкусно пахнут."
    me "А… да. Будешь?"
    show uv laugh with dspr
    uv "Конечно, буду! Давай скорее!"
    "Я выудил из рюкзака одну из плюшек и протянул Юле. Та принялась ее с аппетитом уплетать, а я решил завести светскую беседу."
    show uv smile with dissolve
    me "Так ты, значит, здесь и живешь?"
    show uv normal with dspr
    uv "Ну да. Удобно очень. Нор много. Есть, где запасы прятать. В лесу не спрячешь, белки и мыши найдут."
    me "Какие запасы?"
    uv "Всякие. Вкусную еду когда нахожу - прячу. Грибы еще прячу. Запасы нужны!"
    me "На зиму запасаешься, что ли?"
    show uv upset with dspr
    uv "Зимой? Это когда белое всё? Холодно. Хорошо, что недолго."
    me "Хм, недолго… Ну как скажешь. И как же ты зимой?"
    show uv smile with dissolve
    uv "Сплю. Только просыпаюсь, когда дерево блестяшками обвешивают. Интересно!{w} Я себе некоторые беру, играть.{w} Дай еще булку."
    "В светской беседе наступила небольшая пауза, пока я рылся в рюкзаке."
    me "Юля, а скажи… Откуда ты?"
    show uv normal with dspr
    uv "Я - отсюда."
    me "Нет, а откуда ты здесь появилась?"
    show uv surprise with dspr
    uv "Появилась? Я всегда тут была."
    "От удивления она даже есть перестала на пару секунд. Впрочем, я был удивлён не меньше."
    me "То есть как это - всегда?"
#    show uv normal with dissolve
    uv "Да, всегда. Тут интересно. Всегда есть, за кем посмотреть."
    me "А раньше ты с людьми не разговаривала?"
    show uv normal with dissolve
    uv "Разговаривала. Давно. Со мной вожатая говорила."
    me "И о чем разговаривали?"
    show uv upset with dspr
    uv "Тоже спрашивала, откуда я. Мы недолго разговаривали.{w} Она потом испугалась и убежала. Глупая."
    "Она обиженно прижала уши. Потом улыбнулась мне:"
    show uv smile with dissolve
    uv "Ты не пугайся, с тобой ничего не будет."
    th "Интересный поворот… Получается, что-то со мной {i}могло бы быть{/i}? Или с кем-то другим уже {i}было{/i}?"
    "Пытаясь скрыть свой беспокойство, я отвернулся и принялся сосредоточенно копаться в содержимом рюкзака, затягивая паузу."
    "Справившись наконец со своим лицом, я достал последнюю булку и отдал Юле, постаравшись улыбнуться ей в ответ:"
    me "Да я и не пугаюсь, в общем-то… А почему ты от меня не убежала?"
    uv "А я тебя знала. Во сне видела, долго."
    # me "Странные сны у тебя… И что же ты там видела?"
    # uv "Тебя видела. Ты никак идти не хотел, и не приходил.{w} Всё смотрел в какую-то светящуюся штуку."
    # uv "А потом согласился. Хорошо. Теперь спокойнее."
    dreamgirl "Чувак, а тебе это ничего не напоминает, часом?"
    th "Что ты имеешь в виду?"
    "Ответа я, к сожалению, получить не успел."
    show uv normal with dspr
    "Юля вдруг насторожилась, повела ухом в сторону выхода и вскочила."
    show uv dontlike with dspr
    uv "Там кто-то ходит. Ты кого-то привел."
    "В голосе показались нотки угрозы."
    me "Я?! Не, я никого не приводил. Я вообще один шел!"
    show uv upset with dspr
    uv "А кто это тогда?"
    "Она указала куда-то в сторону леса. Я подошел и, щурясь от яркого солнца, взглянул туда, куда указала Юля."
    "Из кустов показалась шатающаяся фигура, которая тут же принялась себя отряхивать от листьев и налипшего к пионерской форме репейника."
    "Короткие светлые волосы, бликующие на солнце очки…"
    me "Шурик?!"
    me "Он не должен нас видеть!"
    show uv surprise with dspr
    uv "Он не с тобой?"
    me "Нет, он, наверно, шпионил за мной. Тоже тебя ищет, что ли?{w} Наверно, нам лучше спрятаться."
    "Юля проворно скользнула мимо меня и направилась к лестнице."
    show uv smile far at fright with dissolve
    uv "Сюда."
# Люк не в холле под лестницей, а в кабинете начальника, как в Мику-руте (alt_mi_route.rpy)
    "Она поманила меня вглубь здания.{w} Пройдя по коридору, мы оказались в бывшем помещении администрации, судя по останкам массивного письменного стола и застеклённых когда-то шкафов."
    play sound sfx_carousel_squeak
    "Юля повозилась с чем-то у стены и с громким скрипом откинула железную крышку люка."
    hide uv with dissolve
    "Ловко прыгнув вниз, она оставила меня возле открытого люка. Выхода не было, я полез за ней."
    stop ambience fadeout 2
    play sound sfx_carousel_squeak
    "Осмотревшись напоследок, я закрыл за собой скрипучий люк и стал спускаться вниз."
#    window hide
    jump alt_day5_uvao_tunnel