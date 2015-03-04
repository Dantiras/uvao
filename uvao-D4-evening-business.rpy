﻿#День4 Ходим по лагерю перед сном после второй встречи с Юлей
#
label uvao_D4_evening_business:
#День4 Ходим по лагерю перед сном после второй встречи с Юлей
#
# устанавливает флаг вечернего визита к Виоле в медпункт alt_day4_uv_viola_evening
#
    $ alt_day4_uv_viola_evening = False
    $ persistent.sprite_time = "sunset"
    scene bg ext_square_sunset with fade
    play ambience ambience_camp_center_evening fadein 1
    window show
    "Снова вечер, снова недовольный Генда."
    "Я сел на скамейку напротив памятника и откинулся назад."
    th "Так. По крайней мере вырисовывается план действий."
    th "Завтра с самого утра отправляюсь в старый лагерь, к Юле в гости."
#    th "Надеюсь, от нее я узнаю больше, чем из учебников."
# Про что он узнает? про Генду?
    th "Надеюсь, не зря придётся ходить."

    if (uvao_D4_supper_cs):
        dreamgirl "Вообще-то тебя просили доложить о результатах переговоров."
        th "И то верно."
        menu:
#            "Значит, пора навестить доктора Виолу."
            "Пора навестить доктора Виолу.":
                "Я поднялся, пересек площадь и свернул на дорожку к медпункту. Алиса, сидевшая с гитарой на отдаленной скамейке, проводила меня странным взглядом. "
                window hide
                scene bg ext_aidpost_sunset with fade
                window show
                th "Что это она так смотрит? Как на психа."
                dreamgirl "А ты и есть он. Добровольно идешь в логово сексуальной маньячки, затерроризировавшей все мужское население лагеря. Тебе только букета и бутылки вина не хватает для полной картины."
                th "Да ну тебя. Я же по делу."
                dreamgirl "Она-то этого не знает, что у тебя {i}дело{/i}. Жди, теперь слухи пойдут."
                "Переругиваясь сам с собой, я неторопливо добрел до медпункта и постучал."
                play sound sfx_knock_door7_polite
                $ renpy.pause(2)
                cs "Открыто!"
                window hide
                stop ambience fadeout 2
                play sound sfx_open_door_1
                $ renpy.pause(1)
                $ persistent.sprite_time = "day"
                scene bg int_aidpost_day
                with dissolve
                play ambience ambience_medstation_inside_day fadein 3
                play music music_list["eternal_longing"] fadein 3
                show cs normal with dissolve
                me "Добрый вечер, Виола."
                "Она оторвалась от своего допотопного компьютера, в который вбивала какие-то записи с карточек."
                show cs grin with dspr
                "Входи, входи, пионер. Ты с отчетом, или так, заскучал в одиночестве?"
                dreamgirl "Держи себя в руках, прекращай думать всякие пошлости! Думаешь, я не вижу? И взгляд выше."
                me "С отчетом."
                $ renpy.music.set_volume(0.3, delay=3, channel='music')
                show cs normal with dspr
                cs "Тогда присаживайся и выкладывай."
                "Я послушно уселся на край кушетки и принялся докладывать:"
                me "Встретил снова Юлю, покормил булками, немного поболтали.{w} Я так понял, что она в каком-то старом корпусе живет."
                "Виола кивнула."
                cs "Да, есть здесь такой, за пределами территории.{w} Вобщем-то мы это предполагали. Вполне подходящее место - людей нет, и от лагеря недалеко.{w} К тому же… Впрочем неважно, продолжай."
                me "Ну так вот. Она вроде бы не против, если я к ней заявлюсь в гости. С конфетами и булками, само собой - очень практичная девушка."
                cs "Практичная - вполне объяснимо… Но еще раз повторяю, она - не девушка! Не человек. Я даже не уверена, что она живая, а не какая-нибудь массовая галлюцинация."
                cs "Завтра, когда пойдешь в гости - веди себя прилично. Напоминаю, слишком близкие контакты закончатся очень печально. Для тебя - как минимум."
                me "Эээ… А мне обязательно идти?"
                show cs smile with dspr
                "Виола снисходительно усмехнулась."
                cs "Если не хочешь - я не заставляю. Но в твоем положении разбрасываться шансами глупо, где ты еще сможешь докопаться до самой истины?{w} Во всяком случае, интересные впечатления я тебе гарантирую."
                me "Ясно…"
                dreamgirl "Эй! Она что, на слабо тебя пытается взять?"
                show cs normal with dspr
                cs "Так что, пойдешь? Я тогда с утра Ольге передам, что у меня для тебя важное поручение. Иди, пионер, отсыпайся, пока можешь."
                th "Однако, какой решительный подход! Похоже, она за меня уже всё решила."
                th "Хотя, с другой стороны - я ведь и сам не против пойти…"
                me "Виола… Вы еще обещали рассказать, куда это я попал."
                cs "Если вкратце - параллельный мир. Хотя ты это, наверное, уже понял. А подробный рассказ пока подождет."
                show cs grin with dspr
                cs "Ступай, уже поздно."
                stop music fadeout 3
                "Она практически выставила меня за дверь."
                hide cs with dissolve
                $ renpy.music.set_volume(1, delay=0, channel='music')
                $ alt_day4_uv_viola_evening = True
                window hide
                play sound sfx_close_door_1
                $ persistent.sprite_time = "night"
                scene bg ext_aidpost_night with fade
                play ambience ambience_camp_center_night fadein 2
                window show    
                "До отбоя было еще долго, и я пошел обратно на площадь…"
                scene bg ext_square_night with dissolve
                window show
                "…Где немедленно наткнулся на Алису."
                show dv normal pioneer at center   with dissolve
                dv "Что, Семен, в медпункт ходил? заболел?"
                me "Да нет. В гости заходил, поболтать."
                show dv grin pioneer at center   with dspr
                dv "Поболтать?"
                "Ехидно ухмыльнулась она."
                show dv laugh pioneer at center   with dspr
                dv "Судя по тому, как тебя выпнули, поболтать ты ничем не успел."
                me "Успел, успел. Долго ли, умеючи-то…{w} А что, ты тоже собиралась… поболтать?"
                show dv angry pioneer at center   with dspr
                dreamgirl "Молодец. Виола бы тобой гордилась!"
                "Алиса все с тем же выражением смотрела на меня - что-то среднее между «Вот придурок!» и «Нифига себе дает чувак!»."
                "Я гордо расправил плечи и пошёл восвояси."
                hide dv with dissolve
                #плюшки не тырим
                jump uvao_D4_sleep_time
            "Не пойду я к ней!":
                th "…Но это не значит, что я собираюсь делать всё, что она мне скажет!"
                th "Раскомандовалась! Видали мы таких!"
                dreamgirl "Ну смотри, тебе решать."
    else:
        pass
    "Вечерняя площадь была безлюдной - видимо, после родительского дня большинство пионеров собиралось лечь спать пораньше."
    "Мне спать пока не хотелось, я сидел и наслаждался тихим вечером."
    "Незаметно стемнело."
    window hide
    $ persistent.sprite_time = "night"
    scene bg ext_square_night with dissolve
    play ambience ambience_camp_center_night fadein 2
    window show
    "Я решил пройтись туда-сюда перед сном, и в итоге вырулил к столовой."
    window hide
    scene bg ext_dining_hall_away_night with dissolve
    window show
    "На крыльце кто-то копошился. Опять Юля?"
    play sound sfx_alisa_picklock
    th "А, нет. На этот раз действительно Алиса. Снова пытается вскрыть замок, вполголоса ругаясь себе под нос."
    scene bg ext_dining_hall_near_night with dissolve 
    me "Опять замок ломаешь, Двачевская? Сейчас доломаешь, и завтра все без завтрака останемся."
    show dv scared pioneer at center   with dissolve
    "Она аж подпрыгнула - кажется, я подкрался совсем тихо."
    show dv rage pioneer at center   with dspr
    dv "Заикой сделаешь, блин! Чего приперся?"
    me "Того же, чего и ты. А тебе что, из дому припасов не прислали?"
    show dv angry pioneer at center   with dspr
    "Кажется, я что-то не то сказал - Алиса набычилась."
    dv "Не хочешь помогать - так и скажи!"
    me "Да ладно, помогу, не кипятись."
    show dv normal pioneer at center   with dspr
    "Тем более что и мне для завтрашнего похода не помешает запастись."
