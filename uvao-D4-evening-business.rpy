﻿#День4 Ходим по лагерю перед сном после второй встречи с Юлей
#
label uvao_D4_evening_business:
#День4 Ходим по лагерю перед сном после второй встречи с Юлей
#
    $ persistent.sprite_time = "sunset"
    scene bg ext_dining_hall_away_sunset with fade
    play ambience ambience_camp_center_evening fadein 1
    window show
    "Снова вечер, снова недовольный Генда."
    "Я сел на скамейку напротив памятника и откинулся назад."
    th "Так, по крайней мере вырисовывается план действий."
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
                th "Что это она так смотрит? Как на психа."
                dreamgirl "А ты и есть он. Добровольно идешь в логово сексуальной маньячки, затерроризировавшей все мужское население лагеря. Тебе только букета и бутылки вина не хватает для полной картины."
                th "Да ну тебя. Я же по делу."
                dreamgirl "Она-то этого не знает, что у тебя Дело. Жди, теперь слухи пойдут."
                "Переругиваясь сам с собой, я неторопливо добрел до медпункта и постучал."
                cs "Открыто!"
                me "Добрый вечер, Виола."
                "Она оторвалась от своего допотопного компьютера, в который вбивала какие-то записи с карточек."
                "Входи, входи, пионер. Ты с отчетом, или так, заскучал в одиночестве?"
                dreamgirl "Держи себя в руках, прекращай думать всякие пошлости! Думаешь, я не вижу? И взгляд выше."
                me "С отчетом."
                cs "Тогда присаживайся и выкладывай."
                me "Встретил снова Юлю, покормил булками, немного поболтали. Вы знаете, что она в старом корпусе живет?"
                cs "Не знала, но предполагала. Вполне подходящее место - людей нет, и от лагеря недалеко."
                me "Ну так вот. Она вроде бы не против, если я к ней заявлюсь в гости. С конфетами и булками, само собой - очень практичная девушка."
                cs "Практичная - вполне объяснимо… Но еще раз повторяю, она - не девушка! Не человек. Я даже не уверена, что она живая, а не какая-нибудь массовая галлюцинация."
                cs "Завтра, когда пойдешь в гости - веди себя прилично. Напоминаю, слишком близкие контакты закончатся очень печально. Для тебя."
                me "Эээ… А мне обязательно идти?"
                cs "Если не хочешь - я не заставляю. Но в твоем положении разбрасываться шансами глупо, где ты еще сможешь докопаться до самой истины?"
                me "Ясно…"
                cs "Так что, пойдешь? Я тогда с утра Ольге передам, что у меня для тебя важное поручение. Иди, пионер, отсыпайся, пока можешь."
                me "Виола… Вы еще обещали рассказать, куда это я попал."
                cs "Если вкратце - параллельный мир. Хотя ты это, наверное, уже понял. А подробный рассказ пока подождет. Ступай, уже поздно."
                "Она практически выставила меня за дверь."
                "До отбоя еще долго, и я пошел обратно на площадь…"
                "…Где немедленно наткнулся на Алису."
                dv "Что, Семен, в медпункт ходил? заболел?"
                me "Да нет. В гости заходил, поболтать."
                dv "Поболтать?"
                "Ехидно ухмыльнулась она."
                dv "Судя по тому, как тебя выпнули, поболтать ты ничем не успел."
                me "Успел, успел. Долго ли, умеючи-то…{w} А что, ты тоже собиралась… поболтать?"
                dreamgirl "Молодец. Виола бы тобой гордилась!"
                "Алиса все с тем же выражением смотрела на меня - что-то среднее между «Вот придурок!» и «Нифига себе дает чувак!»."
                "Я гордо расправил плечи и пошёл восвояси."
                jump uvao_D4_sleep_time
            "Не пойду я к ней!"
                th "…Но это не значит, что я собираюсь делать всё, что она мне скажет!"
                th "Раскомандовалась! Видали мы таких!"
                dreamgirl "Ну смотри, тебе решать."
    else:
        pass
    "Вечерняя площадь была безлюдной - видимо, после родительского дня большинство пионеров собиралось лечь спать пораньше."
    "Мне спать пока не хотелось, я сидел и наслаждался тихим вечером."
    "Незаметно стемнело."
    "Я решил пройтись туда-сюда перед сном, и в итоге вырулил к столовой."
    "На крыльце кто-то копошился. Опять Юля?"
    th "А, нет. На этот раз действительно Алиса. Снова пытается вскрыть замок, вполголоса ругаясь себе под нос."
    me "Опять замок ломаешь, Двачевская? Сейчас доломаешь, и завтра все без завтрака останемся."
    "Она аж подпрыгнула - кажется, я подкрался совсем тихо."
    dv "Заикой сделаешь, блин! Чего приперся?"
    me "Того же, чего и ты. А тебе что, из дому припасов не прислали?"
    "Кажется, я что-то не то сказал - Алиса набычилась."
    dv "Не хочешь помогать - так и скажи!"
    me "Да ладно, помогу, не кипятись."
    "Тем более что и мне для завтрашнего похода не помешает запастись."
# тырят плюшки
#(Столовая)
    if (keys_keep or keys_take == 1):
    #если есть ключи
        if dv_help:
        #если помогал Алисе в 1 день
            dv "Ты те ключи еще не потерял? Открывай давай."
        else:
            "Алиса уже собралась снова ковырять замок булавкой, но я вытащил из кармана ключи и демостративно позвенел ими."
            dv "Фига себе! Запасливый. Ну открывай тогда."
        th "С ключами любое дело становится намного проще."
        "Я открыл двери и мы проникли в пустую столовую."
    else:
        "Алиса принялась ковырять замок булавкой, как и в тот раз, я же вспомнил, в какое окно залезала Юля, и подошел проверить." "Оказалось, если немного подергать створку, шпингалет сам выходит из гнезда."
        me "Эй, Алиса, хватит замок ломать! Иди сюда!"
        "Стараясь не натоптать следов на подоконнике, мы влезли в пустую столовую."
        "Пяток булочек на брата - неплохой результат набега на столовую."
        "Алиса еще прихватила пару пирамидок с кефиром, а я решил обойтись сухпайком."
        "Поделив добычу, мы замели все следы и разошлись в разные стороны, по направлению к домикам."

# приходит в домик
label uvao_D4_sleep_time
    "Ольги Дмитриевны в домике не было.{w} И хорошо."
    "Сгрузив припасы в рюкзак, я разделся и занырнул под одеяло."
    th "Завтра рано вставать. Лучше даже до завтрака."
    if not uvao_D4_supper_cs:
    # *** если ужинал в одиночестве ***
        "Я выставил будильник на телефоне на пораньше и закрыл глаза."
    else:
        pass
    stop ambience fadeout 5
    window hide

#    return
