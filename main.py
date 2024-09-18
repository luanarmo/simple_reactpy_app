from reactpy import component, html, use_location
from reactpy_router import route, simple, link
from reactpy.backend.fastapi import configure

from fastapi import FastAPI


app = FastAPI()

@component
def about():
    return html.div(
        html.h1("About Page"),
        html.p("Welcome to the about page"),
        html.p(link("Home", to="/")),
    )

@component
def navbar():
    return html.nav(
        html.ul(
            html.li(link("Inicio", to="/")),
            html.li(link("Acerca de", to="/about")),
        )
    )

@component
def missing():
    return html.div(
        html.h1("404 Page"),
        html.p("The page you are looking for does not exist"),
        html.p(link("Home", to="/")),
    )


@component
def home():
    return html.div(
        html.h1("Home Page"),
        html.p("Welcome to the home page"),
        html.p(link("About", to="/about")),
    )

@component
def App():
    location = use_location()
    return simple.router(
        route("/", home()),
        route("/about", about()),
        route("*" , missing())
    )

configure(app, App)