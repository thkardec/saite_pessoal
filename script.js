const questions = [
    {
        "word": "O que define um médium intuitivo?",
        "correct": "Ele recebe inspirações dos espíritos e as interpreta com sua própria mente.",
        "options": [
            "Ele fala diretamente com os espíritos sem intermediários.",
            "Ele recebe inspirações dos espíritos e as interpreta com sua própria mente.",
            "Ele controla os espíritos para que eles se manifestem.",
            "Ele apenas sente a presença dos espíritos sem se comunicar."
        ]
    },
    {
        "word": "O que Allan Kardec recomenda para a proteção contra espíritos enganadores?",
        "correct": "Elevação moral, estudo e vigilância nas comunicações.",
        "options": [
            "Recorrer a práticas esotéricas de proteção.",
            "Evitar qualquer contato com espíritos.",
            "Elevação moral, estudo e vigilância nas comunicações.",
            "Confiar em médiuns experientes para filtrar as comunicações."
        ]
    },
    {
        "word": "Como os espíritos desencarnados influenciam os encarnados, segundo O Livro dos Médiuns?",
        "correct": "Eles influenciam nossos pensamentos e decisões, mas apenas se permitirmos.",
        "options": [
            "Eles controlam completamente nossas ações sem nosso consentimento.",
            "Eles influenciam nossos pensamentos e decisões, mas apenas se permitirmos.",
            "Eles só influenciam médiuns com habilidades especiais.",
            "Eles têm influência direta sobre nossa saúde física."
        ]
    },
    {
        "word": "Qual é a atitude de Kardec em relação a médiuns que abusam de seu poder mediúnico?",
        "correct": "Eles atraem espíritos inferiores e podem prejudicar a si mesmos e aos outros.",
        "options": [
            "Eles fortalecem sua habilidade mediúnica.",
            "Eles atraem espíritos inferiores e podem prejudicar a si mesmos e aos outros.",
            "Eles são guiados pelos espíritos superiores para aprender com seus erros.",
            "Eles são punidos diretamente pelos espíritos."
        ]
    },
    {
        "word": "O que define um médium vidente?",
        "correct": "Ele pode ver espíritos, mesmo que não se comunique com eles.",
        "options": [
            "Ele pode ver espíritos, mesmo que não se comunique com eles.",
            "Ele pode ouvir os espíritos, mas não os vê.",
            "Ele pode controlar os espíritos para se manifestarem.",
            "Ele pode escrever automaticamente sob a influência dos espíritos."
        ]
    },
    {
        "word": "O que Kardec diz sobre a mediunidade em crianças?",
        "correct": "Ela pode existir, mas deve ser tratada com cuidado, respeitando o desenvolvimento infantil.",
        "options": [
            "Ela é mais forte nas crianças do que nos adultos.",
            "Ela é rara e não deve ser encorajada.",
            "Ela pode existir, mas deve ser tratada com cuidado, respeitando o desenvolvimento infantil.",
            "As crianças não podem ser médiuns."
        ]
    },
    {
        "word": "O que O Livro dos Médiuns ensina sobre a necessidade de estudo na prática mediúnica?",
        "correct": "O estudo é fundamental para entender e exercer a mediunidade de maneira segura e eficaz.",
        "options": [
            "O estudo é fundamental para entender e exercer a mediunidade de maneira segura e eficaz.",
            "O estudo é irrelevante, pois a mediunidade é inata.",
            "O estudo só é necessário para médiuns de efeitos físicos.",
            "O estudo impede que o médium desenvolva habilidades intuitivas."
        ]
    }
];

let currentQuestionIndex = 0;
let correctCount = 0;
let wrongCount = 0;
let timer;
let timeLimit = 10;

function shuffleOptions(options) {
    for (let i = options.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [options[i], options[j]] = [options[j], options[i]];
    }
    return options;
}

function checkAnswer(selected, correct) {
    return selected === correct;
}

function showNextButton() {
    document.getElementById("next-btn").style.display = "block";
}

function hideNextButton() {
    document.getElementById("next-btn").style.display = "none";
}

function nextQuestion() {
    if (currentQuestionIndex === questions.length - 1) {
        showFinalScore();
    } else {
        currentQuestionIndex++;
        updateQuestion();
        hideNextButton();
        startTimer();
    }
}

function updateQuestion() {
    clearInterval(timer);
    const currentQuestion = questions[currentQuestionIndex];
    document.getElementById("question").innerText = `"${currentQuestion.word}"?`;

    const options = [...currentQuestion.options, currentQuestion.correct];
    const shuffledOptions = shuffleOptions(options);

    const optionsContainer = document.getElementById("options");
    optionsContainer.innerHTML = "";

    shuffledOptions.forEach(option => {
        const button = document.createElement("button");
        button.innerText = option;
        button.className = "button";
        button.onclick = function () {
            clearInterval(timer);
            if (checkAnswer(option, currentQuestion.correct)) {
                correctCount++;
                button.classList.add("correct");
            } else {
                wrongCount++;
                button.classList.add("wrong");
                const correctButton = Array.from(optionsContainer.children).find(btn => btn.innerText === currentQuestion.correct);
                if (correctButton) {
                    correctButton.classList.add("correct");
                }
            }
            showNextButton();
            document.getElementById("score").innerText = `Acertos: ${correctCount} | Erros: ${wrongCount}`;
            Array.from(optionsContainer.children).forEach(btn => {
                btn.onclick = null; // Remove eventos de clique dos botões
            });
        };
        optionsContainer.appendChild(button);
    });
}

function showFinalScore() {
    document.getElementById("quiz-container").innerHTML = `
        <h1>Quiz Finalizado!</h1>
        <p>Você acertou ${correctCount} de ${questions.length} perguntas.</p>
        <button class="button" onclick="restartQuiz()">Reiniciar</button>
    `;
}

function restartQuiz() {
    correctCount = 0;
    wrongCount = 0;
    currentQuestionIndex = 0;
    updateQuestion();
    hideNextButton();
    startTimer();
}

function startTimer() {
    let timeLeft = timeLimit;
    document.getElementById("timer").innerText = `Tempo restante: ${timeLeft}s`;
    timer = setInterval(() => {
        timeLeft--;
        document.getElementById("timer").innerText = `Tempo restante: ${timeLeft}s`;
        if (timeLeft <= 0) {
            clearInterval(timer);
            wrongCount++; // Conta como erro quando o tempo acaba
            document.getElementById("score").innerText = `Acertos: ${correctCount} | Erros: ${wrongCount}`;
            showNextButton();
            const correctButton = Array.from(document.getElementById("options").children).find(btn => btn.innerText === questions[currentQuestionIndex].correct);
            if (correctButton) {
                correctButton.classList.add("correct");
            }
            Array.from(document.getElementById("options").children).forEach(btn => {
                btn.onclick = null; // Remove eventos de clique dos botões
            });
        }
    }, 1000);
}

// Iniciar o quiz
updateQuestion();
startTimer();
