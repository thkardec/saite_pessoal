import tkinter as tk
from tkinter import messagebox
import random

# Lista das 50 palavras mais usadas no inglês com suas traduções
questions = [
    {"word": "the", "correct": "o, a, os, as", "options": ["você, eu, eles", "feliz", "andar", "rápido"]},
    {"word": "be", "correct": "ser, estar", "options": ["feliz", "tempo", "andar", "voce"]},
    {"word": "to", "correct": "para", "options": ["voce", "feliz", "andar", "rápido"]},
    {"word": "of", "correct": "de", "options": ["ela", "foi", "correr", "rápido"]},
    {"word": "and", "correct": "e", "options": ["lá", "feliz", "andar", "tempo"]},
    {"word": "a", "correct": "um, uma", "options": ["feliz", "correr", "foi", "tempo"]},
    {"word": "in", "correct": "em", "options": ["caminhar", "ontem", "foi", "tempo"]},
    {"word": "that", "correct": "que", "options": ["lá", "ela", "andar", "tempo"]},
    {"word": "have", "correct": "ter", "options": ["rápido", "correr", "andar", "feliz"]},
    {"word": "I", "correct": "eu", "options": ["foi", "andar", "feliz", "lá"]},
    {"word": "it", "correct": "isso", "options": ["ela", "lá", "andar", "tempo"]},
    {"word": "for", "correct": "para", "options": ["foi", "feliz", "andar", "ontem"]},
    {"word": "not", "correct": "não", "options": ["foi", "feliz", "ontem", "rápido"]},
    {"word": "on", "correct": "em", "options": ["foi", "andar", "rápido", "feliz"]},
    {"word": "with", "correct": "com", "options": ["rápido", "feliz", "foi", "tempo"]},
    {"word": "he", "correct": "ele", "options": ["foi", "ela", "andar", "tempo"]},
    {"word": "as", "correct": "como", "options": ["feliz", "foi", "lá", "ontem"]},
    {"word": "you", "correct": "você", "options": ["foi", "andar", "feliz", "tempo"]},
    {"word": "do", "correct": "fazer", "options": ["foi", "feliz", "andar", "ontem"]},
    {"word": "at", "correct": "em", "options": ["feliz", "foi", "andar", "rápido"]},
    {"word": "this", "correct": "isso", "options": ["ela", "foi", "andar", "tempo"]},
    {"word": "but", "correct": "mas", "options": ["foi", "caminhar", "rápido", "andar"]},
    {"word": "his", "correct": "seu, sua", "options": ["foi", "caminhar", "feliz", "tempo"]},
    {"word": "by", "correct": "por", "options": ["foi", "andar", "ela", "tempo"]},
    {"word": "from", "correct": "de", "options": ["foi", "andar", "caminhar", "tempo"]},
    {"word": "they", "correct": "eles", "options": ["foi", "andar", "caminhar", "tempo"]},
    {"word": "we", "correct": "nós", "options": ["foi", "andar", "tempo", "rápido"]},
    {"word": "say", "correct": "dizer", "options": ["foi", "feliz", "andar", "rápido"]},
    {"word": "her", "correct": "dela", "options": ["foi", "andar", "feliz", "rápido"]},
    {"word": "she", "correct": "ela", "options": ["foi", "andar", "feliz", "rápido"]},
    {"word": "or", "correct": "ou", "options": ["foi", "caminhar", "feliz", "tempo"]},
    {"word": "an", "correct": "um, uma", "options": ["foi", "andar", "feliz", "tempo"]},
    {"word": "will", "correct": "vai", "options": ["foi", "andar", "feliz", "tempo"]},
    {"word": "my", "correct": "meu, minha", "options": ["foi", "andar", "feliz", "tempo"]},
    {"word": "one", "correct": "um", "options": ["foi", "andar", "feliz", "tempo"]},
    {"word": "all", "correct": "todos", "options": ["foi", "andar", "feliz", "tempo"]},
    {"word": "would", "correct": "iria", "options": ["foi", "andar", "feliz", "tempo"]},
    {"word": "there", "correct": "lá", "options": ["foi", "andar", "feliz", "tempo"]},
    {"word": "their", "correct": "deles", "options": ["foi", "andar", "feliz", "tempo"]},
    {"word": "what", "correct": "o que", "options": ["foi", "andar", "feliz", "tempo"]},
    {"word": "so", "correct": "então", "options": ["foi", "andar", "feliz", "tempo"]},
    {"word": "up", "correct": "cima", "options": ["foi", "andar", "feliz", "tempo"]},
    {"word": "out", "correct": "fora", "options": ["foi", "andar", "feliz", "tempo"]},
    {"word": "if", "correct": "se", "options": ["foi", "andar", "feliz", "tempo"]},
    {"word": "about", "correct": "sobre", "options": ["foi", "andar", "feliz", "tempo"]},
    {"word": "who", "correct": "quem", "options": ["foi", "andar", "feliz", "tempo"]},
    {"word": "get", "correct": "obter", "options": ["foi", "andar", "feliz", "tempo"]},
    {"word": "which", "correct": "qual", "options": ["foi", "andar", "feliz", "tempo"]},
    {"word": "go", "correct": "ir", "options": ["foi", "andar", "feliz", "tempo"]},
    {"word": "me", "correct": "eu, mim", "options": ["foi", "andar", "feliz", "tempo"]}
]

