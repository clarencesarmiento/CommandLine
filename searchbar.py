from progressbar import *
import time


def search_bar(item):
    widgets = ['Searching: ', Percentage(), ' ', Bar(),
               ' ', ETA(), ' ', FileTransferSpeed()]
    progress_bar = ProgressBar(widgets=widgets, maxval=500).start()
    for i in range(len(item)):
        progress_bar.update(i)
        time.sleep(0.005)
    progress_bar.finish()
