﻿define background = Character(None, kind=nvl)
define UrikMali = Character('Урик Мали', color="#4ed200")
define Irina = Character('Ирина', color="#e500ff")
define Alexandr = Character('Александр', color="#d5ff00")
define Sergei = Character('Сергей', color="#f5a656")

transform pos:
    xalign 0.5
    yalign 1.0

define krits = 0
define perekyr_s_sergeem = False
define zabil = 0
define pomosh = False
define oshibka = 0
define oshibka_achivka = False
define perezagruzka = False
define perezagruzka2 = False
define audio.call = "sounds/call.ogg"

label splashscreen:
    scene black
    pause(0.5)

    scene ligo2 with fade
    pause (2)

    scene black with fade
    return


label start:
    $ renpy.movie_cutscene('video/zastavka.avi')
    play music "audio/fon.ogg"
    scene bg kabgg
    with fade
    window hide
    background '''АКТ 1 "ПОИСК РАБОТЫ"'''
    nvl hide
    nvl clear

    "Сидя за компьютером у себя дома, Александр решил найти своё место в мире компьютерных технологий."
    "Он просматривал множество вакансий в Интернете, надеясь найти работу, которая привнесет в его жизнь не только финансовую стабильность, но и смысл."
    "Именно в такой поисковый момент его взор привлекла необычная вакансия – стажер эникейщика в небольшом офисе. Увлекшись мыслью о возможности войти в мир IT."
    "Александр отправил свое резюме работодателю и спустя небольшое количество времени был приглашен на собеседование."

    scene bg malisroom
    with fade






    window hide
    background '''АКТ 2 “СОБЕСЕДОВАНИЕ”'''
    nvl hide
    nvl clear


    show irina2
    voice "Iri/Irina1.ogg"
    Irina "Здравствуйте, Александр. Рада Вас видеть. Меня зовут Ирина Константиновна, но можно просто Ирина. Добро пожаловать на собеседование."
    hide irina2
    show irina1
    Alexandr "Здравствуйте, Ирина. Спасибо за приглашение."
    hide irina1

    show irina2
    voice "Iri/Irina2.mp3"
    Irina "Подскажите, почему вы выбрали именно нашу компанию?"
    hide irina2

    menu:
        "Выберите вариант ответа"

        "Я думаю ваша компания без меня не справляется со своими задачами, и по этому решил откликнутся.":
            jump exit1

        "Я особо не вникал в объявления, так как мне нужны деньги.":
            jump exit1

        "Я вижу вашу амбициозную и развивающею компанию в будущем и настоящем времени. Судя по объявлению, я способен выполнять необходимые вам задачи.":
            jump ne_exit1


    return

label exit1:

    show irina4
    voice "Iri/Irina2.1_2.2.mp3"
    Irina "Мне нравится ваши амбиции, мы вам перезвоним."

    window hide
    scene plox_konc
    play music "audio/bad_kon.mp3"
    with fade
    $ renpy.notify("Вам не перезвонили...(Плохая концовка)")
    "Конец"
    nvl hide
    nvl clear

    return

label ne_exit1:

    show irina2
    voice "Iri/Irina2.3.mp3"
    Irina "Хорошо, давайте начнём с обсуждения условий работы у нас в компании."

    voice "Iri/Irina3.mp3"
    Irina "Прежде всего, основным условием устройства на работу является успешное прохождение 3-х дневной стажировки у нас в компании. По окончании стажировки вас ожидает анкетирование."

    voice "Iri/Irina4.mp3"
    Irina "Задачи у вас будут разнообразными. Во время прохождения стажировки, вам будет назначен наставник, который будет следить за вашими успехами и направлять вас во время работы. Ваш наставник - главный системный администратор Сергей."
    hide irina2

    menu:
        "Выберите вариант ответа"

        "Спасибо за информацию, Ирина. Я готов начать стажировку и сделать все возможное, чтобы присоединиться к вашей команде.":
            jump ne_exit2
        "Спасибо Ирина, на самом деле, я уже не очень заинтересован в трудоустройстве у вас в компании, но если что я вам позвоню.":
            jump exit2

    return

label exit2:

    show irina6
    voice "Iri/Irina4.2.mp3"
    Irina "Не будем перечить вашему желанию. Если вы передумаете, то обязательно позвоните."

    window hide
    scene plox_konc
    play music "audio/bad_kon.mp3"
    with fade
    $ renpy.notify("Вы отказались от стажировки...(Плохая концовка)")
    "Конец"
    nvl hide
    nvl clear

    return

