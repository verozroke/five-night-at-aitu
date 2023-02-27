init python:
    renpy.music.register_channel("wake_wake_it_is_time_for_school", loop=True)
    renpy.music.register_channel("ja_calendar", loop=True)
    renpy.music.register_channel("afew", loop=False)
    renpy.music.register_channel("sound_people", loop=True)
    renpy.music.register_channel("manyclap", loop=True)
    renpy.music.register_channel("oneclap", loop=True)
    renpy.music.register_channel("one_beat", loop=False)
    renpy.music.register_channel("transition", loop=False)
    
    
label day1:
    $_dismiss_pause = False
    play transition "sound/transition.mp3"
    scene tr_day1
    with Fade(0.5, 1.0, 3.0, color="#000")
    define flash = Fade(0.1, 0.0, 0.5, color="#fff")
    play music "music/day1_music.mp3" fadein(0.1)
    
    scene loc_wake_up
    with fade
    play wake_wake_it_is_time_for_school "sound/s_clock.mp3"
    c_bud "Время 7:45."
    c_bud "WAKE WAKE CMOOON."
    c_gg "Как же не хочется вставать..."
    menu:
        c_gg "Поспать может? Лишь самую малость..."
        "Проспать":
            jump prospal
        "Проснуться":
            jump nep
            
            
            
    label prospal:
        scene loc_wake_up
        with Fade(1.0, 1.0, 1.0, color="#000")
        play wake_wake_it_is_time_for_school "sound/s_clock.mp3"
        c_gg "Аааа..."
        c_gg "Да сколько можно, встаю уже, встаю..."
        stop wake_wake_it_is_time_for_school
        scene loc_house
        with Fade(1.0, 1.0, 1.0, color="#000")
        c_gg "Как же болит голова"
        c_gg "Интересно, что там по времени..."
        c_gg "..."
        c_gg_say "-О нет..."
        c_gg_say "-Я уже опоздал на пару"
        c_gg "*Неприятный запах*"
        c_gg "Только не это..."
        c_gg "Но нужно спешить!"
        jump com1


    label nep:
        stop wake_wake_it_is_time_for_school
        scene loc_house
        with Fade(1.0, 1.0, 1.0, color="#000")
        c_gg_say "-Да встаю я уже, встаю."
        c_gg "Остаются считанные дни до начала сессий, нужно начинать подготовку..."
        
        play wake_wake_it_is_time_for_school "sound/s_clock.mp3"
        c_bud " "
        stop wake_wake_it_is_time_for_school

        c_gg_say "-Понял, понял..."
        c_gg "Мысли прочь. Да и не помешало бы мне помыться"

        scene loc_shower
        with Fade(1.0, 1.0, 1.0, color="#000")
        
        
        play ja_calendar "sound/s_shower.mp3"
        c_gg "Скучновато как-то мыться под звук воды, душе петь хочется"
        c_gg "Что бы такого спеть..."
        c_gg "Блин, не могу вспомнить..."
        c_gg_say "-О, точно!"
        c_gg_say "-Я КАЛЕНДАРЬ, Я КАЛЕНДАРЬ, Я КАЛЕНДАРЬ"
        stop ja_calendar
        
        scene loc_house
        with Fade(1.0, 1.0, 1.0, color="#000")
        c_gg_say "-Фух, как же хорошо стало..."
        c_gg_say "-Теперь и в уник идти не стыдно"
        jump com2
