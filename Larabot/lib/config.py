####################################################################################
# Larabot Discord Bot
# MIT License
# Copyright (c) 2017 Devitgg
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
####################################################################################

####################### Documentation ######################
# Coming Later
############################################################

def token():
    token = '<insert>'
    return token

def googleKey():
    this = '<insert>'
    return this

def modAuthority(message):
    approvedRoles = ['<insert>']
    for role in message.server.roles:
        for approved in approvedRoles:
            if approved == role.name:
                return True

def adminAuthority(message):
    approvedRoles = ['<insert>']
    for role in message.server.roles:
        for approved in approvedRoles:
            if approved == role.name:
                return True

def roleChannel():
    this = '<insert>'
    return this

def searchCommand():
    this = '<insert>'
    return this

def googleResultCount():
    this = 5
    return this

def anonCommand():
    this = '<insert>'
    return this

def anonChannel():
    this = '<insert>'
    return this

def helpCommand():
    this = '<insert>'
    return this

def codeCommand():
    this = '<insert>'
    return this

def addRoleCommand():
    this = '<insert>'
    return this

def removeRoleCommand():
    this = '<insert>'
    return this

def showRoleCommand():
    this = '<insert>'
    return this

def kickCommand():
    this = '<insert>'
    return this

def banCommand():
    this = '<insert>'
    return this

def plusRepCommand():
    this = '<insert>'
    return this

def viewRepCommand():
    this = '<insert>'
    return this

def clearCommand():
    this = '<insert>'
    return this