label ne_exit2:

    show irina2
    voice "Iri/Irina4.1.mp3"
    Irina "Замечательно, Александр. Мы ждем вас завтра. Если у вас есть еще какие-либо вопросы касающиеся прохождения стажировки, не стесняйтесь задавать их Сергею, вашему наставнику."

    window hide
    scene black
    $ renpy.notify("Вы согласились на стажировку")
    background '''АКТ 3 СТАЖИРОВКА'''
    background ''' ДЕНЬ ПЕРВЫЙ'''
    nvl hide
    nvl clear

    scene bg ofice
    with fade

    "Александр входит в офис компании."

    show mali2
    voice "Uri/Urik1.mp3"
    UrikMali "Доброе утро, Александр. Рад видеть тебя на стажировке. Давай поговорим в моем кабинете перед началом рабочего дня."
    hide mali2
    show mali1
    Alexandr "Здравствуйте, мистер Мали."

    scene bg malisroom
    with fade

    "Александр вместе с Уриком Мали входит в кабинет мистера Мали."

    show mali2
    voice "Uri/Urik2.mp3"
    UrikMali "Прошу, садись. Готов к прохождению первого дня стажировки?"
    hide mali2

    show mali1
    Alexandr "Да, уже не терпится."
    hide mali1

    show mali2
    voice "Uri/Urik3.mp3"
    UrikMali "Отлично. На стажировке ты будешь изучать различные аспекты нашей работы."

    voice "Uri/Urik4.mp3"
    UrikMali "Сергей, наш главный системный администратор, не всегда справляется с большой работой. От тебя потребуется помогать Сергею и выполнять его задание которые он тебе будет давать во время работы."
    hide mali2

    show mali1
    Alexandr "Я вас понял, мистер Мали. Я готов помогать Сергею."
    hide mali1

    show mali2
    voice "Uri/Urik5.mp3"
    UrikMali "Теперь давай пойдем к Сергею. Он даст тебе первое поручение."
    hide mali2

    scene bg ofice
    with fade

    "Урик Мали проводит Александра к Сергею."

    show mali6
    voice "Uri/Urik6.mp3"
    UrikMali "Сергей, это Александр, наш новый стажер. Александр, это Сергей, твой наставник. Вы знакомьтесь а я пойду с вой кабинет."

    "Урик Мали уходит в свой кабинет."
    hide mali6
    with fade

    show sergey6
    voice "Ser/Serge1.mp3"
    Sergei "Здравствуй, Саня. Рад тебя видеть. Давай начнем с чего-то интересного. У меня есть для тебя задача, которую ты скорее всего сможешь решить."
    hide sergey6

    show sergey5
    Alexandr "Здравствуйте, Сергей."

    menu:
        "Выберите вариант ответа"

        "Сначала перекур перед рабочим днем, а после за работу.":
            $ krits = krits + 1
            $ renpy.notify("Он запомнит это")
            call krit1 from _call_krit1
            show sergey5
            Alexandr "Я готов к работе. Что нужно делать?"

        "Я готов к работе. Что нужно делать?":
            $ renpy.notify("Он запомнит это")
            Alexandr "Я готов к работе. Что нужно делать?"

    show sergey6
    voice "Ser/Serge3.mp3"
    Sergei "Хорошо, первое задание для тебя. У нас сегодня ожидается поставка комплектующих ПК и периферии для обустройства новых рабочих мест. Мы должны принять и отсортировать все компоненты."

    voice "Ser/Serge4.mp3"
    Sergei "Вот список компонентов, которые должны быть в поставке. Твоя задача - проверить, что все компоненты присутствуют и отсортировать каждый компонент в коробку."
    hide sergey6

    show sergey5
    "Сергей передает Александру список компонентов и документацию."

    Alexandr "Хорошо, поставка будет на складе?"
    hide sergey5

    show sergey6
    voice "Ser/Serge5.mp3"
    Sergei "Верно. Я тебя провожу."

    "Александр с Сергеем направляются на склад для приема поставки."

    scene bg sklad
    with fade

    show sergey6
    voice "Ser/Serge6.mp3"
    Sergei "Вот коробки, можешь начинать работать, а я приду сюда примерно через 10 минут, проведать тебя."
    hide sergey6

    show sergey5
    Alexandr "Хорошо."

    hide sergey5
    with fade

    "Александр начинает разгружать компоненты и также начинает их сортировку."

    "Во время разгрузки компонентов Александр случайно уронил коробку с мониторами."

    menu:
        "Открыть коробку и посмотреть что стало с монитором.":
            call posmotret_v_korobky from _call_posmotret_v_korobky
        "Убрать коробку с монитором в угол склада и сделать вид как будто ничего не было.":
            call ybrat_korobky from _call_ybrat_korobky
    "Александр продолжает работать в своем темпе."
    "Спустя 30 минут."
    "Александр заканчивает разгрузку и сортировку компонентов и в этот момент на склад заходит Сергей."
    show sergey6
    voice "Ser/Serge16.mp3"
    Sergei "Ну что, Саня. Закончил работу с компонентами?"
    hide sergey6

    show sergey5
    Alexandr "Да, Сергей. Как раз закончил."
    hide sergey5

    show sergey6
    voice "Ser/Serge17.mp3"
    Sergei "Тогда пойдем к нам в офис."
    hide sergey6
    "Александр с Сергеем направился обратно в офис компании Rinus Corp."


    scene bg ofice
    with fade

    show sergey6
    voice "Ser/Serge18.mp3"
    Sergei "Так держать. Я пойду покурить, а ты остаешься за старшего."
    hide sergey6

    show sergey5
    menu:
        "Выберите вариант ответа"

        "Хорошо, Сергей.":
            Alexandr "Хорошо, Сергей."

        "Может я с вами пойду?":
            call vishel_pokyrit from _call_vishel_pokyrit
    hide sergey5
    with fade
    "Сергей уходит из офиса компании в курилку."
    "2 минуты спустя."
    "Растерянная Ирина входит в офис компании Rinus Corp. и подходит к Александру."
    jump contin

    return

label vishel_pokyrit:
    hide sergey5
    show sergey6
    voice "Ser/Serge19.mp3"
    Sergei "Нам нужно чтобы, хотя бы 1 человек оставался за главного."
    hide sergey6

    show sergey5

    menu:
        "Выберите вариант ответа"

        "Давайте я тогда схожу первый, а после уже вы.":
            $ perekyr_s_sergeem = True
            $ krits = krits + 1
            $ renpy.notify("Он запомнит это")
            call vishel_pokyrit_krit from _call_vishel_pokyrit_krit
        "Хорошо, я тогда пойду после вас.":
            Alexandr "Хорошо, я тогда пойду после вас."


    return

label vishel_pokyrit_krit:

    Alexandr "Давайте я тогда схожу первый, а после уже вы."
    hide sergey5

    show sergey6
    voice "Ser/Serge20.mp3"
    Sergei "Хорошо, иди. Но не долго!"
    hide sergey6

    scene black
    with fade
    "Александр уходит из офиса компании в курилку."
    "Спустя 5 минут Александр вернулся"

    scene bg ofice
    with fade

    show sergey5

    return




label ybrat_korobky:

    "Александр убирает коробку с монитором в угол склада и идет дальше разгружать комплектующие."

    "В этот момент на склад входит Сергей."

    show sergey6
    voice "Ser/Serge11.mp3"
    Sergei "Ну как дела тут у тебя, Саня?"
    hide sergey6

    show sergey1
    menu:
        "Выберите вариант ответа"

        "Все хорошо, Сергей. Потихоньку выполняю поставленную задачу.":
            $ krits = krits + 1
            $ renpy.notify("Он запомнит это")
            call ne_pravda from _call_ne_pravda
        "Простите меня Сергей, пока я разгружал коробки с комплектующими, я случайно уронил коробку с монитором и разбил его. Из-за того что начал переживать я коробку убрал в угол склада вон там.":
            $ renpy.notify("Он запомнит это")
            call pravda_polomka2 from _call_pravda_polomka2

    return

label pravda_polomka2:
    Alexandr "Простите меня Сергей, пока я разгружал коробки с комплектующими, я случайно уронил коробку с монитором и разбил его. Из-за того что начал переживать я коробку убрал в угол склада вон там."
    hide sergey1

    show sergey6
    voice "Ser/Serge14.mp3"
    Sergei "Ничего страшно, Саня. И такое тоже бывает, оставь коробку там, коробку я с ней позже разберусь"
    voice "Ser/Serge15.mp3"
    Sergei "Продолжай работать, а я пойду дальше по своим делам. Скоро вернусь."
    hide sergey6
    with fade

    "Сергей уходит со склада."

    return

