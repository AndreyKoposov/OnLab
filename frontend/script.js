(function() {
    var url = "http://localhost:8080/ping"
    // Запуск проверки соединения
    const connectionChecker = checkServerConnection(url);
    // Устанавливаем обработчики событий
    connectionChecker.onConnectionLost(() => {
        setConnectionStatus(false)
    });
    connectionChecker.onConnectionRestored(() => {
        setConnectionStatus(true)
    });
    connectionChecker.onStatusChange((isConnected, statusCode, error) => {
        setConnectionStatus(isConnected)
        console.log(`Статус соединения: ${isConnected ? 'Подключено' : 'Отключено'}`, 
                    statusCode ? `Код: ${statusCode}` : '',
                    error ? `Ошибка: ${error.message}` : '');
    });
    // Запускаем проверку
    connectionChecker.start();


    // Элементы интерфейса
    const btn1 = document.getElementById('btn1');
    const btn2 = document.getElementById('btn2');
    const btn3 = document.getElementById('btn3');
    const btn4 = document.getElementById('btn4');
    const btn5 = document.getElementById('btn5');
    const btn6 = document.getElementById('btn6');
    
    const contentTitle = document.getElementById('contentTitle');
    const contentBody = document.getElementById('contentBody');
    const contentCard = document.getElementById('contentCard');

    // Массив всех кнопок для управления active-классом
    const allBtns = [btn1, btn2, btn3, btn4, btn5, btn6];

    // Функция сброса активного класса и установки нового
    function setActiveButton(activeBtn) {
        allBtns.forEach(btn => btn.classList.remove('active'));
        activeBtn.classList.add('active');
    }

    // Функция обновления контента
    function updateContent(btnNumber) {
        // Меняем заголовок
        contentTitle.innerHTML = `🧬 Панель ${btnNumber} <span>онтология</span>`;

        // Меняем основной текст в зависимости от кнопки
        let mainText = '';
        let tags = [];

        switch (btnNumber) {
            case 1:
                mainText = 'Здесь будет контент для кнопки 1. Онтологический слой процессов: классификация сущностей, отношения и аксиомы. Отображаются базовые метаданные выбранного процесса.';
                tags = ['сущность: activity', 'сущность: роль', 'отношение: participates_in', 'аксиома: временные рамки'];
                break;
            case 2:
                mainText = 'Контент второй кнопки. Анализ таксономии процессов, иерархия классов и подклассов. Модель онтологии верхнего уровня.';
                tags = ['класс: процесс', 'подкласс: производственный', 'свойство: имеет_вход', 'свойство: имеет_выход'];
                break;
            case 3:
                mainText = 'Содержимое для кнопки 3. Атрибутивный анализ: объектные свойства и атрибуты данных. Отображение доменов и диапазонов.';
                tags = ['datatype: string', 'datatype: integer', 'objectProperty: выполняет', 'функциональное свойство'];
                break;
            case 4:
                mainText = 'Вы нажали кнопку 4. Связи между процессами и временные паттерны. Алгебра процессов и онтология событий.';
                tags = ['событие: старт', 'событие: финиш', 'отношение: последовательность', 'отношение: параллельность'];
                break;
            case 5:
                mainText = 'Кнопка 5. Семантическая разметка и вывод новых знаний. Правила вывода на основе онтологии (SWRL-подобные конструкции).';
                tags = ['правило: modus_ponens', 'правило: наследование', 'аксиома: транзитивность', 'аксиома: симметричность'];
                break;
            case 6:
                mainText = 'Интерфейс для кнопки 6. Визуализация графа онтологии, метрики и статистика. Здесь будет диаграмма (заглушка).';
                tags = ['граф: 124 узла', 'граф: 287 ребер', 'плотность 0.04', 'компоненты связности: 2'];
                break;
            default:
                mainText = 'Выберите кнопку';
                tags = [];
        }

        contentBody.textContent = mainText;

        // Обновляем блок с тегами
        const oldTagsContainer = contentCard.querySelector('.tags-container');
        if (oldTagsContainer) {
            const newTagsContainer = document.createElement('div');
            newTagsContainer.className = 'tags-container';
            
            tags.forEach(tagText => {
                const span = document.createElement('span');
                span.className = 'ontology-tag';
                span.textContent = tagText;
                newTagsContainer.appendChild(span);
            });

            oldTagsContainer.parentNode.replaceChild(newTagsContainer, oldTagsContainer);
        }
    }

    // Назначаем обработчики кликов
    btn1.addEventListener('click', function(e) {
        setActiveButton(btn1);
        updateContent(1);

        fetch(url)
            .then((response) => response.json())
            .then((json) => alert(json["status"]));
    });

    btn2.addEventListener('click', function(e) {
        setActiveButton(btn2);
        updateContent(2);

        setConnectionStatus(false)
    });

    btn3.addEventListener('click', function(e) {
        setActiveButton(btn3);
        updateContent(3);

        setConnectionStatus(true)
    });

    btn4.addEventListener('click', function(e) {
        setActiveButton(btn4);
        updateContent(4);
    });

    btn5.addEventListener('click', function(e) {
        setActiveButton(btn5);
        updateContent(5);
    });

    btn6.addEventListener('click', function(e) {
        setActiveButton(btn6);
        updateContent(6);
    });

    // Инициализация
    setActiveButton(btn1);
    updateContent(1);
})();


