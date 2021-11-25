###################
#     Imports     #
###################
from guizero import App, Text, ButtonGroup, Combo, PushButton, TextBox, CheckBox, ListBox, Picture, Box, info

##############################################
#                  Procedures                #
##############################################

# creates the hero name
def make_hero_name():
    adjective = bgp_adjective.value
    colour = txt_colour.value
    animal = cmb_animal.value
    hero = adjective + " " + colour + " " + animal
    lbl_output.value = "You are... The " + hero + "."

# checks if the checkbox has been checked or not.
def checkboxcheck():
    print(checkbox.value)
    if checkbox.value == 1:
        output.value = "Your superhero is a Male"
    elif checkbox1.value == 1:
        output.value = "Your superhero is a Female"

# gets the nationality
def ListBoxThing():
    output2.value = "Your heros nationality is "+ listbox.value

# light mode button.
def LightMode():
    app.bg="#CED4DA"
    btn_dark_mode.text_color = "#212529"
    btn_light_mode.text_color= "#212529"
    text1.text_color = "#212529"
    text2.text_color = "#212529"
    text3.text_color = "#212529"
    text4.text_color = "#212529"
    text5.text_color = "#212529"
    bgp_adjective.text_color = "#212529"
    txt_colour.text_color = "#212529"
    cmb_animal.text_color = "#212529"
    btn_dark_mode.text_color = "#212529"
    btn_make_name.text_color = "#212529"
    lbl_output.text_color ="#212529"
    Title.text_color ="#212529"
    checkbox.text_color ="#212529"
    checkbox1.text_color ="#212529"
    listbox.text_color ="#212529"
    output.text_color = "#212529"
    output2.text_color = "#212529"

# dark mode button.
def DarkMode():
    app.bg = "#343A40"
    btn_dark_mode.text_color = "#DEE2E6"
    btn_light_mode.text_color= "#DEE2E6"
    text1.text_color = "#DEE2E6"
    text2.text_color = "#DEE2E6"
    text3.text_color = "#DEE2E6"
    text4.text_color = "#DEE2E6"
    text5.text_color = "#DEE2E6"
    bgp_adjective.text_color = "#DEE2E6"
    txt_colour.text_color = "#DEE2E6"
    cmb_animal.text_color = "#DEE2E6"
    btn_dark_mode.text_color = "#DEE2E6"
    btn_make_name.text_color = "#DEE2E6"
    lbl_output.text_color = "#DEE2E6"
    Title.text_color = "#DEE2E6"
    checkbox.text_color = "#DEE2E6"
    checkbox1.text_color = "#DEE2E6"
    listbox.text_color = "#DEE2E6"
    output.text_color ="#DEE2E6"
    output2.text_color = "#DEE2E6"

########################################
#            MAIN PROGRAMME            #
########################################
app = App(title="Hero-o-matic", width=1000, height=1000)
Title = Text(app, text="Hero Name Generator")
Title.text_size=20
BlankSpace = Text(app, text=" ")
##############################################
#            Dark and Light Modes            #
##############################################
DarkAndLightMode = Box(app, layout = "grid", border=True)
btn_dark_mode = PushButton(DarkAndLightMode, text="Dark Mode", command=DarkMode, width=20, grid=[0,0])
btn_light_mode = PushButton(DarkAndLightMode, text="Light Mode", command=LightMode, width=20, grid=[1,0])
BlankSpace = Text(app, text=" ")
#################################
#            WIDGETS            #
#################################
text1 = Text(app, text="Please choose a adjective:")
bgp_adjective = ButtonGroup(app, options=["Happy  ", "Awesome", "Outgoing", "Funky "])
BlankSpace = Text(app, text=" ")
text2 = Text(app, text="Please enter a colour:")
txt_colour = ButtonGroup(app, options=["Blue  ", "Green ", "Purple", "Red   "])
BlankSpace = Text(app, text=" ")
text3 = Text(app, text="Please pick an animal:")
cmb_animal = Combo(app, options=["Dog", "Cat", "Elephant", "Chicken"])
BlankSpace = Text(app, text=" ")
text4 = Text(app, text="Is your superhero a Male or Female?")
checkbox = CheckBox(app, command=checkboxcheck, text=" Male  ")
checkbox1 = CheckBox(app, command=checkboxcheck, text="Female")
BlankSpace = Text(app, text=" ")
text5 = Text(app, text="What country is your hero from?")
listbox = ListBox(app, command=ListBoxThing, items=["England", "Germany", "America", "Mexico", "Spain", "France", "Belgium", "Scotland", "Ireland"])
BlankSpace = Text(app, text=" ")
#######################
#      Make Hero      #
#######################
GreenBox = Box(app)
GreenBox.bg = "green"
btn_make_name = PushButton(app, text="Make Hero", command=make_hero_name)
lbl_output = Text(GreenBox, text=" -- A hero name will appear here --")
output = Text(GreenBox, text="-- Hero Gender will appear here --")
output2 = Text(GreenBox, text="-- Nationality will appear here --")
app.display()
