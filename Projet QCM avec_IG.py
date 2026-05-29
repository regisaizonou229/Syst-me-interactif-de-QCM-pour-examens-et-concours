# -*- coding: utf-8 -*-
"""
Created on Mon May 26 16:25:54 2025

@author: REGIS AIZONOU
"""

# Interface graphique du QCM avec Tkinter
import tkinter as tk
from tkinter import messagebox, simpledialog

# Questions du QCM
deux_points = chr(58)
questions = [
    {"question": "Résoudre l'équation 3x+5=11", "choix": ["x=2", "x=3", "x=1"], "reponse": "x=2"},
    {"question": "La dérivée de x²", "choix": ["2x", "x", "x²"], "reponse": "2x"},
    {"question": "(a+b)²= ?", "choix": ["a² + b²", "a² +2ab + b²","2a² + 2b²"], "reponse": "a² +2ab + b²"},
    {"question": "L’aire d’un cercle de rayon 3 cm est", "choix": ["9π", "6π", "3π"], "reponse": "9π"},
    {"question": "La masse molaire du carbone (C) est", "choix": ["12 g/mol", "14 g/mol", "16 g/mol"], "reponse": "12 g/mol"},
    {"question": "C=n/V représente", "choix": ["La masse volumique", "La concentration molaire", "La vitesse"], "reponse": "La concentration molaire"},
    {"question": "La vitesse est", "choix": ["distance / temps", "masse / volume", "force / distance"], "reponse": "distance / temps"},
    {"question": "La charge d’un proton est", "choix": ["positive", "négative", "nulle"], "reponse": "positive"},
    {"question": "Une mole contient", "choix": ["6.022X10²³ particules", "1 million de particules", "10³ particules"], "reponse": "6.022X10²³ particules"},
    {"question": "La formule chimique du sel de table est", "choix": ["NaCl", "KCl", "HCl"], "reponse": "NaCl"}
]

participants = []
mot_de_passe = "stopQCM"

# Fonction principale pour lancer un test

def lancer_test():
    global index_question, score, nom_participant
    index_question = 0
    score = 0
    nom_participant = entry_nom.get()
    if not nom_participant:
        messagebox.showerror("Erreur", "Veuillez entrer votre nom.")
        return

    label_nom.pack_forget()
    entry_nom.pack_forget()
    bouton_commencer.pack_forget()
    bouton_stop.pack_forget()

    question_label.pack(pady=20)
    for b in radio_buttons:
        b.pack(anchor="w")
    bouton_valider.pack(pady=10)
    afficher_question()

# Affiche la question suivante

def afficher_question():
    global index_question
    question_label.config(text=f"{index_question + 1}. {questions[index_question]['question']}")
    var_choix.set(0)
    for i in range(3):
        radio_buttons[i].config(text=questions[index_question]["choix"][i])

# Valide la réponse et passe à la suivante

def valider():
    global index_question, score
    if var_choix.get() == 0:
        messagebox.showwarning("Avertissement", "Veuillez choisir une réponse")
        return

    choix_text = questions[index_question]["choix"][var_choix.get() - 1].strip().lower()
    if choix_text == questions[index_question]["reponse"].strip().lower():
        score += 1

    index_question += 1
    if index_question >= len(questions):
        participants.append({"nom": nom_participant, "score": score})
        reset_interface()
    else:
        afficher_question()

# Réinitialise pour un autre participant

def reset_interface():
    question_label.pack_forget()
    for b in radio_buttons:
        b.pack_forget()
    bouton_valider.pack_forget()

    entry_nom.delete(0, tk.END)
    label_nom.pack()
    entry_nom.pack()
    bouton_commencer.pack(pady=10)
    bouton_stop.pack(pady=5)

# Affiche les résultats

def afficher_resultats():
    mot = simpledialog.askstring("Mot de passe", "Entrez le mot de passe pour voir les résultats :")
    if mot == mot_de_passe:
        participants.sort(key=lambda x: x["score"], reverse=True)
        resultats = "\n==== CLASSEMENT FINAL ===="
        for i, p in enumerate(participants, 1):
            resultats += f"\n{i}. {p['nom']} - {p['score']} point(s)"
        messagebox.showinfo("Résultats", resultats)
        fenetre.quit()
    else:
        messagebox.showerror("Erreur", "Mot de passe incorrect.")

# Interface
fenetre = tk.Tk()
fenetre.title("QCM - Concours")
fenetre.geometry("600x400")
fenetre.configure(bg="#4584b5")

label_nom = tk.Label(fenetre, text="Entrez votre nom:", bg="#f0f4f7", font=("Arial", 12))
label_nom.pack()
entry_nom = tk.Entry(fenetre, font=("Arial", 12))
entry_nom.pack()

question_label = tk.Label(fenetre, text="", wraplength=500, font=("Arial", 14), bg="#f0f4f7")

alchoix_vars = []
radio_buttons = []
var_choix = tk.IntVar()

for i in range(3):
    rb = tk.Radiobutton(fenetre, text="", variable=var_choix, value=i + 1, bg="#4584b5", font=("Arial", 12), anchor="w")
    radio_buttons.append(rb)

bouton_valider = tk.Button(fenetre, text="Valider", command=valider, bg="#21B134", fg="white", font=("Arial", 12), padx=10, pady=5)
bouton_commencer = tk.Button(fenetre, text="Commencer le QCM", command=lancer_test, bg="#28a745", fg="white", font=("Arial", 12), padx=10, pady=5)
bouton_commencer.pack(pady=10)

bouton_stop = tk.Button(fenetre, text="Afficher les résultats (Surveillant)", command=afficher_resultats, bg="#dc3545", fg="white", font=("Arial", 12), padx=10, pady=5)
bouton_stop.pack(pady=5)

fenetre.mainloop()
