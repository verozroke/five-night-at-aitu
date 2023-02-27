label day4:
    
    scene wake_up
    with Fade(1.0, 1.0, 1.0, color="#000")
    
    play music "music/day4_music.mp3" fadein(0.1)
    
    c_gg '''
    Утро начинатеся ужасно.
    
    Я чуть не проспал, на улице дождь и слякоть. 
    
    Лишь мысли от мыслей о сессии меня начинает воротить, {w} но надо идти в универ...
    
    '''
    
    scene loc_hall
    with Fade(1.0, 1.0, 1.0, color="#000")
    
    c_gg "Сразу у входа в универ я встречаю Асхатлину, которая выглядела уставшей."
    c_gg "Она всю ночь писала свою часть новеллы, а теперь ей плохо."
    
    show askhatlina_uniform at center:
        yalign 1.0
    with dissolve
        
    c_askhatlina "-Чтож, сегодня наступил день защиты."
    c_askhatlina "-Надеюсь все пройдет хорошо."
    c_gg_say "-Я тоже..."
    
    hide askhatlina_uniform
    with dissolve
    
    scene loc_ict_cab
    with Fade(1.0, 1.0, 1.0, color="#000")
    
    c_gg "Мы оба пошли к кабинету ИКТ."
    c_gg "По пути к кабинету мы встретили Джихангуль и Артемиду, которые оказывается давно пришли."
    
    show artemida_uniformLaugh at center
    with dissolve
    c_artemida "-По хорошему надо бы написать речь, но когда это нас останавливало."
    
    hide artemida_uniformLaugh
    show artemida_uniformLaugh:
        xalign 0.8
        yalign 1.0
    with move
    
    show dzhikhangul_uniformLaugh:
        xalign 0.15
        yalign 1.0 
    with dissolve
    
    c_dzhikhangul "-Именно."
    
    show askhatlina_uniformLaugh at center
    with dissolve
    
    c_askhatlina "-Мы какими по счету защищаем?"
    c_artemida "-Вроде бы третьими."
    c_dzhikhangul "-У нас где-то минут 10."
    
    hide askhatlina_uniformLaugh
    with dissolve
    hide artemida_uniformLaugh
    with dissolve
    hide dzhikhangul_uniformLaugh
    with dissolve
    
    c_gg ''' 
    Пожалуй, эти 10 минут были самыми долгими в моей жизни.
    
    Сердце стучало с такой силой, что казалось что оно сейчас выскочит.
    
    Вдруг мы слышим голос нашей учительницы по ИКТ.
    
    '''
    
    c_ict_teacher "3 группа, ваша очередь."
    
    scene loc_nigger
    with Fade(1.0, 1.0, 1.0, color="#000")
    
    if preparing:
        jump good
    else:
        jump bad
        
label good:
    
    scene loc_ict_cab
    c_gg '''
    Чтож, у меня была 3 глава и вчера я успел ее закончить
    
    Надеюсь я смогу обьяснить свой код и сюжет...
    
    Начинает Асхатлина, затем Джихангуль, а потом я.
    
    Не успел я об этом подумать как Джихангуль говорит что наступила моя очередь.
    '''
    
    show dzhikhangul_uniformFrowned at center
    with dissolve
    
    c_dzhikhangul "-Иван, твоя очередь."

    
    stop music fadeout(0.1)
    play music "music/nervous_music.mp3" fadein(0.1)
    hide dzhikhangul_uniformFrowned
    with dissolve    
    
    c_gg "Наша учительница переходит на 3 главу и видит мой код."
    
    show ict_teacher_casual at center
    with dissolve
    
    c_ict_teacher "-Иван, можешь мне рассказать что ты сделал в моменте выбора действий?"
    
    c_gg_say "-Нуу, смотрите. {w} Тут у главного персонажа есть выбор, влияющий на дальнейшеее развитие..."
    
    c_gg "Обьяснял я свою часть минуты 3."
    
    hide ict_teacher_casual
    show ict_teacher_casualSmile
    
    c_gg "Вроде претензий у учительницы нету."
    
    c_ict_teacher "-Очень хорошо, Иван, теперь очередь Артемиды."
    
    hide ict_teacher_casualSmile
    with dissolve
    
    c_gg '''
    "Я уже не слушал что моя команда говорит."
    
    "В мыслях только было радость что я вчера решил все же подготовиться."
    
    "Мало ли что могло случиться..."
    
    "Спустя 10 минут и пару вопросов наша команда закончила."
    
    "Оценки мы узнаем завтра."
    '''
    
    scene loc_corridor
    with Fade(1.0, 1.0, 1.0, color="#000")
    
    stop music fadeout(0.1)
    play music "music/day3_music.mp3" fadein(0.1)
    
    c_gg "Мы все вышли в корридор"
    
    show askhatlina_uniformLaugh at center
    with dissolve
    
    c_askhatlina "-Отлично выступили, теперь можно быть спокойным."

    hide askhatlina_uniformLaugh
    show askhatlina_uniformLaugh:
        xalign 0.85
        yalign 1.0
    with move
    
    show artemida_uniformLaugh at center
    with dissolve
    
    c_artemida "-Да, первая сессия прошла неплохо."

    show dzhikhangul_uniformLaugh:
        xalign 0.15
        yalign 1.0
    with dissolve
    
    c_dzhikhangul "-Поцаны, я думаю мы сделали все идеально."
    
    c_gg_say "-Согласен, все прошло крайне гладко."
    
    c_artemida "-Ну что, давайте по домам?"
    
    c_askhatlina "-Го, я буду играть в осу!"
    
    c_dzhikhangul "-Давайте поцаны, до завтра!"
    
    c_gg_say "-До завтра!"
    
    hide dzhikhangul_uniformLaugh
    hide artemida_uniformLaugh
    hide askhatlina_uniformLaugh
    
    c_gg "Мы все пожали руки и разошлись."
    
    scene wake_up
    with Fade(1.0, 1.0, 1.0, color="#000")
    
    c_gg '''
    Вот так прошла моя первая сессия.
    Остается лишь дождаться завтрашнего дня и узнать нашу оценку.
    '''
    
    stop music fadeout(0.1)
    play transition "sound/transition.mp3"
    scene tr_day5
    with Fade(0.5, 1.0, 3.0, color="#000")
    jump day5
    
    return