label ne_pravda:
    Alexandr "Все хорошо, Сергей. Потихоньку выполняю поставленную задачу."
    hide sergey1

    show sergey2
    voice "Ser/Serge12.mp3"
    Sergei "Хорошая работа, Саня. Если у тебя возникнут какие-либо вопросы, не стесняйся обращаться ко мне."
    hide sergey2

    show sergey1
    Alexandr "Обязательно. Спасибо, Сергей."
    hide sergey1

    show sergey6
    voice "Ser/Serge13.mp3"
    Sergei "Продолжай работать, а я пойду дальше по своим делам. Скоро вернусь."
    hide sergey6
    with fade

    "Сергей уходит со склада."

    return

label posmotret_v_korobky:
    "Александр открывает коробку с монитором и видит что он оказался разбитым."
    "В этот момент на склад входит Сергей."
    show sergey6
    voice "Ser/Serge7.mp3"
    Sergei "Ну как дела тут у тебя, Саня?"
    hide sergey6
    show sergey1
    menu:
       "Выберите вариант ответа"

       " Пока сортировал тут разгруженные коробки, я заметил что один из мониторов оказался разбитым.":
           $ krits = krits + 1
           $ renpy.notify("Он запомнит это")
           call brak from _call_brak
       "Простите меня Сергей, пока я разгружал коробки с комплектующими, я случайно уронил коробку с монитором и разбил его.":
           $ renpy.notify("Он запомнит это")
           call pravda_polomka1 from _call_pravda_polomka1
    return

label pravda_polomka1:
    Alexandr "Простите меня Сергей, пока я разгружал коробки с комплектующими, я случайно уронил коробку с монитором и разбил его."
    hide sergey1

    show sergey2
    voice "Ser/Serge9.mp3"
    Sergei "Ничего страшно, Саня. И такое тоже бывает, отложи коробку я с ней позже разберусь"
    voice "Ser/Serge10.mp3"
    Sergei "Продолжай работать, а я пойду дальше по своим делам. Скоро вернусь."
    hide sergey2
    with fade
    "Сергей уходит со склада."
    return

label brak:

    Alexandr "Пока сортировал тут разгруженные коробки, я заметил что один из мониторов оказался разбитым."
    hide sergey1

    show sergey2
    voice "Ser/Serge8.mp3"
    Sergei "Плохи дела. Но ты не переживай Саня, я обязательно разберусь с поставщиками за бракованный товар. А ты продолжай работать."
    hide sergey2
    with fade
    "Сергей уходит со склада."
    return

label krit1:

    hide sergey5
    show sergey4
    voice "Ser/Serge2.mp3"
    Sergei "Хорошо, но давай по быстрому."
    hide sergey4

    show sergey3
    Alexandr "Я мигом."
    hide sergey3

    scene black
    with fade
    "Александр выходит на улицу для перекура."
    "Спустя 6 минут, Александр зашел обратно в здание компании Rinus Corp. и подошел к Сергею"

    scene bg ofice
    with fade

    return

label contin:
    show irina_raz
    voice "Iri/Irina5.mp3"
    Irina "Александр, я не могу залогиниться в мой рабочий компьютер. Что-то не так с моей учетной записью. Я вводила пороль а мне высвечивается что он не правильный."
    $ renpy.notify("Важная деталь")
    voice "Iri/Irina6.mp3"
    Irina "Недавно мне переустановили операционную систему из-за вирусов ПРИМЕРНО ГОД НАЗАД. Сергей где-то оставил записку с паролем, но я ее потеряла."
    hide irina_raz

    show irina_mol
    menu:
        "Выберите вариант ответа"

        "Не волнуйтесь, Ирина. Я уверен, мы найдем решение. Где находится ваш рабочий компьютер?":
            $ pomosh = True
            call pomoch_srazy from _call_pomoch_srazy
        "Сейчас Сергей ушел на перекур, я ему передам вашу проблему как он вернется.":
            call pomoch_potom from _call_pomoch_potom

    "Александр начал осматривать рабочий стол Ирины на наличие записки с паролем."
    if (krits >= 3):
        jump ploxai_koncovka
    Alexandr "Да где же она может быть?"
    "Александр поднял папки которые лежали на столе."
    scene zap
    with fade
    "Изучите записки(чтобы скрыть/показать диалоговое окно нажмите H)"
    "Он увидел 4 клочка бумажки с паролями, где на каждом из них в углу написана дата."
    jump contin2
    return

label contin2:
    menu:
        "Выберете записку"

        "Выбрать записку с паролем 12.05.2023":
            call perebor_nevernogo_parola from _call_perebor_nevernogo_parola
            jump konec_pervogo_dna_na_ploho
        "Выбрать записку с паролем 27.09.2023":
            call perebor_nevernogo_parola from _call_perebor_nevernogo_parola_1
            jump konec_pervogo_dna_na_ploho
        "Выбрать записку с паролем 01.03.2019":
            call perebor_nevernogo_parola from _call_perebor_nevernogo_parola_2
            jump konec_pervogo_dna_na_ploho
        "Выбрать записку с паролем 20.11.2022":
            call perebor_vernogo_parola from _call_perebor_vernogo_parola
            jump konec_pervogo_dna_na_horosho
        "Спросить Ирину про дату":
            $ zabil = zabil + 1
            if (zabil <= 2):
                Alexandr "Ирина, не подскажите какая сегодня дата?"
                voice "Iri/Irina10.mp3"
                Irina "Сегодня 24 ноября 2023 года."
                Alexandr "Спасибо!"
                jump contin2
            else:
                Alexandr "Ирина, не подскажите какая сегодня дата?"
                voice "Iri/Irina_izdev.mp3"
                Irina "Вы издеваетесь ?"
                Alexandr "Извиняюсь."
                jump contin2

    return

label perebor_nevernogo_parola:
    Alexandr "Так, попробуем этот…"
    "Александр вводит паролем с записки в компьютер."
    "..."
    "Пароль оказался не верным."
    Alexandr "Черт!"

    return

label pomoch_srazy:
    Alexandr "Не волнуйтесь, Ирина. Я уверен, мы найдем решение. Где находится ваш рабочий компьютер?"
    hide irina_mol

    show irina2
    voice "Iri/Irina7.mp3"
    Irina "Пройдёмте за мной."

    scene bg sergey_room
    with fade

    "Александр и Ирина отправляются в кабинет, где она работала"
    return

