{
    'name': 'Sondaggi magazzino',
    'version': '17.0',
    'author': "Luca Cocozza",
    'application': True,
    'description': "Aggiunta la possibilità di gestire i sondaggi per la merce scaricata nei magazzini",
    'depends': ['fleet','carburante', 'stock'],
    'data': [
        # # Settaggi per accesso ai contenuti
        #'data/ir.model.access.csv',
        # # Caricamento delle view,
        'view/view_update.xml',
    ],
}