label bad:
    scene loc_ict_cab
    with Fade(1.0, 1.0, 1.0, color="#000")

    show artemida_uniform at left
    show askhatlina_uniform at center
    show dzhikhangul_uniform at right
    with dissolve

    c_gg "Чтож, у меня была 3 глава и ее попросту нету."
    c_gg "Как я буду сейчас защищать свою часть..."

    c_gg "Начинает Асхатлина, затем Джихангуль, а потом я."
    c_gg "Не успел я об этом подумать как Джихангуль говорит что наступила моя очередь."
    stop music fadeout(0.1)
    play music "music/nervous_music.mp3" fadein(0.1)
    c_dzhikhangul "-Иван, твоя очередь."
    c_gg "Наша учительница переходит на 3 главу и видит ничего..."

    hide askhatlina_uniform
    with dissolve
    show ict_teacher_casualUpset
    with dissolve
    c_ict_teacher"-Иван, а где твоя часть?"
    c_askhatlina "-Ты не сделал???"
    c_gg "Выражение моей команды резко изменилось."
    hide dzhikhangul_uniform
    hide artemida_uniform
    show dzhikhangul_uniformFrowned at right
    show artemida_uniformFrowned at left
    c_gg_say "-Нууу, как вам сказать..."
    c_gg "Мои попытки хоть как-то оправдаться не увенчались успехом."

    c_ict_teacher"-Я все поняла, Иван. Можете даже ничего не говорить."
    c_ict_teacher "-Артемида, ваша очередь."

    c_gg "Я уже не слушал никого..."
    c_gg "В голове были мысли лишь о том что я не выполнил свою часть."
    c_gg "Что я мог подготовиться, но выбрал веселье..."
    c_gg "Почему же я не могу вернуться в прошлое и все исправить."
    c_gg "Как я буду теперь сдавать сессию..."

    c_gg "Буквально спустя 10 минут и пару вопросов наша команда закончила защиту."
    c_gg "Результаты мы узнаем завтра."

    scene loc_corridor
    with Fade(1.0, 1.0, 1.0, color="#000")

    show dzhikhangul_uniformFrowned at right
    show artemida_uniformFrowned at left
    show  askhatlina_uniformFrowned at center
    with dissolve
    
    stop music fadeout(0.1)
    play music "music/day3_music.mp3" fadein(0.1)

    c_gg "Мы вышли в коридор и вся команда смотрела на меня с недовольством."
    c_askhatlina "-Как это понимать, Иван?"
    c_dzhikhangul "-Неужели нельзя было написать свою часть?"
    c_artemida "-Мы в тебе разочарованы..."

    scene loc_nigger
    with Fade(1.0, 1.0, 1.0, color="#000")
    c_gg "Я решил не отвечая на их вопросы и даже не попрощавшись пойти домой."
    c_gg "Настроение с кем-либо говорить просто не было."
    c_gg "Это был самый худший мой день в жизни..."
    c_gg "И хуже он становится от мысли, что я мог это исправить вчера."
    stop music fadeout(0.1)
    play transition "sound/transition.mp3"
    scene tr_day5
    with Fade(0.5, 1.0, 3.0, color="#000")

    
    jump day5
    
    return