# Variáveis para contadores de acertos e erros
correct_count = 0
wrong_count = 0

# Função para embaralhar as opções
def shuffle_options(options):
    random.shuffle(options)
    return options

# Função para verificar a resposta
def check_answer(question, selected_option):
    return selected_option == question['correct']

# Função para atualizar a pergunta e as opções
def update_question():
    global current_question
    current_question = random.choice(questions)
    
    question_label.config(text=f"Traduza a palavra: {current_question['word']}")
    
    # Cria uma lista com as opções
    options = current_question['options'][:]
    
    # Adiciona a resposta correta, se não estiver na lista
    if current_question['correct'] not in options:
        options.append(current_question['correct'])
    
    # Embaralha as opções
    options = shuffle_options(options)
    
    # Garante que sempre haja 4 opções
    while len(options) < 4:
        options.append("")  # Adiciona opções vazias se necessário
    
    # Remove duplicatas e limita a 4 opções
    options = list(set(options))  # Remove duplicatas
    options = options[:4]  # Mantém apenas as 4 primeiras opções

    # Atualiza os botões com as opções
    for i in range(4):
        option_buttons[i].config(text=options[i], command=lambda opt=options[i]: on_answer_click(opt))

# Função chamada quando uma opção é selecionada
def on_answer_click(selected_option):
    global correct_count, wrong_count
    if check_answer(current_question, selected_option):
        correct_count += 1
        messagebox.showinfo("Correto!", "Você acertou!")
    else:
        wrong_count += 1
        messagebox.showerror("Errado", f"A resposta correta é: {current_question['correct']}")
    
    # Atualiza o rótulo de contagem de acertos e erros
    score_label.config(text=f"Acertos: {correct_count} | Erros: {wrong_count}")
    
    update_question()

# Criação da janela principal
root = tk.Tk()
root.title("Quiz de Tradução")
root.geometry("400x400")
root.configure(bg="white")  # Define o fundo branco

# Rótulo para a pergunta
question_label = tk.Label(root, text="", wraplength=300, font=("Arial", 16), bg="white")  # Fonte maior e fundo branco
question_label.pack(pady=10)

# Rótulo para exibir acertos e erros
score_label = tk.Label(root, text="Acertos: 0 | Erros: 0", font=("Arial", 14), bg="white")  # Fonte maior e fundo branco
score_label.pack(pady=5)

# Botões para as opções
option_buttons = []
for _ in range(4):  # Cria 4 botões de opção
    btn = tk.Button(root, text="", width=30, height=2, font=("Arial", 14))  # Botões maiores com fonte maior
    btn.pack(pady=5)
    option_buttons.append(btn)

# Atualiza a primeira pergunta
update_question()

# Executa o loop principal
root.mainloop()
