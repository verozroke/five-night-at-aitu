
label day3:

  define preparing = False
  define capy = False

  play music "music/day3_music.mp3" fadein(0.1)

  scene  loc_mega_route
  with Fade(1.0, 1.0, 1.0, color="#000")

  c_gg "Наконец-то наступил долгожданный выходной."
  c_gg  "Последний день перед сессиями..."
  c_gg  "Сегодня я решил начать свое утро с прогулки вокруг экспо."
  c_gg "Мне это помогало отвлечься от проблем."

  show danik_casual at center
  with dissolve

  c_danik "-О, привет!"
  c_gg "Я немного удивленный появлению Даника поздоровался с ним в ответ"

  c_danik "-Кстати, ты сегодня свободен?"
  menu:
      "Да, а что?":
        jump chilling

      "Нет, прости, буду готовиться к сессиям.":
        jump preparing



label preparing:

  with dissolve
  hide danik_casual
  show danik_casualFrowned at center
  c_danik "-Ну ладно, тогда до встречи!"
  hide danik_casualFrowned
  c_gg "Мы попрощались и разошлись."
  with dissolve

  c_gg "Я решил пойти в OC чтобы закончить визуальную новеллу."
  play sound_people "sound/manypeople.mp3"
  scene loc_open_space
  with Fade(1.0, 1.0, 1.0, color="#000")

  show askhatlina_casualLaugh at left
  show ellen_uniformLaugh at right
  with dissolve

  c_gg "Неожиданно здесь я вижу радостного Асхата и его девушку."
  c_gg_say "-Привет, голубки!"

  hide askhatlina_casualLaugh
  hide ellen_uniformLaugh
  show askhatlina_casual at left
  show ellen_uniform at right
  c_gg "Их выражение лица резко изменилось."

  c_askhatlina "-Здарова!"
  c_ellen "-Привет!"

  c_gg_say "-А как сюда попала Эллен?"
  c_askhatlina "-Она спряталась в ланч боксе."
  c_ellen "-Там было очень тесно."

  c_gg "Вопросов стало только больше..."

  with dissolve
  hide askhatlina_casual
  hide ellen_uniform
  with dissolve

  c_gg "Асхатлина и Эллен ушли в другой кабинет."

  c_gg "Я нашел свободное место и начал писать код и сюжет для нашей новеллы."
  c_gg "Прошло 5 часов.."
  c_gg "Менюшка сделана, 3 день сделан, осталось совсем немного."
  $ preparing = True

  stop sound_people fadeout(0.1)
  scene loc_corridor
  with Fade(1.0, 1.0, 1.0, color="#000")

  c_gg "Подходя к выходу я вижу грустного Даника."
  c_gg "Я решил подойти к нему и узнать что случилось"

  show danik_casualFrowned at center
  with dissolve

  c_danik "-Я ничего не успеваю..."
  c_gg "-Он много раз повторял эту фразу пока не заметил меня"
  c_danik "-О, ты еще тут! Можешь помочь с дискреткой с дз,
  у меня ничего не получается"
  menu:
      "Помочь ему":
          c_gg "Ты потратил час времени на это, однако Даник все же смог все сдать"
          c_danik "-Спасибо тебе, ты меня спас!"
          $ capy = True
      "Отказать в помощи":
          c_gg_say"-Прости, мне надо идти уже"
          c_danik "-Ладно, давай"



  hide danik_casualFrowned
  with dissolve
  scene loc_mega_route
  with Fade(1.0, 1.0, 1.0, color="#000")

  c_gg "Я вышел, на улицу и увидел Джихангуль, Константина и Даника."
  c_gg "Они были чем-то расстроены."
  c_gg "Я подошел к ним и решил узнать что случилось."

  show danik_casualFrowned at left
  show konstantin_uniformFrowned at center
  show idris_casualFrowned at right
  with dissolve
  c_gg_say "-Привет всем, что случилось?"
  c_dzhikhangul "-Да вот, волнуемся на счет завтрашней сессии."
  c_danik "-Тем более мы еще не закончили..."
  c_konstantin "-Удача нас спасет..."
  c_danik "-Зато мы хорошо провели этот день."
  c_gg "-Конечно, сегодняшний день был довольно скучным,
  однако спать я буду со спокойной душой."
  c_gg "Я попращался с поцанами и пошел домой."

  hide danik_casualFrowned at left
  hide konstantin_uniformFrowned at center
  hide idris_casualFrowned at right
  with dissolve

  stop music fadeout(0.1)

  jump day4


