import re
from dataclasses import dataclass

import UI
from Container import Container
from functools import reduce


all_verbs = ['go', 'look', 'burn', 'take', 'drop', 'get', 'obtain', 'open',
        'close', 'use']
all_nouns = ['north', 'south', 'east', 'west', 'around', 'here', 'me', 'myself',
        'i', 'door', 'vinewall', 'vines', 'battery']

def debug_shell(player):
    while True:
        try:
            var = input('>>> ')
            exec(var, {**player.globals}, {'p': player, 'player': player})
            print(eval(var, {**player.globals}, {'p': player, 'player': player}))
        except EOFError:
            UI.println()
            return
        except:
            pass


def process_input(dirty_input, player):
    if dirty_input == '\\':
        # enter shell
        debug_shell(player)
    else:
        UI.println()
        clean_input = sanitize(dirty_input)
        unaliased_input = expand_aliases(clean_input)
        tokenized_input = unaliased_input.split()
        action = Action.create_action(tokenized_input, player)
        action.run(player)


def expand_aliases(clean_input):
    if clean_input in {'n', 'north'}:
        return 'go north'
    elif clean_input in {'e', 'east'}:
        return 'go east'
    elif clean_input in {'s', 'south'}:
        return 'go south'
    elif clean_input in {'w', 'west'}:
        return 'go west'
    elif clean_input == 'l':
        return 'look'
    else:
        return clean_input


def sanitize(dirty_input):
    regex = re.compile(r'[^a-zA-Z\s]')
    clean_uppercase_input = regex.sub('', dirty_input)
    clean_lowercase_input = clean_uppercase_input.lower()
    return clean_lowercase_input

def breakdown_sentence(tokenized_input):
    sentence = []
    have_verb = False
    have_noun = False
    for word in tokenized_input:
        if word in all_nouns and word in all_verbs:
            sentence.append(Word(word, ['noun', 'verb']), 5)
        elif word in all_verbs:
            sentence.append(Word(word, ['verb'], 10))
        elif word in all_nouns:
            sentence.append(Word(word, ['noun'], 10))
        elif word not in all_nouns and word not in all_verbs:
            # Logger.log()
            if have_noun and not have_verb:
                sentence.append(Word(word, ['verb'], 3))
            elif have_verb and not have_noun:
                sentence.append(Word(word, ['noun'], 3))
            else:
                sentence.append(Word(word, ['verb'], 0))
            
    return sentence

def get_targets_from_string(noun, player):
    '''
    Looks in the current Place for a GameObject with an identifier that matches
    noun. Returns a list of matching GameObject. Returns an empty list if
    nothing matches or if noun or player is null.
    '''
    # First try a couple of special identifiers that change over time
    if noun == 'north':
        return [player.north]
    if noun == 'east':
        return [player.east]
    if noun == 'south':
        return [player.south]
    if noun == 'west':
        return [player.west]

    # If that doesn't work, start going over everything
    everything = player.get_all_things()
    def get_matching(accum, go):
        if isinstance(go, Container):
            if go.get(noun) != []:
                accum.extend(go.get(noun))
        if go.is_called(noun):
            accum.append(go)
    targets = reduce(get_matching, everything, [])
    return targets

# TODO add flag for dev messages
class Action:
    '''
    Action represents a binding from some user input to the resultant in-game
    action that has not yet been invoked. The recommended way to use it is to
    call create_action() and then action.run()
    '''
    # TODO add logging here
    def __init__(self, verb, target, sentence, viable=True):
        self.verb = verb
        self.target = target
        self.sentence = sentence
        self.viable = viable

    @staticmethod
    def create_action(tokenized_input, player):
        '''
        Creates an Action object and returns it. This should be used to process
        user input. An object will always be returned, regardless of whether the
        input is valid or makes sense. Calling action.run() on such an Action
        will result in output telling the user where parsing or comprehesion failed.
        '''
        sentence = breakdown_sentence(tokenized_input)
        # FIXME naive implementation: I just look up that the first verb and
        # then consider the next word the noun
        if len(tokenized_input) == 1 and tokenized_input[0] == 'i':
            return Action('i', player, sentence)
        verb = None
        noun = None
        for index, word in enumerate(sentence):
            if 'verb' in word.part_of_speech:
                verb = word.string
                # If we're not at the end of the sentence
                if index != len(sentence) - 1:
                    noun = sentence[index + 1].string
                break
        if noun is not None and verb is not None:
            possible_targets = get_targets_from_string(noun, player)
            chosen_target = None
            if len(possible_targets) == 0:
                # No targets were found
                # TODO improve message as this is likely to occur a lot
                UI.println(f'Unable to bind token "{noun}" to an object. Sorry.')
                # not viable
                return Action(verb, None, sentence, False)
            elif len(possible_targets) == 1:
                chosen_target = possible_targets[0]
                # viable
                return Action(verb, chosen_target, sentence)
            else:
                for target in possible_targets:
                    pass
                    # TODO decide best target
        elif noun is None and verb is not None:
            # viable - might be intransitive
            return Action(verb, noun, sentence)
        else:
            # not viable - no verb
            return Action(verb, noun, sentence, False)

    def run(self, player):
        self.warn_about_unrecognized()
        if self.viable:
            if self.target is not None:
                self.target.interact.get(self.verb, invalid_verb_handler)(player)
            else:
                # Try to invoke intransitively
                self.try_intransitive(player)
        else:
            self.debug()

    def try_intransitive(self, player):
        if self.verb == 'look':
            player.location.on_look(player)
        else:
            self.debug()

    def warn_about_unrecognized(self):
        for word in self.sentence:
            if word.part_of_speech == 'unknown':
                UI.println(f'Unrecognized token "{word.string}".')
                UI.println('Add it to the global dictionaries in WordParser.py')

    def debug(self):
        if self.verb is None and self.target is None:
            UI.println('I don\'t see a verb in your sentence.')
        elif self.verb is None and self.target is not None:
            UI.println(f'I get that you want to do something with '
            '"{self.target}", but I couldn\'t figure out what.')
        elif self.verb is not None and self.target is None:
            UI.println(f'The verb "{self.verb}" can\'t be used without an object.')
        else:
            raise Exception('Verb should\'ve been run.')

def invalid_verb_handler(player):
    # TODO improve with multiple responses and random choice
    UI.println('You\'re not making any sense.')

@dataclass
class Word:
    string: str
    part_of_speech: list
    confidence: int # confidence in the correct part of speech
