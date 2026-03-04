// Состояние приложения
let currentProcess = null;

async function analyzeProcess() {
    const text = document.getElementById('processText').value;
    if (!text) {
        alert('Введите описание процесса');
        return;
    }
    
    // Показываем загрузку
    document.getElementById('resultSection').style.display = 'block';
    document.getElementById('graphContainer').innerHTML = 'Анализируем...';
    
    try {
        const response = await fetch('/api/analyze/text', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: text, format: 'text' })
        });
        const data = await response.json();
        
        if (data.success) {
            currentProcess = data;
            //displayResults(data);
            alert(data.ontology)
        } else {
            alert('Ошибка: ' + data.message);
        }
    } catch (error) {
        alert('Ошибка при обращении к серверу: ' + error);
    }
}

function displayResults(data) {
    // Отображаем этапы
    const stagesList = document.getElementById('stagesList');
    stagesList.innerHTML = '<h3>Этапы процесса:</h3>';
    
    data.ontology.stages.forEach(stage => {
        stagesList.innerHTML += `
            <div class="stage-card">
                <h4>${stage.name}</h4>
                <p><strong>Параметры:</strong></p>
                <ul>
                    ${stage.parameters.map(p => `
                        <li>${p.name} (${p.type}) ${p.unit ? '[' + p.unit + ']' : ''}</li>
                    `).join('')}
                </ul>
                <p><strong>Переходы к:</strong> ${stage.transitions_to.join(', ') || 'нет'}</p>
            </div>
        `;
    });
    
    // Отображаем точки бифуркации
    const bifurcationsList = document.getElementById('bifurcationsList');
    if (data.bifurcation_points && data.bifurcation_points.length > 0) {
        bifurcationsList.innerHTML = '<h3>Точки бифуркации:</h3>';
        data.bifurcation_points.forEach(bp => {
            bifurcationsList.innerHTML += `
                <div class="bifurcation-card severity-${bp.severity}">
                    <h4>${bp.stage}</h4>
                    <p><strong>Условие:</strong> ${bp.condition}</p>
                    <p><strong>Порог:</strong> ${bp.threshold}</p>
                    <p><strong>Эффект:</strong> ${bp.effect}</p>
                    <p><strong>Важность:</strong> ${bp.severity}</p>
                </div>
            `;
        });
    } else {
        bifurcationsList.innerHTML = '<p>Точки бифуркации не обнаружены</p>';
    }
    
    // Здесь будет визуализация графа (позже добавим D3.js)
    document.getElementById('graphContainer').innerHTML = `
        <pre>${JSON.stringify(data.graph_data, null, 2)}</pre>
    `;
}

async function uploadData() {
    const fileInput = document.getElementById('dataFile');
    const file = fileInput.files[0];
    
    if (!file) {
        alert('Выберите файл');
        return;
    }
    
    const formData = new FormData();
    formData.append('file', file);
    
    try {
        const response = await fetch('/api/upload/data', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        // Строим модель
        const modelResponse = await fetch('/api/build/model', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                process_id: currentProcess?.ontology?.name || 'process',
                data_path: data.path
            })
        });
        
        const modelData = await modelResponse.json();
        
        document.getElementById('modelResults').innerHTML = `
            <h3>Результаты обучения:</h3>
            <pre>${JSON.stringify(modelData, null, 2)}</pre>
        `;
        
    } catch (error) {
        alert('Ошибка при загрузке: ' + error);
    }
}

function showTab(tabName) {
    // Скрываем все табы
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Убираем активный класс у всех кнопок
    document.querySelectorAll('.tab-button').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Показываем выбранный таб
    document.getElementById(tabName + 'Tab').classList.add('active');
    
    // Активируем кнопку
    event.target.classList.add('active');
}