label pomoch_potom:
    Alexandr "Сейчас Сергей ушел на перекур, я ему передам вашу проблему как он вернется."
    hide irina_mol

    show irina2
    voice "Iri/Irina8.mp3"
    Irina "Хорошо, спасибо Александр. Только не забудьте передать."
    hide irina2

    "Ирина выходит из офиса компании."
    "5 минут спустя."
    "Сергей возвращается в офис после перекура."

    show sergey6
    voice "Ser/Serge21.mp3"
    Sergei "Что происходило во время моего отсутствия?"
    hide sergey6

    show sergey5
    Alexandr "Ирина из отдела кадров потеряла вашу записку с паролем от операционной системы."
    hide sergey5

    show sergey6
    voice "Ser/Serge22.mp3"
    Sergei "Ты ей помог?"
    hide sergey6

    show sergey5
    Alexandr "Нет, я решил дождаться вас."
    hide sergey5

    show sergey2
    voice "Ser/Serge23.mp3"
    Sergei "Сможешь сходить посмотреть что у ней не так? А я пойду в кабинет к Урику Мали обсудить рабочие моменты. Если у тебя не получится справится с задачей, не стесняйся, обращайся ко мне. Я помогу."
    hide sergey2

    show sergey1
    if (perekyr_s_sergeem == True):
        menu:
            "Выберите вариант ответа"

            "Хорошо, сейчас схожу.":
                Alexandr "Хорошо, сейчас схожу."
                scene bg sergey_room
                with fade

            "Хорошо, я схожу после ещё после одного перекура.":
                $ krits = krits + 1
                $ renpy.notify("Он запомнит это")

                scene black
                with fade

                "Александр уходит из офиса компании в курилку."

                "6 минут спустя."

                scene bg sergey_room
                with fade

                "Возвращаясь с перекура Александр пошел в кабинет Ирины."
    else:
        menu:
            "Выберите вариант ответа"

            "Хорошо, сейчас схожу.":
                Alexandr "Хорошо, сейчас схожу."
                scene bg sergey_room
                with fade
            "Хорошо, я схожу после перекура.":
                $ krits = krits + 1
                $ renpy.notify("Он запомнит это")
                scene black
                with fade
                "Александр уходит из офиса компании в курилку."
                "6 минут спустя."
                scene bg sergey_room
                with fade
                "Возвращаясь с перекура Александр пошел в кабинет Ирины."
    return

label konec_pervogo_dna_na_ploho:
    "На экране загорелась красным знаком, блокировка 24 часа, из за того что введен не правильный пароль."
    scene bg sergey_room
    with fade

    show irina3
    Alexandr "Извините Ирина. Я сейчас схожу к Сергею, спрошу что делать."
    "Александр выходит из кабинета Ирины  и направляется в кабинет Урика Мали."

    scene black
    with fade

    "Александр входит в кабинет Урика Мали, где разговаривали между собой Сергей и Урик Мали."

    scene bg malisroom
    with fade

    show mali1 at left
    show sergey1 at right
    Alexandr "Здравствуйте, мистер Мали."
    hide mali1

    show mali2 at left
    voice "Uri/Urik7.mp3"
    UrikMali "Здравствуй, Александр."
    hide mali2
    hide sergey1

    show mali1 at left
    show sergey2 at right
    voice "Ser/Serge24.mp3"
    Sergei "Что-то случилось?"
    hide sergey2

    show sergey1 at right
    Alexandr "Я пытался помочь Ирине с паролем от операционной системы, и я ввел пароль 3 раза неправильно. Теперь там стоит временная блокировка 24 часа."
    hide sergey1

    show sergey2 at right
    voice "Ser/Serge25.mp3"
    Sergei "Ты пока постой тут Саня, а я пойду посмотрю компьютер Ирины."

    scene black
    with fade
    "Сергей выходит из кабинета Урика Мали."

    scene bg malisroom
    with fade

    show mali2
    voice "Uri/Urik8.mp3"
    UrikMali "Вот уж дела. Дождемся Сергея, посмотрим что он скажет."
    "Спустя 7 минут."
    hide mali2
    show mali1 at right
    with fade

    show sergey1 at left
    "Сергей заходит в кабинет Урика Мали."
    hide mali1
    show mali2 at right
    voice "Uri/Urik9.mp3"
    UrikMali "Ну что там, Сергей?"
    hide mali2
    hide sergey1

    show mali1 at right
    show sergey2 at left
    voice "Ser/Serge26.mp3"
    Sergei "Стоит блокировка системы на 24 часа."
    hide sergey2
    hide mali1

    show mali2 at right
    show sergey1 at left
    voice "Uri/Urik10.mp3"
    UrikMali "Плохо дела. У нас видишь ли Александр, сейчас из за этого парализуется большая часть работы компании, и мы понесём серозные убытки."
    voice "Uri/Urik11.mp3"
    UrikMali "К сожалению Александр, нам придется попрощаться."
    hide mali2

    show mali1 at right
    Alexandr "Мне жал что произошла такая ситуация. Всего вам доброго и до свидания."
    hide mali1
    hide sergey1
    "Александр выходит из кабинета Урика Мали."

    scene plox_konc
    play music "audio/bad_kon.mp3"
    with fade
    $ renpy.notify("Вы не прошли стажировку...(Плохая концовка)")
    window hide
    "Конец"
    nvl hide
    nvl clear
    return

label perebor_vernogo_parola:
    Alexandr "Так, попробуем этот…"
    "Александр вводит паролем с записки в компьютер"
    "....."
    "Пароль оказался верным."
    return

