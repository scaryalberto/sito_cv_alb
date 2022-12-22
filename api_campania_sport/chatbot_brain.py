#in questo file "creiamo" la batteria di domande per il nostro bot
from levenstein_algoritm import *
import random
import datetime
current_time = datetime.datetime.now()

domande_e_risposte = {
    "che ore sono": f"sono le {str(current_time.hour)+':'+str(current_time.minute)}. Però dai, fammi una domanda su Alberto. Sono qui per questo",
    "che giorno è oggi": f"oggi è il {str(current_time.day) + '/' + str(current_time.month)}. Però dai, fammi una domanda su Alberto. Sono qui per questo",
    "chi è il tuo padrone": "si chiama alberto",
    "chi ti ha inventato": "alberto",
    "cosa fai": "sostiuisco alberto quando non può rispondere",
    "che squadra tifa alberto?": "Tifa Juve, la squadra più forte del mondo",
    "come funzioni": "Mi ha creato alberto, ha utilizzato la distanza di Levenstei per aiutarmi  a capire le domande, se vuoi puoi trovare info qui: https://it.wikipedia.org/wiki/Distanza_di_Levenshtein",
    "help": "tu sei il capo, potresti chiedermi: che ore sono, oppure cosa fa Alberto",
    "che tempo fa oggi": "Non lo so, non so di dove sei. Apri la finestra e vedi",
    "dimmi qualcosa": "tu sei il capo, potresti chiedermi: che ore sono, oppure cosa fa Alberto",
    "quando sei nato": "Nel 2022... sono piccolo",
    "quando è nato alberto": "Alberto è del 1993. Puoi trovare tutto le info nel suo cv presente in questo sito",
    "quali lingue parla Alberto": "Alberto parla italiana, inglese ed un poco di spagnolo",
    "progetti alberto": "puoi trovare alcuni dei progetti di Alberto andando sul suo github: https://github.com/scaryalberto",
    "notizie": "Mmm... ne prendo una a caso da CampaniaSport.it {} .Sai che questo sito è stgato sviluppato anche da Alberto? ",
    "come ti chiami":"Sono AlbertoBot, e sono qui per aiutarti",
}



def question_for_bot (domanda):
    #pre-processiamo la domanda
    domanda=domanda.lower()
    domanda=domanda.replace('?', '').replace('.', '').replace('alberto', '')

    #applichiamo la distanza di levenstein alle domande inserite
    first_word = domanda
    diz_domanda_dist_levestein={}
    for word in domande_e_risposte.keys():
        dist = opti_leven_distance(first_word, word)
        #print(f'Distance between {domanda} and {word}: {dist}')
        diz_domanda_dist_levestein[word]=dist

    #piu basso è il punteggio, meglio è
    domanda_trovata={k: v for k, v in sorted(diz_domanda_dist_levestein.items(), key=lambda item: item[1])}
    if len(domanda_trovata)>0 and list(domanda_trovata.values())[0]<20:
        domanda_trovata=list(domanda_trovata.keys())[0]
        print(domande_e_risposte[domanda_trovata])

    else:
        random_choice=random.randrange(0, len(domande_e_risposte.keys()))
        print(f"Scusami, ma non ho capito la domanda. Ho ancora tanto da imparare. Magari potresti chiedermi: {list(domande_e_risposte.keys())[random_choice]}?")


question_for_bot("progetti alberto")