label com1:   
    scene tr
    with Fade(1.0, 1.0, 1.0, color="#000")
    play afew "sound/s_afew.mp3"
    c_gg "По пути в университет..."
    scene loc_open_space 
    with Fade(1.0, 1.0, 1.0, color="#000")
    play sound_people "sound/manypeople.mp3"
    show idris_uniformLaugh at left
    with dissolve
    show konstantin_uniformSmile at right
    with dissolve
    c_idris "...те видео с капибарами были реально смешными"
    hide konstantin_uniformSmile
    hide idris_uniformLaugh
    show konstantin_uniformFrowned at right
    show idris_uniformFrowned at left
    c_konstantin "-Тих, смотри кто пришёл"
    c_idris "-Ну и ну, а мы то думали, что ты и вовсе не придешь"
    c_konstantin "-Стоп, а чего же мы здесь стоим? {w} Даник же нас звал в столовую"
    c_idris "-Точно, пора нам в путь, ты с нами?"
    c_gg_say "-Да, давай..."
    hide konstantin_uniformFrowned 
    with dissolve
    hide idris_uniformFrowned
    with dissolve
    stop sound_people
    label stolovka1:
    scene loc_cafeteria
    with Fade(1.0, 1.0, 1.0, color="#000")
    play sound_people "sound/manypeople.mp3"
    show idris_uniformLaugh at left
    with dissolve
    show konstantin_uniformSmile at right
    with dissolve
    show danik_casualFrowned at center
    with dissolve
    
    c_danik "-Ну и где вас несло интересно?..."
    hide idris_uniformLaugh
    show idris_uniform at left
    with dissolve 
    c_idris "-Да Ваню в ОС встретили, вот и, разговорились..."
    hide danik_casualFrowned
    show danik_casual at center
    with dissolve
    c_danik "-Другого и не ожидал..."
    c_danik "-Ой, Ваня, привет, не заметил тебя"
    c_danik "-Ты такую новость пропустил"
    c_gg_say "-Какую?"
    c_danik "-Потом расскажем, а сейчас нам нужно..."
    stop sound_people
    play manyclap "sound/manyclaps.mp3"
    hide konstantin_uniformSmile
    with dissolve
    c_danik "-Началось...  {w=1}"
    stop manyclap
    hide danik_casual
    with dissolve
    hide idris_uniform
    with dissolve
    show konstantin_uniformSmile at center
    with dissolve
    play oneclap "sound/clap_echo.mp3"
    show danik_casualFrowned at left
    with dissolve
    show idris_uniformLaugh at right
    with dissolve
    c_danik "-Константин, прекращай, все уже перестали хлопать..."
    stop oneclap
    play one_beat "sound/one_beat.mp3"
    with flash
    hide konstantin_uniformSmile
    stop manyclap
    c_danik "-Фух, наконец-то..."
    c_danik "-Пожалуй мы в ОС, Ыдрыс, Ваня, приходи с Асхатом, он там сидит... ест"
    c_idris "-Ок."
    hide danik_casualFrowned
    with dissolve
    c_idris "-Ох уж эта привычка Константина..."
    show askhatlina_uniformLaugh at left
    with dissolve
    c_askhatlina "-О, привет Ыдырыс, ты случаем не видел Даника, ибо он со мной был, оглянулся и он исчез..."
    c_idris "-Да они с Константином ушли в ОС..."
    c_askhatlina "-ЧТОО?"
    c_askhatlina "-И Константин был здесь?"
    c_idris "-А по твоему, чьи одиночные хлопки, ты думаешь слышал, к тому времени, когда все уже закончили хлопать... "
    c_askhatlina "Точно!"
    c_gg "Надо бы им предложить присоедениться к другим, а то слишком душно становится в этом месте."
    c_gg_say "-Ребят, может уже пойдем в ОС, кажется мы мешаем другим."
    hide idris_uniformLaugh
    hide askhatlina_uniformLaugh
    show idris_uniform at right
    show askhatlina_uniform at left
    c_askhatlina "-Да, конечно, пошлите..."
    hide askhatlina_uniform
    with dissolve
    hide idris_uniform
    with dissolve 
    scene loc_open_space
    with Fade(1.0, 1.0, 1.0, color="#000")
    play sound_people "sound/manypeople.mp3"
    show artemida_uniform at center
    with dissolve
    show danik_casual at right
    with dissolve
    show askhatlina_uniform at left
    with dissolve
    c_artemida "-В общем, ребят, на подготовку у нас есть неделя, {w} и за этот период нам нужно подготовиться к финальному экзамену..."
    c_gg_say "-Финальный экзамен? Стоп, что??!!"
    hide danik_casual 
    show danik_casualSmile at right
    c_danik "-Оп, какие люди, кстати Ваня, {w} мы здесь обсуждаем ту самую новость."
    c_gg_say "-Так вот оно что..."
    c_danik "-Артемида как раз её объясняет. {w} Присоединяйся."
    c_gg "В этот момент, Артемида посмотрел на меня, {w} и..."
    c_gg "И началось..."
    hide artemida_uniform
    show artemida_uniformLaugh at center
    c_artemida "-Для начала, здравствуй, Ваня!"
    c_gg_say "-Здаров..."
    c_artemida "-Чтож, приступим..."
    c_artemida "-Ох, ну и зря ты опоздал..."
    c_artemida "-Преподавательница по ИКТ, выставила нам дедлайн по групповому проекту для финального экзамена..."
    c_artemida "-Суть проекта такова..."
    c_artemida "-Первое..."
    c_artemida "-У тебя должна быть группа для проекта"
    c_artemida "-Второе..."
    c_artemida "-Задача проекта, создать какую-либо программу в коллективе "
    c_gg_say "-Какую?"
    c_artemida "-Любую, вы можете создать хоть игру, сайт, бота, что угодно"
    c_gg_say "-Класс..."
    c_gg "На все это у нас есть всего лишь три дня..."
    c_gg "Три...{w} дня"
    c_gg_say "-Ладно..."
    c_gg_say "-Спасибо за объяснение, Артемида"
    c_artemida "-Да ладно, {w} обращайся!"
    c_gg_say "-Ребят."
    c_artemida "-Угу?"
    c_askhatlina "-Шо?"
    c_gg_say "-Вы пойдете домой? {w} Или здесь будете сидеть?"
    c_artemida "-Нуу..."
    c_artemida "-Я домашкой позанимаюсь."
    c_askhatlina "-Давайте ребят, {w} я к Эллен."
    hide askhatlina_uniform
    with dissolve
    c_gg "Пожалуй, и мне пора."
    c_gg_say "-Я тоже пойду домой!"
    c_gg_say "-Всем пока!"
    c_danik "-Пис!"
    c_artemida "-До встречи!"
    stop sound_people
    scene loc_mega_route
    with Fade(1.0, 1.0, 1.0, color="#000")
    c_gg "..."
    c_gg "По пути домой, я начал задумываться, какая же у меня интересная жизнь."
    c_gg "И какие же интересные люди встретились мне."
    scene mm
    with Fade(1.0, 1.0, 1.0, color="#000")
    jump ending
    
