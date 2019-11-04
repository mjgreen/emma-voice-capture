def define_word_lists():
    PracticeList1 = {
        'words': ['PAINT', 'COUNT', 'THEME', 'SKILL', 'SHAPE', 'FRESH', 'LEARN', 'STORE', 'DRAWN', 'SPEND'],
        'cue': ['ALERT'],
        'freq': 'medium',
        'name': 'PracticeList1'
    }
    PracticeList2 = {
        'words': ['MAGIC', 'YOUTH', 'SORRY', 'GUESS', 'ERROR', 'NOISE', 'CHECK', 'REPLY', 'TRUCK', 'ALLOW'],
        'cue': ['BEGIN'],
        'freq': 'medium',
        'name': 'PracticeList2'
    }
    LowFrequencyList1 = {
        'words': ['MANDREL', 'APTNESS', 'DAPPLED', 'WARPING', 'KNOTTED', 'DIPPING', 'ADAPTER', 'BALLAST', 'AUGMENT', 'MATTING'],
        'cue': ['BOARDER'],
        'freq': 'low',
        'name': 'LowFrequencyList1'
    }
    LowFrequencyList2 = {
        'words': ['AMBROSE', 'WILLOWY', 'RECOUNT', 'HARPING', 'SUBSIDE', 'BIFOCAL', 'PROFUSE', 'LAPPING', 'TOPICAL', 'STOPPER'],
        'cue': ['LATERAL'],
        'freq': 'low',
        'name': 'LowFrequencyList2'
    }
    LowFrequencyList3 = {
        'words': ['SPILLER', 'OBVERSE', 'CLOSURE', 'ISSUING', 'ACSCRIBE', 'LINKAGE', 'DUALISM', 'OUTBACK', 'CONCISE', 'FROSTED'],
        'cue': ['WORDING'],
        'freq': 'low',
        'name': 'LowFrequencyList3'
    }
    LowFrequencyList4 = {
        'words': ['IGNEOUS', 'FLATTEN', 'DRAUGHT', 'FORESEE', 'NUMERAL', 'SHADING', 'CONNECT', 'VOCALLY', 'SEMINAL', 'PAYABLE'],
        'cue': ['CASCADE'],
        'freq': 'low',
        'name': 'LowFrequencyList4'
    }
    HighFrequencyList1 = {
        'words': ['SEVERAL', 'USUALLY', 'WRITTEN', 'SERVICE', 'ALREADY', 'GENERAL', 'PRESENT', 'SUBJECT', 'NOTHING', 'CONTROL'],
        'cue': ['INSTEAD'],
        'freq': 'hi',
        'name': 'HighFrequencyList1'
    }
    HighFrequencyList2 = {
        'words': ['EXAMPLE', 'EXACTLY', 'BECAUSE', 'OUTSIDE', 'PERHAPS', 'PROVIDE', 'BELIEVE', 'BROUGHT', 'VARIOUS', 'SURFACE'],
        'cue': ['MEETING'],
        'freq': 'hi',
        'name': 'HighFrequencyList2'
    }
    HighFrequencyList3 = {
        'words': ['PROBLEM', 'CENTRAL', 'GETTING', 'COVERED', 'DECIDED', 'WHETHER', 'HIMSELF', 'PROGRAM', 'THOUGHT', 'CENTURY'],
        'cue': ['MORNING'],
        'freq': 'hi',
        'name': 'HighFrequencyList3'
    }
    HighFrequencyList4 = {
        'words': ['CURRENT', 'CERTAIN', 'AGAINST', 'FORWARD', 'DROPPED', 'HISTORY', 'GROWING', 'WITHOUT', 'FURTHER', 'HOWEVER'],
        'cue': ['THROUGH'],
        'freq': 'hi',
        'name': 'HighFrequencyList4'
    }

    return PracticeList1, PracticeList2, \
           LowFrequencyList1, LowFrequencyList2, LowFrequencyList3, LowFrequencyList4, \
           HighFrequencyList1, HighFrequencyList2, HighFrequencyList3, HighFrequencyList4


def define_messages():
    text_please_recall_list_1 = \
        "please recall as many words as you can from word list 1 and press the spacebar when you cannot remember any more."

    text_please_recall_list_2 = \
        "please recall as many words as you can from word list 2 and press the spacebar when you cannot remember any more."

    text_start_of_block = [ # a list, with 5 elements, one for each block-start

        "Welcome to the experiment.\n\n"
        "The current task is comprised of a practice block, followed by four blocks of experimental trials. "
        "Each trial block consists of two phases: encoding and recall.\n"
        "During the encoding phase you will be presented with two lists, each consisting of 10 target words "
        "(presented on the right of the screen) and 1 cue word (presented on the left of the screen). "
        "You will be presented with each list twice, once with target words presented sequentially, "
        "and once simultaneously. During the encoding phase you should try to remember as many target "
        "words as you can and may use whatever method you would like to do this.\n\n"
        "The recall stage will then begin. At the start of the recall phase the cue word from list 1 "
        "will appear in the middle of the screen. When the cue word is shown you should recall as many "
        "of the list 1 target words as you can. You should recall each word verbally, into the microphone"
        ", and you should press the spacebar when you cannot remember any further words. "
        "On pressing the spacebar, the cue word from list 2 will appear in the middle of the screen and you "
        "should recall as many target words as you can from list 2.\n\n"
        "Do you have any questions?\n\n"
        "Please press the Spacebar to begin the practice trial block.",

        "You have now finished the practice trial block. "
        "You will now encounter four experimental trial blocks that replicate the procedure you have just completed "
        "(i.e. in each block you will be asked to encode and verbally recall two word lists). "
        "You will be able to take a short break between each of the trial blocks.\n\n"
        "Do you have any questions?\n\n"
        "Press the spacebar when you are ready to begin block 1.",

        "Please take a break.\n"
        "Press the spacebar when you are ready to begin block 2.",

        "Please take a break.\n"
        "Press the spacebar when you are ready to begin block 3.",

        "Please take a break.\n"
        "Press the spacebar when you are ready to begin block 4.",

    ]

    return text_please_recall_list_1, text_please_recall_list_2, text_start_of_block
