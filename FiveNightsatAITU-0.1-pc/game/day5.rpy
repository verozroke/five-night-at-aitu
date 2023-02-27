label day5:
    play music "music/day5_music.ogx" fadein(0.1)
    scene moodle_ict
    with Fade(1.0, 1.0, 1.0, color="#000")
    
    c_gg '''
    Чтож, настал день, когда я узнаю свою оценку.
    
    Надо лишь открыть мудл и посмотреть результат.
    
    Но почему-то руки трясутся и крайне сложно сделать эти 2 клика.
    
    Однако я собрал всю волю в кулак и все же решился.
    
    И увидел я там...
    
    '''

    if preparing:
        jump day5_goodEnding
    else:
        jump day5_badEnding
    
    
label day5_badEnding:
    scene grade_bad
    with Fade(1.0, 1.0, 1.0, color="#000")

    stop music fadeout(0.1)
    play music "music/sad_music.mp3" fadein(0.1)


    c_gg "Ноль. Просто ноль, без каких-либо комментариев."
    c_gg "Настроение стало ужасным, хуже не могло бы и быть."
    c_gg "Понимание того, что я лишился стипендии меня дизморалило."
    c_gg " Да что уж говорить, возможно я уже не айтушник..."
    c_gg "Но надо все равно идти в универ, я обещал придти."

    scene loc_mega_route
    with Fade(1.0, 1.0, 1.0, color="#000")

    c_gg "Подходя к универу я вижу Джихангуль, Константина и Ыдырыса."
    c_gg "Чего я не мог бы сказать о себе..."

    show dzhikhangul_casualLaugh at left
    show konstantin_casualSmile at center
    show idris_casualLaugh at right
    with dissolve

    c_idris "-Иван, иди к нам!"
    "Я неспеша подошел к ним с опущенной головой."

    c_konstantin "-Что-то случилось?"
    c_dzhikhangul "-Ты выглядишь очень грустный."
    c_gg_say "-Да вот, я получил ноль за файнал по ИКТ."
    c_gg_say "-Теперь не знаю что делать."
    hide dzhikhangul_casualLaugh 
    hide konstantin_casualSmile 
    hide idris_casualLaugh 
    show dzhikhangul_casualFrowned at left
    show konstantin_casualFrowned at center
    show idris_casualFrowned at right
    c_gg "Поцаны тоже расстроились."
    c_dzhikhangul "Неужели так сложно было все сделать?"
    c_gg_say "-Нет, просто я решил отдохнуть вместо этого..."
    c_konstantin "Мда, неповезло тебе."
    c_konstantin "-Может тебе стоит подойти к ней и узнать можно ли как-то это решить."
    c_idris "-Хорошая идея!"
    c_dzhikhangul "-Я бы так и сделал на твоем месте"
    c_gg_say "-Действительно, я тогда так и сделаю."
    c_gg_say "-Тогда я пошел к ней."
    c_gg "Даник, Ыдырыс и Джихангуль пожелали мне удачи."


    scene loc_ict_cab
    with Fade(1.0, 1.0, 1.0, color="#000")

    c_gg "Я пошел в кабинет нашей учительницы по ИКТ."
    c_gg "Постучавшись в дверь, я медленно подошел к ней."

    show ict_teacher_casual
    with dissolve
    c_gg_say "-З...здравствуйте, а м...можно как-то исправить оценку по файналу?"
    c_ict_teacher "-Здравствуй, к сожалению, нет. Ты уже попал на пересдачу, а именно на летник по моему предмету."
    c_gg "Я думал что хуже уже не будет."
    c_gg "Как же я ошибался..."
    c_gg "Попрощавшись с ней я грустно пошел домой."

    scene loc_wake_up
    with Fade(1.0, 1.0, 1.0, color="#000")

    c_gg "Пожалуй, хуже дня в моей жизни не могло быть."
    c_gg "И все из-за моей лени."
    c_gg "А ведь 2 дня назад казалось, что погулять с одногруппниками вместо проекта была хорошей идеей."
    c_gg "Как же я ошибался на это счет."
    c_gg "И больше всего обидно что этого можно было избежать..."
    c_gg "Жаль что нельзя вернуться назад во времени и все исправить."

    stop music fadeout(0.1)
    return
    
