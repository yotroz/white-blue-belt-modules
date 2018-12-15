#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 09:35:35 2018

@author: yotroz
"""

#%%

from flask import Flask, jsonify 

server = Flask("books!")

list_of_books = []

@server.route("/books")
def get_books(): 
    return jsonify(list_of_books)

@server.route("/add/<title>", methods=["POST"])
def add_books(title): 
    list_of_books.append(title)
    return jsonify(title + " added")

@server.route("/delete/<title>", methods=["DELETE"])
def whatever(title):
    if title in list_of_books: 
        list_of_books.remove(title)
        
    else: 
        return jsonify("book not in the list")
    
    
server.run()