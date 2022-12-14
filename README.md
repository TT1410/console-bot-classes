# console-bot
 **Консольний бот**


<div class="theme-doc-markdown markdown"><header><h1>Домашнее задание</h1></header><hr><h2 class="anchor anchorWithHideOnScrollNavbar_R0VQ" id="задача">Задача<a class="hash-link" href="#задача" title="Прямая ссылка на этот заголовок">​</a></h2><p>В этой домашней работе мы продолжим развивать нашего виртуального ассистента с
CLI интерфейсом.</p><p>Наш ассистент уже умеет взаимодействовать с пользователем посредством командной
строки, получая команды и аргументы и выполняя нужные действия. В этом задании
нужно будет поработать над внутренней логикой ассистента, над тем, как хранятся
данные, какие именно данные и что с ними можно сделать.</p><p>Применим для этих целей объектно-ориентированное программирование. Для начала
выделим несколько сущностей (моделей) с которыми будем работать.</p><p>У <strong>пользователя</strong> будет адресная книга или <strong>книга контактов</strong>. Эта <strong>книга
контактов</strong> содержит <strong>записи</strong>. Каждая <strong>запись</strong> содержит некоторый набор
<strong>полей</strong>.</p><p>Таким образом мы описали сущности (классы), которые необходимо реализовать.
Далее рассмотрим требования к этим классам и установим их взаимосвязь, правила,
по которым они будут взаимодействовать.</p><p>Пользователь взаимодействует с <strong>книгой контактов</strong>, добавляя, удаляя и
редактируя <strong>записи</strong>. Также пользователь должен иметь возможность искать в
<strong>книге контактов</strong> <strong>записи</strong> по одному или нескольким критериям (полям).</p><p>Про <strong>поля</strong> также можно сказать, что они могут быть обязательными (имя) и
необязательными (телефон или email например). Также <strong>записи</strong> могут содержать
несколько <strong>полей</strong> одного типа (несколько телефонов например). Пользователь
должен иметь возможность добавлять/удалять/редактировать <strong>поля</strong> в любой
записи.</p><p>В этой домашней работе вы должны реализовать такие классы:</p><ul><li>Класс <code>AddressBook</code>, который наследуется от <code>UserDict</code>, и мы потом добавим
логику поиска по записям в этот класс.</li><li>Класс <code>Record</code>, который отвечает за логику добавления/удаления/редактирования
необязательных полей и хранения обязательного поля <code>Name</code>.</li><li>Класс <code>Field</code>, который будет родительским для всех полей, в нем потом
реализуем логику общую для всех полей.</li><li>Класс <code>Name</code>, обязательное поле с именем.</li><li>Класс <code>Phone</code>, необязательное поле с телефоном и таких одна запись (<code>Record</code>)
может содержать несколько.</li></ul><h1>Критерии приёма</h1><ul><li>Реализованы все классы из задания.</li><li>Записи <code>Record</code> в <code>AddressBook</code> хранятся как значения в словаре. В качестве
ключей используется значение <code>Record.name.value</code>.</li><li><code>Record</code> хранит объект <code>Name</code> в отдельном атрибуте.</li><li><code>Record</code> хранит список объектов <code>Phone</code> в отдельном атрибуте.</li><li><code>Record</code> реализует методы для добавления/удаления/редактирования объектов
<code>Phone</code>.</li><li><code>AddressBook</code> реализует метод <code>add_record</code>, который добавляет <code>Record</code> в
<code>self.data</code>.</li></ul></div>