label com2:   
    scene tr
    with Fade(1.0, 1.0, 1.0, color="#000")
    play afew "sound/s_afew.mp3"
    
    c_gg "По пути в университет..."
    stop afew
    play music "music/ava.mp3" fadein(0.1)
    scene loc_mega_route
    with Fade(1.0, 1.0, 1.0, color="#000")
    c_gg "Время 8:30..."
    c_gg "Как же приятно не опаздывать"
    scene loc_hall
    c_gg "..."
    c_gg "Пройдя через турникет, я заметил Артемиду с Асхатлиной..."
    show askhatlina_uniform at left
    with dissolve
    show artemida_uniform at right
    with dissolve

    c_gg "Они торопятся, но куда?! Они же ведь успевают на пару..."
    c_gg "Надо бы спросить..."
    c_gg_say "Хэй, утречка ребята"
    c_askhatlina "-Утречка."
    c_artemida "-Привет, привет."
    c_gg_say "-К чему такая спешка?"
    c_artemida "-А ты не знаешь?..."
    c_artemida "-На уроке ИКТ будет важное объявление."
    c_askhatlina "-Вот, и чтобы ничего не пропустить ничего, спешим."
    c_askhatlina "-Ладно, Ваня, мы побежали, ты давай..."
    c_askhatlina "-Не опаздывай"
    hide askhatlina_uniform
    with dissolve
    hide artemida_uniform
    with dissolve
    c_gg "И в ту же минуту их уже не было видно..."
    c_gg "Словно ветром сдуло."
    c_gg_say "Хмм, ну и ладно..."
    scene loc_cafeteria
    with Fade(1.0, 1.0, 1.0, color="#000")
    play sound_people "sound/manypeople.mp3"
    c_gg "Стоило мне оглянуться, как я тут же увидел знакомую фигуру"
    show danik_casual at center
    with dissolve
    c_gg "Подойдя, я узнал в нем своего одногруппника."
    c_gg "*Тык*"
    hide danik_casual
    show danik_casualSmile at center
    with dissolve
    c_danik "-Привет, Ваня, как ты?"
    c_gg_say "-Привет, вот по унику решил прогуляться перед парой..."
    c_gg_say "-Что у нас интересного здесь есть?"
    c_danik "-Не знаю..."
    c_danik "-Вот жду пока выпечку не выносят."
    c_danik "-Можешь пока идти на пару, я догоню."
    c_gg_say "-Хорошо."
    c_gg "И без всяких раздумий, я ринулся в путь..."
    hide danik_casualSmile
    with dissolve
    scene loc_corridor 
    with Fade(1.0, 1.0, 1.0, color="#000")
    show danik_casualFrowned at center
    with dissolve
    c_danik "-Блин..."
    c_danik "-Ничего из моих любимых пирожков не осталось."
    hide danik_casualFrowned 
    show danik_casual
    c_danik "-Ну ладно, айда на урок, не то опоздаем."
    c_gg_say "-Точно! Погнали."
    hide danik_casual
    with dissolve
    stop sound_people
    scene ict_cab
    with Fade(1.0, 1.0, 1.0, color="#000")
    c_gg "После того, как мы зашли в кабинет, тут же преподавательница посмотрела на нас..."
    show ict_teacher_casualSmile at center
    with dissolve
    c_ict_teacher "-Даник, Ваня, вы как раз во время!"
    c_ict_teacher "-Быстрей садитесь на свои места..."
    c_ict_teacher "-Ребята, сегодня мне пришло объявление с которым я хочу поделиться с вами."
    c_gg "Интересно..."
    c_ict_teacher "-На следующей неделе..."
    c_ict_teacher "-У вас начинаются файналы."
    c_ict_teacher "-Критерии таковы..."
    c_ict_teacher "-Работать в команде, не списывать, не копировать работы других студентов."
    c_ict_teacher "-На файнале вы должны будете..."
    c_ict_teacher "-Создать программу вместе с людьми в команде."
    c_ict_teacher "-Каждая из команд должна состоять не менее 3 участников."
    c_ict_teacher "-На этом у меня всё, а сегодняшние задачи я закрепила на платформе Moodle."
    c_ict_teacher "-Если возникнут вопросы, обращайтесь ко мне по Microsoft Teams."
    c_ict_teacher "-Можете быть свободны, всем хороших выходных!"
    hide ict_teacher_casualSmile
    with dissolve
    c_gg "Уроки окончены. Наконец, можно отправляться домой."
    c_gg "Не успел я выйти из класса, как Константин созвал всех на курултай."
    show konstantin_uniformSmile at center
    with dissolve
    show danik_casualSmile at left
    with dissolve
    show idris_uniformLaugh at right
    with dissolve
    c_konstantin "Ну шо народ, погнали на курултай?"
    hide konstantin_uniformSmile
    with dissolve
    hide danik_casualSmile at left
    with dissolve
    hide idris_uniformLaugh
    with dissolve
    c_gg "И все пошли за ним..."
    scene mega_route 
    with Fade(1.0, 1.0, 1.0, color="#000")
    show konstantin_uniformSmile at center
    with dissolve
    show danik_casualSmile at left
    with dissolve
    show idris_uniformLaugh at right
    with dissolve
    c_konstantin "Так, все в сборе, начинаем..."
    c_konstantin "WAKA WAKA E E"
    c_danik "WAKA WAKA WAKA"
    c_danik "Zan mina mina zan mina mina"
    c_idris "This time for Africa"
    hide konstantin_uniformSmile at center1
    hide danik_casualSmile at left1
    hide idris_uniformLaugh at right1
    scene tr 
    with Fade(1.0, 1.0, 1.0, color="#000")
    play afew "sound/s_afew.mp3"
    c_gg "..."
    scene mega_route
    with Fade(1.0, 1.0, 1.0, color="#000")
    show konstantin_uniformSmile at center
    with dissolve
    show danik_casualSmile at left
    with dissolve
    show idris_uniformLaugh at right
    with dissolve
    c_konstantin "Отлично, ребята, так держать!"
    c_danik "Фух, ну что, по домам?"
    c_idris "По домам!"
    c_gg "После этого, все отправились по своим домам..."
    c_gg "А я шёл и думал..."
    c_gg "Шёл и думал..."
    stop music fadeout(0.1)
    scene mm
    with Fade(1.0, 1.0, 1.0, color="#000")
    jump ending

