label day2:
    
    play music "music/day2_music.mp3" fadein(0.1)
    define flash = Fade(0.1, 0.0, 0.5, color="#fff")
    
    scene loc_wake_up
    with fade
    
    c_gg '''  
    Мне приснился странный сон.
        
    Будто бы я сдал мидку по дискретке на 100 процентов.
    
    Одни бредни снятся последнее время...

    Ну и вчерашний день был необычным.
    
    Будто я попал в какую-то визуальную новеллу.
    
    Кстати, {w} нам вчера сказали о чём то...
    
    Уже забыл.
    
    Ну, значит это не так ужи и важно!
    '''
    c_gg_say "-Ладно. Пора идти в университет."


    scene loc_route_from_home
    with Fade(1.0, 1.0, 1.0, color="#000")
    
    c_gg "На-улице малая прохлада. {w} Зима скоро."
    c_gg "Благо я в своей любимой куртке."
    c_gg "В автобусе много людей которые едут по своим работам, школам или даже домой после тяжелой рабочей смены."
    c_gg "Унылые и скудные лица. А их случайный взгляд на меня бьет по самые пятки."
    c_gg_say "-Надеюсь вы все умрёте..."
    play one_beat "sound/one_beat.mp3"
    scene loc_route_from_home
    with flash
    c_stranger "-Эй, малой, чё сказал?"
    c_gg_say "-Я имел ввиду..эээ...вы скоро выходите?"
    c_stranger "-Гм....Следи за своим языком в следующий раз! {w} Да, я выхожу."
    c_gg "Я вышел вместе с ним и начал идти в сторону своего университета."

    scene loc_hall
    with Fade(1.0, 1.0, 1.0, color="#000")
    c_gg_say "-Наконец-то я тут, как же холодно."
    c_gg "Я провел свой рюкзак через проверочную ленту и хотел было пройти, но..."
    c_security_guard "-Эй, ты!"
    c_gg "-Мне послышался чей-то крик."

    show security_guard_casual at center
    with dissolve
    c_security_guard "-С сегодняшнего дня, вход в университет разрешается только с айди картой! {w}Неужели твой староста тебе это не сказал?"
    c_gg "Чёртов Ыдырыс..."
    c_gg_say "-Да... тоесть нет. Я просто её забыл."
    hide security_guard_casual
    show security_guard_casualFrowned at center
    c_security_guard "-Да как ты посмел?!"
    c_security_guard "-Я тебя не впущу! {w} Вдруг ты не наш студент!"
    c_gg "Боже, какой же бред..."
    c_gg_say "-Слушайте, я конечно понимаю всё, но я правда у вас учусь."
    c_gg_say "-Я ведь могу просто показаться свой мудл?"
    hide security_guard_casualFrowned
    show security_guard_casualFrowned at center
    with zoomin
    c_security_guard "-Ты кого мудлом назвал? А-НУ, ТЫ СЕЙЧАС ПОЙДЁШЬ СО МНОЙ!!!!!"
    c_ict_teacher "-Кхм-кхм..."
    hide security_guard_casualFrowned
    show security_guard_casualFrowned:
        xalign .75
    with moveoutright
    c_gg "Я повернулся налево там стояла наша учительница по ИКТ."
    show ict_teacher_casualUpset:
        xalign .25
    with dissolve 
    c_ict_teacher "-Мистер Охранник, это наш студент, я вас уверяю."
    c_ict_teacher "-Он мне нужен. Пропустите его."
    hide security_guard_casualFrowned
    show security_guard_casualSmile:
        xalign .75
    c_security_guard "-Э.... Простите Миссис Учительница ИКТ, это было моя оплошность."
    
    hide ict_teacher_casualUpset
    show ict_teacher_casualSmile:
        xalign .25
        
    
    c_ict_teacher "..."
    
    hide security_guard_casualSmile
    with dissolve
    hide ict_teacher_casualSmile
    show ict_teacher_casualSmile at center
    with move
    
    c_gg_say "-Спасибо ва..."
    hide ict_teacher_casualSmile
    show ict_teacher_casual
    c_ict_teacher "-У нас нет времени, иди за мной."
    
    scene loc_open_space
    with Fade(1.0, 1.0, 1.0, color="#000")
    
    c_gg "Она отвела меня в ОС, где пока что было мало студентов."
    
    show ict_teacher_casual at center
    with dissolve
    c_ict_teacher "-И так, Ваня, ты ведь из группы CS-2209?"
    c_gg_say "-Да, верно. {w} А что?"
    c_ict_teacher '''
    -Ты ведь знаешь, что скоро у вас будет защита проекта?
    
    -Я хотела узнать в какой ты группе, потому что на прошлом уроке тебя не было.
    
    -А так же, что вы будете делать?
    '''
    c_gg_say "-Эээ... {w} прошу прощения, что не предупредил."
    c_gg '''
        Как я мог забыть! Точно!
        Я даже ни с кем не в команде...
    '''
    c_gg_say "-Я.... {w} в команде с Артёмидой, Джихагулей, и Асхатлиной."
    
    hide ict_teacher_casual
    show ict_teacher_casualSmile at center
    c_ict_teacher "-Мило."
    
    c_gg_say "А делать мы б-будем....."
    c_gg "Нужно срочно что-то придумать."
    c_gg_say "Визуальную новеллу!"
    
    c_ict_teacher "Ну-с, желаю вам удачи. Увидимся на уроке. Готовьтесь, детки!"
    
    hide ict_teacher_casualSmile
    with dissolve
    
    c_gg_say "Фуххххх....."
    c_gg_say "Так, теперь надо предупредить этих троих, что я ляпнул."
    c_gg_say "Они сто процентов в столовке!"
    
    scene loc_cafeteria
    with Fade(1.0, 1.0, 1.0, color="#000")
    play sound_people "sound/manypeople.mp3"
    
    "{w}"
    c_gg "Ну-с, где они?"
    
    
    show artemida_uniform at center
    with dissolve
    
    c_artemida '''
    Хэй, Ваня, как ты?
    
    Что тебя привело в столовую?
    
    Обычно ты сюда не заходишь...
    '''
    
    c_gg_say "О, Артёмида, привет! {w} Ты мне как раз нужна!"
    hide artemida_uniform
    show artemida_uniformFrowned at center
    c_artemida "Что-то случилось?"
    c_gg_say "ДА! Помнишь что нам задали проект по ИКТ? Короче, я случа-"
    hide artemida_uniformFrowned
    show artemida_uniformLaugh at center
    c_artemida "Да, мы как раз собирались с Асхатлиной и Джихангулей начать уже делать."
    c_artemida "Не хочешь с нами?"
    c_gg "..."
    c_gg "В этот момент я поверил в бога."
    c_gg "Как удобно. {w} Я действительно везунчик."
    c_gg_say "Думаю, да. Давайте! А что вы планируете?"
    c_artemida "Визуальную новеллу!"
    c_gg "Мысль о том что я теперь нахожусь в игре увеличилась."
    c_artemida "О, смотри! Вот и они!"
    
    show askhatlina_casual:
        xalign 0.15
        yalign 1.0
    show dzhikhangul_casual:
        xalign 0.8
        yalign 1.0 
    
    c_askhatlina "Привет, Ваня!"
    c_dzhikhangul "Здравствуй!"
    
    c_gg_say "Эм, да... Привет, девочки!"    
    
    c_gg "Спустя пару секунд начались хлопки по всей столовке."
    
    play manyclap "sound/manyclaps.mp3" fadein (0.1)
    
    hide dzhikhangul_casual
    show dzhikhangul_casualFrowned:
        xalign 0.8
        yalign 1.0
        
    c_dzhikhangul "Опять..."
    hide askhatlina_casual
    show askhatlina_casualFrowned:
        xalign 0.15
        yalign 1.0
    c_askhatlina "Сейчас начнётся. Остановите этого безумца!"
    
    hide artemida_uniformLaugh
    show artemida_uniformFrowned at center
    
    stop manyclap fadeout(0.1)
    
    play oneclap "sound/clap_echo.mp3" fadein(0.1)
    
    c_gg "Константин, пресуще ему, продолжил хлопать один."

    c_artemida "Это надолго..."
    hide askhatlina_casualFrowned
    show askhatlina_casual: 
        xalign 0.15
        yalign 1.0
    c_askhatlina "Ладно, гайс, давайте двигаться. {w} Мне еще Элленочку встречать."
    hide dzhikhangul_casualFrowned
    show dzhikhangul_casual:
        xalign 0.8
        yalign 1.0
        
    c_dzhikhangul "Погнали. {w} Ваня, ты с нами?"
    c_gg_say "Думаю, я сразу пойду домой."
    c_gg_say "Как насчёт того, чтобы собраться в дискорде и начать делать игру?"
    
    hide artemida_uniformFrowned
    show artemida_uniformLaugh at center
    
    c_artemida "Отличная идея! Давайте таки сделаем."
    stop oneclap fadeout(0.1)
    stop sound_people fadeout(0.1)
    
    scene loc_wake_up
    with Fade(1.0, 1.0, 1.0, color="#000")
    
    c_gg ''' 
    Таки закончился мой второй день в университете.
    
    Думаю, вы уже давно поняли, что в тот день никто в дискорде не собрался.
    
    Может на следующий день мне повезет...
    
    Ну, а теперь самое время спать.
    
    Вот бы завтрашний день был лучше чем сегодняшний.
    '''
    
    scene loc_nigger
    with Fade(1.0, 5.0, 3.0, color="#000")
    stop music fadeout(0.1)
    play transition "sound/transition.mp3"
    scene tr_day3
    with Fade(0.5, 1.0, 3.0, color="#000")
    
    jump day3
    
    