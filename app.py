#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on Thu Dec  8 19:15:47 2022

@author: sarahsweigart
"""



from shiny import App, ui, render

app_ui = ui.page_fluid(
    ui.panel_sidebar("Available Countries"),
    ui.panel_main("Pulled Country")
)

def server(input, output, session):
    @output
    @render.text
    #def report_check():
        #return str(a_missing_variable)

    @output
    @render.text
    def another_output():
        return "This output is looking good"


app = App(app_ui, server)