label day5_goodEnding:
    scene grade_good
    c_gg '''
    100!!!

    "Я даже и не мог поверить своим глазам этому."

    "Неожиданно весь страх и плохое настроение исчезло и осталось только лишь спокойствие и счастье."

    "На такое хорошей ноте я быстро оделся и отправился в университет."
    '''
    
    scene loc_mega_route
    with Fade(1.0, 1.0, 1.0, color="#000")
    
    c_gg '''
    Подходя к универу я вижу Джихангуль, Константина и Ыдырыса.
    
    Они стояли на курултаи и были как всегда счастливыми.
    
    Видимо они тоже хорошо сдали сессию.
    '''
    c_idris "-Иван, иди к нам!"
    c_gg "Я довольный подхожу к ним."
    
    show dzhikhangul_casualLaugh at left:
        yalign 1.0
    with dissolve
    show idris_casualLaugh at center
    with dissolve
    show konstantin_casualSmile at right
    with dissolve
    
    c_konstantin "-Что-то случилось?"
    c_dzhikhangul "-Ты сегодня прямо сияешь."
    c_gg_say '''
    -Да вот, я получил 100 за файнал по ИКТ.
    
    -Я был в шоке когда узнал это.
    '''
    c_gg "Поцаны порадовались за меня."
    c_dzhikhangul "-Ты действительно хорошо постарался."
    c_gg_say "-Да, более 5 часов потратил на это."
    c_konstantin "-Ого, молодец!"
    c_konstantin "Куда пойдешь теперь?"
    c_idris "Наверное идет рассказать Асхатлине и Данику об этом."
    c_dzhikhangul "Я тоже так думаю."
    c_gg_say "-Да, вы меня раскусили"
    c_gg_say "-Ну все, я пойду."
    
    hide dzhikhangul_casualLaugh
    with dissolve
    hide idris_casualLaugh
    with dissolve
    hide konstantin_casualSmile
    with dissolve
    
    c_gg "Константин, Ыдырыс и Джихангуль пожелали мне удачи."
    if capy:
        jump day5_goodEndingCapy
    else:
        scene loc_cafeteria 
        with Fade(1.0, 1.0, 1.0, color="#000")
        play music "music/day5_music.ogx" fadein(0.1)
        
        c_gg '''
        Я пошел в столовую чтобы найти Асхатлину
        
        Бинго! Она оказалась тут.
        
        Асхатлина сидела за столом и вкушала свой обед из ланчбокса.
        
        Рядом с ним сидел грустный Даник.
        
        Я подошел к ним.
        '''
        
        show askhatlina_uniformLaugh at left
        with dissolve
        show danik_casualFrowned at right
        with dissolve
        
        c_gg_say "-Привет Асхат и Даник!"
        c_askhatlina "-Дарова!"
        c_danik "-П...привет."
        
        c_gg_say "-Что случилось у тебя?"
        
        c_danik "-Я получил ретейк по дискретке из-за ДЗ..."
        c_gg "Неожиданно я вспомнил момент когда он просил меня помочь с этим."
        c_gg "Я почувствовал вину за это, но не сказал ему."
        c_gg_say "-Понятно..."
        c_gg_say "-Сколько вы получили за ИКТ?"
        c_askhatlina "-100, я крайне доволен результатом."
        c_danik "-85."
        c_gg_say "-Тоже неплохо."
        c_danik "Но меня больше волнует дискретка..."
        c_gg_say "-Мда, сочувствую тебе."
        
        c_gg "Я пожелал им удачи и пошел домой."
        
        scene wake_up
        with Fade(1.0, 1.0, 1.0, color="#000")
        
        c_gg '''
        День прошел неплохо, но, конечно, жалко Даника.
        
        Наверное он бы смог сдать, если я помог ему 2 дня назад.
        
        Но что сделано, то сделано.
        
        Главное что хорошо сдал ИКТ.
        
        Теперь можно отдыхать со спокойной душой.
        '''
        return