label ending: 
    c_gg "Жизнь - интересная вещь..."
    c_gg "Вот учусь в самом лучшем университете, и удивляюсь, как человек должен быть столь везучим, чтобы попасть в университет такого уровня"
    c_gg "Где учатся, очень умные и одаренные ребята..."
    c_gg "То есть, мои одногруппники..."
    show askhatlina_casualLaugh at right
    with fade
    show artemida_casualLaugh at left
    with fade
    c_gg "Асхатлина и Артемида, дуо умных парней..."
    c_gg "Два гения, чьи мозги стремятся поглощать новые знания со скоростью света..."
    hide askhatlina_casualLaugh
    with fade
    hide artemida_casualLaugh
    with fade
    show konstantin_casualSmile at left
    with fade 
    show idris_casualLaugh at right
    with fade
    c_gg "Константин и Ыдрыс - вундеркинды нашей группы..."
    c_gg "В 4 классе изучили всю линейную алгебру, а ближе к 8 классу они знали дискретную математику наизусть, вот это умы!"
    hide konstantin_casualSmile 
    with fade 
    hide idris_casualLaugh 
    with fade
    c_gg "И последний..."
    c_gg "Наиумнейший..."
    show danik_casualSmile at center
    with fade
    c_gg "Даник..."
    c_gg "Имея Нобелевскую премию, он все равно, пытается скрывать могучую силу своего ума, чтобы сверстники не отставали от него"
    hide danik_casualSmile
    with dissolve 
    c_gg "Вот это да, чуток пофантазировал и сразу такое"
    c_gg "Человеческий мозг - вещь интересная..."
    c_gg "Где-то я это уже слышал..."
    scene loc_house
    with Fade(1.0, 1.0, 1.0, color="#000")
    c_gg_say "-Прошел очередной учебный день..."
    menu:
     c_gg_say "-Не помешало бы принять душ, затем отправиться спать" 
     "Принять душ":
            jump shower
     "Не принимать душ":
            jump notsh
    label shower: 
    scene loc_shower
    with Fade(1.0, 1.0, 1.0, color="#000")
    play ja_calendar "sound/s_shower.mp3"
    stop ja_calendar
    scene loc_house 
    with Fade(1.0, 1.0, 1.0, color="#000")
    c_gg_say "Отлично, можно погружаться в сон"
    jump mir
label notsh:
    c_gg "Пожалуй, я уж лучше обойдусь..."
    c_gg_say "Спокойных снов, мир!"
    jump mir
label mir:
    scene mm
    with Fade(1.0, 1.0, 1.0, color="#000")
    c_gg "Впереди файналы..."
    c_gg "Нужно быть готовым..."
    c_gg "А я готов спать"
    c_gg "To be continued..."
    play transition "sound/transition.mp3"
    scene tr_day2
    with Fade(0.5, 1.0, 3.0, color="#000")
    stop music fadeout(0.1)
    jump day2
return