label konec_pervogo_dna_na_horosho:
    scene bg sergey_room
    with fade

    show irina2
    voice "Iri/Irina11.mp3"
    Irina "Спасибо, Александр!"
    hide irina2

    show irina3
    Alexandr "Нет проблем. Если у вас возникнут еще какие-либо трудности, то обязательно обращайтесь."

    "Александр выходит из кабинета Ирины и возвращается в офис компании."

    scene bg ofice
    with fade

    "6 минут спустя."
    "Сергей заходит в офис компании."
    if (pomosh == True):
        show sergey6
        voice "Ser/Serge21.mp3"
        Sergei "Что нибудь происходило в моё отсутствие, Саня?"
        hide sergey6
        show sergey1
        Alexandr "Нужно было помочь Ирине. Она не могла залогиниться"
        Alexandr "Я нашел вашу записку с паролем, и теперь все заработало."
    else:
        show sergey2
        voice "Ser/Serge27.mp3"
        Sergei "Ну что Саня, ты справился с задачей?"
        hide sergey2
        show sergey1
        Alexandr "Да, я нашел вашу записку с паролем, и теперь все заработало."

    hide sergey1

    show sergey2
    voice "Ser/Serge28.mp3"
    Sergei "Ты молодец Саня!"
    voice "Ser/Serge29.mp3"
    Sergei "Пошли выпьем кофе и можем уже расходится. До конца рабочего дня осталось 10 минут."
    hide sergey2

    show sergey1
    Alexandr "Пойдемте."

    "Александр с Сергеем направились на кухню компании за кофе."

    scene black
    with fade

    window hide
    if (krits == 0):
        $ renpy.notify("Вы идеально завершили первый день стажировки")
    elif ((krits > 0) and (krits < 3)):
        $ renpy.notify("Вы успешно завершили первый день стажировки")
    else:
        $ renpy.notify("Вы завершили первый день стажировки")

    background '''АКТ 3 СТАЖИРОВКА'''
    background ''' ДЕНЬ ВТОРОЙ'''
    nvl hide
    nvl clear
    jump day2
    return
#-----------------------------------ВТОРОЙ ДЕНЬ СТАЖИРОВКИ--------------------------------------------


label day2:
    play music "audio/fon2.mp3"
    "Александр заходит в офис компании и видит там Сергея."
    scene bg ofice
    with fade

    show sergey5
    Alexandr "Здравствуйте, Сергей. Я готов начать новый день стажировки."
    hide sergey5

    show sergey6
    voice "Ser/Serge30.mp3"
    Sergei "Привет Саня. Рад видеть твою готовность к работе. Сегодня у нас есть еще одна интересная задача. Ты должен собрать новый ПК для нового сотрудника с использованием комплектующих, которые мы получили вчера."
    hide sergey6

    show sergey5
    Alexandr "Хорошо, где находятся комплектующие, которые понадобятся для сборки ПК?"
    hide sergey5

    show sergey6
    voice "Ser/Serge31.mp3"
    Sergei "Комплектующие уже размещены на специальной площадке в складском помещении."
    voice "Ser/Serge32.mp3"
    Sergei "Я сейчас пойду в серверную исправлять неполадки, а тебе нужно собрать компьютер, подключить монитор, клавиатуру и мышь. Тебе показать, где складское помещение?"
    hide sergey6

    show sergey5
    Alexandr "Нет, спасибо. Я уже разобрался где он находится."
    hide sergey5

    show sergey6
    voice "Ser/Serge33.mp3"
    Sergei "Прекрасно. Возвращайся обратно в офис после окончания работы."
    hide sergey6

    show sergey5
    Alexandr "Хорошо."

    scene black
    with fade

    "Александр направился в складское помещение."
    scene bg sklad
    with fade

    "По прибытию Александр обнаружил аккуратно сложенные комплектующие на специальной площадке и принялся собирать и подключать ПК."

    jump sborka_pk
    return

label sborka_pk: #------------------КОРПУС------------------------
    if (oshibka == 3):
        $ renpy.notify("Получено достижение: Невыспавшийся")
        Alexandr "Что то я сегодня туплю, наверное не выспался"
        $ oshibka = oshibka + 1
        $ oshibka_achivka = True
    menu:
        "Помогите Александру собрать ПК"

        "Материнская плата":
            $ oshibka = oshibka + 1
            Alexandr "Мда уж, куда я собрался ее закреплять?"
            jump sborka_pk

        "Процессор":
            $ oshibka = oshibka + 1
            Alexandr "Мда уж, куда я собрался ее закреплять?"
            jump sborka_pk

        "Кулер для процессора":
            $ oshibka = oshibka + 1
            Alexandr "Мда уж, куда я собрался ее закреплять?"
            jump sborka_pk

        "Корпус":
            jump sborka_pk_prod1
        "ОЗУ":
            $ oshibka = oshibka + 1
            Alexandr "Мда уж, куда я собрался ее закреплять?"
            jump sborka_pk

        "Видеокарта":
            $ oshibka = oshibka + 1
            Alexandr "Мда уж, куда я собрался ее закреплять?"
            jump sborka_pk

        "Нанести термопасту":
            $ oshibka = oshibka + 1
            Alexandr "Мда уж, куда я собрался ее наносить??"
            jump sborka_pk

        "Жесткий диск":
            $ oshibka = oshibka + 1
            Alexandr "Мда уж, куда я собрался ее закреплять?"
            jump sborka_pk

    return

label sborka_pk_prod1:  #------------------МАТЕРИНСКАЯ ПЛАТА------------------------
    if (oshibka == 3):
        Alexandr "Что то я сегодня туплю, наверное не выспался"
        $ oshibka = oshibka + 1
        $ oshibka_achivka = True

    menu:
        "Помогите Александру собрать ПК"

        "Материнская плата":
            jump sborka_pk_prod2

        "Процессор":
            $ oshibka = oshibka + 1
            Alexandr "Мда уж, куда я собрался ее закреплять?"
            jump sborka_pk_prod1

        "Кулер для процессора":
            $ oshibka = oshibka + 1
            Alexandr "Мда уж, куда я собрался ее закреплять?"
            jump sborka_pk_prod1
        "ОЗУ":
            $ oshibka = oshibka + 1
            Alexandr "Мда уж, куда я собрался ее закреплять?"
            jump sborka_pk_prod1

        "Видеокарта":
            $ oshibka = oshibka + 1
            Alexandr "Мда уж, куда я собрался ее закреплять?"
            jump sborka_pk_prod1

        "Нанести термопасту":
            $ oshibka = oshibka + 1
            Alexandr "Мда уж, куда я собрался ее наносить??"
            jump sborka_pk_prod1

        "Жесткий диск":
            $ oshibka = oshibka + 1
            Alexandr "Мда уж, куда я собрался ее закреплять?"
            jump sborka_pk_prod1
    return

