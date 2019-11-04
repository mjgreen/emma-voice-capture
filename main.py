"""
this is being written on linux, using an anaconda python2.7 environment with psychopy installed using pip thus:
pip install psychopy pyglet==1.3.2

it is going to be run on windows, using standalone Psychopy3_Py2, from the coder interface
"""

import os, sys
from psychopy import prefs
prefs.hardware['audioLib'] = ['pyo']
prefs.hardware['audioLatencyMode'] = '0'
from psychopy import visual, core, event, microphone, gui, data
from numpy.random import random
from definitions import *


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# GUI
psychopyVersion = '3.2.3'
expName = u'voiceCaptureForEmma_v3'  # from the Builder filename that created this script
expInfo = {u'gender': ['female', 'male'], u'age': u'20', u'session': u'001', 'participantNumber': 999, 'devMode': False}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=True, title=str(expName))
if not dlg.OK:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + "P" + str(expInfo['participantNumber']).zfill(3) + os.path.sep + expInfo['date']
os.path.exists(_thisDir + os.sep + u'data') or os.mkdir( _thisDir + os.sep + u'data')
os.path.exists(_thisDir + os.sep + u'data' + os.sep + "P" + str(expInfo['participantNumber']).zfill(3)) or os.mkdir(_thisDir + os.sep + u'data' + os.sep + "P" + str(expInfo['participantNumber']).zfill(3))
os.path.exists(filename) or os.mkdir(filename)
wavDirName = filename
if not os.path.isdir(wavDirName):
    os.makedirs(wavDirName)  # to hold .wav files

# determine devMode
dev_mode = expInfo['devMode']

# variables pertaining to timing, in seconds
show_word_dur_in_serial_presentation       = 4 # how long to show each individual word for in serial presentation
wait_between_serial_lists                  = 8 # interval between word list 1 and word list 2 in serial presentations
show_wordlist_dur_in_parallel_presentation = 4 # how long to show each word list for in parallel presentation
wait_between_parallel_lists                = 8 # how long to wait for between word lists in parallel presentation
i_dur                                      = 2 # how long the "please encode each target word in list x" is up for
mic_timeout                                = 60 # set the mic to record for this long, but break out when they press the key to say they have finished speaking
text_height                                = 32 # how big the text should be (having this as a variable allows wholesale changes more easily)
end_of_block_wait                          = 2 # how long to wait between blocks


# set the timings up: short durs for dev_mode; normal durs for real runs and for testing out
if dev_mode:
    # variables pertaining to timing, in seconds
    show_word_dur_in_serial_presentation       = 1  # how long to show each individual word for in serial presentation
    wait_between_serial_lists                  = 8  # interval between word list 1 and word list 2 in serial presentations
    show_wordlist_dur_in_parallel_presentation = 4  # how long to show each word list for in parallel presentation
    wait_between_parallel_lists                = 8  # how long to wait for between word lists in parallel presentation
    i_dur                                      = 2  # how long the "please encode each target word in list x" is up for
    mic_timeout                                = 60  # set the mic to record for this long, but break out when they press the key to say they have finished speaking
    text_height                                = 32  # how big the text should be (having this as a variable allows wholesale changes more easily)
    end_of_block_wait                          = 2  # how long to wait between blocks

# read in word lists from file
PracticeList1, PracticeList2, \
LowFrequencyList1, LowFrequencyList2, LowFrequencyList3, LowFrequencyList4, \
HighFrequencyList1, HighFrequencyList2, HighFrequencyList3, HighFrequencyList4 = \
define_word_lists()

# randomly assign participants to condition (a between-subjects factor easy-first or hard-first)
condition = str(None)
if random() < 0.5:
    condition = "easy-first"
    blocks = [
        [PracticeList1, PracticeList2],           # Block 0
        [HighFrequencyList1, HighFrequencyList2], # Block 1
        [HighFrequencyList3, HighFrequencyList4], # Block 2
        [LowFrequencyList1, LowFrequencyList2],   # Block 3
        [LowFrequencyList3, LowFrequencyList4]    # Block 4
    ]
else:
    condition = "hard-first"
    blocks = [
        [PracticeList1, PracticeList2],           # Block 0
        [LowFrequencyList1, LowFrequencyList2],   # Block 1
        [LowFrequencyList3, LowFrequencyList4],   # Block 2
        [HighFrequencyList1, HighFrequencyList2], # Block 3
        [HighFrequencyList3, HighFrequencyList4]  # Block 4
]

# write session information to file info.txt in the results directory for that participant
with open(os.path.join(filename, "info.txt"), "w") as f:
    f.write("condition {}\nage {}\ngender {}\nsession {}\ndevmode {}\n".format(
        condition, expInfo['age'], expInfo['gender'], expInfo['session'], expInfo['devMode']))

# read in the contents of text messages
text_please_recall_list_1, text_please_recall_list_2, text_start_of_block = define_messages()

# Setup the Window
# full screen, can be hard to debug because there are long periods where nothing gets printed to screen
win = visual.Window(size=[1920, 1080], units='pix', fullscr=True, screen=0, winType='pyglet', allowGUI=False, allowStencil=False, monitor='testMonitor', color=[0,0,0], colorSpace='rgb', blendMode='avg', useFBO=True)
# small window
# win = visual.Window(size=[800, 600], units='pix', fullscr=False, screen=0, winType='pyglet', allowGUI=True, allowStencil=False, monitor='testMonitor', color=[0,0,0], colorSpace='rgb', blendMode='avg', useFBO=True)

