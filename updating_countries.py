#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on Thu Dec  8 19:15:47 2022

@author: sarahsweigart
"""



from shiny import ui, render, App



def generate_button(ui, city_id, city_name):
    ui.input_action_button(country_id, country_name, class_="btn-success")
    return ui

app_ui = ui.page_fluid(
    ui.input_slider("n", "N", 0, 100, 40),
    generate_button(ui, 'London','London')
    #ui.input_action_button("go", "Go!", class_="btn-success")
    ui.output_text_verbatim("txt"),
)

def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"

# This is a shiny.App object. It must be named `app`.
app = App(app_ui, server)


