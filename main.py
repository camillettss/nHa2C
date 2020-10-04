import os, sys
import random, time
import json

paths={
    "dataset":"data/dataset.json"
}

def intentToClass(intent:'a json-like object', on_act:'a function, "auto" to the default func'='auto'):
    class r:
        def __init__(self):
            pass
    def on_activate(*args):
        '''
        default function, random regression
        '''
        print(', '.join(args))
    if on_act=='auto':
        setattr(r, intent['on_activate'][0], on_activate)
    else:
        setattr(r, intent['on_activate'][0], on_act)
    return r

class OSH():
    def __init__(self):
        self.ints=json.loads(open(paths['dataset']).read())
    
    def dump(self, x):
        '''
        dump the input in the dataset as an intent
        '''
        return
    
    def push(self, intname):
        '''
        using the recognised intent return the specified on_activate function
        '''
        exec('intentToClass(self.ints[intname]).'+self.ints[intname]['on_activate'][0]+'('+'"'+'", "'.join(self.ints[intname]['on_activate'][1:])+'"'+')')

nh=OSH()
#nh.push('intentName') va chiamato quando intentName viene riconosciuto tramite i suoi ins (if x in intents[ins])
