define background = Character(None, kind=nvl)
define UrikMali = Character('Урик Мали', color="#4ed200")
define Irina = Character('Ирина', color="#e500ff")
define Alexandr = Character('Александр', color="#d5ff00")
define Sergei = Character('Сергей', color="#f5a656")

label start:
    scene bg kabgg
    window hide
    background '''АКТ 1 - ПОИСК РАБОТЫ(Будет дополнено)'''
    nvl hide
    nvl clear

    background '''Акт 2 "Собеседование" '''
    nvl hide
    nvl clear

    scene bg stolperegovorov

    show character right
    Irina " Здравствуйте, Александр. Рада вас видеть. Добро пожаловать на собеседование. Давайте начнём с обсуждения условий работы у нас в компании."

    show character left
    Alexandr "Здравствуйте, Ирина. Спасибо за приглашение. Какие условия у вас в компании?"

    show character right
    Irina "Прежде всего, основным условием устройства на работу является успешное прохождение 3-х дневной стажировки у нас в компании. По окончанию стажировки вас ожидает экзамен. Если вы его успешно сдадите, то станете частью нашей команды."

    show character left
    Alexandr "Хорошо. Какие задачи ожидают меня на стажировке?"

    show character right
    Irina "Задачи будут разнообразными, для вас будет назначен наставник, который будет следить за вашими успехами и направлять вас во время работы. Ваш наставник - главный системный администратор Сергей."

    show character left
    Alexandr "Спасибо за информацию, Ирина. Я готов начать стажировку и сделать все возможное, чтобы присоединиться к вашей команде."

    show character right
    Irina "Замечательно, Александр. Мы ждем вас завтра. Если у вас есть еще какие-либо вопросы касающиеся прохождения стажировки, не стесняйтесь задавать их Сергею, вашему наставнику."


    scene bg kabmon
    window hide
    background '''Акт 3 "Стажировка"'''
    nvl hide
    nvl clear

    background '''Первый день стажировки'''
    nvl hide
    nvl clear

    show character right
    UrikMali "Доброе утро, Александр. Рад видеть тебя на стажировке. Давай поговорим в моем кабинете перед началом рабочего дня."

    show character left
    Alexandr "Здравствуйте, мистер Мали."
    hide character left

    scene bg kaburimali
    with fade
    "Александр заходит в кабинет Урика Мали"

    show character right
    UrikMali "Прошу, садись. Готов к прохождению первого дня стажировки?"

    show character left
    Alexandr "Да, уже не терпится"

    show character right
    UrikMali "Отлично. На стажировке ты будешь изучать различные аспекты нашей работы."
    UrikMali "Теперь давай пойдем к Сергею, нашему главному системному администратору. Он даст тебе первое поручение."
    hide character right

    scene bg kabmon
    with fade
    "Урик Мали проводит Александра к Сергею."

    show character right
    UrikMali "Сергей, это Александр, наш новый стажер. Александр, это Сергей, твой наставник."
    hide character right

    "Урик Мали уходит"

    show character right
    Sergei "Здравствуй, Саня. Рад тебя видеть. Давай начнем с чего-то интересного. У меня есть для тебя задача, которую ты сможешь решить."

    show character left
    Alexandr "Здравствуй, Сергей. Я готов к работе. Что нужно делать?"

    show character right
    Sergei "Отлично. Давай сначала поговорим о том, что мы сегодня будем делать, а поcле приступим к работе."

    Sergei "Хорошо, первое задание для тебя. У нас сегодня ожидается поставка комплектующих ПК и периферии для обустройства новых рабочих мест. Мы должны принять и отсортировать все компоненты."

    Sergei "Вот список компонентов, которые должны быть в поставке. Твоя задача - проверить, что все компоненты присутствуют и отсортировать каждый компонент в коробку. "
    hide character right

    "Сергей передает Александру список компонентов и документацию."

    show character left
    Alexandr "Хорошо, поставка будет на складе?"

    show character right
    Sergei "Верно. Я тебя провожу."
    hide character right

    scene bg sklad
    with fade

    "Александр с Сергеем направляются на склад для приема поставки. Александр аккуратно разгружает компоненты и начинает их сортировку."

    show character right
    Sergei "Хорошая работа, Саня. Если у тебя возникнут какие-либо вопросы, не стесняйся обращаться ко мне."
    hide character right

    scene bg kabmon
    with fade

    "После того как Саня закончил проверку компонентов, он с Сергеем направился обратно в офис компании Rinus Corp."

    show character right
    Sergei "Так держать. Я пойду покурить, а ты остаешься за старшего."

    show character left
    Alexandr "Хорошо, Сергей"
    hide character left

    "6 МИНУТ СПУСТЯ"

    show character right
    Irina "Александр, я не могу залогиниться в мой рабочий компьютер. Что-то не так с моей учетной записью."

    show character left
    Alexandr "Вам высвечивается ошибка что введен неправильный пароль? "

    show character right
    Irina "Да, недавно мне переустановили операционную систему из-за вирусов. Сергей где-то оставил записку с паролем, но я ее потеряла."

    show character left
    Alexandr "Не волнуйтесь, Ирина. Я уверен, мы найдем решение. Где находится ваш рабочий компьютер?"

    show character right
    Irina "Пройдёмте за мной."
    hide character right

    scene bg kabsisadmin
    with fade

    "Александр и Ирина отправляются в кабинет, где она работала"

    "Александр сразу начал осматривать рабочий стол на наличие записки с паролем."

    show character left
    Alexandr "Да где же она может быть?"
    hide character left

    "Александр поднял папки которые лежали на столе и увидел там маленький клочек бумаги."

    "Он его взял в руки и развернув увидел что это и есть записка с паролем"

    show character left
    Alexandr "Вот же она!"

    show character right
    Irina "Как же я не подумала что она может быть под документами?"

    show character right
    Irina "Спасибо, Александр!"

    show character left
    Alexandr "Нет проблем. Если у вас возникнут еще какие-либо трудности, то обязательно обращайтесь."
    hide character left

    scene bg kabmon
    with fade

    "6 МИНУТ СПУСТЯ"

    show character right
    Sergei "(Возвращаясь из перерыва) Что происходило во время моего отсутствия?"

    show character left
    Alexandr "Ирина из отдела кадров потеряла вашу записку с паролем от операционной системы и попросила ей помочь. В итоге бумажка с паролем лежала на столе под документами."

    show character right
    Sergei "И такое тоже бывает. Ты молодец Саня!"
    hide character right

    scene bg kabgg
    with fade

    window hide
    background '''Второй день стажировки"'''
    nvl hide
    nvl clear

    return