label day5_goodEndingCapy:
    scene loc_cafeteria 
    with Fade(1.0, 1.0, 1.0, color="#000")
    play music "music/day5_music.ogx" fadein(0.1)
    
    c_gg "Асхат сидел за столом и вкушал свой обед из ланчбокса."
    c_gg "Рядом с ним сидела веселая капибара."
    c_gg "Я подошел к ним."
    
    
    show askhatlina_uniformLaugh at left
    with dissolve
    show capySmile at right
    with dissolve
    c_gg_say "-Привет Асхат и капибара!"
    
    c_askhatlina "-Дарова!"
    c_capy "-Ok I pull up."
    
    c_gg_say "-Асхат, почему рядом с тобой сидит капибара?"
    c_capy "-Это я {w}, Даник, {w} я превратился в капибару."
    c_capy "Потому что я сдал дискретку благодаря тебе."
    
    c_gg_say "-А почему же ты превратился в капибару?"
    
    c_capy "Когда я очень радуюсь, то я превращаюсь в капибару. {w}Это у меня с самого детства."
    c_gg "Я очень обрадовался за него, ведь смог помочь ему."
    c_gg "Однако странно, что он превращается в капибару."
    c_gg "Но да ладно, это выглядит очень смешно."
    
    c_gg_say "-Понял, рад за тебя?"
    c_gg_say "-Сколько вы получили за ИКТ?"
    
    c_askhatlina "-100 {w}, я крайне доволен результатом."
    c_capy "-85."
    
    c_gg_say "-Молодцы!"
    
    c_capy "Но радует меня больше дискретка и ее успешное закрытие."
    c_capy "Наконец-то можем отдыхать с вами."
    
    c_askhatlina "-ДА!"
    c_capy "-УРА!"
    
    c_gg_say "-Ну ладно, я пойду уже."
    
    c_askhatlina "-Давай."
    hide askhatlina_uniformLaugh
    hide capySmile
    show capyFrowned:
        xalign 0.5
        yalign 0.5
    stop music fadeout(0.1)
    play music "music/napryazhenia.mp3" fadein(0.1)
    c_capy  "-Подожди!"
    c_gg_say "-Что?"
    c_capy "-Я ведь не один такой..."
    c_gg_say "-Так... в каком плане? Какой?"
    c_capy "-Ну такой."
    c_gg_say "-Я тебя не понимаю."
    c_capy "-Ладно, давай я просто их позову. {w} Поздоровайся с ними."
    c_gg_say "-Чт..."
    hide capyFrowned
    
    show capySmile5_2:
        xalign 0.1
        yalign 0.0
    with dissolve
    show capySmile5_3:
        xalign 0.2
        yalign 0.0
    with dissolve
    show capySmile5_4:
        xalign 0.3
        yalign 0.0
    with dissolve
    show capySmile5_5:
        xalign 0.4
        yalign 0.0
    with dissolve
    show capySmile5_6:
        xalign 0.5
        yalign 0.0
    with dissolve
    show capySmile5_7:
        xalign 0.6
        yalign 0.0
    with dissolve
    show capySmile5_8:
        xalign 0.7
        yalign 0.0
    with dissolve
    show capySmile5_9:
        xalign 0.8
        yalign 0.0
    with dissolve
    show capySmile5_10:
        xalign 0.9
        yalign 0.0
    with dissolve
    
    show capySmile4_2:
        xalign 0.1
        yalign 0.3
    with dissolve
    show capySmile4_3:
        xalign 0.2
        yalign 0.3
    with dissolve
    show capySmile4_4:
        xalign 0.3
        yalign 0.3
    with dissolve
    show capySmile4_5:
        xalign 0.4
        yalign 0.3
    with dissolve
    show capySmile4_6:
        xalign 0.5
        yalign 0.3
    with dissolve
    show capySmile4_7:
        xalign 0.6
        yalign 0.3
    with dissolve
    show capySmile4_8:
        xalign 0.7
        yalign 0.3
    with dissolve
    show capySmile4_9:
        xalign 0.8
        yalign 0.3
    with dissolve
    show capySmile4_10:
        xalign 0.9
        yalign 0.3
    with dissolve
    
    show capySmile3_2:
        xalign 0.1
        yalign 0.5
    with dissolve
    show capySmile3_3:
        xalign 0.2
        yalign 0.5
    with dissolve
    show capySmile3_4:
        xalign 0.3
        yalign 0.5
    with dissolve
    show capySmile3_5:
        xalign 0.4
        yalign 0.5
    with dissolve
    show capySmile3_6:
        xalign 0.5
        yalign 0.5
    with dissolve
    show capySmile3_7:
        xalign 0.6
        yalign 0.5
    with dissolve
    show capySmile3_8:
        xalign 0.7
        yalign 0.5
    with dissolve
    show capySmile3_9:
        xalign 0.8
        yalign 0.5
    with dissolve
    show capySmile3_10:
        xalign 0.9
        yalign 0.5
    with dissolve
    
    show capySmile2_2:
        xalign 0.1
        yalign 0.7
    with dissolve
    show capySmile2_3:
        xalign 0.2
        yalign 0.7
    with dissolve
    show capySmile2_4:
        xalign 0.3
        yalign 0.7
    with dissolve
    show capySmile2_5:
        xalign 0.4
        yalign 0.7
    with dissolve
    show capySmile2_6:
        xalign 0.5
        yalign 0.7
    with dissolve
    show capySmile2_7:
        xalign 0.6
        yalign 0.7
    with dissolve
    show capySmile2_8:
        xalign 0.7
        yalign 0.7
    with dissolve
    show capySmile2_9:
        xalign 0.8
        yalign 0.7
    with dissolve
    show capySmile2_10:
        xalign 0.9
        yalign 0.7
    with dissolve
    
    show capySmile2:
        xalign 0.1
        yalign 1.0
    with dissolve
    show capySmile3:
        xalign 0.2
        yalign 1.0
    with dissolve
    show capySmile4:
        xalign 0.3
        yalign 1.0
    with dissolve
    show capySmile5:
        xalign 0.4
        yalign 1.0
    with dissolve
    show capySmile6:
        xalign 0.5
        yalign 1.0
    with dissolve
    show capySmile7:
        xalign 0.6
        yalign 1.0
    with dissolve
    show capySmile8:
        xalign 0.7
        yalign 1.0
    with dissolve
    show capySmile9:
        xalign 0.8
        yalign 1.0
    with dissolve
    show capySmile10:
        xalign 0.9
        yalign 1.0
    with dissolve
    
    
    
    c_gg_say "ИЗВИНИТЕ Я НИ В ЧЕМ НЕ ВИНОВАТ, ЭТО БЫЛ РУСЛАН ЭТО БЫЛ РУСЛАН."
    c_capys "Жан, ты что? {w} Ты что сбрить меня решил?"
    stop music fadeout(0.1)
    c_capys "Мы ведь просто хотим потусить!!!"
    show discoshar
    with moveinbottom
    $ renpy.movie_cutscene("sound/dance.webm")

    c_gg "Концовка с капибарой"
    return