label chilling:

  c_danik "-Хочешь с нами пойти в столовку а потом погулять?"

  menu:
      "Пошли, я не против":
        c_danik "-Тогда давай быстрей, пока людей в столовке немного"

      "Не, что-то желания нет":
        jump preparing

  hide danik_casual at center
  with dissolve
  scene loc_cafeteria
  with Fade(1.0, 1.0, 1.0, color="#000")

  play manyclap "sound/manyclaps.mp3" fadein (0.1)
  c_gg "Не успели мы войти, как уже слышим гул от хлопков"
  show  dzhikhangul_uniformFrowned at left
  with dissolve
  c_dzhikhangul "-О нет, сейчас это опять произойдет"
  stop manyclap fadeout(0.1)
  play oneclap "sound/clap_echo.mp3" fadein(0.1)
  show  konstantin_casualFrowned at right
  with dissolve
  c_gg "Константин снова решил похлопать за компанию"

  c_dzhikhangul "-ХВАТИТ!!!"
  hide konstantin_casualFrowned
  show konstantin_casual at right
  c_konstantin "-Ладно..."
  stop oneclap fadeout(0.1)
  show danik_casualSmile at center
  with dissolve
  c_danik "-Хоть бы здесь что-то новое произошло."
  c_danik "-Давайте быстрее садиться за стол."

  c_gg "Мы сели все за стол и начали разговаривать на разные темы"
  c_dzhikhangul "-Гайс, вы готовы к завтрашнему дню?"
  c_danik "-У меня сайт еще не готов, но думаю все будет нормально"
  c_konstantin  "-И я тоже."
  c_gg "Воодушевившись их надеждой я тоже понадеялся что
  мы тоже сможем все сделать за пару часов"
  c_gg "После 30 минут обеда и разговоров о всякей чепухе мы отправились снова на улицу."

  scene loc_mega_route
  with Fade(1.0, 1.0, 1.0, color="#000")

  show danik_casualSmile at left
  show dzhikhangul_casual at center
  show konstantin_uniformSmile at right
  with dissolve

  c_gg "На улице было тепло несмотря на то что был октябрь"
  c_gg "Отличная возможность чтобы погулять на улице"

  show konstantin_uniformSmile at right
  with dissolve
  c_konstantin "-Предлагаю пойти на курултай"

  show dzhikhangul_casual at center
  with dissolve
  c_dzhikhangul "-Давайте"

  show danik_casualSmile at left
  with dissolve
  c_danik "-ООО, погнали"

  c_gg "Неожиданно Константин решил рассказать свою грустную историю"
  hide konstantin_uniformSmile
  show konstantin_uniformFrowned at right

  c_gg "Исторю о том, почему он постоянно хлопает."
  c_konstantin "-Это случилось 5 лет назад."
  c_konstantin "-На школьной линейке произошел ужасный случай..."
  c_konstantin "-После душевной речи директора никто из учеников решил не хлопать"
  c_konstantin "-Что расстроило его самого."
  c_konstantin "-Чтобы его развеселить, я решил похлопать."
  c_konstantin "-С такой силой чтобы казалось что хлопает целай толпа."
  c_konstantin "-Директор посмотрел на меня, и начал плакать..."
  c_konstantin "-А я продолжал хлопать."
  c_konstantin "-До того момента пока меня не остановила учительница."
  c_konstantin "-После этого момента я всегда поддерживаю
  любые случаи когда надо похлопать."

  hide danik_casualSmile
  show danik_casualFrowned at left
  c_danik "-Это очень печальная история..."
  c_gg "Даника задела данная история"

  c_gg "Джихангуль решила перевести тему"
  c_dzhikhangul "-А вы знаете что на следующей неделе придет стипендия?"
  hide danik_casualFrowned
  show danik_casualSmile at left
  hide konstantin_uniformFrowned
  show konstantin_uniformSmile at right

  c_gg "У всех сразу поднялось настроение"
  c_danik "-УРААА, можно снова кушать в столовой!"
  c_konstantin "-ДААА!"
  c_gg "Все очень ждут этого момента"
  c_dzhikhangul "-Надо спросить у старосты так ли это"

  c_gg "Неожиданно появляетсся Ыдырыс"
  hide  dzhikhangul_casual
  show idris_casual at center
  with dissolve
  c_gg "Мы дружно поздоровались с ним"
  c_konstantin "-Ыдырыс, ты знаешь когда стипендия?"
  c_idris "-Должна быть на следующей неделе, но..."
  c_danik "-Но?"
  c_idris "-Но если мы не сдадим хорошо сессии, то это будет последняя."

  hide idris_casual
  hide konstantin_uniformSmile
  hide danik_casualSmile
  show danik_casualFrowned at left
  show konstantin_uniformFrowned at right
  show idris_casualFrowned at center

  c_gg "Все снова вспомнили о сессии, которая будет завтра."
  c_gg "Настроение всех снова упало..."
  c_gg "Никто не заметил как уже начало вечереть."
  c_gg "Было решено расходиться, чтобы выспаться перед днем X."

  c_dzhikhangul "-Хорошо погуляли, поцаны."
  c_konstantin "-Согласен."
  c_danik "-Да, но пора идти."
  c_danik "-До завтра всем!"
  c_konstantin "-Давай!"
  c_dzhikhangul "-Надеюсь все сдадим."
  hide danik_casualFrowned
  with dissolve
  hide konstantin_uniformFrowned
  with dissolve
  hide idris_casualFrowned
  with dissolve
  
  
  
  c_gg "Мы пожали руки друг другу и пошли по домам"
  
  scene loc_wake_up
  with Fade(1.0, 1.0, 1.0, color="#000")    
  c_gg "День прошел крайне весело, но..."
  c_gg "К сессии я так и не успел закончить свой проект"
  c_gg "Остается надеется завтра лишь на свою удачу."

  stop music fadeout(0.1)
  play transition "sound/transition.mp3"
  scene tr_day4
  with Fade(0.5, 1.0, 3.0, color="#000")
  
  jump day4