# тырят плюшки
#(Столовая)
    if (keys_keep or keys_take == 1):
    #если есть ключи
        if dv_help == 1:
        #если помогал Алисе в 1 день
            dv "Ты те ключи еще не потерял? Открывай давай."
        else:
            "Алиса уже собралась снова ковырять замок булавкой, но я вытащил из кармана ключи и демостративно позвенел ими."
            show dv grin pioneer at center   with dspr
            dv "Фига себе! Запасливый. Ну открывай тогда."
        th "С ключами любое дело становится намного проще."
        "Я открыл двери и мы проникли в пустую столовую."
    else:
        "Алиса принялась ковырять замок булавкой, как и в тот раз, я же вспомнил, в какое окно залезала Юля, и подошел проверить."
        "Оказалось, если немного подергать створку, шпингалет сам выходит из гнезда."
        show dv surprise pioneer at center   with dspr
        me "Эй, Алиса, хватит замок ломать! Иди сюда!"
        show dv normal pioneer at center   with dspr
        "Стараясь не натоптать следов на подоконнике, мы влезли в пустую столовую."
    hide dv with dissolve
    "Пяток булочек на брата - неплохой результат набега на столовую."
    "Алиса еще прихватила пару пирамидок с кефиром, а я решил обойтись сухпайком."
    "Поделив добычу, мы замели все следы и разошлись в разные стороны, по направлению к домикам."

# приходит в домик
label uvao_D4_sleep_time:
    window hide
    play sound sfx_open_dooor_campus_1
    stop ambience fadeout 1
    scene bg int_house_of_mt_noitem_night with dissolve
    play ambience ambience_int_cabin_night fadein 1
    window show
    "Ольги Дмитриевны в домике не было.{w} И хорошо."
    if not uvao_D4_supper_cs:
        "Сгрузив припасы в рюкзак, я разделся и занырнул под одеяло."
    else:
        pass
    th "Завтра рано вставать. Лучше даже до завтрака."
#    if not uvao_D4_supper_cs:
    if not alt_day4_uv_viola_evening:
        "Я выставил будильник на телефоне на пораньше и закрыл глаза."
    else:
        pass
    stop ambience fadeout 5
    window hide

#    return