// Функция переключения состояния соединения
function setConnectionStatus(isOnline) {
    const indicator = document.getElementById('statusIndicator');
    const statusText = document.getElementById('statusText');
    
    if (isOnline) {
        indicator.classList.remove('offline');
        indicator.classList.add('online');
        statusText.textContent = 'Соединение установлено';
    } else {
        indicator.classList.remove('online');
        indicator.classList.add('offline');
        statusText.textContent = 'Нет соединения';
    }
}

function checkServerConnection(url = window.location.origin, timeout = 5000) {
    // Переменная для хранения интервала
    let intervalId = null;
    
    // Флаг для отслеживания состояния соединения
    let isConnected = true;
    
    // Функция для выполнения проверки соединения
    async function checkConnection() {
        try {
            const controller = new AbortController();
            const timeoutId = setTimeout(() => controller.abort(), timeout);
            
            const response = await fetch(url, {
                method: 'HEAD', // Используем HEAD запрос для минимальной нагрузки
                cache: 'no-cache',
                signal: controller.signal
            });
            
            clearTimeout(timeoutId);
            
            const newStatus = response.ok;
            
            // Если статус изменился, вызываем соответствующий колбэк
            if (newStatus !== isConnected) {
                if (newStatus) {
                    onConnectionRestored?.();
                } else {
                    onConnectionLost?.();
                }
                isConnected = newStatus;
            }
            
            // Вызываем колбэк с результатом проверки
            onStatusChange?.(newStatus, response.status);
            
        } catch (error) {
            // Если произошла ошибка (сеть недоступна, таймаут и т.д.)
            if (error.name === 'AbortError') {
                console.log('Request timeout - connection may be slow or unavailable');
            }
            
            if (isConnected) {
                onConnectionLost?.();
                isConnected = false;
            }
            
            onStatusChange?.(false, null, error);
        }
    }
    
    // Колбэки для различных событий
    let onConnectionLost = null;
    let onConnectionRestored = null;
    let onStatusChange = null;
    
    // Запуск проверки
    function start() {
        if (intervalId === null) {
            // Сразу выполняем первую проверку
            checkConnection();
            // Затем запускаем интервал
            intervalId = setInterval(checkConnection, 1000);
            console.log('Connection checking started');
        }
    }
    
    // Остановка проверки
    function stop() {
        if (intervalId !== null) {
            clearInterval(intervalId);
            intervalId = null;
            console.log('Connection checking stopped');
        }
    }
    
    // Методы для установки колбэков
    return {
        start,
        stop,
        onConnectionLost: (callback) => { onConnectionLost = callback; },
        onConnectionRestored: (callback) => { onConnectionRestored = callback; },
        onStatusChange: (callback) => { onStatusChange = callback; },
        isRunning: () => intervalId !== null,
        getCurrentStatus: () => isConnected
    };
}