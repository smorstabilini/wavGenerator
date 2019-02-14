from splinter import Browser

SELEZIONE_FAMILIARE = "Selezione familiare"
PRESTAZIONE = "Prestazione"
PRESTAZIONE_PROPEDEUTICA = "La prestazione è propedeutica ad un ricovero non ancora effettuato?"
HAI_LA_PRESCRIZIONE = "Hai la prescrizione?"
TARIFFE_AGEVOLATE = "Hai la possibilità di usufruire delle tariffe agevolate. Vuoi procedere?"
PRENOTAZIONE_GIA_EFFETTUATA = "Prenotazione già effettuata"
STRUTTURA_PRENOTATA = "Struttura prenotata"
DATA_PRENOTAZIONE = "Data prenotazione"
ORA_PRENOTAZIONE = "Ora prenotazione"
SELEZIONE_ALTRA_STRUTTURA = 'Selezione altra struttura'
SELEZIONE_STRUTTURA = 'Selezione struttura'
SELEZIONE_RICOVERO_COLLEGATO = 'Selezione ricovero collegato'
NUMERO_DI_CONTATTO = 'Numero di contatto'

"""
# fill the query form with our search term
# browser.fill('sb_form_q', 'mastro35 twitter')

# find the search button on the page and click it
# button = browser.find_by_id('sb_form_go')
# button.click()

# browser.find_by_css('a.my-website').first.click()
# assert browser.find_by_css('a.banner').first.visible


browser.find_by_css('h1')
browser.find_by_xpath('//h1')
browser.find_by_tag('h1')
browser.find_by_name('name')
browser.find_by_text('Hello World!')
browser.find_by_id('firstheader')
browser.find_by_value('query')
"""

import traceback

def who_am_i():
    """
    Restituisce il nome della funzione che ha chiamato 'get_caso_duso'.
    Usare stack[-2] per ottenere il nome della funzione chiamante who_am_i
    """
    stack = traceback.extract_stack()
    filename, codeline, funcName, text = stack[-3]
    
    return funcName

def get_caso_duso():
    func_name = who_am_i()
    return func_name.replace('test_', '')

def test_IVR1807CL04():
    # print(who_am_i())
    caso = get_caso_duso()

    print('\n--------- Caso d\'uso {} ---------'.format(caso))
    url = "http://localhost:4200/home?guid={}&hash=0123456".format(caso)
    browser.visit(url)

    selezione_altra_struttura = browser.is_text_present(SELEZIONE_ALTRA_STRUTTURA, wait_time=7)
    print(selezione_altra_struttura)
    assert not selezione_altra_struttura

    selezione_struttura = browser.is_text_present(SELEZIONE_STRUTTURA)
    print(selezione_struttura)
    assert not selezione_struttura

    prestazione_propedeutica = browser.is_text_present(PRESTAZIONE_PROPEDEUTICA)
    print(prestazione_propedeutica)
    assert not prestazione_propedeutica

    hai_la_prescrizione = browser.is_text_present(HAI_LA_PRESCRIZIONE)
    print(hai_la_prescrizione)
    assert hai_la_prescrizione
    
    # tariffe_agevolate = browser.is_text_present(TARIFFE_AGEVOLATE)
    # print(tariffe_agevolate)
    # assert not tariffe_agevolate

    # Questa verifica ha senso solo se si è risposto "No" manualmente alla domanda "Hai la prescrizione?":
    tariffe_agevolate = browser.is_text_present(TARIFFE_AGEVOLATE)
    print(tariffe_agevolate)
    assert tariffe_agevolate