label sborka_pk_prod2:    #------------------ПРОЦЕССОР------------------------
    if (oshibka == 3):
        Alexandr "Что то я сегодня туплю, наверное не выспался"
        $ oshibka = oshibka + 1
        $ oshibka_achivka = True

    menu:
        "Помогите Александру собрать ПК"

        "Процессор":
            jump sborka_pk_prod3

        "Кулер для процессора":
            $ oshibka = oshibka + 1
            Alexandr "Для этого нужно поставить процессор."
            jump sborka_pk_prod2
        "ОЗУ":
            Alexandr "Думаю лучше сначала поставить процессор."
            jump sborka_pk_prod2

        "Видеокарта":
            Alexandr "Думаю лучше сначала поставить процессор."
            jump sborka_pk_prod2

        "Нанести термопасту":
            $ oshibka = oshibka + 1
            Alexandr "Мда уж, куда я собрался ее наносить??"
            jump sborka_pk_prod2

        "Жесткий диск":
            Alexandr "Думаю лучше сначала поставить процессор."
            jump sborka_pk_prod2
    return

label sborka_pk_prod3:    #------------------ТЕРМОПАСТА------------------------
    if (oshibka == 3):
        Alexandr "Что то я сегодня туплю, наверное не выспался"
        $ oshibka = oshibka + 1
        $ oshibka_achivka = True

    menu:
        "Помогите Александру собрать ПК"

        "Кулер для процессора":
            $ oshibka = oshibka + 1
            Alexandr "Для этого нужно нанести термопасту на процессор."
            jump sborka_pk_prod3
        "ОЗУ":
            Alexandr "Думаю лучше сначала закончить с процессором."
            jump sborka_pk_prod3

        "Видеокарта":
            Alexandr "Думаю лучше сначала закончить с процессором."
            jump sborka_pk_prod3

        "Нанести термопасту":
            jump sborka_pk_prod4

        "Жесткий диск":
            Alexandr "Думаю лучше сначала закончить с процессором."
            jump sborka_pk_prod3
    return

label sborka_pk_prod4: #---------------------КУЛЕР ДЛЯ ПРОЦЕССОРА------------------------
    if (oshibka == 3):
        Alexandr "Что то я сегодня туплю, наверное не выспался"
        $ oshibka = oshibka + 1
        $ oshibka_achivka = True

    menu:
        "Помогите Александру собрать ПК"

        "Кулер для процессора":
            jump sborka_pk_prod_vib
        "ОЗУ":
            Alexandr "Думаю лучше сначала закончить с процессором."
            jump sborka_pk_prod4

        "Видеокарта":
            Alexandr "Думаю лучше сначала закончить с процессором."
            jump sborka_pk_prod4

        "Жесткий диск":
            Alexandr "Думаю лучше сначала закончить с процессором."
            jump sborka_pk_prod4
    return
#---------------------------------------------------------------------------
label sborka_pk_prod_vib:

    menu:
        "Помогите Александру собрать ПК"

        "ОЗУ": #--- 1
            jump sborka_pk_prod_vib_1

        "Видеокарта": #---- 2
            jump sborka_pk_prod_vib_2

        "Жесткий диск": #---- 3
            jump sborka_pk_prod_vib_3
    return

#---------------------------ВЕТКА ОЗУ-------------------------
label sborka_pk_prod_vib_1:

    menu:
        "Помогите Александру собрать ПК"

        "Видеокарта": #---- 2
            jump sborka_pk_prod_vib_1_2

        "Жесткий диск": #---- 3
            jump sborka_pk_prod_vib_1_3
    return

label sborka_pk_prod_vib_1_2:

    menu:
        "Помогите Александру собрать ПК"

        "Жесткий диск": #---- 3
            jump fin_sborki
    return

label sborka_pk_prod_vib_1_3:

    menu:
        "Помогите Александру собрать ПК"

        "Видеокарта": #---- 2
            jump fin_sborki

    return
#-----------------------------ВЕТКА ВИДЕОКАРТЫ---------------------
label sborka_pk_prod_vib_2:

    menu:
        "Помогите Александру собрать ПК"

        "ОЗУ": #--- 1
            jump sborka_pk_prod_vib_2_1

        "Жесткий диск": #---- 3
            jump sborka_pk_prod_vib_2_3
    return

label sborka_pk_prod_vib_2_1:

    menu:
        "Помогите Александру собрать ПК"

        "Жесткий диск": #---- 3
            jump fin_sborki
    return

label sborka_pk_prod_vib_2_3:

    menu:
        "Помогите Александру собрать ПК"

        "ОЗУ": #--- 1
            jump fin_sborki
    return
#-----------------------------------ВЕТКА ЖЕСТКОГО ДИСКА-----------------------
label sborka_pk_prod_vib_3:

    menu:
        "Помогите Александру собрать ПК"

        "ОЗУ": #--- 1
            jump sborka_pk_prod_vib_3_1

        "Видеокарта": #---- 2
            jump sborka_pk_prod_vib_3_2

    return
label sborka_pk_prod_vib_3_1:

    menu:
        "Помогите Александру собрать ПК"

        "Видеокарта": #---- 2
            jump fin_sborki

    return

label sborka_pk_prod_vib_3_2:

    menu:
        "Помогите Александру собрать ПК"

        "ОЗУ": #--- 1
            jump fin_sborki

    return

label fin_sborki:

    "Александр собрал компьютер и начал подключать периферийное оборудование."
    "3 минуты спустя"
    menu:
        "Выберите вариант ответа"

        "Это было легко":
            Alexandr "Это было легко"
        "Это было сложно":
            Alexandr "Это было сложно"
    scene black
    with fade
    "Александр направился в офис компании Rinus Corp."

    scene bg ofice
    with fade

    show sergey5

    "Александр заходит в офис компании и видит уже находящегося там Сергея."
    Alexandr "Я закончил обустройство рабочего места, для нового сотрудника."
    hide sergey5

    show sergey6
    voice "Ser/Serge34.mp3"
    Sergei "Отлично. Ты справился довольно быстро. Хорошая работа!"
    hide sergey6

    show sergey5
    play sound "call.ogg"
    "Телефон Сергея звонит."


    hide sergey5
    show sergey6
    voice "Ser/Serge35.mp3"
    Sergei "Извини, мне нужно ответить на звонок. Подожди, пожалуйста, пару минут."

    "Сергей разговаривает по телефону с Уриком Мали, после чего говорит к Александру."
    voice "Ser/Serge36.mp3"
    Sergei "Урик Мали звонил и просил помочь ему разобраться с проблемой. Он говорит, что после скачивания игры, у него начались проблемы с интернетом. Ты можешь пойти к нему и посмотреть, что случилось?"

    voice "Ser/Serge37.mp3"
    Sergei "А я займусь установкой ПО на компьютер, который ты собрал."
    hide sergey6
    show sergey5

    Alexandr "Конечно, я уже иду."

    jump mali_problem

    return

