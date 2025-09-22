from flask import Flask, render_template, flash, redirect, session, request, url_for

app = Flask(__name__,template_folder='templates')

