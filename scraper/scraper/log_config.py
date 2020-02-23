import os
import logging.config

# configuration de log
standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]'  # Où nom est le nom spécifié par getlogger
simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

# Définir le format de sortie du journal
logfile_dir = os.path.dirname(os.path.abspath(__file__)) + '/spiders/logs'  # Répertoire des fichiers journaux
logfile_name = 'paper.log'  # le nom de log

# Créez un répertoire de journaux défini s'il n'existe pas
if not os.path.isdir(logfile_dir):
    os.mkdir(logfile_dir)

# Le chemin complet du fichier journal
logfile_path = os.path.join(logfile_dir, logfile_name)

# dictionnaire de configuration des journaux
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        # Connectez-vous au terminal
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',  # Imprimer à l'écran
            'formatter': 'simple'
        },
        # Imprimer les journaux dans les fichiers, collecter les informations et les journaux ci-dessus
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # Enregistrer dans un fichier
            'formatter': 'standard',
            'filename': logfile_path,  # Fichier journal
            'maxBytes': 1024*1024*3,  # Taille  3M
            'backupCount': 1,
            'encoding': 'utf-8',  # Encodage des fichiers journaux
        },
    },
    'loggers': {
        # configuration de l'enregistreur obtenue par logging.getLogger (__ name__)
        '': {
            'handlers': ['default', 'console'],  # Ajoutez les deux gestionnaires définis ci-dessus, c'est-à-dire que les données du journal sont écrites dans le fichier et imprimées à l'écran
            'level': 'INFO',
            'propagate': True,  # Passe vers le haut (enregistreur de niveau supérieur)
        },
    },
}

logging.config.dictConfig(LOGGING_DIC)  # Importez la configuration de journalisation définie ci-dessus
logging.getLogger('readability').setLevel(logging.WARNING)
logger = logging.getLogger(__name__)  # Générer une instance de journal
