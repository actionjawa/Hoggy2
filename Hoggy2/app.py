from flask import Flask, url_for, request
from twisted.words.protocols import irc
from twisted.internet import reactor
import time, os, logging, sys, Hoggy2.utils
from Hoggy2.utils.HoggyLogger import HoggyLogger
from irc_bot import HoggyBot, HoggyBotFactory

config = Hoggy2.utils.get_config()
log = HoggyLogger(__name__, config.get('hoggy', 'logfile'))

def main():
    log.info("Hello! - Starting IRC Bot!")

    # create factory protocol and application
    f = HoggyBotFactory(config, log)
    
    # connect factory to this host and port
    reactor.connectTCP(config.get('irc', 'host'), int(config.get('irc', 'port')), f)
    
    # run bot
    reactor.run()

if __name__ == "__main__":
    main()