def test_IVR1807CL07():
    """
    L'ultimo script esistente è isOwnSubscription che però vocalizza una riposta non valida.
    """
    caso = get_caso_duso()
    print('\n--------- Caso d\'uso {} ---------'.format(caso))
    url = "http://localhost:4200/home?guid={}&hash=0123456".format(caso)
    browser.visit(url)

    selezione_altra_struttura = browser.is_text_present(SELEZIONE_ALTRA_STRUTTURA, wait_time=6)
    print(selezione_altra_struttura)
    assert not selezione_altra_struttura

    selezione_struttura = browser.is_text_present(SELEZIONE_STRUTTURA)
    print(selezione_struttura)
    assert not selezione_struttura

    prestazione = browser.is_text_present(PRESTAZIONE)
    print(prestazione)
    assert not prestazione

    prestazione_propedeutica = browser.is_text_present(PRESTAZIONE_PROPEDEUTICA)
    print(prestazione_propedeutica)
    assert not prestazione_propedeutica

    hai_la_prescrizione = browser.is_text_present(HAI_LA_PRESCRIZIONE)
    print(hai_la_prescrizione)
    assert not hai_la_prescrizione

    prenotazione_gia_effettuata = browser.is_text_present(PRENOTAZIONE_GIA_EFFETTUATA)
    print(prenotazione_gia_effettuata)
    assert not prenotazione_gia_effettuata

    data_prenotazione = browser.is_text_present(DATA_PRENOTAZIONE)
    print(data_prenotazione)
    assert not data_prenotazione

    ora_prenotazione = browser.is_text_present(ORA_PRENOTAZIONE)
    print(ora_prenotazione)
    assert not ora_prenotazione

    numero_di_contatto = browser.is_text_present(NUMERO_DI_CONTATTO)
    print(numero_di_contatto)
    assert not numero_di_contatto

    selezione_ricovero_collegato = browser.is_text_present(SELEZIONE_RICOVERO_COLLEGATO)
    print(selezione_ricovero_collegato)
    assert not selezione_ricovero_collegato
    

def test_IVR1807CL38():
    """
    Prestazione per familiare. Si dovrebbe arrivare fino allo step checkDisposabilityDate e superarlo.
    """
    caso = get_caso_duso()
    print('\n--------- Caso d\'uso {} ---------'.format(caso))
    url = "http://localhost:4200/home?guid={}&hash=0123456".format(caso)
    browser.visit(url)

    selezione_altra_struttura = browser.is_text_present(SELEZIONE_ALTRA_STRUTTURA, wait_time=6)
    print(selezione_altra_struttura)
    assert not selezione_altra_struttura

    selezione_struttura = browser.is_text_present(SELEZIONE_STRUTTURA)
    print(selezione_struttura)
    assert selezione_struttura


def test_IVR1807CL40():
    caso = get_caso_duso()
    print('\n--------- Caso d\'uso {} ---------'.format(caso))
    url = "http://localhost:4200/home?guid={}&hash=0123456".format(caso)
    browser.visit(url)

    selezione_familiare = browser.is_text_present(SELEZIONE_FAMILIARE, wait_time=5)
    print(selezione_familiare)
    assert not selezione_familiare

    selezione_altra_struttura = browser.is_text_present(SELEZIONE_ALTRA_STRUTTURA)
    print(selezione_altra_struttura)
    assert not selezione_altra_struttura

    selezione_struttura = browser.is_text_present(SELEZIONE_STRUTTURA)
    print(selezione_struttura)
    assert not selezione_struttura

    prestazione = browser.is_text_present(PRESTAZIONE)
    print(prestazione)
    assert prestazione

    # fino a qui ci sono i campi mostrati dopo aver lanciato gli script di questo caso d'uso

    prestazione_propedeutica = browser.is_text_present(PRESTAZIONE_PROPEDEUTICA)
    print(prestazione_propedeutica)
    assert not prestazione_propedeutica

    hai_la_prescrizione = browser.is_text_present(HAI_LA_PRESCRIZIONE)
    print(hai_la_prescrizione)
    assert not hai_la_prescrizione

    prenotazione_gia_effettuata = browser.is_text_present(PRENOTAZIONE_GIA_EFFETTUATA)
    print(prenotazione_gia_effettuata)
    assert not prenotazione_gia_effettuata

    struttura_prenotata = browser.is_text_present(STRUTTURA_PRENOTATA)
    print(struttura_prenotata)
    assert not struttura_prenotata

    data_prenotazione = browser.is_text_present(DATA_PRENOTAZIONE)
    print(data_prenotazione)
    assert not data_prenotazione

    ora_prenotazione = browser.is_text_present(ORA_PRENOTAZIONE)
    print(ora_prenotazione)
    assert not ora_prenotazione

    numero_di_contatto = browser.is_text_present(NUMERO_DI_CONTATTO)
    print(numero_di_contatto)
    assert not numero_di_contatto