label mali_problem:
    scene black
    with fade
    "Александр направляется в кабинет к Урику Мали, чтобы помочь ему с проблемой интернета."
    "Александр, постучав, заходит в кабинет Урика Мали."

    scene bg malisroom
    with fade

    show mali1
    Alexandr "Здравствуйте, мистер Мали."
    hide mali1

    show mali2
    voice "Uri/Urik12.mp3"
    UrikMali "Здравствуй, Александр. У меня перестал работать интернет на компьютере после того, как я скачал игру . Можешь посмотреть, в чем проблема?"
    hide mali2

    show mali1
    Alexandr "Сейчас посмотрю."
    hide mali1

    "Посмотрев на рабочий стол, увидел, что интернет и вправду не работает."

    jump sborka_pk_mali

    return

label sborka_pk_mali:

    menu:
        "Выберите вариант действия"

        "Перезагрузить компьютер":
            if (perezagruzka == True):
                "Александр решил ещё перезагрузить компьютер"
                "После перезагрузки, проблема не решилась. Интернет также не работает."
            else:
                "Александр решил перезагрузить компьютер."
                "После перезагрузки, проблема не решилась. Интернет также не работает."
            $ perezagruzka = True
            jump sborka_pk_mali

        "Проверить компьютер на вирусы":
            "Александр решил проверить компьютер на вирусы."
            "После запуска сканирования антивирусом компьютер на вирусы, Александру пришлось ждать."
            jump sborka_pk_mali_prod

    return

label sborka_pk_mali_prod:

    show mali1
    with fade

    hide mali1
    show mali2
    voice "Uri/Urik13.mp3"
    UrikMali "Может, пока ждем, кофе или чай налить?"

    hide mali2
    show mali1
    Alexandr "Нет, спасибо."

    scene black
    with fade
    "Спустя 20 минут"

    scene bg malisroom
    with fade

    "Антивирус проверил компьютер на вирусы и выявил 2 угрозы."

    jump ustran_ugroz

    return

label ustran_ugroz:

    if (perezagruzka2 == False):
        menu:
            "Выберите вариант действия"

            "Устранить угрозы, не перезагружая компьютер":
                "После того, как Александр устранил угрозы и проигнорировал сообщения антивируса о перезагрузке ПК, он сразу обратил внимание, что интернет так и не заработал."
                show mali2
                with fade
                voice "Uri/Urik14.mp3"
                UrikMali "Может, все же стоит перезагрузить компьютер?"
                hide mali2
                show mali1
                Alexandr "Скорее да, чем нет."
                hide mali1
                with fade
                "Александр перезагрузил компьютер."
                "Проблема с интернетом так и не решилась."
                $ perezagruzka2 = True
                jump ustran_ugroz

            "Устранить угрозы, перезагружая компьютер":
                "Александр устранил угрозы и перезагрузил компьютер."
                "Проблема с интернетом, так и не решилась."
                $ perezagruzka2 = True
                jump ustran_ugroz
    else:
        menu:
            "Осмотреть корпус компьютера":
                "Так как проблема с интернетом так и не решилась."
                "Александр решает осмотреть подключение кабелей в компьютер."
                "Во время осмотра, Александр заметил, что сетевой кабель оказался отключенным от компьютера."
                "Александр подключил сетевой кабель к компьютеру и тут же проверил, заработал ли интернет на компьютере."
                "Интернет на компьютере заработал."

    jump ustran

    return

label ustran:

    show mali1
    with fade
    Alexandr "Все готово. У Вас сетевой провод отключился от компьютера, поэтому интернет  перестал работать."
    hide mali1

    show mali2
    voice "Uri/Urik15.mp3"
    UrikMali "Спасибо, Александр, похоже, что я случайно его ногой задел и отключил."
    hide mali2

    show mali1
    Alexandr "Рад был помочь, мистер Мали. Если у Вас будут еще какие-либо проблемы, не стесняйтесь обращаться."
    hide mali1

    show mali2
    voice "Uri/Urik16.mp3"
    UrikMali "И еще, Александр. До конца смены осталось 30 минут, и так как ты сегодня хорошо поработал, можешь уйти пораньше."
    hide mali2

    show mali1
    Alexandr "Спасибо вам, мистер Мали."

    jump konec_vtorogo_dna

    return

label konec_vtorogo_dna:

    scene black
    with fade

    "Александр возвращается обратно в офис компании для того, чтобы попрощаться с Сергеем."

    scene bg ofice
    with fade

    show sergey5
    Alexandr "Задача выполнена, интернет снова заработал. Меня мистер Мали отпустил пораньше. Я могу идти?"
    hide sergey5

    show sergey6
    voice "Ser/Serge38.mp3"
    Sergei "Конечно, молодчина, Саня. Удачи тебе!"
    hide sergey6

    show sergey5
    Alexandr "И вам."

    scene black
    with fade
    "Конец второго дня стажировки"

    jump treti_den

    return

label treti_den:

    scene black
    window hide
    background '''АКТ 3 СТАЖИРОВКА'''
    background ''' ДЕНЬ ТРЕТИЙ'''
    nvl hide
    nvl clear

    scene black
    with fade

    "Александр заходит в офис компании и видит там Ирину."

    scene bg ofice
    with fade

    show irina2
    voice "Iri/Irina12.mp3"
    Irina "Здравствуйте, Александр. Сегодня у вас финальный день стажировки. Вас ожидает анкетирование."
    hide irina2

    show irina1
    Alexandr "Здравствуйте, Ирина. Я уже готов к его прохождению."
    hide irina1

    show irina2
    voice "Iri/Irina13.mp3"
    Irina "Отлично, тогда присаживайтесь за этот компьютер. Там уже все открыто и настроено, можете начинать."
    hide irina2

    show irina1
    Alexandr "Хорошо, Спасибо."
    hide irina1
    with fade

    "Александр присаживается за компьютер, на который указала Ирина."
    "Александр, нажал кнопку начать тест и на экране сразу появился первый вопрос."

    menu:
        "1. Какие навыки вы считаете ключевыми для успешной работы в команде?"

        "Коммуникация и слушание":
            jump vopr_2

        "Работа с конструктивной критикой":
            jump vopr_2

        "Эмпатия и умение воспринимать разнообразные точки зрения":
            jump vopr_2

        "Организация и распределение обязанностей":
            jump vopr_2

    return