# Enable sound input/output: you need to do this well before you actually record anything, it is like 'power on'
microphone.switchOn(sampleRate=16000)

""" loop 5 times: one practice block + 4 real blocks """
for blockn in range(5):

    # pull out the current block
    block = blocks[blockn]

    # message at start of block
    print("starting block {}".format(blockn))
    event.clearEvents()
    txt = visual.TextStim(win, text_start_of_block[blockn], pos=(0,0), alignHoriz='center', wrapWidth=1000, height=28)
    txt.draw()
    win.flip()
    while True:
        if len(event.getKeys(['space'])):
            win.flip()
            break
        if len(event.getKeys(['escape'])):
            core.quit()

    # serial presentation of list 1 and then list 2
    for listn in range(2):
        print("starting serial presentation of list {}".format(listn+1))
        List = block[listn]
        if blockn == 0: i = visual.TextStim(win, "please encode each target word in List " + str(listn+1), pos=(0, 0), alignHoriz='center', wrapWidth=1000, height=text_height); i.draw(); win.flip(); core.wait(i_dur); win.flip()
        l = visual.TextStim(win, text="List {}".format(str(listn+1)), pos=(-400,400), alignHoriz='center', wrapWidth=1000, height=text_height)
        c = visual.TextStim(win, text=List['cue'][0], pos=(-400,0), alignHoriz='center', wrapWidth=1000, height=text_height)
        for wordn in range(10):
            w = visual.TextStim(win, text=List['words'][wordn], pos=(0,0), alignHoriz='center', wrapWidth=1000, height=text_height)
            l.draw()
            c.draw()
            w.draw()
            win.flip()
            core.wait(show_word_dur_in_serial_presentation)
        win.flip()
        core.wait(wait_between_serial_lists)
        win.flip()

    # parallel presentation of list 1 and then list 2
    for listn in range(2):
        print("starting parallel presentation of list {}".format(listn+1))
        List = block[listn]
        if blockn == 0: i = visual.TextStim(win, "please encode each target word in List " + str(listn+1), pos=(0, 0), alignHoriz='center', wrapWidth=1000, height=text_height); i.draw(); win.flip(); core.wait(i_dur); win.flip()
        l = visual.TextStim(win, text="List {}".format(str(listn + 1)), pos=(-400,400), alignHoriz='center', wrapWidth=1000, height=text_height)
        c = visual.TextStim(win, text=List['cue'][0], pos=(-400,0), alignHoriz='center', wrapWidth=1000, height=text_height)
        ypositions = [450, 350, 250, 150, 50, -50, -150, -250, -350, -450]
        for wordn in range(10):
            w = visual.TextStim(win, text=List['words'][wordn], pos=(0, ypositions[wordn]), alignHoriz='center', wrapWidth=1000, height=text_height)
            w.draw()
        l.draw()
        c.draw()
        win.flip()
        core.wait(show_wordlist_dur_in_parallel_presentation)
        win.flip()
        core.wait(wait_between_parallel_lists)
        win.flip()

    # speak into mic for list 1
    print("mic 1")
    event.clearEvents()
    mic_text = visual.TextStim(win, text="please recall as many words as you can from word list 1 and press the spacebar when you cannot remember any more", pos=(0,250), alignHoriz='center', wrapWidth=1000, height=text_height)
    mic_text.draw()
    cue = visual.TextStim(win, block[0]['cue'][0], pos=(-400,0), alignHoriz='center', wrapWidth=1000, height=text_height)
    cue.draw()
    win.flip()
    t0 = core.getTime()
    mic_list_1 = microphone.AudioCapture(name=block[0]['name'], saveDir=wavDirName, stereo=False, chnl=0)
    mic_list_1.reset()
    mic_list_1.record(sec=mic_timeout, block=False)
    while mic_list_1.recorder.running:
        if len(event.getKeys(['space'])):
            mic_list_1.stop()
            mic_list_1.recorder.running = False
            mic_list_1.reset()
            break
    win.flip()
    print("mic 1 end")

    # speak into mic for list 2
    print("mic 2")
    event.clearEvents()
    mic_text = visual.TextStim(win, text="please recall as many words as you can from word list 2 and press the spacebar when you cannot remember any more", pos=(0,250), alignHoriz='center', wrapWidth=1000, height=text_height)
    mic_text.draw()
    cue = visual.TextStim(win, block[1]['cue'][0], pos=(-400,0), alignHoriz='center', wrapWidth=1000, height=text_height)
    cue.draw()
    win.flip()
    t0 = core.getTime()
    mic_list_2 = microphone.AudioCapture(name=block[1]['name'], saveDir=wavDirName, stereo=False, chnl=0)
    mic_list_2.reset()
    mic_list_2.record(sec=mic_timeout, block=False)
    while mic_list_2.recorder.running:
        if len(event.getKeys(['space'])):
            mic_list_2.stop()
            mic_list_2.recorder.running = False
            mic_list_2.reset()
    win.flip()
    print("mic 2 end")

    print("end of block core.wait")
    core.wait(end_of_block_wait)

# it takes a long time for the audio processes to shut down gracefully, but I don't know why (bad programming from me? natural consequenec of how it's done in psychopy?)
pw = visual.TextStim(win, "Please wait while the experiment shuts down. This can take a minute or more.")
pw.draw()
win.flip()

print("endex")
core.quit()