def test_IVR1807CL41():
    """
    Allo step checkBookingDate viene vocalizzata una data non valida, quindi il campo DataPrenotazione deve essere visibile (e anche
    l'ora prenotazione).
    """
    caso = get_caso_duso()
    print('\n--------- Caso d\'uso {} ---------'.format(caso))
    url = "http://localhost:4200/home?guid={}&hash=0123456".format(caso)
    browser.visit(url)

    selezione_altra_struttura = browser.is_text_present(SELEZIONE_ALTRA_STRUTTURA, wait_time=6)
    print(selezione_altra_struttura)
    assert not selezione_altra_struttura

    selezione_struttura = browser.is_text_present(SELEZIONE_STRUTTURA)
    print(selezione_struttura)
    assert not selezione_struttura

    prestazione = browser.is_text_present(PRESTAZIONE)
    print(prestazione)
    assert prestazione

    prestazione_propedeutica = browser.is_text_present(PRESTAZIONE_PROPEDEUTICA)
    print(prestazione_propedeutica)
    assert not prestazione_propedeutica

    hai_la_prescrizione = browser.is_text_present(HAI_LA_PRESCRIZIONE)
    print(hai_la_prescrizione)
    assert hai_la_prescrizione

    prenotazione_gia_effettuata = browser.is_text_present(PRENOTAZIONE_GIA_EFFETTUATA)
    print(prenotazione_gia_effettuata)
    assert prenotazione_gia_effettuata

    data_prenotazione = browser.is_text_present(DATA_PRENOTAZIONE)
    print(data_prenotazione)
    assert data_prenotazione

    # in questo caso phoneCallFlusso.askOraPrenotazioneEffettuata arriva uguale a True dal backend, quindi va mostrato anche il campo 
    # Ora prenotazione:
    ora_prenotazione = browser.is_text_present(ORA_PRENOTAZIONE)
    print(ora_prenotazione)
    assert ora_prenotazione

    # dopo il lancio dell'ultimo script python di questo caso d'uso il cruscotto dovrebbe essere fermo a "Ora prenotazione", quindi questo 
    # campo non dovrebbe essere visibile (a meno che non sia stato inserito a mano...)
    numero_di_contatto = browser.is_text_present(NUMERO_DI_CONTATTO)
    print(numero_di_contatto)
    assert not numero_di_contatto

def test_IVR1807CL43():
    caso = get_caso_duso()
    print('\n--------- Caso d\'uso {} ---------'.format(caso))
    url = "http://localhost:4200/home?guid={}&hash=0123456".format(caso)
    browser.visit(url)

    selezione_altra_struttura = browser.is_text_present(SELEZIONE_ALTRA_STRUTTURA, wait_time=6)
    print(selezione_altra_struttura)
    assert not selezione_altra_struttura

    selezione_struttura = browser.is_text_present(SELEZIONE_STRUTTURA)
    print(selezione_struttura)
    assert not selezione_struttura

    prestazione = browser.is_text_present(PRESTAZIONE)
    print(prestazione)
    assert prestazione

    prestazione_propedeutica = browser.is_text_present(PRESTAZIONE_PROPEDEUTICA)
    print(prestazione_propedeutica)
    assert not prestazione_propedeutica

    hai_la_prescrizione = browser.is_text_present(HAI_LA_PRESCRIZIONE)
    print(hai_la_prescrizione)
    assert hai_la_prescrizione

    prenotazione_gia_effettuata = browser.is_text_present(PRENOTAZIONE_GIA_EFFETTUATA)
    print(prenotazione_gia_effettuata)
    assert prenotazione_gia_effettuata

    struttura_prenotata = browser.is_text_present(STRUTTURA_PRENOTATA)
    print(struttura_prenotata)
    assert struttura_prenotata

    data_prenotazione = browser.is_text_present(DATA_PRENOTAZIONE)
    print(data_prenotazione)
    assert data_prenotazione

    ora_prenotazione = browser.is_text_present(ORA_PRENOTAZIONE)
    print(ora_prenotazione)
    assert ora_prenotazione

    # l'ora dovrebbe essere valorizzata e uguale a 9.30.

    numero_di_contatto = browser.is_text_present(NUMERO_DI_CONTATTO)
    print(numero_di_contatto)
    assert numero_di_contatto