label vopr_2:

    menu:
        "2. Как вы реагируете на стрессовые ситуации на работе?"

        "Практикую техники релаксации, такие как глубокое дыхание":
            jump vopr_3

        "Разбиваю сложные задачи на более мелкие подзадачи":
            jump vopr_3

        "Обращаюсь к коллегам за поддержкой и советом":
            jump vopr_3

        "Пересматриваю свой план работы и при необходимости корректирую его":
            jump vopr_3

    return

label vopr_3:

    menu:
        "3. Как вы поддерживаете свое профессиональное развитие и обучение?"

        "Регулярно посещаю семинары и конференции по теме моей области":
            jump vopr_4

        "Читаю профессиональные блоги и литературу":
            jump vopr_4

        "Занимаюсь онлайн-курсами и обучением в формате вебинаров":
            jump vopr_4

        "Участвую в профессиональных сообществах и форумах.":
            jump vopr_4

    return

label vopr_4:

    menu:
        "4. Как вы оцениваете свою способность адаптироваться к изменениям в рабочей среде?"

        "Адаптируюсь легко и быстро, умею находить решения в новых условиях":
            jump vopr_5

        "Требуется некоторое время, чтобы адаптироваться, но я успешно справляюсь":
            jump vopr_5

        "Нуждаюсь в структуре и поддержке при изменениях":
            jump vopr_5

        "Переживаю трудности при адаптации, но всегда готов учиться и развиваться":
            jump vopr_5

    return

label vopr_5:

    menu:
        "5. Какие качества вы считаете наиболее важными для эффективного лидера?"

        "Вдохновляющая коммуникация и мотивация коллектива":
            jump vopr_6

        "Способность делегировать задачи и доверять сотрудникам":
            jump vopr_6

        "Умение принимать решения в сложных ситуациях":
            jump vopr_6

        "Эмпатия и способность создавать благоприятную атмосферу в коллективе":
            jump vopr_6

    return

label vopr_6:

    menu:
        "6. Как вы оцениваете свою эффективность в управлении временем?"

        "Очень эффективен, строго следую планам и графикам":
            jump vopr_7

        "Хорошо управляю временем, но иногда требуется коррекция расписания":
            jump vopr_7

        "Имею трудности с управлением временем, но работаю над собой":
            jump vopr_7

        "Часто испытываю сложности в распределении времени, но готов улучшить свои навыки":
            jump vopr_7

    return

label vopr_7:

    menu:
        "7. Как вы справляетесь с критикой вашей работы?"

        "Принимаю критику как возможность для роста и улучшений":
            jump konec_anketi

        "Анализирую конструктивную критику и использую ее для коррекции ошибок":
            jump konec_anketi

        "Иногда трудно принимать критику, но стараюсь не принимать это близко к сердцу":
            jump konec_anketi

        "Реагирую на критику негативно, но потом нахожу позитивные стороны в полученных замечаниях":
            jump konec_anketi

    return

label konec_anketi:

    "После того, как Александр ответил на 7 вопрос, на экране загорелась надпись, что анкетирование пройдено."
    "В офис заходит Сергей и подходит к Александру."

    show sergey6
    with fade
    voice "Ser/Serge39.mp3"
    Sergei "Здарова, Саня. Я вижу, ты уже написал анкетирование."
    hide sergey6

    show sergey5
    Alexandr "Здравствуйте, Сергей. Да, уже написал."
    hide sergey5

    show sergey6
    voice "Ser/Serge40.mp3"
    Sergei "На сегодня для тебя дел больше нет. Приходи сюда завтра, Урик Мали посмотрит твое анкетирование и примет решение."
    hide sergey6

    show sergey5
    Alexandr "Хорошо, до свидания, Сергей."
    hide sergey5

    show sergey6
    voice "Ser/Serge41.mp3"
    Sergei "До завтра."

    scene black
    with fade
    jump chetverti_den

    return

label chetverti_den:

    scene black
    window hide
    background '''АКТ 3 СТАЖИРОВКА'''
    background ''' ДЕНЬ ЧЕТВЁРТЫЙ'''
    nvl hide
    nvl clear

    scene bg ofice

    "Александр заходит в офис компании, где никого нет."
    Alexandr "Хм, может, я рано пришел?"
    "Спустя 7 минут."

    "В офис заходит Урик Мали и подходит к Александру."
    show mali2
    with fade
    voice "Uri/Urik17.mp3"
    UrikMali "Здравствуй, Александр. Пройдем ко мне в кабинет, обсудим твое трудоустройство."
    hide mali2

    show mali1
    Alexandr "Здравствуйте, мистер Мали. Конечно, уже иду."

    "Урик Мали с Александром поспешили в кабинет начальника."

    scene bg malisroom
    with fade

    show mali2
    voice "Uri/Urik18.mp3"
    UrikMali "Присаживайся. Я посмотрел твое анкетирование и также спросил Сергея, как ты работал."

    "..."

    voice "Uri/Urik19.mp3"
    UrikMali "По итогу я хочу сказать, что ты принят в наш штат!"
    hide mali2

    show mali1
    Alexandr "Спасибо Вам большое, мистер Мали. Я Вас не подведу."

    scene bg kabgg
    with fade
    $ renpy.notify("Вы прошли стажировки (Хорошая концовка)")
    "Конец"

    return

label ploxai_koncovka:
    play sound "call.ogg"
    "У Александра зазвонил телефон в кармане."

    Alexandr "Ало..."
    voice "Uri/Urik20.mp3"
    UrikMali "Александр, это Урик Мали. Можешь подойти в мой кабинет, обсудить пару вопросов?"

    Alexandr "Кончено, я уже иду."

    "Александр поспешил в кабинет Урика Мали."

    scene bg malisroom
    with fade

    "Александр постучав в дверь зашёл в кабинет Урика Мали."

    show mali1
    Alexandr "Здравствуйте, мистер Мали."
    hide mali1

    show mali2
    voice "Uri/Urik21.mp3"
    UrikMali "Здравствуй, Александр, присаживайся."

    voice "Uri/Urik22.mp3"
    UrikMali "Я тут следил за твоей работой, и не очень доволен ею. К сожалению нам проедется разойтись."
    hide mali2

    $ renpy.notify("Получено достижение: Перекурщик")

    show mali1
    Alexandr "Простите меня мистер Мали за мои ошибки. Всего вам доброго, до свидания!"
    hide mali1

    show mali2
    voice "Uri/Urik23.mp3"
    UrikMali "Всего доброго, Александр."

    play music "audio/bad_kon.mp3"
    scene plox_konc
    with fade
    $ renpy.notify("Вы не смогли завершить стажировку (Плохая концовка)")

    "Конец"

    return