def test_L13():
    caso = get_caso_duso()
    print('\n--------- Caso d\'uso {} ---------'.format(caso))
    url = "http://localhost:4200/home?guid={}&hash=0123456".format(caso)
    browser.visit(url)

    selezione_altra_struttura = browser.is_text_present(SELEZIONE_ALTRA_STRUTTURA, wait_time=5)
    print(selezione_altra_struttura)
    assert selezione_altra_struttura

    selezione_struttura = browser.is_text_present(SELEZIONE_STRUTTURA)
    print(selezione_struttura)
    assert not selezione_struttura

    prestazione_propedeutica = browser.is_text_present(PRESTAZIONE_PROPEDEUTICA)
    print(prestazione_propedeutica)
    assert not prestazione_propedeutica

def test_L05():
    caso = get_caso_duso()
    print('\n--------- Caso d\'uso {} ---------'.format(caso))
    url = "http://localhost:4200/home?guid={}&hash=0123456".format(caso)
    browser.visit(url)

    selezione_familiare = browser.is_text_present(SELEZIONE_FAMILIARE, wait_time=5)
    print(selezione_familiare)
    assert selezione_familiare

    selezione_altra_struttura = browser.is_text_present(SELEZIONE_ALTRA_STRUTTURA)
    print(selezione_altra_struttura)
    assert not selezione_altra_struttura

    selezione_struttura = browser.is_text_present(SELEZIONE_STRUTTURA)
    print(selezione_struttura)
    assert not selezione_struttura

    prestazione = browser.is_text_present(PRESTAZIONE)
    print(prestazione)
    assert prestazione

    prestazione_propedeutica = browser.is_text_present(PRESTAZIONE_PROPEDEUTICA)
    print(prestazione_propedeutica)
    assert not prestazione_propedeutica

    hai_la_prescrizione = browser.is_text_present(HAI_LA_PRESCRIZIONE)
    print(hai_la_prescrizione)
    assert not hai_la_prescrizione

    prenotazione_gia_effettuata = browser.is_text_present(PRENOTAZIONE_GIA_EFFETTUATA)
    print(prenotazione_gia_effettuata)
    assert prenotazione_gia_effettuata

    struttura_prenotata = browser.is_text_present(STRUTTURA_PRENOTATA)
    print(struttura_prenotata)
    assert struttura_prenotata

    data_prenotazione = browser.is_text_present(DATA_PRENOTAZIONE)
    print(data_prenotazione)
    assert data_prenotazione

    ora_prenotazione = browser.is_text_present(ORA_PRENOTAZIONE)
    print(ora_prenotazione)
    # assert not ora_prenotazione
    assert ora_prenotazione

    numero_di_contatto = browser.is_text_present(NUMERO_DI_CONTATTO)
    print(numero_di_contatto)
    assert numero_di_contatto


with Browser('chrome') as browser:
    
    # test_IVR1807CL04()      # ok
    # test_IVR1807CL07()      # ok
    # test_IVR1807CL38()      # ok
    test_IVR1807CL40()      # dovrebbe mostrare la domanda "Per quale motivo devi eseguire la prestazione" ma invece mostra "Prestazione già eseguita?"
    # test_IVR1807CL41()      # ok
    # test_IVR1807CL43()      # ok
    # test_L13()        # ok
    # test_L05()        # ok

    print("Fine test")
